# Graph-Rep.-in-Adjacency-Matrix
A program to create, check if it's connected, pathfind, and get degree of a graph representation in adjacency matrix. 
## Program Feature
#### Program Menu
![alt text](pictures/menu.PNG?raw=true)
#### Create a Adjacency Matrix
We create an adjacency matrix using numpy array, and the fill it. We add a feature so that user can choose, if the matrix is directed or undirected
#### Check if it's a Conected Matrix
We check it using recursion, we select one vertex and traverse to all connected vertex from that vertex. If 'vertex == len(tranversed_vertex)' its connected. If we use the for loop method. It will not work on this kind of case:
![alt text](pictures/UnconnectedGraph.PNG?raw=true)
#### Get Degree Matrix
We first check if the matrix is directed or not, and then we use for loop to get diagonal of a matrix add all the connected vertices to the diagonal of said matrix
#### Pathfind
For pathfinding we use 2 value, start(asal) and finish(tujuan). In this part of the code we implement the concept of backtracking, for this case:
![alt text](pictures/BacktrackingExample.PNG?raw=true)  
We use stack list, and travelled list. If the function reach a dead end. We remove the last space and set start value to (-1) of the stack.
