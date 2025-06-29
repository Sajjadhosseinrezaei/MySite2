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

**۳. تنظیم متغیرهای محیطی **

یک فایل به نام .env در ریشه پروژه بسازید و متغیرهای زیر را با مقادیر مناسب پر کنید:
# فایل .env

# کلید مخفی جنگو (یک رشته تصادفی و طولانی بسازید)
SECRET_KEY='your-super-secret-key'

# آدرس اتصال به دیتابیس PostgreSQL
# فرمت: postgresql://USER:PASSWORD@HOST:PORT/DBNAME
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/mysite'

# تنظیمات ایمیل برای فرم تماس (از یک حساب Gmail با App Password استفاده کنید)
EMAIL_HOST_USER='your-email@gmail.com'
EMAIL_HOST_PASSWORD='your-gmail-app-password'

# کلیدهای API سرویس Cloudinary
CLOUD_NAME='your-cloudinary-cloud-name'
API_KEY='your-cloudinary-api-key'
API_SECRET='your-cloudinary-api-secret'

**۴.اجرای برنامه**
# 5. مایگریشن‌های دیتابیس را اجرا کنید
python manage.py migrate

# 6. یک کاربر ادمین (superuser) بسازید تا بتوانید به پنل ادمین و API دسترسی داشته باشید
python manage.py createsuperuser

# 7. سرور توسعه را اجرا کنید
python manage.py runserver

حالا می‌توانید پروژه را در آدرس http://127.0.0.1:8000 مشاهده کنید.

**🐳 نصب و اجرا با داکر (محیط پروداکشن)**
برای اجرای پروژه با استفاده از داکر، مراحل زیر را دنبال کنید:

۱. پیش‌نیازها

Docker

۲. مراحل اجرا
# 1. ایمیج داکر را بسازید
docker build -t mysite-portfolio .

# 2. کانتینر را اجرا کنید
# مطمئن شوید که فایل .env شما با مقادیر صحیح پر شده است
docker run --name portfolio-app -p 8000:8000 --env-file .env -d mysite-portfolio


این دستور کانتینر را در پس‌زمینه اجرا کرده و پورت 8000 سیستم شما را به پورت 8000 کانتینر متصل می‌کند.

نکته: این Dockerfile از یک اسکریپت entrypoint.sh استفاده می‌کند. محتوای این اسکریپت باید چیزی شبیه به زیر باشد تا مایگریشن‌ها را اجرا کرده و سرور Gunicorn را روشن کند:

#!/bin/sh

# اجرای مایگریشن‌های دیتابیس
echo "Running database migrations..."
python manage.py migrate --noinput

# اجرای سرور Gunicorn
echo "Starting Gunicorn server..."
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000


** 📚 راهنمای استفاده از API**

این پروژه یک API کامل برای مدیریت محتوا ارائه می‌دهد.

احراز هویت
برای دسترسی به Endpointهای محافظت‌شده (مانند افزودن یا حذف پروژه)، ابتدا باید یک توکن JWT دریافت کنید.

دریافت توکن: یک درخواست POST به آدرس زیر با نام کاربری و رمز عبور خود ارسال کنید:

POST /api/token/

استفاده از توکن: توکن دسترسی (access token) دریافتی را در هدر تمام درخواست‌های بعدی خود به شکل زیر قرار دهید:

Authorization: Bearer <YOUR_ACCESS_TOKEN>

مستندات تعاملی Swagger
برای مشاهده لیست کامل Endpointها، مدل‌ها و تست تعاملی API، به آدرس زیر مراجعه کنید:

/api/schema/swagger-ui/

Endpointهای اصلی
/api/projects/: GET, POST (برای لیست و ساخت پروژه‌ها)

/api/projects/<id>/: GET, PUT, DELETE (برای یک پروژه خاص)

/api/technologies/: GET, POST (برای لیست و ساخت تکنولوژی‌ها)

/api/technologies/<id>/: GET, PUT, DELETE (برای یک تکنولوژی خاص)


**📬 تماس با من**
سجاد حسینی رضایی - sajjadhosseinrezaei@yahoo.com

