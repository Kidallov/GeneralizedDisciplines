# Отчет по выполненной лабораторной работе 

## Получение сертификата через snap

Для начала переходим на сайт certbot

1. Установка `snap` на нашем сервер: 
	`apt install snap`

2. Далее выполняем проверку, что все корректно работает:
	`sudo ln -s /snap/bin/certbot /usr/local/bin/certbot`
	Можно писать без *sudo*, так как мы подключились к root.

3. Так как я использую nginx, то следующая команда для запуска certbot мне нужно выполнить команду:
	`sudo certbot --nginx`

После всех выполненный команд мы можем проверить, что все отображается корректно:

```
ootomytlastservers# sudo certbot --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email - можно пропустить вставку Email, этот шаг не является обязательным.
address or hit Enter to skip.
	(Enter'c" to cancel):

Please read the Terms of Service at:
https://letsencrypt.org/documents/LE=SA-vI.6-August=18=2025.pdf
You must agree in order to register with the ACME server. Do you agree? - даем согласие, что прочли и поняли все условия.

(Y)es/(N)o: Y
Account registered
Please enter the domain name(s) you would like on your certificate (comma and/or (space separated) CEnter c to cancel: kdlv.duckdns.org
Requesting a certificate for kdly.duckdns. org

Successfully received certificate.
Certificate is saved at:/etc/letsencrypt/live/kdlv.duckdns.org/fullchain.pem
Key is saved at: /etc/letsencrypt/live/kdlv.duckdns.org/privkey.pem
This сertificate expires on 2026-06-24.
Thesefiles will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

DepLoying certificate
Successfully deployed certificate for kdlv.duckdns.org to /etc/nginx/sites-enabled/default 
Congratulations! You have successfully enabled HTTPS on https://kdlv.duckdns.org

If you like Certbot, please consider supporting our work by:
* Donating to ISRG / Let's Encrypt: https://letsencrypt.org/donate
* Donating to EFF https://eff.org/donate-le
```

4. Можем сделать к http сайту через curl

```
Iroot@myfirstserver:~# curl http://kdlv.duckdns.org
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body> 
</html>
```

curl автоматически не перенаправляет на https стандарт, такое делает сайт.
