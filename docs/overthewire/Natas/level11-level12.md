# Level 12

Leviathan OverTheWire Level 12: [level 12](https://overthewire.org/wargames/natas/)

## Level 12 info
Find words containing: 


## Answer
We first look at the sourcecode to understand how this programs finds words
[here](http://natas11.natas.labs.overthewire.org/index-source.html)

```php
<?
function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);?>
```

Need to reverse the loadData function


```shell
php -a

function xor_encrypt($in, $key) {
    $out = '';
    for($i=0; $i<strlen($in); $i++) {
        $out .= $in[$i] ^ $key[$i % strlen($key)];
    }
    return $out;
}

$known_plain = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

$cookie = base64_decode("HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=");

$key = '';
for($i=0; $i<strlen($known_plain); $i++) {
    $key .= $cookie[$i] ^ $known_plain[$i];
}

$new_plain = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#0000ff"));
$new_cookie = base64_encode(xor_encrypt($new_plain, "eDWo"));
echo $key;
echo $new_cookie;
```



natas 12 password: 


## Level 12 Website
[natas12](http://natas12.natas.labs.overthewire.org)