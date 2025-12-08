*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
LoginTest
    open browser    https://demowebshop.tricentis.com/register      chrome
    select radio button    Gender       M
    input text      //input[@id='FirstName']    Asmit kumar kanar
    input text    //input[@id='LastName']       jhingur
    input text    //input[@id='Email']      asmitkumar7750@gmail.com
    input password    //input[@id='Password']       asmit7750@
    input password    //input[@id='ConfirmPassword']    asmit7750@
    click button    //input[@id='register-button']
    sleep    5
    handle alert    accept
    sleep    3
    close browser

