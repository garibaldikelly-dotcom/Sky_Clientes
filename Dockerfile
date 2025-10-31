FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
# CMD para iniciar tu aplicación, ej:
CMD ["python", "clientes_service.py"]