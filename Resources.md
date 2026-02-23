## **Common Commands**

### **Common Username/password**
- Username: root, admin, sysadmin, user, test
- Password: password, password123, password1234, 1234

### **Nmap**
```bash
nmap -v -A <ip-address> -p <port-range>
```
![nmap_Cheat_sheet](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fsecurityonline.info%2Fwp-content%2Fuploads%2F2017%2F08%2Fnmap.png&f=1&nofb=1&ipt=5ab6028ec932ef96018cb00657dc4100175e4674b98cb998b3cfc36e89bdeff5&ipo=images)

### **Content Discovery**
```bash
curl <site>/sites/favicon/images/favicon.ico | md5sum

gobuster dir --url <site> -w <wordlist>
```
[MD5_Favicon_Database](https://wiki.owasp.org/index.php/OWASP_favicon_database)
[Web_Framework_analyzer](https://www.wappalyzer.com/)

### **Brute Force Login**
```bash
crunch <min> <max> <characters> -o <output.txt>

hydra -l '' -P <output.txt> -f -v MACHINE_IP http-post-form "<post-url>:<input_name>=^PASS^:<Error_Result>" -s <port_Name>

cewl -d <depth_search> -m <mininum_len> -x <max_len> http://<ip-address> -w <output.txt>

wfuzz -c -z file,<filename> -z file,<filename> --hs <string of error> -u <login_page_location> -d <username=FUZZ&password=FUZ2Z>
```
[Hydra Cheatsheet](https://github.com/frizb/Hydra-Cheatsheet)


### **Fancy things to do in Lunx**
```bash
cat <filename>

less <filename>

head -n <#_of_lines> <filename>

tail -n <#_of_lines> <filename>

wc -l <filename>

nl <filename>

cut -d <delm_string> -f<col_#> <filename>
```

### **SQL Injection**
```sql
<webiste>?age='; <SQL_INEJCTION_COMMAND> -- 
```

### **MSF VENOM**
[msfvenom cheatsheet](https://github.com/frizb/MSF-Venom-Cheatsheet)