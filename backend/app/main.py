"""FastAPIアプリケーションのエントリポイント。
ルータの組み立てと、起動時設定をここに集約する。"""

from fastapi import FastAPI

from app.api import health

# title/version/description は /docs（自動生成のSwagger UI）に反映される
app = FastAPI(
    title="vocab-snap API",
    version="0.1.0",
    description="Backend API for vocab-snap (パシャ単): image-to-vocabulary registration app",
)

# 各機能のルータを include_router で組み込む。
# 今は /health のみ。後続タスクで /ocr (T06), /words (T08, T08b) を追加していく
app.include_router(health.router)