import networkx as nx

class GraphIntelligence:
    """Incremental transaction graph with structural mule indicators."""
    def __init__(self): self.g=nx.DiGraph()
    def observe(self, sender, receiver, amount):
        self.g.add_edge(sender, receiver, weight=float(amount))
    def features(self, account_id):
        if account_id not in self.g: return {"degree":0,"pagerank":0.0,"betweenness":0.0,"fan_in":0,"fan_out":0}
        deg=self.g.degree(account_id); n=max(1,self.g.number_of_nodes()-1)
        pr=nx.pagerank(self.g, weight="weight").get(account_id,0.0) if self.g.number_of_edges() else 0.0
        fan_in=self.g.in_degree(account_id); fan_out=self.g.out_degree(account_id)
        return {"degree":deg,"pagerank":pr,"betweenness":0.0,"fan_in":fan_in,"fan_out":fan_out,"degree_ratio":deg/n}
