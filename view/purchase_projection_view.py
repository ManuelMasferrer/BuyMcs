from flask_restful import Resource
from flask import jsonify
from werkzeug.wrappers import response

from flask import request
from datetime import date, datetime, timedelta
from sqlalchemy import func

import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
from azure.identity.aio import DefaultAzureCredential


import os, uuid

# NAMESPACE_CONNECTION_STR = "Endpoint=sb://buy-queue.servicebus.windows.net/;SharedAccessKeyName=AllUsers;SharedAccessKey=VVtBolR2LiDKhwrnxrrJWmkXSlMtIXTsF+ASbK1gCaY="
# QUEUE_NAME = "buy-queue"

NAMESPACE_CONNECTION_STR = "Endpoint=sb://sbpurchases.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=TAZI8x82mRdU4/QXYQ8XyWXhUlov26467+ASbLGDaoE="
QUEUE_NAME = "buyqueue"


async def send_single_message(sender, message):
        # Create a Service Bus message and send it to the queue
        # message = ServiceBusMessage("Single Message")
    await sender.send_messages(message)


async def run(message):
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        # Get a Queue Sender object to send messages to the queue
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
                # Send one message
            await send_single_message(sender, message)

class ViewPurchaseProjection(Resource):


    def get(self, product_name):
        message = ServiceBusMessage(product_name)
        asyncio.run(run(message))

        return jsonify("Proyeccion de compras solicitada")
