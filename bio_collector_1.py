def get_stocked_qty(item_id: string):
    stocked = 0
    
    for slot in get_component("inventory").get_slots():
        if slot.id == item_id:
            stocked += slot.count

    return stocked

def get_req_fragment_coords(fragment_id):
    for fragment in get_component("journal").cataloged_fragments("nocturna"):
        if fragment.fragment_id == fragment_id:
            return fragment.coords

    return None

active_order = get_component("bio_exchange_1").active_order()

while active_order.percent < 100:
    for req_fragment_id, req_count in active_order.requires.items():
        stocked = get_stocked_qty(req_fragment_id)
        rest = req_count - active_order.delivered[req_fragment_id]

        if stocked == 0 and rest > 0:    
            required_fragment_coords = get_req_fragment_coords(req_fragment_id)
            
            if not required_fragment_coords:
                locations = self.scan()
                for location in locations:
                    if not location.cataloged and not self.cargo:
                        self.collect(location.coords)
                        break
            else:
                if not self.cargo:
                    self.collect(required_fragment_coords)
                else:
                    sleep(0.1)

        sleep(0.1)
        