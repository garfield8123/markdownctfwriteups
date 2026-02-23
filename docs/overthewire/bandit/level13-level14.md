# Level 14

Bandit OverTheWire Level 14: [level 14](https://overthewire.org/wargames/bandit/bandit14.html)

## **Level Goal**
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

## **Walkthrough**
- Figure out ssh keys work in authenitcation for ssh
- Figure out key permissions for ssh 

## **level 14 Solution**
```shell
cat bandit14.key
# copy bandit14.key to local machine
chmod 400 bandit14.key
ssh -i bandit14.key bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14
```

## **Generated password for level 14**
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
