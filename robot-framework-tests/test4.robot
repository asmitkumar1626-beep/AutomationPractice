*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php
${bro}  chrome
*** Test Cases ***
LoginTest
    open browser    ${url}      ${bro}
    maximize browser window
    input text    //input[@id='name']   asmit
    input text    //input[@id='email']  asmitkumar7750@gmail.com
    element should be visible    //input[@id='gender']
    click element    //input[@id='gender']
    element should be enabled    //input[@id='gender']
    input text    //input[@id='mobile']     9937148895
    click element    //input[@id='dob']
    input text    //input[@id='dob']    11
    sleep    2
    input text    //input[@id='dob']    22
    sleep    2
    input text    //input[@id='dob']    2003
    input text    //input[@id='subjects']   CS
    wait until element is visible    //input[@id='hobbies']
    click element    //input[@id='hobbies']
    input text    //input[@id='picture']    C:/selenium/goofy/practice/prac40.py
    input text    //textarea[@id='picture']     bad bad bad bad bad bad bad
    select from list by value    id:state      Uttar Pradesh
    select from list by value    id:city        Lucknow
    wait until element is visible    //input[@value='Login']
    click element    //input[@value='Login']
    sleep    4



