# وب‌سایت پورتفولیو شخصی با جنگو و DRF

این پروژه یک وب‌سایت پورتفولیو (نمونه کار) پویا است که با استفاده از فریم‌ورک جنگو و Django REST Framework ساخته شده است. این سایت به شما اجازه می‌دهد تا پروژه‌ها و مهارت‌های خود را به نمایش بگذارید و همچنین یک API کامل برای مدیریت محتوا از طریق رابط برنامه‌نویسی فراهم می‌کند.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15-red.svg)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/)

---

## 🚀 ویژگی‌های کلیدی

* **مدیریت پویای محتوا**: افزودن، ویرایش و حذف پروژه‌ها، مهارت‌ها و تکنولوژی‌ها از طریق پنل ادمین جنگو.
* **API کامل (Full CRUD)**: یک API قدرتمند برای مدیریت کامل محتوای سایت.
* **احراز هویت JWT**: امنیت API با استفاده از توکن‌های وب JSON (JWT) برای دسترسی به Endpointهای حساس.
* **مستندات خودکار API**: مستندات تعاملی و خودکار با استفاده از Swagger UI (ارائه شده توسط `drf-spectacular`).
* **فرم تماس با ما**: فرم تماس کاربردی با قابلیت ارسال مستقیم پیام‌ها به ایمیل مدیر سایت.
* **ذخیره‌سازی ابری رسانه**: آپلود و مدیریت فایل‌های تصویری پروژه‌ها در سرویس ابری Cloudinary.
* **آماده برای پروداکشن**: پیکربندی شده برای دیپلوی در محیط پروداکشن با استفاده از Docker, Gunicorn و WhiteNoise.
* **مدیریت خودکار منابع**: حذف اتوماتیک فایل تصویر پروژه از سرور هنگام حذف خود پروژه.
* **قابلیت‌های پیشرفته API**: پشتیبانی از صفحه‌بندی (Pagination) و ساخت دسته‌ای (Bulk Create) در API.

---

## 🛠 تکنولوژی‌های استفاده شده

* **Backend**:
    * [Python](https://www.python.org/)
    * [Django](https://www.djangoproject.com/)
    * [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Database**:
    * [PostgreSQL](https://www.postgresql.org/)
* **API & Authentication**:
    * [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
    * [drf-spectacular](https://drf-spectacular.readthedocs.io/) (برای مستندات Swagger/OpenAPI)
* **Deployment & Serving**:
    * [Docker](https://www.docker.com/)
    * [Gunicorn](https://gunicorn.org/) (WSGI Server)
    * [WhiteNoise](http://whitenoise.evans.io/) (برای ارائه فایل‌های استاتیک)
* **File Storage**:
    * [Cloudinary](https://cloudinary.com/)
* **Environment Variables**:
    * [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ راهنمای نصب و راه‌اندازی (محیط توسعه)

برای اجرای این پروژه در محیط توسعه محلی خود، مراحل زیر را دنبال کنید:

**۱. پیش‌نیازها**
* Python 3.10+
* PostgreSQL
* Git

**۲. مراحل نصب**

```bash
# 1. پروژه را از گیت‌هاب کلون کنید
git clone <URL-REPOSITORY-SHOMA>
cd <NOME-DIRECTORY-PROZHE>

# 2. یک محیط مجازی (virtual environment) بسازید و آن را فعال کنید
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

# 3. وابستگی‌های پروژه را نصب کنید
pip install -r requirements.txt

# 4. یک فایل .env بسازید
# فایل .env.example را به .env کپی کرده و مقادیر آن را با اطلاعات خود جایگزین کنید
cp .env.example .env
