import os
import uvicorn
from celery import chain
from fastapi import FastAPI
from celery.result import AsyncResult

from src.models.models import Item
from src.utils.utils import *
from src.constant import *

from tasks import download_video, extract_audio_task, transcribe_task, generate_subtitle_file_task, add_subtitle_to_video_task
from config import Config


# Create necessary directories
os.makedirs(AUDIOS_PATH, exist_ok=True)
os.makedirs(VIDEOS_PATH, exist_ok=True)
os.makedirs(SUBTITLES, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

app = FastAPI()


@app.post("/download/")
async def download_video_via_url(item: Item):
    # Đẩy tác vụ tải video vào hàng đợi Celery
    task = download_video.delay(item.url)
    return {"message": "Video download task added to the queue", "task_id": task.id}


@app.post("/generate/{yt_id}")
async def generate_subtitle(yt_id: str, dest: str):
    task_chain = chain(
        extract_audio_task.s(yt_id),
        transcribe_task.s(dest),
        generate_subtitle_file_task.s(),
        add_subtitle_to_video_task.s()
    )
    
    result = task_chain.delay()
    return {"message": "Subtitle task added to the queue", "task_id": result.id}


@app.get("/task-status/{task_id}")
async def task_status(task_id: str):
    # Kiểm tra trạng thái tác vụ
    task_result = AsyncResult(task_id)
    return {"status": task_result.status, "result": task_result.result}


if __name__ == "__main__":
    uvicorn.run("main:app", port=Config.FASTAPI_PORT, host=Config.HOST)