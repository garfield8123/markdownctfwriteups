# Level 30

Bandit OverTheWire Level 30: [level 30](https://overthewire.org/wargames/bandit/bandit30.html)

## **Level Goal**
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

## **Walkthrough**
- git change branches and analyzing git

## **level 30 Solution**
```shell
mktemp -d /tmp/helloXXX

git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo

#password is: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

cat repo/README
#nothing 

git show 
#nothing
git logs
#nothing
git branch -r
#potential branch called dev
git checkout dev

cat README.md
```

## **Generated password for level 30**
qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
