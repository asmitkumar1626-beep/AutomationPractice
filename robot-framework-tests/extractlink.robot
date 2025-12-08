*** Settings ***
Library    SeleniumLibrary


*** Variables ***



*** Test Cases ***
extract
    open browser    https://toppornsites.com/       chrome
    maximize browser window
    ${count}        get element count    xpath://a
    log to console    ${count}

      FOR     ${i}     IN RANGE    1   ${count}
             ${links}      get text    xpath:(//a)[${i}]
               log to console    ${links}
      END


*** Keywords ***
