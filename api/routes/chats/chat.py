"""Chat routers"""

from fastapi import APIRouter
from datetime import datetime
import json
from utils.websocker_manager import ConnectionManager
from fastapi import WebSocket, WebSocketDisconnect


router = APIRouter(prefix="/chat", tags=["Chat"])
manager = ConnectionManager()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            message = {"time": current_time, "clientId": client_id, "message": data}
            await manager.broadcast(json.dumps(message))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {"time": current_time, "clientId": client_id, "message": "Offline"}
        await manager.broadcast(json.dumps(message))
