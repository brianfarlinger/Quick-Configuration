#!/bin/python
from new-vm.py import *
from libvirt-ks-kvm.conf import *

#Generates a KS file. 
#This KS file is just an example and will not work with your environment. You will need to manually edit this config file. 
def ks_configurator():
  KS = "
install
text
cdrom
lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp --hostname " + NAME + "
rootpw --iscrypted " + ROOTPW + "
firewall --disabled
authconfig --enableshadow --sha-512
selinux --disabled
timezone --utc America/Vancouver
zerombr
clearpart --all --initlabel
part /boot --fstype=xfs --size=512 
part pv.01 --size=1 --grow
volgroup vg00 pv.01
logvol swap --fstype=swap --name=swap --vgname=vg00 --recommended
logvol / --fstype=xfs --name=lv_root --vgname=vg00 --size=1 --grow
bootloader --location=mbr --append="crashkernel=auto rhgb quiet" "console=ttyS0,115200"
user --name=" + LOCALADMIN + " --iscrypted --groups=wheel --password=" + LOCALADMINPW + "
reboot

%packages 
@core
-NetworkManager*
%end

%post --nochroot
%end


%post
#!/bin/bash
yum -y update
yum -y install openssh-server
yum -y install ipa-client
yum -y install vim
yum -y install wget
yum -y install nfs-utils
yum -y install git
yum -y install curl
yum -y install iptables
yum -y install rsync
systemctl enable sshd
systemctl enable nfs-server
systemctl enable rpcbind
systemctl enable nfs-idmap
systemctl enable nfs-lock

echo "192.168.69.10:/mnt/Primary      /mnt/share      nfs     auto    0 0" >> /etc/fstab
echo $hostname > /etc/hostname

hostname=$(curl http://cobbler.lilac.red/centos-7-install/hostname.cfg)
echo "$hostname" > /etc/hostname

d=$(echo "DHCP_HOSTNAME=")
h=$(cat /etc/hostname)
echo $d$h >> /etc/sysconfig/network-scripts/ifcfg-eth0

ipa-client-install --server=freeipa.lilac.red --domain=lilac.red --mkhomedir --hostname=$hostname --principal=join --password=MQIZE10ruI85tVkWaJI5 --unattended
gpasswd -a brian wheel

reboot
%end
"
  return KS
