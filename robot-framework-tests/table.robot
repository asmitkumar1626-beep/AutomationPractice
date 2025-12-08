*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.w3schools.com/html/html_tables.asp
*** Test Cases ***
LoginTest
    open browser    ${url}  chrome
    ${webelements}  get webelements    //table[@id='customers']//tbody//tr
    FOR    ${webelement}   IN   @{webelements}
        ${text}     get text    ${webelement}
        log to console    ${text}
        exit for loop
    END
    close browser



