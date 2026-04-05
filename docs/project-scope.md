# Project Scope — ShopSmart QA Automation Framework

## Project Name
ShopSmart QA Automation Framework

## Business Description
ShopSmart is a simulated e-commerce platform that allows users to:
- browse products
- add items to cart
- complete checkout
- authenticate via login

The goal of this project is to validate the quality, stability, and correctness of both backend and frontend systems using automated testing.

---

## Modules

### API Layer (DummyJSON)
- Authentication
- Products
- Carts
- Orders

### UI Layer (SauceDemo)
- Login
- Inventory (Products)
- Cart
- Checkout
- Logout

---

## User Roles
- Standard user (valid login)
- Invalid user (negative scenarios)

---

## Functional Requirements

### API
- User can login and receive token
- User can retrieve product list
- User can retrieve single product
- API returns valid JSON schema

### UI
- User can login with valid credentials
- User cannot login with invalid credentials
- User can add product to cart
- User can view cart
- User can complete checkout
- User can logout

---

## Non-Functional Requirements
- API response time < 1 second
- UI should load within acceptable time
- System should handle invalid input gracefully
- Tests should be stable and repeatable

---

## Risk Areas
- Authentication failures
- Incorrect API schema
- UI locator instability
- Cart/checkout flow issues
- Environment inconsistencies

---

## Test Strategy (Summary)
- Smoke tests for critical flows
- Regression tests for broader coverage
- Unit tests for utilities
- API + UI automation combined

---

## Automation Scope

### Included
- API automation (pytest + requests)
- UI automation (Playwright)
- Schema validation
- Auth token handling
- Reporting (HTML + logs)
- CI/CD (GitHub Actions)

### Not Included (Future Work)
- Performance testing (JMeter)
- Security testing
- Mobile testing