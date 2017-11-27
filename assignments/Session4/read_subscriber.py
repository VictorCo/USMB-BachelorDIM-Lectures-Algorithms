# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief read as a subscriber


from S4_queues_tools import *
import pika

def callback(ch, method, properties, body) :
    print("[X] %r" % body)

def read_fanout_data(args, value) :
    exchange_name = settings["default_exchange"]
    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.exchange_declare(exchange = exchange_name,
                             exchange_type = "fanout")

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    print("queue {0}".format(queue_name))
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    print("[*] Waiting for messages. To exit press Ctrl+C")
    channel.start_consuming()
    
if __name__ == "__main__" :
    args, value = check_argument()

    read_fanout_data(args, value)
