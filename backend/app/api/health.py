"""GET /health: アプリケーションが起きていることを確認するためのエンドポイント。
ロードバランサや監視ツールが叩く想定で、内部状態には触らず固定値を返す。"""

from fastapi import APIRouter

# APIRouterで機能ごとにルータを分けると、main.pyが肥大化せず
# 後から /ocr, /words を追加する際の差分が小さく済む
router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """常に 200 OK と {"status":"ok"} を返すヘルスチェック。"""
    return {"status": "ok"}