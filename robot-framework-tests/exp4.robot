*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://duckduckgo.com/
${browser}  chrome
*** Test Cases ***
LoginTest

    open browser    ${url}  ${browser}
    wait until element is visible    //input[@id='searchbox_input']
    input text  //input[@id='searchbox_input']    robotframework
    click element    //button[@aria-label='Search']//*[name()='svg']
    assert page contains
    sleep    4
