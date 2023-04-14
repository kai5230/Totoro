import os
import logging.config
import yaml
from gevent import pywsgi
from flask import Flask
from api import rest
from pages import page

app = Flask(__name__)
app.register_blueprint(rest)
app.register_blueprint(page)


def setup_logging(default_path="logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    '''initial log'''
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def start(host, port):
    ''' start server '''
    logging.info('starting service ...')
    server = pywsgi.WSGIServer((host, port), app)
    server.serve_forever()


if __name__ == "__main__":
    start('0.0.0.0', 5000)
