# Domen IP manzillarini MySQL bazasiga yozish

## Vazifa tavsifi
Sizning vazifangiz `domains.txt` faylida berilgan domenlarning IP manzillarini aniqlash va ularni MySQL bazasiga yozishdan iborat.

## Talablar
1. **Domenlarni olish**
   - `domains.txt` faylida quyidagi domenlar berilgan:
     ```
     google.com
     instagram.com
     facebook.com
     twitter.com
     youtube.com
     amazon.com
     wikipedia.org
     linkedin.com
     reddit.com
     netflix.com
     ```

2. **Domenlarning IP manzillarini aniqlash**
   - Python'da `socket` moduli orqali har bir domenning IP manzilini toping.

3. **MySQL bazasini yaratish**
   - `Internet` nomli MySQL bazasini yarating.
   - `Domain` nomli jadval yaratib, quyidagi ustunlarni qo‘shing:
     - `id` (Primary Key, AUTO_INCREMENT)
     - `domain` (VARCHAR, domen nomi)
     - `ip` (VARCHAR, IP manzili)

4. **Ma'lumotlarni MySQL bazasiga yozish**
   - Har bir domen va uning IP manzilini `Domain` jadvaliga kiriting.

## Loyihaning tuzilishi
```
project_folder/
│-- domains.txt
│-- main.py  # Asosiy kod
```

## Ko'rsatmalar
1. **MySQL bazasini yarating** va quyidagi SQL buyruqlarni bajaring:
   ```sql
   CREATE DATABASE Internet;
   USE Internet;
   CREATE TABLE Domain (
       id INT AUTO_INCREMENT PRIMARY KEY,
       domain VARCHAR(255) NOT NULL,
       ip VARCHAR(45) NOT NULL
   );
   ```
2. **Python yordamida IP manzillarni aniqlang** va bazaga yozing.
3. **MySQL bazasiga ulanish** uchun `mysql-connector-python` kutubxonasidan foydalaning:
   ```bash
   pip install mysql-connector-python
   ```

## Vazifani topshirish
- Kodni GitHub'ga yuklab, `git push` qiling va havolasini taqdim eting.

Omad! 🚀

