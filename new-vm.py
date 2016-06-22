#!/bin/python
import sys
import virtinst.util
import subprocess
from libvirt-ks-vm.conf import *

NAME = raw_input("VM Name (FQDN): ")
MAC = virtinst.util.randomMAC()
RAM = raw_input("RAM: ")
CPU = raw_input("Number of vCPUs: ")
FRESHDISK = query_yes_no(Create a fresh disk?)

if FRESHDISK is True:
  DISKSIZE = disk_size_selector()
  produce_ks_cfg()
  KSFILE="ks-" + MAC + ".cfg"
  create_vm(1)
  
if FRESHDISK is False:
  DISKNAME = disk_image_select()
  create_vm(2)

def create_vm(option):
  name_vm = " -n " + NAME
  cpu_vm = " -r " + RAM + "--cpu host --vcpus=" + CPU
  location_vm = " --location http://cobbler.lilac.red/centos-7-install/mount/"
  os_vm = " --os-variant=rhel7"
  disk_pool_vm = " --disk pool=disks,size=" + DISKSIZE
  disk_vm = " --disk /home/kvm/disks/" + DISKNAME
  network_vm = " bridge= br1,mac=" + MAC
  nographics = " --nographics"
  extra-args = " --extra-args='ks=http://cobbler.lilac.red/centos-7-install/" + KSFILE + " ksdevice=eth0 console=tty0 console=ttyS0,115200'"
  debug = " --debug"
  autostart = " --autostart"
  disk_import = " --import"
  if option == 1:
    subprocess.Popen("virt-install" + name_vm + cpu_vm + location_vm + os_vm + disk_vm + network_vm + nographics + extra-args + debug + autostart)
  elif option == 2:
    subprocess.Popen("virt-install" + name_vm + cpu_vm + disk_import + os_vm + disk_vm + network_vm + nographics + debug + autostart)

def disk_image_selector():
  question = "Please select a disk from the list below"
  disk_location = "/home/kvm/disks/"
  while True:
    sys.stdout.write(question)
    subprocess.Popen("ls " + disk_location)
    choice = raw_input()
    return choice
    
def disk_size_selector():
  question = "What size disk would like you to create? (Enter GB) [10]"
  while True:
    sys.stdout.write(question)
    choice = raw_input()
    if choice.isdigit() == True:
      return choice
    else: 
      sys.stdout.write("Please respond with a valid number. ie) 8")

def query_yes_no(question):
  valid = {"yes": True, "y": True, "ye": True,
    "no": False, "n": False}
  prompt = " [Y/n] "
  while True:
    sys.stdout.write(question + prompt)
    choice = raw_input().lower()
    if choice == '':
      return valid[default]
    elif choice in valid:
      return valid[choice]
    else:
      sys.stdout.write("Please respond with 'yes' or 'no')

def produce_ks_cfg():
  file = "ks-" + MAC + ".cfg"
  with open "/home/kvm/kickstart/" + file, 'a'):
    file.write(
  transfer_file("home/kvm/kickstart/" + file):
    
def transfer_file(file):
  subprocess.call("transfer.sh")
  







