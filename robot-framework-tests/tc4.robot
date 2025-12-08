*** Settings ***
Library    SeleniumLibrary


*** Variables ***


*** Test Cases ***
Logintc
    open browser    https://demowebshop.tricentis.com/      chrome
    maximize browser window
    capture element screenshot    //img[@alt='Tricentis Demo Web Shop']     C:\selenium\goofy\login.png
    close browser


*** Keywords ***
