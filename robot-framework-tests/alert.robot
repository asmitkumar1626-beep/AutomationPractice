*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${browser}      chrome


*** Test Cases ***
LoginTest
    open browser    https://testautomationpractice.blogspot.com/        ${browser}
    maximize browser window
    wait until page contains        //button[@id='confirmBtn']
    click button        //button[@id='confirmBtn']
    alert should be present    Press a button!
    handle alert    ACCEPT


*** Keywords ***
