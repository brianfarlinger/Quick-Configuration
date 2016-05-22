#!/bin/bash
echo "Hostname(FQDN): "
read hostname
echo $hostname > /etc/hostname


d=$(echo "DHCP_HOSTNAME=")
h=$(cat /etc/hostname)
echo $d$h >> /etc/sysconfig/network-scripts/ifcfg-eth0

ipa-client-install --server=freeipa.lilac.red --domain=lilac.red --mkhomedir --hostname=$hostname --principal=admin
gpasswd -a brian wheel
