import networkx as nx
from automobile import Automobile

import matplotlib.pyplot as plt

# Creo il mio oggetto grafo
#g = nx.Graph() # Simple graph, un solo arco tra i nodi
g = nx.DiGraph() # Simple graph, un solo arco tra i nodi

g.add_node(1)
g.add_node(2)

g.add_edge(1, 2)
g.add_edge(1, 3, peso = 5)

g.add_node("pippo")

# Posso usare come nodi qualsiasi oggetto ...
# ... purché sia hashable (quindi implementi __hash()__
#auto = Automobile("FJ198CV", "Bianco", "Nero")
#g.add_node(auto)

print(g)

print(g[1]) # Un dizionario dei nodi connessi a 1

print(g[1][3]) # Un arco

print(g[1][3]["peso"]) # Il peso dell'arco da 1 a 3

g.add_edge(2,1)

# Archi
nodi = g.nodes
print(nodi)
archi = g.edges
print(archi)

if 7 in g.nodes:
    print("Nodo presente")
else:
    print("Nodo assente")

for n in g.nodes:
    print(n)

densita = nx.density(g)
print(f"Densita: {densita}")

nx.draw(g,
        connectionstyle=["arc3,rad=0.1","arc3,rad=0.5"],
        with_labels=True,
        arrows=True)
plt.show()


mg = nx.MultiGraph() #MultiDiGraph
mg.add_node(1)
mg.add_node(2)
mg.add_edge(1, 2, peso = 5)
mg.add_edge(1, 2, peso = 7)

