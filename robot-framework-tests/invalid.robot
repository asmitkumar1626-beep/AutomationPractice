*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/resources.robot
Suite Setup    openmybrowser
Suite Teardown    closemybrowser
Task Template    invalid login


*** Test Cases ***
right username empty password       admin@yourstore.com         ${EMPTY}
right username wrong password       admin@yourstore.com          admin1
wrong username wrong password       admi@yourstore.com           admin1
wrong username empty password       admi@yourstore.com           ${EMPTY}
wrong username right password       admi@yourstore.com          admin



*** Keywords ***
invalid login
    [Arguments]    ${username}      ${password}
    enterusername       ${username}
    enterpassword        ${password}
    login
    invalidlogin


