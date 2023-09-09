FROM python:3.9-slim

WORKDIR /app/backend/visual_quality_inspection

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]