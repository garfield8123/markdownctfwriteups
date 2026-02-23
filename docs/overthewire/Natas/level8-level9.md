# Level 9

Leviathan OverTheWire Level 9: [level 9](https://overthewire.org/wargames/natas/)

## Level 9 info
 Input secret:
View sourcecode


## Answer
We first look at the sourcecode to understand how the input secret validates our entry
[here](http://natas8.natas.labs.overthewire.org/index-source.html)

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

We have to reverse the encodesecret 
```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
```

The reverse would be a hex2bin then reverse the string and then lastly base64_decode
You can put in the shell with 
```shell
php -a
function decodeSecret($encodedSecret) {
    return base64_decode(strrev(hex2bin($encodedSecret)));
}

// Example usage:
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
$decodedSecret = decodeSecret($encodedSecret);

echo $decodedSecret; // Outputs the original secret

//oubWYf2kBq
```
The secret token is: oubWYf2kBq

```html
Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t 
```

## Level 9 Website
[natas9](http://natas9.natas.labs.overthewire.org)