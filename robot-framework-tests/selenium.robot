*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.selenium.dev/
*** Test Cases ***
Logintest
    open browser    ${url}  chrome
    ${items}    Get WebElement  //ul[@class='navbar-nav mr-4 mb-2 mb-lg-0 ps-4 ps-lg-2']//li
    FOR    ${item}   IN     ${items}
    ${text}     get text    ${item}
    log to console    ${text}

    END
    close browser

