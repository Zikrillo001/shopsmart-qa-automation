
````md
# 🚀 ShopSmart QA Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green)
![Playwright](https://img.shields.io/badge/Playwright-UI--Automation-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-black)
![Status](https://img.shields.io/badge/Tests-Passing-brightgreen)

> Portfolio-grade QA automation framework combining API and UI testing with real-world scenarios, regression coverage, and CI/CD pipelines.

---

## 📌 Project Overview

This project simulates a real-world QA automation framework for an e-commerce platform.

It demonstrates:
- API testing
- UI automation
- test architecture design
- regression coverage
- reporting and logging
- CI/CD integration

---

## 🔥 Key Features

- ✅ API Automation (Pytest + Requests)
- ✅ UI Automation (Playwright)
- ✅ Smoke & Regression Testing
- ✅ JSON Schema Validation
- ✅ Auth Token Fixture System
- ✅ Page Object Model (POM)
- ✅ Screenshot on Failure
- ✅ HTML Reporting
- ✅ GitHub Actions CI/CD

---

## 🧰 Tech Stack

- **Language:** Python  
- **Test Framework:** Pytest  
- **API Testing:** Requests  
- **UI Testing:** Playwright  
- **Validation:** JSON Schema  
- **Reporting:** Pytest HTML  
- **CI/CD:** GitHub Actions  

---

## 🧱 Project Structure

```text
src/
  clients/        # API clients
  schemas/        # JSON schemas
  ui/
    pages/        # Page Object Model
    components/
  utils/          # helpers, logger, config

tests/
  api/
    smoke/
    regression/
  ui/
    smoke/
    regression/
  unit/

config/
data/
docs/
reports/

.github/workflows/
````

---

## 🧪 Test Coverage

### API Testing

* Authentication
* Products
* Carts
* Orders
* Schema validation

### UI Testing

* Login / Invalid login
* Add to cart
* Cart validation
* Checkout flow
* Logout

---

## 🧪 Test Types

| Type       | Description        |
| ---------- | ------------------ |
| Smoke      | Critical flows     |
| Regression | Full coverage      |
| API        | Backend testing    |
| UI         | End-to-end testing |
| Unit       | Internal logic     |

---

## ⚙️ Setup & Installation

### 1. Clone repository

```bash
git clone https://github.com/Zikrillo001/shopsmart-qa-automation.git
cd shopsmart-qa-automation
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

### API Smoke

```bash
pytest tests/api/smoke -m "api and smoke" -v
```

### API Regression

```bash
pytest tests/api/regression -m "api and regression" -v
```

### UI Smoke

```bash
pytest tests/ui/smoke -m "ui and smoke" -v
```

### UI Regression

```bash
pytest tests/ui/regression -m "ui and regression" -v
```

### Full Suite

```bash
pytest -v
```

## Robot Framework Tests

Run Robot tests:
```bash
robot --outputdir reports/robot robot/tests
```

---

## 📊 Reporting

Framework generates:

* ✅ HTML reports
* ✅ Logs
* ✅ Screenshots on UI failure

Reports are stored in:

```text
reports/
```

---

## 🧠 Framework Highlights

* Config-driven setup
* Reusable API client architecture
* Token-based authentication fixture
* Page Object Model for UI
* Stable selectors (`data-test`)
* Failure debugging support
* Clean separation of test layers

---

## 🔄 CI/CD

GitHub Actions workflows included:

* API tests
* UI tests
* Full regression

Tests run automatically on:

* push
* pull request

---

## 🐞 Sample Bugs Found

* Duplicate locator issue (Playwright strict mode)
* API schema mismatch
* Incorrect authentication credentials
* Wrong response field (`token` vs `accessToken`)

---

## 🚀 Future Improvements

* Allure reporting integration
* Qase TestOps integration
* Parallel execution
* Dockerized test environment
* Cross-browser testing matrix

---

## 👨‍💻 Author

**QA Automation Engineer (Portfolio Project)**

---

## ⭐ Why This Project Matters

This project demonstrates real-world QA skills:

* test design
* automation architecture
* debugging
* framework building
* CI/CD integration

---

## 🔗 Project Link

👉 [https://github.com/](https://github.com/)Zikrillo001/shopsmart-qa-automation




