*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}   https://letcode.in/home
${bro}  chrome
*** Test Cases ***
LoginTest
    open browser    ${url}  ${bro}
    maximize browser window
        Execute Javascript
    ...    var iframes = document.querySelectorAll('iframe');
    ...    function removeAllFrames(frames) {
    ...        for (var i = 0; i < frames.length; i++) {
    ...            try {
    ...                if (frames[i].contentDocument) {
    ...                    removeAllFrames(frames[i].contentDocument.querySelectorAll('iframe'));
    ...                }
    ...            } catch(e){}
    ...            frames[i].remove();
    ...        }
    ...    }
    ...    removeAllFrames(iframes);



    Scroll Element Into View    //button[contains(text(),'₹ 109.95')]
    wait until element is visible    //button[contains(text(),'₹ 109.95')]
    click element    //button[contains(text(),'₹ 109.95')]
    wait until element is visible    //span[normalize-space()='Add to Cart']
    click element    //span[normalize-space()='Add to Cart']
    go back


    Scroll Element Into View        //button[contains(text(),'₹ 22.3')]
    wait until element is visible    //button[contains(text(),'₹ 22.3')]
    click element   //button[contains(text(),'₹ 22.3')]
    wait until element is visible    //span[normalize-space()='Add to Cart']
    click element    //span[normalize-space()='Add to Cart']
    go back

    scroll element into view    //button[@class='button is-pulled-right']
    wait until element is visible    //button[@class='button is-pulled-right']
    click element    //button[@class='button is-pulled-right']
    wait until element is visible    //button[normalize-space()='Checkout']
    click element    //button[normalize-space()='Checkout']


    handle alert    ACCEPT

    wait until element is visible    //button[normalize-space()='Continue Shopping']
    click element    //button[normalize-space()='Continue Shopping']
    close browser
