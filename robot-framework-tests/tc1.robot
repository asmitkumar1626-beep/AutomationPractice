*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://automationexercise.com/
${browser}      chrome
*** Test Cases ***
LoginTest
    open browser  ${url}    ${browser}
    maximize browser window
    wait until page contains element    //a[normalize-space()='Signup / Login']
    click element    //a[normalize-space()='Signup / Login']
    input text    //input[@data-qa='login-email']     asmitkumar1626@gmail.com
    input text    //input[@placeholder='Password']      asmit7750@
    wait until element is enabled    //button[normalize-space()='Login']
    click element    //button[normalize-space()='Login']
    title should be    Automation Exercise
    scroll element into view    //body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/img[1]
    mouse over    //body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/img[1]
    click element    //div[5]//div[1]//div[1]//div[2]//div[1]//a[1]
    wait until page contains element    //button[normalize-space()='Continue Shopping']
    click element    //button[normalize-space()='Continue Shopping']
    scroll element into view    //body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[16]/div[1]/div[1]/div[1]/img[1]
    mouse over    //body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[16]/div[1]/div[1]/div[1]/img[1]
    click element    //body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[16]/div[1]/div[1]/div[1]/a[1]
    scroll element into view    //body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]
    click element    //body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]
    title should be    Automation Exercise - Checkout
    element should be enabled    //a[normalize-space()='Proceed To Checkout']
    click element    //a[normalize-space()='Proceed To Checkout']
    scroll element into view    //textarea[@name='message']
    wait until page contains element    //textarea[@name='message']
    input text    //textarea[@name='message']     good!!
    click element    //a[normalize-space()='Place Order']
    sleep    4
    close browser


*** Keywords ***
