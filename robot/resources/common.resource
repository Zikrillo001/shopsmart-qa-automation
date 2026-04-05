*** Settings ***
Library    Browser

*** Variables ***
${BASE_URL}       https://www.saucedemo.com
${VALID_USER}     standard_user
${VALID_PASS}     secret_sauce
${INVALID_USER}   locked_out_user123
${INVALID_PASS}   wrong_password

*** Keywords ***
Open Login Page
    New Browser    chromium    headless=False
    New Context
    New Page    ${BASE_URL}

Close Browser Session
    Close Browser

Login With Credentials
    [Arguments]    ${username}    ${password}
    Fill Text    id=user-name    ${username}
    Fill Text    id=password     ${password}
    Click        id=login-button

Page Should Be Inventory
    Wait For Elements State    [data-test="inventory-container"]    visible

Error Message Should Be Visible
    Wait For Elements State    [data-test="error"]    visible

Add Backpack To Cart
    Click    id=add-to-cart-sauce-labs-backpack

Cart Badge Should Be
    [Arguments]    ${count}
    Get Text    .shopping_cart_badge    ==    ${count}