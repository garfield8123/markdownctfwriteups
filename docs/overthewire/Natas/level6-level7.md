# Level 7

Leviathan OverTheWire Level 7: [level 7](https://overthewire.org/wargames/natas/)

## Level 7 info
Input secret:
View sourcecode

## Answer
We first look at the sourcecode to understand how the input secret validates our entry
[here](http://natas6.natas.labs.overthewire.org/index-source.html)

This is what seems to check the secret validation
```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
If we access includes/secret.inc we might be able to see the secret as it seems there are using POST, which sends the data 

We can use the GET method to get the information from includes/secret.inc

http://natas6.natas.labs.overthewire.org/includes/secret.inc

```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

Then input the secret

```html
Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS 
```

## Level 7 Website
[natas7](http://natas7.natas.labs.overthewire.org)