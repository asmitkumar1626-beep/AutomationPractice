*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome

*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    maximize browser window
    click element    //a[normalize-space()='Log in']
    input text    xpath://input[@id='Email']    asmitkumarkanar
    input password    xpath://input[@id='Password']  1234567890
    select checkbox    xpath://input[@id='RememberMe']
    checkbox should be selected     xpath://input[@id='RememberMe']
    sleep    4

    click button    xpath://button[normalize-space()='Log in']

*** Keywords ***

