*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://demowebshop.tricentis.com/
${browser}      chrome


*** Test Cases ***
Logintesst
    launchbrowser   ${url}      ${browser}



*** Keywords ***
launchbrowser
    [Arguments]    ${appurl}     ${browserapp}
    open browser    ${appurl}      ${browserapp}
    maximize browser window

