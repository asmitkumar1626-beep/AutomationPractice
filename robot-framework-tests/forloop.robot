*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
For Loop With Exit
    @{items}    Create List    rama    harri    giga    munu    lulu
    FOR    ${i}    IN    @{items}
        Log To Console    ${i}
        Exit For Loop If    '${i}' == 'giga'
    END
