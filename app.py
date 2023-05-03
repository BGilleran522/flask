import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from ddtrace import tracer, patch_all

# Initialize Flask app
app = Flask(__name__)

# Configure Datadog tracing
patch_all()
# Configure logging
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                   '[in %(pathname)s:%(lineno)d]')
log_file_handler = RotatingFileHandler('/home/pi/flask/logs/app.log', maxBytes=100000, backupCount=10)
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(log_formatter)
app.logger.addHandler(log_file_handler)

# Define a route
@app.route('/')
def index():
    app.logger.info('Hello, world!')
    response = {'message': 'Hello, world!'}
    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run(port=50011)

