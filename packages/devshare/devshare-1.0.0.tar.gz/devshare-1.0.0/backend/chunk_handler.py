import time
import threading
from config import TRANSFER_TIMEOUT

# Temporary in-memory storage for active transfers
active_transfers = {}

def store_chunk(file_id, chunk, filename=None, extension=None):
    """ Store encrypted file chunks in memory """
    if file_id not in active_transfers:
        active_transfers[file_id] = {"chunks": [], "filename": filename, "extension": extension, "password": None}
    
    active_transfers[file_id]["chunks"].append(chunk)
    if filename and extension:
        active_transfers[file_id]["filename"] = filename
        active_transfers[file_id]["extension"] = extension

def get_file(file_id):
    """ Reassemble file from chunks and return it """
    if file_id in active_transfers:
        file_data = b"".join(active_transfers[file_id]["chunks"])  # Reassemble chunks
        filename = active_transfers[file_id]["filename"]
        extension = active_transfers[file_id]["extension"]
        return file_data, filename, extension
    return None, None, None

def cleanup_transfer(file_id, timeout=TRANSFER_TIMEOUT):
    """ Delete file after timeout to ensure security """
    time.sleep(timeout)
    if file_id in active_transfers:
        del active_transfers[file_id]
