# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief brodcast one message


from S4_queues_tools import *
from time import sleep
import pika



def fanout_data(args, value) :
    exchange_name = settings["default_exchange"]
    message = "You listen {0}".format(exchange_name)

    if args & arg_delay :
        delay = value[arg_delay]
        
    else :
        delay = settings["default_delay"]
    
    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange_name,
                             exchange_type="fanout")

    #simple loop for send message periodically
    #ctrl+c to break it
    while True :
        channel.basic_publish(exchange=exchange_name,
                              routing_key="",
                              body=message)

        sleep(delay)

    

if __name__ == "__main__" :
    args, value = check_argument()

    fanout_data(args, value)
