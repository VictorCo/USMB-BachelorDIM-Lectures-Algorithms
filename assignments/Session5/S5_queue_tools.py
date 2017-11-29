# -*- coding: utf-8 -*-

##
#@author Victor Cominotti
#@brief miscellaneous tools : global settings...

#global settings
settings = {}
settings["default_queue"] = "rpc_queue"
settings["url"] = "amqp://rrcieycj:5J4zugPSgWKzv264ta8jbex6q7r5FhvD@puma.rmq.cloudamqp.com/rrcieycj"

#set of discussions
#question -> q_x
#response -> r_x
settings["q_welcome"] = "hello, how are you ?"
settings["r_welcome"] = "fine and you ?"
settings["r_default"] = "I don't know what say to that"

#test for serialization with message pack module
settings["q_welcome"] = {"type":0, "value":"hello, how are you ?"}
settings["r_welcome"] = {"type":1, "value":"fine and you ?"}
settings["r_default"] = {"type":777, "value":"I don't know what say to that"}

#TODO
#instead of return a string, return the function that filter an image
#ex :  settings["filter_types"] = {"invert" : invert_color_manual(img), 
#                                  "threshold" : invert_color_manual(img),
#                                  "none" : "this filter doesn't exist"} 
#for now we change only a string to see that the communication works correctly
settings["filter_types"] = {"invert" : "function to invert", 
                            "threshold" : "function to threshold",
                            "none" : "this filter doesn't exist"} 
#input value                            
settings["invert_color"] = {"type" : "invert", 
                            "image" : "your image"} 
                            
settings["threshold"] = {"type" : "threshold",
                         "image" : "your image"}

settings["no_exist"] = {"type" : "toon_shading",
                         "image" : "your image"} 
