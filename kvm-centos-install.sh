#! /bin/bash
echo -n "Hostname: "
read hostname
echo $hostname > /tmp/hostname
virt-install \
-n $hostname \
-r 1024 --vcpus=2 \
--cpu host \
--cdrom=/var/lib/libvirt/images/CentOS-7-x86_64-Minimal-1511.iso \
--os-variant=rhel7 \
--disk pool=libvirt-images,size=8 \
--network bridge=virbr0,mac=RANDOM \
--nographics \
-x "ks=/var/lib/libvirt/scripts/ks.cfg"
