# Level 24

Bandit OverTheWire Level 24: [level 24](https://overthewire.org/wargames/bandit/bandit24.html)

## **Level Goal**
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## **Walkthrough**
- Figure out how to concat a command result to a file in shell

## **level 24 Solution**
```shell
cat /etc/cron.d/cronjob_bandit24

cat /usr/bin/cronjob_bandit24.sh

#figures out is runs and deletes all the files in /var/spool/bandit24/foo

# make a temp directory
mktemp -d /tmp/helloXXX

#create a shell script in /tmp/helloXXX

cat /etc/bandit_pass/bandit24 > /tmp/helloXXX/password

#this allows any user to execute the script 
chmod 777 test.sh 

#copy the shell file to the /var/spool/bandit24/foo so it runs and deletes the file 
cp test.sh /var/spool/bandit24/foo/

# wait 1 minute

cat /tmp/helloXXX/password
```

## **Generated password for level 24**
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
