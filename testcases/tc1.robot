*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/resources.robot
Suite Setup    browser
Suite Teardown    Close_browser
Test Template    invalid_scenes

*** Test Cases ***
right_username_wrong_password    asmit@gmail.com    xyz
wrong_username_right_password    asmi@gmail.com    admin123
right_username_empty_password    asmit@gmail.com    ${EMPTY}
empty_username_right_password    ${EMPTY}    admin123
right_username_right_password    asmit@gmail.com    admin123

*** Keywords ***
invalid_scenes
    [Arguments]    ${username}    ${password}
    Input_username    ${username}
    Input_password    ${password}
    Click_login_button
    Error_message_is_shown
