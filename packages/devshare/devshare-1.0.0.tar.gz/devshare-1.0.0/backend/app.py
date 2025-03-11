from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
import asyncio
from backend.encryption import encrypt_chunk, decrypt_chunk, verify_password, hash_password
from backend.chunk_handler import store_chunk, get_file, cleanup_transfer
from backend.config import TRANSFER_TIMEOUT

app = FastAPI()

# Active transfers stored in memory (Temporary)
active_transfers = {}

@app.websocket("/transfer/{file_id}")
async def transfer(websocket: WebSocket, file_id: str, password: str):
    """ WebSocket connection for real-time file transfer with password protection """
    await websocket.accept()

    if file_id not in active_transfers:
        hashed_password = hash_password(password)
        active_transfers[file_id] = {"chunks": [], "filename": None, "extension": None, "password": hashed_password}

    try:
        while True:
            data = await websocket.receive_bytes()
            encrypted_chunk = encrypt_chunk(data)
            store_chunk(file_id, encrypted_chunk)
            await websocket.send_text("Chunk received")
    
    except WebSocketDisconnect:
        print(f"Transfer {file_id} disconnected.")
    
    finally:
        await websocket.close()
        asyncio.create_task(cleanup_transfer(file_id, TRANSFER_TIMEOUT))

@app.post("/download/{file_id}")
async def download_file(file_id: str, password: str):
    """ Endpoint to retrieve full file after transfer with password validation """
    if file_id not in active_transfers:
        raise HTTPException(status_code=404, detail="File not found or expired")

    if not verify_password(password, active_transfers[file_id]["password"]):
        raise HTTPException(status_code=403, detail="Incorrect password")

    file_data, filename, extension = get_file(file_id)

    if file_data:
        # Delete file immediately after download
        del active_transfers[file_id]
        return {
            "file_data": file_data.hex(),
            "filename": filename,
            "extension": extension
        }

    raise HTTPException(status_code=404, detail="File not found or expired")
