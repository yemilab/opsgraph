import pygraphviz as pgv

G = pgv.AGraph(strict=False,directed=True)

G.add_node('Pavement')
G.add_node('Door')
G.add_node('Coating')

G.add_edge('Pavement', 'Door')
G.add_edge('Pavement', 'Coating')

G.add_node('Hoist')

G.add_edge('Coating', 'Hoist')

G.add_node('1st floor')
G.add_node('DR supporting structure')
G.add_node('Vibration control decision')

G.add_edge('Door', '1st floor')
G.add_edge('Coating', '1st floor')
G.add_edge('Hoist', 'DR supporting structure')
G.add_edge('Vibration control decision', 'DR supporting structure')

G.add_node('RRS')
G.add_node('PCW')

G.add_edge('Pavement', 'RRS')
G.add_edge('Pavement', 'PCW')

G.add_node('DR')

G.add_edge('RRS', 'DR')
G.add_edge('PCW', 'DR')
G.add_edge('DR supporting structure', 'DR')

G.add_node('Water tank')

G.add_edge('DR', 'Water tank')
G.add_edge('1st floor', 'Water tank')

G.layout(prog='dot')

G.draw('file.png')
