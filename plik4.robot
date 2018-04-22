*** Variables ***
${MESSAGE}  Hello Patrycja!

*** Test Cases ***
My test 01
  My log

*** Keywords ***
My log
  Log to console  ${MESSAGE}
