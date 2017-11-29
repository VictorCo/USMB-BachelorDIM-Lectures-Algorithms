# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief basic rpc server, receive message and send a answer

#import
from S5_queue_tools import settings
import pika

import msgpack
import msgpack_numpy as m
import numpy as np

##when server receive a message, on request is called and answer to client
#@param ch : channel
#@param method : method
#@param props : properties transaction
#@param body : message
def on_request(ch, method, props, body) :
    request_param = str(body)
    decoded_message = msgpack.unpackb(request_param, object_hook=m.decode)

    print("[X] Message received : {}".format(decoded_message))
    response = find_response(decoded_message)
    encoded_response = msgpack.packb(response, default = m.encode)
          
    print("\t---> {}".format(response))
    
    ch.basic_publish(exchange = "",
                     routing_key = props.reply_to,
                     body = str(encoded_response),
                     properties = pika.BasicProperties(
                                     correlation_id = props.correlation_id
                                                      )
                     )
    ch.basic_ack(delivery_tag = method.delivery_tag)

##Tell what say to the client
#@param s : str which is the client's question
#@return reponse of the question, if no reponse send the default reponse
def find_response(m) :
    if m["type"] in settings["filter_types"] :
        return settings["filter_types"][m["type"]]

    #if no question entry, answer with the default answer
    return settings["filter_types"]["none"]

##perform the connection
def setup_connection() :

    queue_name = settings["default_queue"]
    url = settings["url"]

    params = pika.URLParameters(url)
    params.socket_timeout = 5


    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request,
                          queue = queue_name,
                          no_ack = False)
    print("Wait for requests in the '{}' queue".format(queue_name))
    channel.start_consuming()

if __name__ == "__main__" :
    setup_connection()
