#!/usr/local/bin/python3
import shutil
import os

#Change directory to /home/student/mycode/
os.chdir('/home/student/mycode/')

#copy the sdn_network.txt file to a new directory and rename it sdn_network.txt.copy
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
shutil.copytree('5g_research/', '5g_research_backup/')
