FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# غير البورت لـ 7860
EXPOSE 7860

# عدل أمر التشغيل عشان يفتح على البورت ده
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]