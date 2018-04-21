#! /usr/bin/python

import paramiko # wczytuje paramiko
import re # import biblioteki wyrazen regularnych

print("Hello Patrycja")

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
    if element.find("tester01")>=0: # jesli znajdzie to print i break
        print("element find, user 'tester01' exists")
        break # jesli nie znajdzie to else i print
else:
    print("element not found, user 'tester01' not exists")

for element in listaElementow: # szukamy elementu, ktory nie istnieje w liscie
    if element.find("myownuser")>=0:
        print("element find, user 'myownuser' exists")
        break
else:
    print("element not found, user 'myownuser' not exists")

# z wykorzystaniem wyrazen regularnych (wczesniej nalezy je zaimportowac)

for element in listaElementow: # szukamy elementu w liscie
    if re.search("tester01",element): # warunek jako wyrazenie regularne
        print("element find, user 'tester01' exists")
        break # jesli nie znajdzie to else i print
else:
    print("element not found, user 'tester01' not exists")


print("Goodbye")
