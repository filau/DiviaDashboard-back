from divia_api import DiviaAPI
from flask import Flask, request
from datetime import datetime
from json import dumps
from waitress import serve

app = Flask(__name__)


@app.route("/divia")
def divia():
    now = datetime.now()
    rr = DiviaAPI().get_line(request.args.get("line_id")).get_stop(request.args.get("stop_code")).totem()
    rt = []
    for r in rr:
        rt.append(str(round((r - now).total_seconds() / 60)))
    return dumps(rt)


if __name__ == "__main__":
    try:
        serve(app, port=5000, host="0.0.0.0")
    except KeyboardInterrupt:
        pass
