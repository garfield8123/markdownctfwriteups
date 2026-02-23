# Level 6

Bandit OverTheWire Level 6: [level 6](https://overthewire.org/wargames/bandit/bandit6.html)

## **Level Goal**
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable


## **Walkthrough**
- Figure out how to add size to the find command
- Figure out how to add not executable to find command

## **Level 6 Solution**
```shell
find inhere/ -type f -size 1033c -readable ! -executable -exec file {} + | grep 'text'

cat inhere/maybehere07/.file2
```

## **Generated password for level 6**
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
