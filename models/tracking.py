class Tracking:
    def __init__(self, id):
        self.id = id
        self.history = []

    def update(self, msg):
        self.history.append(msg)
