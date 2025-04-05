# استفاده از ایمیج Alpine
FROM python:alpine

# نصب پکیج‌های سیستمی لازم
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    linux-headers \
    zlib-dev \
    jpeg-dev \
    && pip install --no-cache-dir --upgrade pip

# دایرکتوری کاری
WORKDIR /app

# کپی و نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نصب gunicorn و whitenoise
RUN pip install --no-cache-dir gunicorn 
RUN pip install --no-cache-dir whitenoise

# کپی بقیه کدها
COPY . .

# جمع‌آوری فایل‌های استاتیک موقع ساخت
RUN python manage.py collectstatic --noinput

# اضافه کردن دسترسی اجرایی به اسکریپت
RUN chmod +x entrypoint.sh

# باز کردن پورت
EXPOSE 8000

# اجرای اسکریپت entrypoint
CMD ["sh", "-c", "./entrypoint.sh"]