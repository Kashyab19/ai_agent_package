# AI Agent Package

## 📌 Overview
This package provides a modular AI agent for interacting with the **NEAR blockchain**. It enables querying **account details**, and serves as a foundation for building more advanced blockchain automation tools.

---

## ⚡ Installation

## Requirements: Python > 3.11

### **1️⃣ Clone the Repository via your terminal or any GUI **

```
git clone https://github.com/yourusername/ai_agent.git
cd ai_agent
```

## 2️⃣ Creating a virtual env(recommended to save time from package conflicts)
```
python3 -m venv venv #feel free to give your venv name
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

## 3️⃣ Installing dependencies:

```
pip install -r requirements.txt
```

## 4️⃣ Install our packages locally

```
pip install -e .
```

## 5️⃣ Running tests:

### Run all tests

```
pytest tests/
```
### Run tests with printed output

```
pytest tests/ --capture=tee-sys
```