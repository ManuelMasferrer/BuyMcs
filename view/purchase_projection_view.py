from flask_restful import Resource
from flask import jsonify
from werkzeug.wrappers import response

from flask import request
from datetime import date, datetime, timedelta
from sqlalchemy import func

from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid

class ViewPurchaseProjection(Resource):


    def get(self, product_name):

        return jsonify("Proyeccion de ventas solicitada")
