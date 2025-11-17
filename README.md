# 📘 AI Design Pattern Cookbook

*A curated collection of essential design patterns for Data Scientists, ML Engineers, and AI Engineers.*

This repository is a personal “AI design pattern cookbook” — a reference you can study, recall by heart, and reuse across real-world machine learning, AI engineering, and data science roles.

Rather than overwhelming you with *all* design patterns, this repo focuses on the essentials in production AI systems.

---

# 📂 Repository Structure

```
ai-design-pattern-cookbook/
│
├── data_scientist/
│   └── <pattern_name>/
│       └── use_cases.md
│
├── ml_engineer/
│   └── <pattern_name>/
│       └── use_cases.md
│
├── ai_engineer/
│   └── <pattern_name>/
│       └── use_cases.md
│
└── README.md
```

* Each role has its own folder
* Each folder contains subfolders for each relevant design pattern
* Each pattern folder contains:

  * **use_cases.md** — examples, rationale, and minimal Python templates

---

# 🎯 Goal of This Cookbook

To build a **memorized toolkit** of design patterns that appear repeatedly in:

* ML model development
* Data pipelines
* Experimentation systems
* Training/evaluation loops
* Deployment and productionization
* Observability and orchestration
* Inference and serving codebases

The patterns here are based on real-world usage across ML teams, MLOps platforms, research pipelines, and scalable production systems.

---

## 🧪 Data Scientist

These patterns appear constantly in notebooks, analytics code, ML prototypes, and lightweight pipelines.

### **Core Patterns**

| Pattern       | Why It Matters                                      |
| ------------- | --------------------------------------------------- |
| **Factory**   | Swap models/encoders/vectorizers via config         |
| **Strategy**  | Interchangeable algorithms & preprocessing methods  |
| **Singleton** | Central configs, loggers, DB connections            |
| **Observer**  | Auto-logging experiments & triggering workflows     |
| **Adapter**   | Normalize messy data sources into unified interface |
| **Decorator** | Add logging/timing/caching with clean syntax        |
| **Builder**   | Construct complex sklearn/feature pipelines         |
| **Command**   | Reproducible experiment actions (train/eval/deploy) |

### **Honorable Mentions**

* Template Method
* Proxy
* Facade

---

## 🛠️ ML Engineer

These patterns appear in model training codebases, data loaders, distributed training, and pipelines.

### **Core Patterns**

| Pattern                  | Why It Matters                                     |
| ------------------------ | -------------------------------------------------- |
| **Factory**              | Create models/loaders/optimizers dynamically       |
| **Strategy**             | Multiple training & augmentation schemes           |
| **Observer**             | Callbacks (logging, early stopping, checkpointing) |
| **Singleton**            | Config managers, logger, seed/GPU manager          |
| **Adapter**              | Normalize APIs across ML libraries                 |
| **Decorator**            | Profiling, caching, retry logic                    |
| **Builder**              | Assemble model & pipeline configs                  |
| **Dependency Injection** | Modular, testable training loops                   |
| **Command**              | Encapsulated experiment steps                      |
| **Pipeline**             | ETL → Dataset → Features → Model                   |

---

## 🤖 AI Engineer

These patterns dominate modern AI systems: retrieval pipelines, LLM applications, vector DBs, inference APIs, model registries, and orchestration.

### **Core Patterns**

| Pattern                        | Biggest Benefit                                    |
| ------------------------------ | -------------------------------------------------- |
| **Factory / Abstract Factory** | Flexible creation of models/tokenizers/dataloaders |
| **Strategy**                   | Swap inference/training/decoding behaviors         |
| **Adapter**                    | Integrate PyTorch/TensorFlow/ONNX/HuggingFace      |
| **Decorator**                  | Logging, tracing, retry, batching, caching         |
| **Observer (Pub-Sub)**         | Metrics, events, checkpoint notifications          |
| **Builder**                    | Construct complex inference/training pipelines     |
| **Facade**                     | Simplify multi-step training/inference processes   |
| **Singleton**                  | Global config/model registry                       |
| **Command**                    | Reproducible workflow commands                     |
| **Prototype**                  | Clone models/configs for experiments               |

---

# 🚀 How to Use This Cookbook

1. **Pick your role**
   → `data_scientist/`, `ml_engineer/`, or `ai_engineer/`

2. **Open a pattern folder**
   Each pattern includes:

   * What the pattern solves
   * Minimal implementation in Python
   * Real ML/AI use cases
   * When *not* to use the pattern

3. **Copy templates** into your own projects
   Simplify pipelines, training loops, feature engineering, deployment code, etc.

4. **Memorize the high-leverage patterns**
   These patterns appear everywhere in interviews and real systems.

---

# 📥 Adding New Patterns (Contribution Guidelines)

Although this is your personal cookbook, use this structure for adding new content:

### ✔️ Each pattern folder should include:

* `use_cases.md`
* Minimal working Python template
* Realistic ML/AI context
* Tradeoffs & anti-patterns

### ✔️ Include examples from:

* sklearn
* PyTorch/TensorFlow
* HuggingFace
* Airflow/Prefect
* Vector DB pipelines
* API/inference serving

### ✔️ Prioritize:

* Clarity
* Practicality
* Minimal boilerplate
* Real-world relevance

---

# 🧠 Why This Repository Matters

Mastering design patterns gives you:

* Cleaner pipelines
* More modular training loops
* Faster experimentation
* Production-ready code structure
* Easier debugging & logging
* Better architecture thinking
* Stronger interview performance

These patterns are the **architecture backbone** of real ML/AI systems.

---

# 🏁 Final Notes

This cookbook is designed to be **living documentation**.
As you encounter new systems, libraries, workflows, or deployment patterns, simply add to the folders.