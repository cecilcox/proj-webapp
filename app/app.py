from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Base index page"""
    return render_template("index.html")


@app.route("/_parse", methods=['POST'])
def parse():
    """Parse blazon text using 'backend'"""
    blazon = request.get_json()['blazon']
    return jsonify(parse_blazon(blazon))


def parse_blazon(blazon):
    """Dummy method in place of parser"""
    payload = {}
    if blazon.lower() == "scrope":
        payload = {
            "field": "azure",
            "charges": [
                {
                    "charge": "bend",
                    "tincture": "or"
                }
            ]
        }
    elif blazon.lower() == "st andrew":
        payload = {
            "field": "azure",
            "charges": [
                {
                    "charge": "saltire",
                    "tincture": "argent"
                }
            ]
        }
    else:
        payload = {
            "field": "gules",
            "charges": [
                {
                    "charge": "bend_sinister",
                    "tincture": "sable"
                }
            ]
        }

    return payload
