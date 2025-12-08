*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
nav
    open browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login         chrome
    ${loc}      get location
    log to console    ${loc}
    sleep       3

    capture page screenshot    C:/python/logo2.png



