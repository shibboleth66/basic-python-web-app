# wsgi.py
 
from app import application
from app import views
import logging
 
if __name__ != "__main__":
    
    gunicorn_logger = logging.getLogger('gunicorn.error')
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":

    application.run()
