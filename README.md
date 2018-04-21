- z pbone pobieramy: python2-paramiko-1.16.1-2.el7.noarch.rpm
- następnie doinstalowujemy to czego brakuje
- w terminalu:
    python
- potem (mówimy pythonowi by korzystał z ssh)
    import paramiko
- ssh_localhost (hasło: adam)
- (na su - sprawdzamy czy działa ssh) systemch status.sshs.service
- dodawanie nowego użytkownika tester01 (na su)
    adduser tester01
    passwd tester01 (zmiana hasła dla tester01)

# SSH Library - exercise
piszemy program, który sprawdzi czy mamy "ownuser"

  1. tworzymy plik1.py
    na początku pliku .py musi być zawsze: #! /usr/bin/python

    # komenda w terminalu: chmod 755 nazwaPliku.py zmienia uprawnienia

    plik1.py na podstawie SSH Example
    # tworząc plik odwołujemy się do wcześniej utworzonego użytkownika
