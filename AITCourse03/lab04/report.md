# Лабораторная работа №3: "Установка Docker и запуск простого приложения"

**Тема:** Установка и настройка Docker с запуском Redmine на Ubuntu

---

## Цель работы

Освоить базовые навыки работы с Docker на сервере под управлением Ubuntu: установка Docker, запуск контейнеров, проброс портов и настройка обратного прокси с помощью Nginx.

---

## Ход работы

### 1. Подготовка сервера

Для начала работы подключились к серверу под управлением Ubuntu и подготовили систему к установке Docker.

Добавили официальный репозиторий Docker:

```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

### 2. Установка Docker

Установили последнюю стабильную версию Docker и сопутствующих компонентов:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Проверили корректность установки:

```bash
docker --version
```

---

### 3. Настройка Nginx для проброса порта Docker

Файл конфигурации Nginx: `/etc/nginx/sites-available/kdlv`
Настроили `location`, чтобы запросы к сайту [kdlv.duckdns.org](https://kdlv.duckdns.org/) перенаправлялись на порт Docker:

```nginx
location / {
    proxy_pass http://localhost:3000; # Перенаправляем запросы на порт 3000
    proxy_set_header Host $host; # Передача заголовка Host
    proxy_set_header X-Forwarded-Proto $scheme; # Передача схемы запроса (http/https)
}
```

Перезапустили Nginx для применения изменений:

```bash
sudo systemctl restart nginx
```

---

### 4. Запуск Redmine в Docker

Скачали официальный образ Redmine с Docker Hub и запустили его:

```bash
docker run -d --name some-redmine redmine
```

Для проброса порта наружу (чтобы Nginx мог его использовать) контейнер был пересоздан:

```bash
docker rm -f some-redmine

docker run -d \
  --name some-redmine \
  -p 3000:3000 \
  redmine
```

Таким образом, Redmine доступен на порту `3000`, а через Nginx — на основном домене.

---

## Заключение

Задание выполнено успешно. В ходе работы были приобретены следующие навыки:

* Установка Docker на Ubuntu;
* Работа с Docker-контейнерами: запуск, остановка, удаление;
* Настройка проброса портов;
* Настройка обратного прокси с помощью Nginx;
* Развёртывание официального образа Redmine.
