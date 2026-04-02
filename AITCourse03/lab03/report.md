# Лабораторная работа №3 "Несколько статических сайтов на одном сервере"

У меня уже был сайт на `kdlv.duckdns.org` и я создал второй домен `mypoortf.duck.dns`, прикрепив его к тому же серверу, где у меня находился первый домен.

NGINX уже был установлен - поэтому этот пункт я пропустил.

Перейдя в `/etc/nginx/sites-available/` я переименовал файл default -> kdlv для первого домена и создал второй файл mypoortf для второго домена соответственно.

Далее перейдя в enable для каждого создал ссылки:

	* kdlv -> /etc/nginx/sites-available/kdlv
	* mypoortf -> /etc/nginx/sites-available/mypoortf

После чего выпустил сертификат уже для домена mypoortf.duckdns.org.

Оба файла я скорректировал, отсавив только самое нужное:

```
# HTTP → HTTPS редирект
server {
    listen 80;
    listen [::]:80;
    server_name kdlv.duckdns.org;
    return 301 https://$server_name$request_uri;
}

# HTTPS блок
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name kdlv.duckdns.org;

    root /var/www/html;
    index index.nginx-debian.html;

    ssl_certificate /etc/letsencrypt/live/kdlv.duckdns.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/kdlv.duckdns.org/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        try_files $uri $uri/ =404;
    }
}
```
