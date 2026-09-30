atmosphere = get_component("atmosphere")

while True:
    self.set_intake(atmosphere.get_co2() * 0.1)
    
    if 50 < self.waste() < 60:
        self.dump_waste()
        sleep(0.1)
    
    sleep(0.1)