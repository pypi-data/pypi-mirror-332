import numpy as np
import networkx as nx

def build_graph_from_bool_matrix(M):
    """
    Build an undirected graph G where there's an edge between i and j
    iff M[i][j] == True AND M[j][i] == True.
    """
    n = len(M)
    G = nx.Graph()
    G.add_nodes_from(range(n))  # Add all nodes
    
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] and M[j][i]:
                G.add_edge(i, j)
    
    return G

def keep_rows_and_columns(matrix, indices_to_keep):
    """
    Return the submatrix that only includes rows/columns in indices_to_keep,
    and the sorted list of original indices.
    """
    indices_sorted = sorted(indices_to_keep)
    # Use np.ix_ for "fancy" indexing of rows and columns by the same list
    submatrix = matrix[np.ix_(indices_sorted, indices_sorted)]
    return submatrix, indices_sorted

def find_minimal_removal_for_no_false(M):
    """
    - Convert the Boolean matrix M into an undirected graph G.
    - Find a maximum clique in G (largest set of mutually adjacent nodes).
    - Return (submatrix, survivors), where submatrix is M[S, S] 
      and S is the clique with no False entries among them.
    """
    G = build_graph_from_bool_matrix(M)
    
    # find_cliques(G) returns an iterator of *maximal* cliques.
    # We'll take the largest by size => a *maximum* clique.
    max_clique = max(nx.find_cliques(G), key=len)
    
    # Build the reduced matrix
    submatrix, survivors = keep_rows_and_columns(M, max_clique)
    mask = np.zeros(M.shape[0], bool)
    mask[survivors] = True
    return submatrix, survivors, mask

if __name__ == "__main__":
    # EXAMPLE USAGE

    # Suppose we have a Boolean matrix M (not necessarily symmetric),
    # but we interpret edges only if both M[i][j] AND M[j][i] are True.
    # We'll create a small random example:
    np.random.seed(42)
    n = 6
    M = np.random.choice([False, True], size=(n, n))

    # It's often convenient to ensure M[i][i] = True for all i,
    # but it's not strictly required.
    np.fill_diagonal(M, True)

    submat, survivors, mask = find_minimal_removal_for_no_false(M)
    
    print("Original matrix (True=1, False=0):\n", M.astype(int))
    print("\nMaximum clique (surviving indices):", survivors)
    print("\nSubmatrix with no False:\n", submat.astype(int))
    print("\Mask:\n", mask.astype(int))
