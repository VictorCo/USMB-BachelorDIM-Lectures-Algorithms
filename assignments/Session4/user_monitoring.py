# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief monitoring users, display all user connected when new user is comming

from S4_queues_tools import *
import pika

#list that save the user name
users = []


#print user connected when a new user is comming
def callback(ch, method, properties, body) :
    global users
    if body not in users :
        users.append(body)
        print("[X] User connected :")
        for user in users :
            print user
    

def read_users(args, value) :
    
    queue_name = "presentation"
    url = settings["url"]
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=False)

    print("[*] Waiting for users. To exit press CTRL+C")
    channel.start_consuming()
    
if __name__ == "__main__" :
    args, value = check_argument()

    read_users(args, value)
