from collections import defaultdict

class Graph:
  
    def __init__(self, vertices):
        # num of vertices
        self.V = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    # a recursive function to print all paths from origin to destination.
    # visited[] keeps track of vertices in current path.
    # path[] stores actual vertices and path_index is current
    # index in path[]
    def print_Paths_util(self, u, d, visited, path):
 
        # note the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # if current vertex is same as destination, then print
        # current path[]
        if u == d:
            print (path)
        else:
            # if current vertex is not destination
            # recursion for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.print_Paths_util(i, d, visited, path)
                     
        # remove current vertex from path[] and note it as unvisited
        path.pop()
        visited[u]= False
  
  
    # prints the paths from 'origin' to 'destination'
    def print_Paths(self, o, d):
 
        # note all the vertices as not visited
        visited =[False]*(self.V)
        path = []
 
        # go back to helper to print the short paths
        self.print_Paths_util(o, d, visited, path)
  
  
  
# I immediately don’t know how to do Depth first traversal in python with strings, but I have done similar with ints so I made a sudo Dictionary to help organize the variables
'''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

dict1 = {'NY': 0,
'Iceland': 1,
'London': 2,
'Berlin': 3,
'Maine': 4,
'Paris': 5,
'Amsterdam': 6,
'Egypt': 7}
      
g = Graph(8)
g.addEdge(dict1['NY'],dict1['Iceland'])
g.addEdge(dict1['Iceland'],dict1['London'])
g.addEdge(dict1['London'],dict1['Berlin'])
g.addEdge(dict1['NY'],dict1['Maine'])
g.addEdge(dict1['Maine'],dict1['London'])
g.addEdge(dict1['Berlin'],dict1['Paris'])
g.addEdge(dict1['Paris'],dict1['Amsterdam'])
g.addEdge(dict1['Paris'],dict1['London'])
g.addEdge(dict1['London'],dict1['Egypt'])

# lists of test cases range
o = [0, 1, 2, 3, 4, 5, 6, 7];
d = [0, 1, 2, 3, 4, 5, 6, 7];

# change me for different tests
x = dict1['NY']
y = dict1['Berlin']

# catch out of bounds error
try:
    gotdata = '1'
except IndexError:
    gotdata = 'none'
    print(gotdata)
    quit()
print ("Here is the dictionary \n")
print (dict1)
print ('\n')

print ("Following are the paths from % o to % d:" %(o[x], d[y]))
g.print_Paths(o[x], d[y])