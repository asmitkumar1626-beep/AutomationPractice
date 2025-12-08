*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}  https://demoqa.com/automation-practice-form
${browser}  chrome
*** Test Cases ***
LoginTest

    open browser    ${url}  ${browser}
    maximize browser window
    title should be    DEMOQA
    input text    xpath://input[@id='firstName']    asmit
    input text    //input[@id='lastName']   kumar
    input text    //input[@id='userEmail']  asmitkumar7750@gmail.com
    scroll element into view    //label[normalize-space()='Female']
    click element    //label[normalize-space()='Female']
    input text    xpath://input[@id='userNumber']   9937148895

    sleep    3
    close browser