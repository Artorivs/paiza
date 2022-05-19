from itertools import combinations 
from networkx import Graph
from networkx import all_simple_paths

M, N = map(int, input().split()) # M: no. of people; N: no. of total point
Start, Goal = map(int, input().split()) # S: start point; G: goal point

D = list(int(input()) for _ in range(M)) # d: distance which a person can move

x_i = []

for _ in range(N):
    a_i = list(map(int, input().split()))
    x_i.append(a_i[1:])

# compute the distance between the start point and the goal point in x_i
edges = []
for subgraph in x_i:
    edges_sub_graph = list(combinations(subgraph, 2))
    edges.extend(edges_sub_graph)

print(edges)


G = Graph()
G.add_edges_from(edges)

paths = []
# calculate all possible paths length from S to G 
for path in all_simple_paths(G, Start, Goal):
    if len(path) in paths:
        continue
    else:
        paths.append(len(path))

# if D meet one of the path length, print yes, else print no
for i in D:
    if i in paths:
        print('yes')
    elif i not in paths:
        print('no')
