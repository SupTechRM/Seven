from data.realtime_mic import takeCommand
from intents import *

# Take Speech Recognition input and process it realtime running a main function
# main function will take the query
# query is sample input from which intent will be called, the modules will be runned
# speech synthesis as a response


#####################################
# Main Function
#####################################

while True:
    user_input = takeCommand()
    user_input = user_input.lower()
    intents(user_input)
