# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief basic rpc client, send a message and receive an answer from server

#import
from S5_queue_tools import settings
from uuid import uuid4
import pika

import msgpack
import msgpack_numpy as m
import numpy as np

#global definition
response = None
corr_id = 0

##when client receive a response of the server, this callback function is call
#@param ch : channel
#@param method : method
#@param props : properties transaction
#@param body : message
def on_response(ch, method, props, body) :
    global response
    global corr_id
    
    #not the same corr_id ? this is an intrusion, raise an error
    if corr_id != props.correlation_id :
        raise ValueError("Intrusion is comming...")

    #good reception
    response = str(body)
    decoded_response = msgpack.unpackb(response, object_hook=m.decode)
    print("reponse : {}".format(decoded_response['value']))

    
##perform the connection
def setup_connection() :

    queue_name = settings["default_queue"]
    url = settings["url"]
    request_msg = settings["q_welcome"]

    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    
    channel = connection.channel()
    result = channel.queue_declare(exclusive=True)
    callback_queue = result.method.queue
    global corr_id
    corr_id = str(uuid4())
    
    print("Your request in '{}' is '{}'".format(queue_name, request_msg))

    ##encode message
    encoded_message = msgpack.packb(request_msg, default = m.encode)
    ##
    channel.basic_publish(exchange = "",
                          routing_key = queue_name,
                          body = encoded_message,
                          properties = pika.BasicProperties(
                                              reply_to = callback_queue,
                                              correlation_id = corr_id,
                                                            ))

    print("Starting to wait on the response queue")
    channel.basic_consume(on_response,
                          no_ack = True,
                          queue = callback_queue)

    while response is None :
        connection.process_data_events()

    connection.close()
    
if __name__ == "__main__" :
    setup_connection()
