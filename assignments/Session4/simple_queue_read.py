# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief read in a queue

import pika
import os
from S4_queues_tools import *
from time import sleep

#global variable for callback function, not the better solution I think...
args = 0
value = {}



def callback(ch, method, properties, body):
    global args
    print("[X] Received '{0}' in {1} [{2}]".format(body,
                                                   method.routing_key,
                                                   method.delivery_tag))
    
    if args & arg_delay :
        print "sleep time : {0}".format(value[arg_delay])
        sleep(value[arg_delay])
        
    if args & arg_concurrency :
        ch.basic_ack(delivery_tag=method.delivery_tag)


## read data with amqp protocol
#@param args : arguments wanted, see S4_queues_tools for the list
#@param value : value of arguments, see S4_queues_tools for the list
def read_data(init_args, init_value):
    global args
    global value

    args = init_args
    value = init_value
    
    queue_name = set_queueName(args, value)

    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=False)

    print("[*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__" :
    args, value = check_argument()

    read_data(args, value)
