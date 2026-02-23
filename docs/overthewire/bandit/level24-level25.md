# Level 25

Bandit OverTheWire Level 25: [level 25](https://overthewire.org/wargames/bandit/bandit25.html)

## **Level Goal**
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

## **Walkthrough**
- Figure out how send strings in conjuction to the netcat command so it sends the command as well

## **level 25 Solution**
```shell
{
for i in $(seq -w 0000 9999); do 
    echo  "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i" 
done 
} | nc localhost 30002 | grep -v "Try again"
```

## **Generated password for level 25**
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
