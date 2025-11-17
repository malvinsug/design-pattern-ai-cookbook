# The goal is to avoid long if statements
# Inference Code (Top Layer)
class InferenceFactory:
    @staticmethod
    def create(backend_type: str):
        backend_type = backend_type.lower()

        if backend_type == "onnx":
            return ONNXBackend()
        elif backend_type == "tensorrt":
            return TensorRTBackend()
        elif backend_type == "torchscript":
            return TorchScriptBackend()
        
        raise ValueError(f"Unknown backend type: {backend_type}")


engine = InferenceFactory.create("tensorrt")
engine.load_model("model.trt")
input_tensor = np.random.rand(1, 3, 224, 224).astype(np.float32)
prediction = engine.predict(input_tensor)

### BACKEND ####
import onnxruntime as ort
import numpy as np

# Portable Backend
class ONNXBackend:
    def load_model(self, path):
        self.session = ort.InferenceSession(path)
    
    def predict(self, inputs):
        ort_inputs = {self.session.get_inputs()[0].name: inputs}
        outputs = self.session.run(None, ort_inputs)
        return outputs[0]

import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit

# Super fast NVIDIA-optimized
class TensorRTBackend:
    def load_model(self, path):
        self.runtime = trt.Runtime(trt.Logger(trt.Logger.ERROR))
        with open(path, "rb") as f:
            engine_data = f.read()

        self.engine = self.runtime.deserialize_cuda_engine(engine_data)
        self.context = self.engine.create_execution_context()

        # allocate buffers
        self.inputs = []
        self.outputs = []
        self.bindings = []

        for i in range(self.engine.num_bindings):
            size = trt.volume(self.engine.get_binding_shape(i)) * 4
            device_mem = cuda.mem_alloc(size)
            self.bindings.append(int(device_mem))

            if self.engine.binding_is_input(i):
                self.inputs.append(device_mem)
            else:
                self.outputs.append(device_mem)

    def predict(self, host_input):
        cuda.memcpy_htod(self.inputs[0], host_input)
        self.context.execute_v2(self.bindings)
        host_output = np.empty(host_input.shape, dtype=np.float32)
        cuda.memcpy_dtoh(host_output, self.outputs[0])
        return host_output
    

# Experiment and Modelling
import torch
class TorchScriptBackend:
    def load_model(self, path):
        self.model = torch.jit.load(path)
        self.model.eval()

    def predict(self, inputs):
        with torch.no_grad():
            return self.model(torch.tensor(inputs)).numpy()


