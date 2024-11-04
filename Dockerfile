FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt update
RUN apt install libmagic1 -y
RUN pip install -r requirements.txt
EXPOSE 7860
ENV GRADIO_SERVER_NAME=0.0.0.0
CMD ["python", "app.py"]
