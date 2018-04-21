#! /usr/bin/python

print("Patrycja")

import paramiko # wczytuje paramiko

x=paramiko.SSHClient()
type(x)
x.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # by akceptowal zew.klucze
x.connect("localhost", username='tester01', password="testpati123") # laczymy sie
# a,b,c=x.exec_command("uname -a") # wywolywanie komendy
a,b,c=x.exec_command("cat /etc/passwd")
print b.read(),
