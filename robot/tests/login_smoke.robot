*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Login Page
Suite Teardown    Close Browser Session

*** Test Cases ***
Valid Login Should Open Inventory Page
    [Documentation]    Verify that a standard user can log in successfully.
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Page Should Be Inventory