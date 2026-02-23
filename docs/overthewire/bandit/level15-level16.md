# Level 16

Bandit OverTheWire Level 16: [level 16](https://overthewire.org/wargames/bandit/bandit16.html)

## **Level Goal**
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

## **Walkthrough**
- Figure out OpenSSL works
- How to make a client with server and port

## **level 16 Solution**
```shell
openssl s_client -connect localhost:30001 -ign_eof
# Put password for Level 15
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

## **Generated password for level 16**
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
