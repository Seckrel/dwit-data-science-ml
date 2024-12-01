class Coordinate:
    def __init__(self, lat=0.0, long=0.0) -> None:
        self.lat = lat
        self.long = long

    def __add__(self, coord):
        print(self.lat, coord, type(coord))
        if isinstance(coord, Coordinate):
            return Coordinate(self.lat + coord.lat, self.long + coord.long)
        
    def __str__(self) -> str:
        return f"Lat: {self.lat:.2f} | Long: {self.long:.2f}"
        

coord1 = Coordinate(12.34, 56.78)
coord2 = Coordinate(34.56, 78.90)

coord_sum = coord1 + 12

print(coord_sum)
