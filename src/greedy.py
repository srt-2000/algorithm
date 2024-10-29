class PathFinder:
    def __init__(self):
        self.postman_path = []
        self.distance = 0

    def find_postman_path(self, street_gr):
        for i in street_gr:
            self.postman_path.append(min(street_gr[i], key=street_gr[i].get))
            self.distance += min(street_gr[i].values())
        print(f"optimal postman path is {self.postman_path} with distance {self.distance} km")
