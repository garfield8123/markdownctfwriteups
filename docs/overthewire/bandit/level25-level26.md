# Level 26

Bandit OverTheWire Level 26: [level 26](https://overthewire.org/wargames/bandit/bandit26.html)

## **Level Goal**
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

## **Walkthrough**
- Figure out what shell the user could be using?
- Figure out vim shortcuts as vim could give you priveilege esclation
- Figure out the less/more command linux

## **level 26 Solution**
```shell
getent passwd bandit26
# shows us the shell being using by bandit26 is /usr/bin/showtext
 cat /usr/bin/showtext
# seems to be the ssh key for bandit26, which seems like we solved it, but the shell isn't /usr/bin
cat bandit26.sshkey 
#copy the contents to your local machine 
chmod 400 bandit26.key

ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220 

#if the window is too big it will just show and exit, but what if we make the window smaller and take use of the less command 

#---- press v to go into vim ----

#---- Keys to type for vim ----
:e /etc/bandit\_pass/bandit26 (view the password)
set shell before opening shell (default open in normal getent shell)
:set shell=/bin/bash
:shell (Opens a shell terminal)
#---- Should get shell ----
cat /etc/bandit_pass/bandit26
```

## **Generated password for level 26**
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
