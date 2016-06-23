#!/bin/bash

virsh list --all

echo -n "Which VM would you like to delete?: "
read VMname
virsh list --all | grep $VMname | grep -qi "running" && state="yes"
if [ $state == "yes" ]
        then
                echo "Please wait while we shutdown the $VMname."
                virsh shutdown $VMname
                echo "VM is now shutdown"
        else
                echo "$VMname is already shutdown."
fi

echo -n "Proceed to delete $VMname and all related files? [Y/n]?"
read input

if [ "$input" == "n" -o "$input" == "no" -o "$input" == "No" -o "$input" == "NO" -o "$input" == "N" ]
        then
                echo "Now exiting"
        else
                echo "Destorying $VMname"
                virsh destroy $VMname
                virsh undefine $VMname
                echo "Success"
fi
