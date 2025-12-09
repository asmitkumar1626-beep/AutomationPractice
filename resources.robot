*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://admin-demo.nopcommerce.com/login
${browser}    chrome

*** Keywords ***
browser
    Open Browser     ${url}    ${browser}    options=add_argument("--disable-blink-features=AutomationControlled")
    Maximize Browser Window
login
    Click Link    Log in
    Wait Until Element Is Visible    //input[@id='Email']
input_username
    [Arguments]    ${username}
    Input Text    //input[@id='Email']    ${username}
input_password
    [Arguments]    ${password}
    Input Text    //input[@id='Password']    ${password}
close_browser
    Close All Browsers
click_login_button
    Wait Until Element Is Enabled    //button[normalize-space()='Log in']
    Click Button    //button[normalize-space()='Log in']
error_message_is_shown
    Page Should Contain    Login was unsuccessful. Please correct the errors and try again.
login_succesfull
    Page Should Contain    Welcome to our store


