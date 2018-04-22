*** Variables ***
${MESSAGE}  Hello Patrycja!

*** Test Cases ***
My test 01
  My log 01

My test 02
  My log 02

*** Keywords ***
My log 01
  Log to console  ${MESSAGE}

My log 02
  Log to console  Goodbye
