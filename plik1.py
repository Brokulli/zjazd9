#! /usr/bin/python

print("Patrycja")

import paramiko

x=paramiko.SSHClient()
type(x)
x.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x.connect("localhost", username='tester01', password="testpati123")
a,b,c=x.exec_command("uname -a")
print b.read(),
