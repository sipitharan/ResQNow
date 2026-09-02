from flask_socketio import SocketIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

socketio = SocketIO(async_mode="threading", cors_allowed_origins="*")
limiter = Limiter(
	key_func=get_remote_address,
	default_limits=["200/day", "60/hour", "10/minute"],
	storage_uri="memory://",
)
