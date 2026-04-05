# Test Strategy

## Overview
This document defines the testing approach used in the ShopSmart QA Automation Framework.

---

## Test Types

### 1. Smoke Testing
Smoke tests verify that critical application functionality works.

Examples:
- user login
- add to cart
- API authentication

Purpose:
- fast validation after deployment
- detect critical failures early

---

### 2. Regression Testing
Regression tests ensure that existing functionality is not broken after changes.

Examples:
- multiple product retrieval
- checkout flow
- logout flow

Purpose:
- broader coverage
- prevent regressions

---

### 3. Unit Testing
Unit tests validate individual components.

Examples:
- data loader
- helpers
- validation utilities

Purpose:
- ensure internal logic correctness
- fast feedback

---

## Test Levels

### API Testing
- endpoint validation
- response status codes
- schema validation
- authentication handling

### UI Testing
- login flows
- product interactions
- cart behavior
- checkout flow

---

## Test Coverage

| Area        | Coverage |
|-------------|----------|
| API         | High     |
| UI          | Medium   |
| Unit        | Medium   |

---

## Tools Used
- Pytest
- Requests
- Playwright
- JSON Schema validation

---

## Execution Strategy

### Local
- run smoke tests first
- then regression tests

### CI/CD
- API and UI tests run separately
- full regression run available manually

---

## Risks & Mitigation

| Risk                    | Mitigation |
|-------------------------|------------|
| flaky UI tests          | stable selectors (data-test) |
| API instability         | schema validation |
| environment differences | config-driven setup |