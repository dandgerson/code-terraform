transmitter = get_component("transmitter")
thermometer = get_component("thermometer")

for planet in transmitter.list_planets():
    if planet.name == "Earth":
        connection = transmitter.connect(planet.id)
        if connection.status == 'ok':
            transmitter.transmit("current_temperature", thermometer.get_value())