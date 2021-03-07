# import the required libraries
import json

from flask import Flask, request

# create a Flask instance
app = Flask(__name__)


# define the application route and the type of request that is allowed
@app.route("/my_sum", methods=["POST"])
def my_sum():

    # convert the POST json object into a Python object
    request_data = request.get_json(force=True)

    # ensure that the dictionary contains a list
    if request_data["data"]:

        # convert the numbers from stings to floats
        float_list = [float(x) for x in request_data["data"]]

        # sum the values in the list
        data_sum = sum(float_list)

        # return the sum of the list
        response = app.response_class(
            response=json.dumps(data_sum), status=200, mimetype="application/json"
        )
        return response

    # return an error message if the list is empty
    else:
        return app.response_class(
            response="Invalid passed list.",
            status=400,
            mimetype="application/json",
        )


if __name__ == "__main__":
    # allow access to the Flask app via port 5000 of your local machine (your local
    # machines IP)
    app.run(debug=True, host="0.0.0.0", port=5000)
