# 🌐 وب‌سایت پورتفولیو شخصی با Django & DRF

این پروژه یک وب‌سایت پورتفولیوی مدرن و پویا است که با استفاده از Django و Django REST Framework پیاده‌سازی شده. این سیستم به شما اجازه می‌دهد پروژه‌ها، مهارت‌ها و تکنولوژی‌های خود را از طریق یک API امن و مستند به راحتی مدیریت کرده و نمایش دهید.

🔗 **دموی آنلاین (Render)**:  
[https://sajjadhossin.onrender.com](https://sajjadhossin.onrender.com)  
⏳ *ممکن است بارگذاری اولیه تا ۴۵ ثانیه طول بکشد (به‌دلیل استفاده از سرویس رایگان Render).*

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
# کلون کردن پروژه
git clone https://github.com/Sajjadhosseinrezaei/DivineBeauty.git
cd DivineBeauty

# ساخت محیط مجازی و فعال‌سازی
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# ساخت فایل .env از نمونه
cp .env.example .env
