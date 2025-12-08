*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://demoqa.com/automation-practice-form
${browser}  chrome
*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    maximize browser window
    input text    //input[@id='firstName']  asmit
    input text    //input[@id='lastName']   kumar
    input text    //input[@id='userEmail']  asmitkumar7750@gmail.com
    scroll element into view    //label[normalize-space()='Female']
    execute javascript    window.scrollBy(0,-200)
    click element    //label[normalize-space()='Female']
    input text    //input[@id='userNumber']     9937148895
    scroll element into view    //input[@id='dateOfBirthInput']
    execute javascript    window.scrollBy(0, -250)
    click element    id:dateOfBirthInput
    click element    .react-datepicker__month-select
    select from list by label    .react-datepicker__month-select    March
    click element    //select[@class='react-datepicker__year-select']
    select from list by label    .react-datepicker__year-select     1902
    click element    //div[contains(@class,'day') and text()=15]
    sleep    4

