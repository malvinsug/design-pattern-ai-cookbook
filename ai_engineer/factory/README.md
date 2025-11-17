Here is a **job-realistic, AI-engineering exercise** where the *only scalable solution* is to use the **Factory Design Pattern**.
The exercise is designed so that you naturally realize *“Oh… I need a factory here.”*

---

# 🧠 **Exercise: Multi-Backend Inference Loader for a Production AI Service**

You are an **AI Engineer** working on a production inference system.
Your company deploys AI models on different hardware environments:

* Cloud GPU servers using **TensorRT**
* Cloud CPU servers using **ONNX Runtime**
* Edge devices (ARM boards) using **OpenVINO**
* Fallback mode using standard **PyTorch JIT**

You are assigned to build the **model loading module** that will be used by the entire backend inference system.

---

## **Your Requirements**

### Requirements (as written by your engineering lead)

> Build a `load_inference_engine()` function that:
>
> * Receives a configuration file with fields:
>
>   * `backend` (string): `"tensorrt"`, `"onnx"`, `"openvino"`, `"torchscript"`
>   * `model_path` (string)
>   * `device` (string): `"cpu"`, `"cuda"`, `"edge"`
> * Based on config, loads the *appropriate inference backend*
> * Exposes a **unified interface**:
>
>   ```python
>   engine.load_model()
>   engine.predict(input_array)
>   ```
> * The inference service must work **without modifying the main code** when we add a new backend.
> * The loading logic will grow as new hardware accelerators arrive.
> * The system must prevent long `if/elif` chains inside business logic.

---

## **The Intent of the Exercise**

You must recognize constraints:

* multiple classes
* they share an interface
* different creation logic
* runtime configuration
* future extension expected
* no changes should be needed in the inference pipeline

➡️ **This situation strongly suggests using a Factory.**

---

# 🎯 **Your Task (What You Must Implement)**

1. Create **four classes**, each representing one inference backend:

   * `TensorRTBackend`
   * `ONNXBackend`
   * `OpenVINObackend`
   * `TorchscriptBackend`

   Each must implement:

   ```python
   load_model(self, path)
   predict(self, input)
   ```

2. Implement a mechanism to choose the backend **dynamically**, based on config.

3. The inference pipeline will be:

   ```python
   engine = load_engine_from_config("config.yaml")
   outputs = engine.predict(inputs)
   ```

4. Requirements:

   * You **must not** use `if backend == "...":` inside your pipeline.
   * You must support future backend types without modifying the main inference script.

---

# 💡 **Questions You Should Ask Yourself**

These are designed to push you toward realizing you need a Factory.

### ❓ How do I avoid scattering `if/elif` for backends across multiple files?

### ❓ How can I create backend objects without hardcoding them?

### ❓ How do I let the system add new backends in the future (e.g., Apple Neural Engine, Qualcomm AI Engine)?

### ❓ How do I give other engineers a *simple* and *unified* API?

### ❓ What is the cleanest way to instantiate classes from config?

➡️ All answers point to: **Factory Pattern**.

---

# 🧪 **Additional Challenge (Optional)**

Extend the exercise:

* Add `"webgpu"` or `"wasm"` as a new backend
* Add a `"profile=True"` option to wrap the backend with a decorator
* Use environment variables to override the backend
* Add a fallback mechanism if the desired backend is unavailable

Your factory must still:

* remain clean,
* keep the inference pipeline unchanged,
* and support future expansion.

---

# 👌 If you want, I can provide:

* A *complete* solution with Python code
* A *partial* solution with hints only
* Unit tests for your implementation
* A diagram showing the architecture

Just tell me which one you want!
