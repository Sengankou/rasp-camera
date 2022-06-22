import mimetypes
from flask import Flask, make_response, send_file
from camera import Video
import time
import threading
import os
import io

app = Flask(__name__)


def gen(camera):
    while True:
        return camera.get_frame()


@app.route("/video_feed")
def video_feed():
    return make_response(send_file(io.BytesIO(gen(Video())), mimetype='image/jpeg'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
