*** Settings ***
Library    SeleniumLibrary



*** Test Cases ***
tabbed
    open browser    https://demo.automationtesting.in/Windows.html      chrome
    click element    xpath://*[@id="Tabbed"]/a/button
    switch window    title=Selenium
    click element    xpath://*[@id="main_navbar"]/ul/li[2]/a/span
    sleep   3
    close browser