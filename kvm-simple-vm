#! /bin/bash
virt-install -n ansible -r 1024 --vcpus=1 --cpu host --cdrom=/var/lib/libvirt/images/CentOS-7-x86_64-Minimal-1511.iso --os-variant=rhel7 --disk pool=libvirt-images,size=8 --network bridge=virbr0,mac=RANDOM --graphics vnc
