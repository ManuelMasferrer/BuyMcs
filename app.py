from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask import Response
from view.purchase_projection_view import ViewPurchaseProjection

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

api = Api(app)

api.add_resource(ViewPurchaseProjection, '/api/projection/purchases/<string:product_name>')

@app.route('/')
def home():
    return Response("{'a':'b'}", status=201, mimetype='application/json')

if __name__ == "__main__":
    app.run(port = 5000, debug = True, host='0.0.0.0')