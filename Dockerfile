FROM python:3.9
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install python-telegram-bot yt-dlp
WORKDIR /app
COPY . .
CMD ["python", "bot.py"]
