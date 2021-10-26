#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import getpass
import os

while True:
    ex = input("Continue? (Y/n)").lower()
    if ex == "n" or ex == "no":
        break
    IP=input("Enter the IP address of the machine you would like to connect to: ")
    user= input("Enter the username: ")
    pwd= getpass.getpass("Enter the password: ")
    ## where to connect to
    t = paramiko.Transport( IP , 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=user, password=pwd)

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection
