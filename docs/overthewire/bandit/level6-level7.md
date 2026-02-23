# Level 7

Bandit OverTheWire Level 7: [level 7](https://overthewire.org/wargames/bandit/bandit7.html)

## **Level Goal**
The password for the next level is stored somewhere on the server and has all of the following properties:

    owned by user bandit7
    owned by group bandit6
    33 bytes in size


## **Walkthrough**
- Figure out how to to add user to find command
- Figure out how to add group to find command
- Figure out how to add size to find command

## **Level 7 Solution**
``` shell
find / -type f -group bandit6 -user bandit7 -size 33c -readable ! -executable -exec file {} + | grep 'text'

cat /var/lib/dpkg/info/bandit7.password
```

## **Generated password for level 7**
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
