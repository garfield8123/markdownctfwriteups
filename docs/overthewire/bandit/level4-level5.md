# Level 5

Bandit OverTheWire Level 5: [level 5](https://overthewire.org/wargames/bandit/bandit5.html)

## **Level Goal**
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

## **Walkthrough**
- Figure out how the find command works
- Figure out how to add type in find 
- Figure out how to find human readable text

## **Level 5 Solution**
```shell
for file in $(find . -name "*-file0*"); do
  cat "$file"
  echo
done
# or 
find inhere/ -type f -readable -exec file {} + | grep 'text'

cat ./-file0*
```

## **Generated password for level 5**
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
