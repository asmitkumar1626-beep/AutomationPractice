*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}          https://demo.nopcommerce.com/
${BROWSER}      chrome
${EMAIL}        asmitkumar7750@gmail.com
${PASSWORD}     asmit7750

*** Test Cases ***
Login Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    xpath=//a[@class='ico-login']
    Input Text       id=Email       ${EMAIL}
    Input Text       id=Password    ${PASSWORD}
    Click Button     xpath=//button[@class='button-1 login-button']
    Wait For Alert    5
    ${alert_text}=    Get Alert Message
    Log    Alert message: ${alert_text}
    Handle Alert    accept
    Sleep    2
    Close Browser

