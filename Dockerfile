FROM python:3.11-slim
WORKDIR /app
RUN pip install flask requests
COPY app/ .
EXPOSE 5000
CMD ["python", "app.py"]
