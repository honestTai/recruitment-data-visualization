
FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r re.txt
EXPOSE 8080
ENV FLASK_APP=app.py

CMD ["python", "app.py"]