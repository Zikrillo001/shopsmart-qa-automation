# Bug Reports

---

## Bug 1: Duplicate Locator Issue

**ID:** BUG-001  
**Type:** UI  

**Description:**
Locator "#inventory_container" matches multiple elements causing Playwright strict mode failure.

**Steps to Reproduce:**
1. Run UI login test
2. Observe failure on inventory page check

**Actual Result:**
- Test fails with strict mode violation

**Expected Result:**
- Locator should match only one element

**Fix:**
- Use stable selector: `[data-test="inventory-container"]`

---

## Bug 2: API Schema Mismatch

**ID:** BUG-002  
**Type:** API  

**Description:**
Product list schema did not match actual API response format.

**Steps:**
1. Run product API test
2. Validate schema

**Actual Result:**
- Schema validation fails

**Expected Result:**
- Response matches schema

**Fix:**
- Update schema to match DummyJSON format

---

## Bug 3: Wrong Auth Credentials

**ID:** BUG-003  
**Type:** API  

**Description:**
Login failed due to incorrect credentials.

**Steps:**
1. Send login request with invalid credentials

**Actual Result:**
- Status 400

**Expected Result:**
- Valid login should return token

**Fix:**
- Use correct credentials:
  - username: emilys
  - password: emilyspass

---

## Bug 4: Missing Auth Token Field

**ID:** BUG-004  
**Type:** API  

**Description:**
Response validation expected "token" but API returned "accessToken".

**Fix:**
- Update schema and tests to use correct field