class Hospital:

    # 생성자
    def __init__(self, lat, lng, capacity, name):
        self.lat = lat
        self.lng = lng
        self.capacity = capacity
        self.name = name
        self.processing = {}
        self.total = 0
        self.currPatient = 0
        self.complete = {}

    def show(self):
        print("lat=", self.lat, "lng=", self.lng, "c=", self.capacity, "name=", self.name)

    def setprocessing(self, key, value, movetime):

        setlist = [value, movetime]
        if key in self.processing:
            self.processing[key][0] += value

        else:
            self.processing[key] = setlist

    def setcomplete(self, key, value):

        if key in self.complete:
            self.complete[key] += value

        else:
            self.complete[key] = value
