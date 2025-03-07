# Syncstate mqtt

This package is made to read from a mqtt broker and update a python dictionary accordingly

## How to use

To use syncstate you will need a MQTT broker, for the example the broker is set up on `localhost:1883`

```python
import syncstate_mqtt

synced_dict = {"value1" : 1, "value2" : 2} # the states will not be changed my syncstate


# Create a connection manager
syncstate = syncstate_mqtt.SyncstateConnectionManager("localhost", 1883)
syncstate.attach(synced_dict) # select the dictionary to attach to

# now your dictonary is synced
while True:
    print(synced_dict)
    input()
```

## LICENSE

    Syncstate - keep python dictionary syncronised over network
    Copyright (C) 2025  Goldenbeasty

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

