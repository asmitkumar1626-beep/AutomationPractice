*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${browser1}     https://www.google.com/
${browser2}     https://www.bing.com/
${b}        chrome


*** Test Cases ***
multiple
    open browser    ${browser1}     ${b}
    maximize browser window
    sleep       3
    open browser    ${browser2}     ${b}
    maximize browser window
    sleep    2
    switch browser    1
    ${title1}   get title
    log to console    ${title1}
    switch browser    2
    ${title2}   get title
    log to console    ${title2}
    close all browsers
