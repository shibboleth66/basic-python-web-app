# wsgi.py
 
from app import app
from app import views
import logging
 
if __name__ != "__main__":
    
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    app.run()