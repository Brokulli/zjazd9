#! /usr/bin/python

import paramiko # wczytuje paramiko

x=paramiko.SSHClient()
type(x)
x.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # by akceptowal zew.klucze
x.connect("localhost", username='tester01', password="testpati123") # laczymy sie
# a,b,c=x.exec_command("uname -a") # wywolywanie komendy
a,b,c=x.exec_command("cat /etc/passwd") # zmiana wywolywanej komendy
wynik = b.read()
listaElementow = wynik.split('\n') # tnie na linijki

# print(wynik) 

for element in listaElementow: # szukamy elementu w liscie
    if element.find("tester01")>=0:
        print("element find, user 'tester01' exists")
        break
    # else:
    #     print("element not found")

print("Hello Patrycja")
