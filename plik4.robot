*** Settings ***
Library SSHLibrary

*** Variables ***
${MESSAGE01}  Hello Patrycja!

*** Test Cases ***
My test 01
  My log 01

My test 02
  My log 02  jakis glupi tekst

My test 03
  My log 03

*** Keywords ***
My log 01
  Log to console  ${MESSAGE01}

My log 02
  [Arguments]  ${MESSAGE02}
  Log to console  ${MESSAGE02}

My log 03
  Log to console  Goodbye
