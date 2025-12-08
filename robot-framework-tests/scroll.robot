*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${browser}      chrome
${url}          https://www.google.com/search?q=sunny+leone+xxx&sca_esv=a2190f49cb9e7b26&udm=2&biw=1707&bih=772&sxsrf=AE3TifMbtb9iVfKT8e0lJprICXd1Go1BYA%3A1756039575342&ei=lwmraP-8FL7H4-EP86-bKQ&ved=0ahUKEwi_5OWYvaOPAxW-4zgGHfPXJgUQ4dUDCBE&uact=5&oq=sunny+leone+xxx&gs_lp=EgNpbWciD3N1bm55IGxlb25lIHh4eDIKEAAYgAQYsQMYCjIKEAAYgAQYsQMYCjIKEAAYgAQYsQMYCjIKEAAYgAQYsQMYCjIKEAAYgAQYsQMYCjINEAAYgAQYsQMYgwEYCjIHEAAYgAQYCjIKEAAYgAQYsQMYCki7DVDUA1jwCHABeACQAQCYAb4CoAG2CKoBBTItMy4xuAEDyAEA-AEBmAIFoALLCMICBxAjGCcYyQLCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIIEAAYChgNGB6YAwCIBgGSBwcxLjAuMy4xoAfDEbIHBTItMy4xuAfECMIHBTAuMi4zyAcS&sclient=img


*** Test Cases ***
scrollingtest
        open browser    ${url}  ${browser}
        maximize browser window
        #execute javascript    window.scrollTo(0,6000)
        scroll element into view    xpath://*[@id="dimg_JwuraIvTGOOuwcsPt9qZmAw_299"]
        sleep       4
