
*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}      https://www.selenium.dev/selenium/web/web-form.html
*** Test Cases ***
LoginTest
    open browser    ${url}  chrome
    wait until element is visible    //input[@id='my-text-id']
    input text    //input[@id='my-text-id']     hello
    input text    //input[@name='my-password']      madhuri
    input text    //textarea[@name='my-textarea']   yang midu phonk
    element should be disabled    //input[@placeholder='Disabled input']
    select from list by label    //select[@name='my-select']    One
    input text    //input[@placeholder='Type to search...']     New York
    choose file    //input[@name='my-file']     C:/selenium/goofy/practice/prac56.py
    element should be enabled    //input[@id='my-check-1' ]
    select checkbox    //input[@id='my-check-2']
    element should be enabled    //input[@id='my-check-2']
    element should be enabled    //input[@id='my-radio-1']
    click element    //input[@id='my-radio-2']
    Execute Javascript    document.querySelector("input[name='my-range']").value = 8;
    Execute Javascript    document.querySelector("input[value='#563d7c']").value = "#57fb2b";
    element should be visible    //button[normalize-space()='Submit']
    click element    //button[normalize-space()='Submit']
