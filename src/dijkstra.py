class BestPath:

    def __init__(self):
        self.processed = []

    def find_lower_costs_node(self, costs_gr):
        lower_cost = float("inf")
        lower_cost_node = None
        for node in costs_gr:
            cost = costs_gr[node]
            if cost < lower_cost and node not in self.processed:
                lower_cost = cost
                lower_cost_node = node
        return lower_cost_node

    def dsa(self, graph_gr, costs_gr, parents_gr):
        node = self.find_lower_costs_node(costs_gr)
        while node:
            cost = costs_gr[node]
            n_bors = graph_gr[node]
            for n in n_bors.keys():
                new_cost = cost + n_bors[n]
                if new_cost < costs_gr[n]:
                    costs_gr[n] = new_cost
                    parents_gr[n] = node
            self.processed.append(node)
            node = self.find_lower_costs_node(costs_gr)
        return self.processed
