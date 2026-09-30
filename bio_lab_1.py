collector = get_component("bio_collector_1")

def get_stocked_qty(item_id: string):
    inventory = get_component("inventory")
    
    stocked = 0
    
    for slot in inventory.get_slots():
        if slot.id == item_id:
            stocked += slot.count

    return stocked

def buy_items(item_id, qty):
    get_component("shop").buy(item_id, qty)


def clear_output():
    connected_id = self.output.connected_id()
    self.output.connect("inventory")
    
    for stack in self.output.stacks():
        self.output.send(stack.id, stack.count)

    self.output.connect(connected_id)

self.input.connect("inventory")

def send_specimen(fragment_id, qty):
    for req_fragment_id, req_qty in get_component("bio_exchange_1").active_order().requires.items():
        if req_fragment_id == fragment_id:
            self.output.connect("bio_exchange_1")
            self.output.send(fragment_id, qty)

    self.output.connect("inventory")
    self.output.send(fragment_id, qty)

clear_output()

while True:
    specimen = self.specimen
    if not self.specimen and not collector.cargo:
        sleep(0.1)
        continue
    
    if not self.specimen and collector.cargo.stage == "collected":
        self.take_from(collector)
        sleep(0.1)
        continue

    if self.specimen.stage == "collected":
        self.analyze()
        sleep(0.1)
        continue

    if self.specimen.stage == "analyzed":
        if not self.loaded_reagents:
            for reagent_id, qty in self.specimen.recipe.items():
                if self.input.count() > 0:
                    self.input.eject("inventory", reagent_id, self.input.capacity())
                
                stocked = get_stocked_qty(reagent_id)
                if stocked < qty:
                    buy_items(reagent_id, qty - stocked)
    
            for reagent_id, qty in self.specimen.recipe.items():
                self.input.take(reagent_id, qty)
                self.load(reagent_id, qty)
            
        self.extract()
        send_specimen(specimen.fragment_id, 1)
        sleep(0.1)
        continue