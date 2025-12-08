*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}      https://www.google.com/
${browser}      chrome
*** Test Cases ***
mouse
    openbrowserd    ${url}  ${browser}
    input text    APjFqb    xnxx.com
    click button    xpath:/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[1]
    sleep   3


*** Keywords ***
openbrowserd
    [Arguments]    ${appurl}       ${appbrowser}
    open browser    ${appurl}       ${appbrowser}
    maximize browser window

