# Level 20

Bandit OverTheWire Level 20: [level 20](https://overthewire.org/wargames/bandit/bandit20.html)

## **Level Goal**
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## **Walkthrough**
- Figure out Set ID can be exploited. S chmod 
- Set ID privlege esclation and what user it runs the command

## **level 20 Solution**
```shell
 cat ./bandit20-do

 ./bandit20-do id 
 # shows the id of the current user

# executible as it shows id
 ./bandit20-do cat /etc/bandit_pass/bandit20

 ```

## **Generated password for level 20**
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
