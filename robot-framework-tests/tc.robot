*** Settings ***
Library    SeleniumLibrary



*** Variables ***



*** Test Cases ***
logintest
    open browser    https://demo.nopcommerce.com/   chrome
    click element    xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    input text    Email     asmitkumar7750@gmail.com
    input text    Password        asmit7750
    click button    xpath://*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button
    sleep   3
    close browser



*** Keywords ***


