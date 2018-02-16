# Graphs
A graph is a set of vertices plus a set of edges (or vertex pairs). G = (V, E)

A tree is a unidirected graph where two vertices are connected by only one path.

## Types

### Direction
  * Unidirected: Edge `(x, y) ∈ E` implies edge `(y, x) ∈ E`
  * Directed: Edge `(x, y) ∈ E` does **NOT** imply edge `(y, x) ∈ E`

### Weight
  * Weighted: each edge (or vertex) has a numerical value.
  * Unweighted: no numerical values

### Edge special cases
   * Non-Simple: with self-loops and/or multiedge: when the same edge appears more than once.
   * Simple without loops and multiedge.

### Amount of edges
  * Sparse: few edges. For example: combination (n 2) for n vertices in a simple unidirected graph. 
  * Dense

### Cycles
  * Cyclic:
  * Acyclic: For example: Directed acyclic used in scheduling.

### Representation
  * Embedded: Vertices and edges have geometric positions. A drawing is then an embedding and the graph can be described by it.
  * Topological: matrices with implicit edges or vertices without positions.

### Construction
  * Implicit: built as you go.
  * Explicit: built beforehand

### Labels
  * Labeled
  * Unlabeled

## Data structures

### Matrix

For n vertices, a matrix `n x n` where a cell (i,j) is an edge if it contains a 1, and a 0 if it isn't.

  * Good to test if (i, j) exists, to add and remove edges.
  * Too much memory if there are many nodes and few edges.

### Adjacent list

Where each vertex store in a linked list its edges to neighbours.

  * Less memory for small graphs. In a n-vertex m-edge graph, Use if `n+2m < n^2`