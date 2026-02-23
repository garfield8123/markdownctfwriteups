# Level 22

Bandit OverTheWire Level 22: [level 22](https://overthewire.org/wargames/bandit/bandit22.html)

## **Level Goal**
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## **Walkthrough**
- Figure out what Cron does in Linux
- Figure out what a cronjob does

## **level 22 Solution**
```shell
# Look at the cronjob associated with bandit 22
cat /etc/cron.d/conjob_bandit22

# Figure out it runs the following script 
cat /usr/bin/cronjob_bandit22.sh

# View the file it copies the contents to /etc/bandit_pass/bandit22
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

## **Generated password for level 22**
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
