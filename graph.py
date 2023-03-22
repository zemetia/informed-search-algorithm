import json


class Node:
    def __init__(self, city: str, heur: int = 0) -> None:
        self.city: str = city
        self.heur: int = heur
        self.child = []


class ChildNode:
    def __init__(self, node: Node, dist: int) -> None:
        self.node: Node = node
        self.dist: int = dist


class CityGraph:
    def __init__(self) -> None:
        self.map = {}
        self.heuristic = {}
        self.cities = {}

    def load_dataset(self, dataset_directory: str):
        self.map: dict = json.load(
            open(f'./dataset/{dataset_directory}/map.json'))
        self.heuristic: dict = json.load(
            open(f'./dataset/{dataset_directory}/heuristic.json'))

        self.cities = {city: Node(city, heur) for _, (city, heur) in enumerate(
            self.heuristic.items())}

        self.create_adj_list()

    def create_adj_list(self):
        if len(self.map) < 1:
            return

        for data in self.map:
            self.cities[data['city1']].child.append(
                ChildNode(self.cities[data['city2']], data["distance"]))
            self.cities[data['city2']].child.append(
                ChildNode(self.cities[data['city1']], data["distance"]))
