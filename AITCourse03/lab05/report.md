# Отчет по лабораторной работе "Запуск контейнеров и подключение Volumes"

## 1. Нейронная сеть DeepSeek
С помощью нейронной сети запросом "Создай мне, пожалуйста, два файла .html, чтобы это было два статичных сайта" создал два .html файла, которые позже загрузил в Docker и назвал их site1 и site2.

## 2. Дальше я создал папку, куда поместил две папки со своими статическими сайтами:
```
root:~/projects# ls -R
.:
site1  site2

./site1:
index.html

./site2:
index.html
```

## 3. Запустил контейнеры командами:
```
docker run --name site1 -p 8080:80 -v ./site1:/usr/share/nginx/html:ro -d nginx
docker run --name site2 -p 8081:80 -v ./site2:/usr/share/nginx/html:ro -d nginx
```

## 4. Зайдя на два моих сайта, увидел следующее:

### Первый сайт
<img width="1710" height="953" alt="Screenshot 2026-04-30 at 11 39 22 PM" src="https://github.com/user-attachments/assets/51a50f9d-e8ef-4f9c-aaab-0dc8a0ccbea9" />

### Второй сайт:
<img width="1710" height="953" alt="Screenshot 2026-04-30 at 11 39 45 PM" src="https://github.com/user-attachments/assets/40edc118-465a-491c-ab69-313eca58b5d3" />

