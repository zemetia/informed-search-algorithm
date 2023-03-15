import json

class Node:
    def __init__(self, city: str, dist: int) -> None:
        self.city: str = city
        self.dist: int = dist

class CityGraph:
    def __init__(self) -> None:
        self.map = {}
        self.heuristic = {}
        self.city = {}

    def load_data(self, dataset_name: str) -> None:
        self.map: dict = json.load(open(f'./data/{dataset_name}/map.json'))
        self.heuristic: dict = json.load(open(f'./data/{dataset_name}/heuristic.json'))

        for data in self.heuristic:
            self.city.setdefault(data['city'], [])
        
        self.create_adj_list()

    def create_adj_list(self):
        if len(self.map) < 1:
            return
        
        for data in self.map:
            self.city[data['city1']].append(Node(data['city2'], data['distance']))
            self.city[data['city2']].append(Node(data['city1'], data['distance']))

            

