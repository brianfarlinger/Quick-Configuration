#!/bin/bash
echo -n "VM Name (FQDN): "
read name
echo "$name" > /tmp/hostname.cfg
runuser -l brian -c 'rsync /tmp/hostname.cfg cobbler.lilac.red:/var/www/html/centos-7-install/'
echo -n "RAM: "
read RAM 
echo -n "Use disk existing disk?[y/N]: "
read disk

if [ "$disk" == "yes" -o "$disk" == "y" -o "$disk" == "YES" -o "$disk" == "Y" -o "$disk" == "Yes" ]
        then 
                ls /home/kvm/disks/
                echo -n "Pick a disk:(type name exactly as it appears) "
                read diskname
                virt-install \
                -n $name \
                -r $RAM --vcpus=2 \
                --cpu host \
                --import \
                --os-variant=rhel7 \
                --disk /home/kvm/disks/$diskname \
                --network bridge=br1,mac=RANDOM \
                --nographics \
                --debug \
                --autostart

        else
                echo -n "What size disk would you like to create?:(GB)[10]"
                read disksize && if [ "$disksize" == "" ]; then disksize=10 ; fi
                virt-install \
                -n $name \
                -r $RAM --vcpus=2 \
                --cpu host \
                --location http://cobbler.lilac.red/centos-7-install/mount/ \
                --os-variant=rhel7 \
                --disk pool=disks,size=$disksize \
                --network bridge=br1,mac=RANDOM \
                --nographics \
                --extra-args "ks=http://cobbler.lilac.red/centos-7-install/ks.cfg ksdevice=eth0 console=tty0 console=ttyS0,115200" \
                --debug \
                --autostart
fi
