# Level 19

Bandit OverTheWire Level 19: [level 19](https://overthewire.org/wargames/bandit/bandit19.html)

## **Level Goal**
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## **Walkthrough**
- Figure out how to run other commands for ssh in conjunction

## **level 19 Solution**
```shell
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

## **Generated password for level 19**
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
