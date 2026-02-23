# Pico Practice GYM

Writeups for Pico Practice General Category [pico ctf general category](https://play.picoctf.org/practice?category=5&page=1)

## **Time Machine**
```shell

git log message.txt
```

## **Log Hunt**
```shell
wget https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log
cat server.log | grep -i flag | gawk '{print $5}' | uniq
```

## **Obedient Cat**

```console
wget https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag *
cat flag
```

## **Python Wrangling**

```shell
wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py
wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt
wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en
echo "File Password:"
cat pw.txt
python3 ende.py -d flag.txt.en
```

## **Wave a Flag**

```shell
wget https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm
chmod +x warm
./warm -h
```

## **Nice Netcat**

```shell
nc mercury.picoctf.net 43239 >> flag.txt
python3 -c "lines = []
with open('flag.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())
text = ''
for x in lines:
    text += chr(int(x))
print(text)"
```

## **Static ain't always noise**

```shell
wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static
wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh
chmod +x ltdis.sh
./ltdis.sh static
cat static.ltdis.strings.txt | grep "pico"
```

## **Tab, Tab, Attack**

```shell
wget https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip
unzip Addadshashanammu.zip
./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

## **Magikarp Ground Mission**

```shell
echo "password is: 6d448c9c"
ssh ctf-player@venus.picoctf.net -p 59579
cat 1of3.flag.txt /2of3.flag.txt ~/3of3.flag.txt >> flag.txt
tr -d '\n' < flag.txt 
```

## **Lets Warm Up**

{% raw %}

```shell
python3 -c "print('picoCTF{%s}'%(chr(int('0x70',16))))"
```

{% endraw %}

## **Warmed Up**

{% raw %}

```shel
python3 -c "print('picoCTF{%s}'%(str(int('0x3D',16))))"
```

{% endraw %}

## **2Warm**

{% raw %}

```shell
python3 -c "print('picoCTF{' +'{0:b}'.format(int(42)) +'}')"
```

{% endraw %}

## **What's a net cat?**

```shell
nc jupiter.challenges.picoctf.org 25103
```

## **Strings it**

```shell
wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
strings strings | grep "picoCTF"
```

## **Bases**

{% raw %}

```shell
python3 -c "import base64
base64_message = 'bDNhcm5fdGgzX3IwcDM1 '
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
print('picoCTF{%s}'%(message))"
```

{% endraw %}

## **First Grep**

```shell
wget https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file
cat file | grep "picoCTF"
```

## **Codebook**

```shell
wget https://artifacts.picoctf.net/c/102/code.py
wget https://artifacts.picoctf.net/c/102/codebook.txt
python3 code.py
```

## **convertme.py**

```shell
wget https://artifacts.picoctf.net/c/31/convertme.py
echo "change to if True"
nano convertme.py
python3 convertme.py
```

## **fixme1.py**

```shell
wget https://artifacts.picoctf.net/c/39/fixme1.py
echo "fix print identidatiion error"
nano fixme1.py
python3 fixme1.py
```

## **fixme2.py**

```shell
wget https://artifacts.picoctf.net/c/65/fixme2.py
echo "fix to if ==''"
nano fixme2.py 
python3 fixme2.py
```

## **Glitch Cat**

{% raw %}

```shell
nc saturn.picoctf.net 51109
python3 -c "print('picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}')"
```

{% endraw %}

## **HashingjobApp**

```shell
echo "https://www.md5hashgenerator.com/"
echo "copy the text from the quotes"
nc saturn.picoctf.net 57689
```

## **PW Crack 1**

```shell
wget https://artifacts.picoctf.net/c/52/level1.py
wget https://artifacts.picoctf.net/c/52/level1.flag.txt.enc
echo "password is 1e1a"
python3 level1.py
```

## **PW Crack 2**

```shell
wget https://artifacts.picoctf.net/c/18/level2.py
wget https://artifacts.picoctf.net/c/18/level2.flag.txt.enc
echo "password is:")
python3 -c "print(chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))"
python3 level2.py
```

## **PW Crack 3**

```shell
wget https://artifacts.picoctf.net/c/23/level3.py
wget https://artifacts.picoctf.net/c/23/level3.flag.txt.enc
wget https://artifacts.picoctf.net/c/23/level3.hash.bin
python3 -c 'import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
correct_pw_hash = open("level3.hash.bin", "rb").read()
pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
for x in pos_pw_list:
    if (hash_pw(x) == correct_pw_hash):
        print("password is:" +x)'
python3 level3.py
```

## **PW Crack 4**

```shell
wget https://artifacts.picoctf.net/c/59/level4.py
wget https://artifacts.picoctf.net/c/59/level4.flag.txt.enc
wget https://artifacts.picoctf.net/c/59/level4.hash.bin
python3 -c 'import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
correct_pw_hash = open("level4.hash.bin", "rb").read()
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]
for x in pos_pw_list:
    if (hash_pw(x) == correct_pw_hash):
        print("password is:" +x)'
python3 level4.py
```

## **PW Crack 5**

```shell
wget https://artifacts.picoctf.net/c/80/level5.py
wget https://artifacts.picoctf.net/c/80/level5.flag.txt.enc
wget https://artifacts.picoctf.net/c/80/level5.hash.bin
wget https://artifacts.picoctf.net/c/80/dictionary.txt
python3 -c 'import hashlib
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
correct_pw_hash = open("level5.hash.bin", "rb").read()
lines = []
with open("dictionary.txt", "r") as f:
    for line in f:
        lines.append(line.strip())
for x in lines:
    if (hash_pw(x) == correct_pw_hash):
        print("password is:" +x)'
python3 level5.py
```

## **runme.py**

```shell
wget https://artifacts.picoctf.net/c/86/runme.py
python3 runme.py
```

## **Serpentine**

```shell
wget https://artifacts.picoctf.net/c/93/serpentine.py
echo "Add print_flag()"
nano serpentine.py
python3 serpentine.py
```

## **First Find**

```shell
wget https://artifacts.picoctf.net/c/552/files.zip
unzip files.zip
find files -name uber-secret.txt
cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt 
```

## **Big Zip**

```shell
wget https://artifacts.picoctf.net/c/555/big-zip-files.zip
unzip big-zip-files.zip
grep -rl "picoCTF" ./big-zip-files
cat ./big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
```

## **Based**

```shell
echo "https://www.rapidtables.com/convert/number/binary-to-ascii.html"
echo "http://www.unit-conversion.info/texttools/octal/" 
echo "https://www.rapidtables.com/convert/number/hex-to-ascii.html"
nc jupiter.challenges.picoctf.org 15130.
```

## **Plubming**

```shell
nc jupiter.challenges.picoctf.org 14291 | grep "picoCTF"
```

## **mus1c**

{% raw %}

```shell
wget https://jupiter.challenges.picoctf.org/static/c0863a3b0170d6dd176be3a595b4b75e/lyrics.txt
cat lyrics.txt
echo "https://codewithrockstar.com/online"
echo "https://www.utilities-online.info/ascii-to-text"
touch flag.txt
python3 -c "lines = []
with open('flag.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())
text = ''
for x in lines:
    text += chr(int(x))
print('picoCTF{%s}'%(text))"
```

{% endraw %}

## **flag_shop**

```shell
wget https://jupiter.challenges.picoctf.org/static/dd28f0987f28c894f35d5d48564c3402/store.c
echo "buffer overflow"
echo " buy 999999999999999"
nc jupiter.challenges.picoctf.org 44566
```

## **1_wanna_b3_a_r0ck5tar**

{% raw %}

```shell
wget https://jupiter.challenges.picoctf.org/static/96904d361d61fada5bd2d13536706f9a/lyrics.txt
echo "depreciated"
echo "picoCTF{BONJOVI}"
```

{% endraw %}
