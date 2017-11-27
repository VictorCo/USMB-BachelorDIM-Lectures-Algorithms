# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief sign in and publish messages

from S4_queues_tools import *
from time import sleep
import pika

def callback(ch, method, properties, body) :
    print("[X] message received : {}".format(body))

def fanout_data(args, value) :
    exchange_name = "caramail"
    message = "You listen {0}".format(exchange_name)
    
    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)

    #sign in
    if args & arg_signin :
        channel = connection.channel()
        channel.basic_publish(exchange="",
                              routing_key="presentation",
                              body=value[arg_signin])

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue   

    
        channel_read = connection.channel()
        channel_read.exchange_declare(exchange=exchange_name,
                                      exchange_type="fanout")
        channel_read.queue_bind(exchange=exchange_name,
                                queue = queue_name)
        channel_read.basic_consume(callback,
                              queue=queue_name,
                              no_ack=True)
        channel_read.start_consuming()

        #Consume and publish without thread ??
        while True :
            message = raw_input("message : ")
            channel.basic_publish(exchange=exchange_name,
                                  routing_key="",
                                  body=message)

            sleep(delay)
        
    #not signin no read and no write message
    else :
        print("enter a name please")
    

if __name__ == "__main__" :
    args, value = check_argument()

    fanout_data(args, value)
