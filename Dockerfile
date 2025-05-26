# Python Image
FROM python:3.14.0b1-slim

# Container directory
RUN mkdir -p /home/app

COPY . /home/app

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Port
EXPOSE 8000

# Run the project
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3401"]
