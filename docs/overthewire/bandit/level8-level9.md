# Level 9

Bandit OverTheWire Level 9: [level 9](https://overthewire.org/wargames/bandit/bandit9.html)

## **Level Goal**
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

## **Walkthrough**
- Figure out how the sort command works
- Figure out how the uniq command works
- Figure out how to combine them to find text only once

## **Level 9 Solution**
``` shell
cat data.txt | sort | uniq -u
```

## **Generated password for level 9**
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
