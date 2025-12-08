*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.saucedemo.com/
*** Test Cases ***
Logintest
    open browser    ${url}  chrome
    wait until element is visible    //input[@id='user-name']
    input text    //input[@id='user-name']  standard_user
    wait until element is visible    //input[@id='password']
    input text    //input[@id='password']   secret_sauce
    click element    //input[@id='login-button']
    log to console    DONE!!!

