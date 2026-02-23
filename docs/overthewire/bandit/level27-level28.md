# Level 28

Bandit OverTheWire Level 28: [level 28](https://overthewire.org/wargames/bandit/bandit28.html)

## **Level Goal**
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

## **Walkthrough**
- Figure out ssh github works
- Look into connecting github ssh: [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- Figure out how git works 

## **level 28 Solution**
```shell
mktemp -d /tmp/helloXXX
/tmp/helloXXX

git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo

# password: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

cat repo/README

```

## **Generated password for level 28**
Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
