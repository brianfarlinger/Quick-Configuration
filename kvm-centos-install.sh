#! /bin/bash
echo -n "Hostname: "
read hostname
echo -n "Ram: "
read RAM 
virt-install \
-n $hostname \
-r $RAM --vcpus=2 \
--cpu host \
#--cdrom=/var/lib/libvirt/images/CentOS-7-x86_64-Minimal-1511.iso \
--location http://cobbler.lilac.red/CentOS-7-x86_64-Minimal-1511.iso \
--os-variant=rhel7 \
--disk pool=libvirt-images,size=8 \
--network bridge=virbr0,mac=RANDOM \
--nographics \
--extra-args "http://cobbler.lilac.red/ks.cfg ksdevice=eth0 console=tty0 console=ttyS0,115200" \
--debug
