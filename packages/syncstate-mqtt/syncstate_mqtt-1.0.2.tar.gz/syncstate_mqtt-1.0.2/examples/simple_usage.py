import syncstate_mqtt

synced_dict = {"value1" : 1, "value2" : 2}


syncstate = syncstate_mqtt.SyncstateConnectionManager()
syncstate.attach(synced_dict)

while True:
    input(synced_dict)

