# Level 29

Bandit OverTheWire Level 29: [level 29](https://overthewire.org/wargames/bandit/bandit29.html)

## **Level Goal**
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

## **Walkthrough**
- Figure out git commands
- Figure out how to use older versions of git repos

## **level 29 Solution**
```shell
mktemp -d /tmp/helloXXX

git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo

# password is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

cat repo/README
# shows it has been changed to not show the password

git log
# Shows all the commits to this repo and see one potential holding the password

#use the commit hash
git checkout 73f5d0435070c8922da12177dc93f40b2285e22a

cat README.md
```

## **Generated password for level 29**
cat README.md
