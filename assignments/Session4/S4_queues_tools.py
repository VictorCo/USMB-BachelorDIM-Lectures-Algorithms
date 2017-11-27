# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief miscellaneous tools : check arguments, get url, global settings...

import pika
import os
import argparse

#define global settings for the software
settings = {}
settings["default_queue"] = "presentation"
settings["default_exchange"] = "posts"
#send 1 message every 5 seconds in fanout mode
settings["default_delay"] = 5
settings["url"] = "amqp://rrcieycj:5J4zugPSgWKzv264ta8jbex6q7r5FhvD@puma.rmq.cloudamqp.com/rrcieycj"

#list of possible argument
arg_concurrency = 0x1
arg_queueName = 0x2
arg_read = 0x4
arg_delay = 0x8
arg_signin = 0x16

#key_queueName = "queueName"

def check_argument():
    flag = 0
    #store value for arguments which are a value as queue_name 
    value = {}
    
    ##Init arguments -> create function for this
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency",
                        help="activate persistent message mode",
                        action="store_true")

    parser.add_argument("-q", "--queue_name",
                        help="define where you want to publish")

    parser.add_argument("-r", "--read",
                        help="read mode",
                        action="store_true")

    parser.add_argument("-d", "--delay",
                        help="allow a delay in read action. Value is a ms unit",
                        type=int)

    parser.add_argument("-s", "--signin",
                        help="sign in in the caramail instance",
                        type=str)

    args = parser.parse_args()
    ##

    ##check arguments
    if args.concurrency :
        flag = flag | arg_concurrency
    
    if args.queue_name :
        flag = flag | arg_queueName
        value[arg_queueName] = args.queue_name

    if args.read :
        flag = flag | arg_read

    if args.delay :
        flag = flag | arg_delay
        value[arg_delay] = float(args.delay / 1000.0)

    if args.signin :
        flag = flag | arg_signin
        value[arg_signin] = args.signin
    ##
        
    return [flag, value]


def set_queueName(args, value) :
    queue_name = ""
    
    if args & arg_queueName :
        queue_name = value[arg_queueName]
    else :
        queue_name = settings["default_queue"]

    return queue_name
