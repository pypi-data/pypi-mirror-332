from .logger import logger
from flask import jsonify

def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            return jsonify(response), 200
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            return jsonify({'error': str(e)}), 500
    return wrapper