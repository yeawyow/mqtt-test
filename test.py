import time
import paho.mqtt.client as mqtt

# Callback Functions
def on_message (client, userdata, message) :
    raw_message = str(message.payload.decode("utf-8"))
    topic = message.topic
    print(raw_message)
    

    print(int(time.time()), 'Received', topic, raw_message)

def on_subscribe (client, obj, mid, granted_qos) :
    print("Subscribe Succeed")


def on_connect (client, userdata, flags, rc) :
    print("Broker is connected")
    client.subscribe('moph/ict/mqtt')    
    
  
# Creating client
client = mqtt.Client()

# Configuring Callbacks
client.on_message=on_message 
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# Connecting to Broker
client.connect('localhost',10883)

client.loop_forever()