*** Settings ***
Library    SeleniumLibrary


*** Variables ***




*** Test Cases ***
LoginTest

    open browser    https://www.youtube.com/   chrome
    maximize browser window
    loginyoutube
    close browser


*** Keywords ***
loginyoutube
    input text    //input[@placeholder='Search']    hello
    click button    //button[@title='Search']//div



