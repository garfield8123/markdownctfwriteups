# Level 21

Bandit OverTheWire Level 21: [level 21](https://overthewire.org/wargames/bandit/bandit21.html)

## **Level Goal**
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

## **Walkthrough**
- figure out how to send command to nc
- figure out the executible runs of succonnect
- Figure out how to run commands in the background

## **level 21 Solution**
```shell
# First launch a netcat server with the password of the previous level
echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l localhost 61423 &

./succonnect 61423

```

## **Generated password for level 21**
EeoULMCra2q0dSkYj561DX7s1CpBuOBt

