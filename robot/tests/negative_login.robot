*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Login Page
Suite Teardown    Close Browser Session

*** Test Cases ***
Invalid Login Should Show Error Message
    [Documentation]    Verify that invalid credentials show an error.
    Login With Credentials    ${INVALID_USER}    ${INVALID_PASS}
    Error Message Should Be Visible