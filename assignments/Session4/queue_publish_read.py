# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief publish or read in a queue

from S4_queues_tools import *
from simple_queue_publish import publish_data
from simple_queue_read import read_data

args, value = check_argument()

if args & arg_read :
    read_data(args, value)
else :
    publish_data(args, value)
