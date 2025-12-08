*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.flipkart.com/
${browser}  chrome
*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    maximize browser window
    title should be    Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!
    wait until element is visible   /html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input
    element should be enabled    /html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input
    element should be visible    /html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input
    input text    /html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input     asmitkumar7750@gmail.com
    clear element text   /html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input
    close browser
