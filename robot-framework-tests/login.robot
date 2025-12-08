*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
LoginTest
    Open Browser    https://www.saucedemo.com/    chrome
    Input Text    //input[@id='user-name']    standard_user
    Input Password    //input[@id='password']    secret_sauce
    Wait Until Element Is Enabled    //input[@id='login-button']
    Click Element    //input[@id='login-button']
    Sleep    3
    Wait Until Page Contains    Swag Labs
    Title Should Be    Swag Labs
    Log To Console    Logged in
    Click Element    //button[@id='add-to-cart-sauce-labs-backpack']
    Scroll Element Into View    //button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']
    Wait Until Element Is Visible    //button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']
    Click Element    //button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']
    Wait Until Element Is Visible    //button[@id='react-burger-menu-btn']
    Click Element    //button[@id='react-burger-menu-btn']
    Wait Until Element Is Visible    //button[@id='react-burger-cross-btn']
    Click Element    //button[@id='react-burger-cross-btn']
    Select From List By Index    //select[@class='product_sort_container']    3
    Wait Until Element Is Visible        //button[@id='add-to-cart-sauce-labs-onesie']
    Click Element    //button[@id='add-to-cart-sauce-labs-onesie']
    Wait Until Element Is Visible        //a[@class='shopping_cart_link']
    Click Element    //a[@class='shopping_cart_link']
    Wait Until Element Is Visible    //button[@id='checkout']
    Click Element    //button[@id='checkout']
    Wait Until Element Is Visible        //input[@id='first-name']
    Input Text    //input[@id='first-name']    asmit
    Input Text    //input[@id='last-name']    kumar
    Input Text    //input[@id='postal-code']    751016
    Wait Until Element Is Enabled    //input[@id='continue']
    Click Element    //input[@id='continue']
    ${price}=    Get Text    //div[@class='summary_total_label']
    Log To Console    price is ${price}
    Wait Until Element Is Enabled    //button[@id='finish']
    Click Element    //button[@id='finish']
    Close Browser


