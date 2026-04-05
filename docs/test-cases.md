# Test Cases

## 1. Valid Login

**ID:** TC-001  
**Type:** Smoke / UI  

**Steps:**
1. Open login page
2. Enter valid username and password
3. Click login

**Expected Result:**
- User is redirected to inventory page

---

## 2. Invalid Login

**ID:** TC-002  
**Type:** Negative / UI  

**Steps:**
1. Enter invalid credentials
2. Click login

**Expected Result:**
- Error message is displayed

---

## 3. Add Product to Cart

**ID:** TC-003  
**Type:** Smoke / UI  

**Steps:**
1. Login as standard user
2. Click "Add to cart"

**Expected Result:**
- Cart badge shows "1"

---

## 4. View Cart

**ID:** TC-004  
**Type:** UI  

**Steps:**
1. Add product
2. Open cart

**Expected Result:**
- Cart contains 1 item

---

## 5. Checkout Flow

**ID:** TC-005  
**Type:** Regression / UI  

**Steps:**
1. Add product to cart
2. Go to checkout
3. Fill user info
4. Complete order

**Expected Result:**
- Order is successfully completed

---

## 6. API Login

**ID:** TC-006  
**Type:** API / Smoke  

**Steps:**
1. Send POST request to /auth/login

**Expected Result:**
- Status 200
- Access token returned

---

## 7. Get Product List

**ID:** TC-007  
**Type:** API  

**Steps:**
1. Send GET request to /products

**Expected Result:**
- Status 200
- Valid schema

---

## 8. Get Single Product

**ID:** TC-008  
**Type:** API  

**Steps:**
1. Send GET request to /products/{id}

**Expected Result:**
- Status 200
- Product data returned

---

## 9. Invalid API Login

**ID:** TC-009  
**Type:** Negative / API  

**Steps:**
1. Send login request with wrong credentials

**Expected Result:**
- Status 400