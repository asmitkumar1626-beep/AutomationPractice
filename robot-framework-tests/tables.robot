*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
LoginTest
    open browser    https://testautomationpractice.blogspot.com/        chrome
    execute javascript    window.scrollTo(0,2000)
    ${tables}      get element count    xpath://table[@name='BookTable']/tbody/tr
    ${gettext}      get text    xpath://table[@name='BookTable']/tbody/tr
    FOR    ${i}   IN    ${tables}
    LOG TO CONSOLE    ${i}
    log to console    ${gettext}
    END
    close browser



