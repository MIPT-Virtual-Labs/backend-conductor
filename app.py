import solver_dummy
import solver_gas_dynamics_1d
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/solver/<solvername>", methods=["POST"])
def solver(solvername):

    request_json = request.get_json()

    if solvername == "dummy":
        response = solver_dummy.handle_request(request_json)

    elif solvername == "gas_dynamics_1d":
        response = solver_gas_dynamics_1d.handle_request(request_json)

    else:
        response = {
            "status": "error",
            "errors": [
                {"error": f"unknown solver: {solvername}", "field": "solvername"}
            ],
        }

    return response
