from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask import Response
from view.purchase_projection_view import ViewPurchaseProjection
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

api = Api(app)

api.add_resource(ViewPurchaseProjection, '/api/projection/purchases/<string:product_name>')

@app.route('/')
def home():
    return Response("{'a':'b'}", status=201, mimetype='application/json')

@app.errorhandler(NotFound)
def page_not_found_handler(e: HTTPException):
    return "404"

@app.errorhandler(Unauthorized)
def unauthorized_handler(e: HTTPException):
    return "401"

@app.errorhandler(Forbidden)
def forbidden_handler(e: HTTPException):
    return "403"

@app.errorhandler(RequestTimeout)
def request_timeout_handler(e: HTTPException):
    return "408"


if __name__ == "__main__":
    app.run(port = 80, debug = True, host='0.0.0.0')