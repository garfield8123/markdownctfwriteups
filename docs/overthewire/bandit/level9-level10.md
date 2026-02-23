# Level 10

Bandit OverTheWire Level 10: [level 10](https://overthewire.org/wargames/bandit/bandit10.html)

## **Level Goal**
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

## **Walkthrough**
- Figure out how to get only the human-readable strings from the text file 
- Figure out how to find only == signs and text

## **Level 10 Solution**
```shell
cat data.txt | strings | grep "=="
```

## **Generated password for level 10**
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
