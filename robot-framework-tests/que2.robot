*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}  https://www.saucedemo.com/
*** Test Cases ***
LoginTest
    open browser    ${url}  chrome
    input text    //input[@id='user-name']  asmit
    wait until element is visible    //input[@id='user-name']
    log to console    username done
    input text    //input[@id='password']   asmit
    wait until element is visible    //input[@id='password']
    log to console    password done
    click element    //input[@id='login-button']
    wait until element is visible    //input[@id='login-button']
    log to console    button present