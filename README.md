
# 🌐 وب‌سایت پورتفولیو شخصی با Django & DRF

این پروژه یک وب‌سایت پورتفولیوی مدرن و پویا است که با استفاده از Django و Django REST Framework پیاده‌سازی شده. این سیستم به شما اجازه می‌دهد پروژه‌ها، مهارت‌ها و تکنولوژی‌های خود را از طریق یک API امن و مستند به راحتی مدیریت کرده و نمایش دهید.

🔗 **دموی آنلاین (Render)**:  
[https://sajjadhossin.onrender.com](https://sajjadhossin.onrender.com)  
⏳ *ممکن است بارگذاری اولیه تا ۱ دقیقه طول بکشد (به‌دلیل استفاده از سرویس رایگان Render).*

---

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15-red.svg)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/)

---

## 🚀 ویژگی‌های کلیدی

- مدیریت پروژه‌ها، مهارت‌ها و تکنولوژی‌ها از پنل ادمین یا API
- API کامل با قابلیت‌های CRUD و احراز هویت JWT
- مستندات تعاملی Swagger/OpenAPI با drf-spectacular
- فرم تماس با ارسال پیام به ایمیل ادمین
- ذخیره‌سازی تصاویر در Cloudinary
- آماده برای پروداکشن با Docker، Gunicorn و WhiteNoise
- حذف خودکار فایل‌های تصویر پروژه‌ها هنگام حذف آیتم
- پشتیبانی از صفحه‌بندی و ساخت دسته‌ای (Bulk Create)

---

## 🛠 تکنولوژی‌های استفاده‌شده

### Backend
- Python 3.11+
- Django 5.2
- Django REST Framework 3.15

### Database
- PostgreSQL

### API & Auth
- Simple JWT
- drf-spectacular

### Deployment
- Docker
- Gunicorn
- WhiteNoise

### File Storage
- Cloudinary

### Dev Tools
- python-dotenv

---

## ⚙️ راه‌اندازی در محیط توسعه

### ۱. پیش‌نیازها
- Python 3.10+
- PostgreSQL
- Git

### ۲. مراحل نصب

```bash
git clone https://github.com/Sajjadhosseinrezaei/DivineBeauty.git
cd DivineBeauty

python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
```

### ۳. پیکربندی متفیرهای محیطی

```env
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mysite
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
CLOUD_NAME=your-cloud-name
API_KEY=your-cloudinary-api-key
API_SECRET=your-cloudinary-api-secret
```

### ۴. اجرای پروژه

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

آدرس: http://127.0.0.1:8000

---

### 🐳 اجرای پروژه با Docker (محیط پروداکشن)

**۱. پیش‌نیاز: نصب Docker**  
**۲. اجرا:**

```bash
docker build -t portfolio-app .
docker run --name portfolio-app -p 8000:8000 --env-file .env -d portfolio-app
```

### 📄 فایل entrypoint.sh

```bash
#!/bin/sh
echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn server..."
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
```

---

### 📚 مستندات API

**احراز هویت JWT**  
```http
POST /api/token/

Body:
{
  "username": "your_username",
  "password": "your_password"
}
```

هدر درخواست‌ها:  
```
Authorization: Bearer <access_token>
```

### Swagger UI  
http://127.0.0.1:8000/api/schema/swagger-ui/

---

### Endpointهای اصلی

#### پروژه‌ها
- `GET /api/projects/` : لیست پروژه‌ها
- `POST /api/projects/` : ساخت پروژه جدید
- `GET /api/projects/<id>/` : دریافت پروژه خاص
- `PUT /api/projects/<id>/` : بروزرسانی پروژه
- `DELETE /api/projects/<id>/` : حذف پروژه

#### تکنولوژی‌ها
- `GET /api/technologies/` : لیست تکنولوژی‌ها
- `POST /api/technologies/` : افزودن تکنولوژی
- `GET /api/technologies/<id>/` : دریافت تکنولوژی خاص
- `PUT /api/technologies/<id>/` : بروزرسانی تکنولوژی
- `DELETE /api/technologies/<id>/` : حذف تکنولوژی

---

### 📬 تماس با من

**سجادحسین رضایی**  
📧 sajjadhosseinrezaei@yahoo.com  
🌐 https://sajjadhossin.onrender.com
