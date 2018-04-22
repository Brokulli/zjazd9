*** Settings ***
Library  SSHLibrary
Suite Setup  Open Connection And Log In
Suite Teardown  Close All Connections

*** Variables ***
${MESSAGE01}  Hello Patrycja!
${REMOTE_HOST}  localhost
${REMOTE_USERNAME}  tester
${REMOTE_PASSWORD}  adam

*** Test Cases ***
My test 01
  My log 01

My test 02
  My log 02  jakis glupi tekst

My test 03
  My log 03

My test 04 SSH
  Open Connection And Log In

*** Keywords ***
My log 01
  Log to console  ${MESSAGE01}

My log 02
  [Arguments]  ${MESSAGE02}
  Log to console  ${MESSAGE02}

My log 03
  Log to console  Goodbye

Open Connection And Log In
  Open Connection  ${REMOTE_HOST}
  Login  ${REMOTE_USERNAME}   ${REMOTE_PASSWORD}
