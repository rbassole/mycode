#!/usr/bin/env python3
import shutil
import os

#change directory to the mycode folder
os.chdir('/home/student/mycode/')

#move the file raynor.obj to the ceph_storage directory
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ')

#rename kerrigan.obj file to the new name entred by the user
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
