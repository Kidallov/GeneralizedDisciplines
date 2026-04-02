# Лабораторная работа №3 "Несколько статических сайтов на одном сервере".

## Развернуть сервер на хостинге.

У меня уже был сайт на `kdlv.duckdns.org` и я создал второй домен `mypoortf.duck.dns`, прикрепив его к тому же серверу, где у меня находился первый домен.

## Установить NGINX.

NGINX уже был установлен - поэтому этот пункт я пропустил.

## Создать несколько конфигураций в каталоге /etc/nginx/sites-available/ с разными  сайтами.  В названии файлов конфигураций указать доменные имена.

Перейдя в `/etc/nginx/sites-available/` я переименовал файл default -> kdlv для первого домена и создал второй файл mypoortf для второго домена соответственно.

## Создать для сайтов символические ссылки (из sites-available в sites-enabled).

Далее перейдя в enable для каждого создал ссылки:

	* kdlv -> /etc/nginx/sites-available/kdlv
	* mypoortf -> /etc/nginx/sites-available/mypoortf

## Выпустить сертификаты, проверить конфигурацию и работу.

Выпустил сертификат уже для домена mypoortf.duckdns.org командой: `sudo certbot --nginx -d mypoortf.duckdns.org`

Оба файла я скорректировал, оставив только самое нужное:

```
server {
    listen 80;
    listen [::]:80;
    server_name kdlv.duckdns.org;
    return 301 https://$server_name$request_uri;
}

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

Можно проверить обоих сайтов по ссылкам:
* [Основной сайт](kdlv.duckdns.org)
* [Мини-портфолио](https://mypoortf.duckdns.org)
