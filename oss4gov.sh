#!/bin/bash
WORKGROUP="VILNIUS"
REALM="VILNIUS.VILNIUS.LT"
DC="DC1.VILNIUS.VILNIUS.LT"
DOMADM="a.stankevic@VILNIUS.VILNIUS.LT"

# download configs
cat templates/krb5.conf | sed -E "s/__REALM__/${REALM}/g" > /etc/krb5.conf
cat templates/smb.conf | sed -E "s/__WORKGROUP__/${WORKGROUP}/g" | sed -E "s/__REALM__/${REALM}/g" > /etc/samba/smb.conf
cat templates/nsswitch.conf > /etc/nsswitch.conf

# install software
export DEBIAN_FRONTEND=noninteractive  
apt-get update > /dev/null
apt-get install -fqqy -o Dpkg::Options::='--force-confold' winbind samba krb5-user libnss-winbind libpam-winbind

# join the AD
kinit ${DOMAMD}
net ads join -S ${DC} -U ${DOMADM} 

# fix pam for AD integration
pam-auth-update --force --package
cat templates/common-session > /etc/pam.d/common-session

# make lightdm allow you to log in with custom username
cat templates/lightdm.conf > /usr/share/lightdm/lightdm.conf.d/50-ad.conf

# restart services
service winbind stop
service samba stop
service samba start
service winbind start

# reboot ?
