import os
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Server Configuration
WEBSOCKET_HOST = os.getenv("WEBSOCKET_HOST", "0.0.0.0")
WEBSOCKET_PORT = int(os.getenv("WEBSOCKET_PORT", 8000))
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 500))  # Maximum file size (MB)
TRANSFER_TIMEOUT = int(os.getenv("TRANSFER_TIMEOUT", 300))  # 5 minutes in seconds

# Allowed File Types & MIME Types
ALLOWED_FILE_TYPES = {
    "text": [".txt", ".log", ".csv"],
    "code": [".py", ".js", ".html", ".css", ".json", ".yaml"],
    "documents": [".pdf", ".docx", ".xlsx"],
    "compressed": [".zip", ".tar.gz", ".7z", ".rar"],
    "images": [".jpg", ".png", ".gif", ".svg"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "executables": [".exe", ".bin", ".sh", ".appimage"],
    "keys": [".pem", ".key", ".crt", ".pfx"]
}

# Encryption Configuration
AES_KEY_SIZE = int(os.getenv("AES_KEY_SIZE", 32))  # AES-256 (32 bytes)
BCRYPT_SALT_ROUNDS = int(os.getenv("BCRYPT_SALT_ROUNDS", 12))  # Secure password hashing

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Options: DEBUG, INFO, WARNING, ERROR
LOG_FILE = os.getenv("LOG_FILE", "server.log")  # Log output file

# Function to validate file types
def is_allowed_file(filename):
    """Check if the given filename has an allowed extension."""
    ext = os.path.splitext(filename)[1].lower()
    return any(ext in exts for exts in ALLOWED_FILE_TYPES.values())
