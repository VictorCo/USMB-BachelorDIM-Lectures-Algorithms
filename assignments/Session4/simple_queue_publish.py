# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief publish in a queue

import pika
import os
from S4_queues_tools import *

#how many messages publish
n_message = 1000

## publish data with amqp protocol
#@param args : arguments wanted, see S4_queues_tools for the list
#@param value : value of arguments, see S4_queues_tools for the list
def publish_data(args, value) :
    
    queue_name = set_queueName(args, value)
    user_name = raw_input("please enter your name : ")
                        
    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    basic_properties = pika.BasicProperties(delivery_mode = 1)
    if args & arg_concurrency:
        basic_properties.delivery_mode = 2

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    for i in range(n_message) :
        
        channel.basic_publish(exchange="",
                              routing_key=queue_name,
                              body=user_name,
                              properties=basic_properties)

        print("[X] Sent '{0}' to the queue '{1}'".format(user_name, queue_name))
        
    connection.close()


if __name__ == "__main__" :
    args, value = check_argument()

    publish_data(args, value)
