class PKT_TYPE:
    RREQ = 'REQ'
    RREP = 'REP'
    DPKT = 'DATA'


class Packet:
    def __init__(self, id, type_):
        self.id = id
        self.type = type_
        self.target = None
        self.source_route = []
        self.data = None
        self.cur_hop = 0
        self.source = None

    def add_id(self, id):
        self.source_route.append(id)

    def check_id(self, id):
        if id in self.source_route:
            return True
        return False
