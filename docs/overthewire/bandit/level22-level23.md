# Level 23

Bandit OverTheWire Level 23: [level 23](https://overthewire.org/wargames/bandit/bandit23.html)

## **Level Goal**
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

## **Walkthrough**
- Figure out how the echo command works
- Figure out what the md5sum command does and what it calculates
- Figure out what the command whoami does

## **level 23 Solution**
```shell
cat /etc/cron.d/cronjob_bandit23

#view the running script
cat /usr/bin/cronjob_bandit23.sh

# Figure out this is the $mytarget variable
echo I am user bandit23 | md5sum | cut -d ' ' -f 1  

$mytarget = 8ca319486bfbbc3663ea0fbe81326349

#view the contents storing to /etc/bandit_pass/bandit23
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

## **Generated password for level 23**
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
