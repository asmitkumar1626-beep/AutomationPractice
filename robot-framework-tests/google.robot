*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.google.com/
*** Test Cases ***
LoginTest
    open browser    ${url}  chrome
    title should be    Google
    log to console    It is google
