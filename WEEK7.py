class Tracking:
    def __init__(self, tid):
        self.tracking_id = tid
        self.location = "Warehouse"
        self.history = []

    def update_location(self):
        loc = input("Enter new location: ")
        self.location = loc
        self.history.append(loc)
        print("Location updatd")

    def show_tracking(self):
        print("Tracking ID:", self.tracking_id)
        print("Current Location:", self.location)
        print("History:", self.history)