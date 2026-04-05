# ShopSmart QA Automation Framework

A portfolio-grade QA automation project that demonstrates API testing, UI testing, unit testing, regression coverage, reporting, and CI integration.

## Project Goal
This project simulates a real-world QA automation framework for an e-commerce platform.  
It combines:
- API automation
- UI automation
- unit-level validation
- smoke and regression coverage
- reporting
- GitHub Actions CI

## Tech Stack
- Python
- Pytest
- Requests
- Playwright
- Robot Framework
- JSON Schema
- Pytest HTML
- GitHub Actions

## Covered Areas

### API Testing
- authentication
- products
- carts
- orders

### UI Testing
- login
- invalid login
- add to cart
- logout
- checkout
- inventory validation

### Test Types
- smoke
- regression
- unit
- ui
- api

## Project Structure
```text
src/
  clients/
  schemas/
  services/
  ui/
  utils/

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
robot/
.github/workflows/


Running Tests
Install dependencies
pip install -r requirements.txt
playwright install

Run API smoke
pytest tests/api/smoke -m "api and smoke" -v
Run API regression
pytest tests/api/regression -m "api and regression" -v
Run UI smoke
pytest tests/ui/smoke -m "ui and smoke" -v
Run UI regression
pytest tests/ui/regression -m "ui and regression" -v
Run full suite
pytest -v
Reporting

The framework generates:

HTML reports
screenshots on UI failure
logs for API and UI execution

Reports are stored in:

reports/
CI/CD

GitHub Actions workflows are included for:

API tests
UI tests
full regression run
Highlights
config-driven framework
reusable API clients
JSON schema validation
Page Object Model for UI
auth token fixture support
failure screenshot capture
regression-ready structure
Future Improvements
Allure reporting
Qase integration
cross-browser matrix execution
Dockerized test execution
parallel run optimization