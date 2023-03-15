from graph import CityGraph

romania = CityGraph()
romania.load_data('dataset-1')
print(romania.city)


# romania.setdefault(city1, []).append(CityNode(city2, dist))
# romania.setdefault(city2, []).append(CityNode(city1, dist))