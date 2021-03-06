import itertools
import math
import matplotlib.pyplot as plt
import networkx as nx
from networkx.utils import py_random_state
from collections import defaultdict

def _random_subset(seq, m, rng):
    """ Return m unique elements from seq.

    This differs from random.sample which can return repeated
    elements if seq holds repeated elements.

    Note: rng is a random.Random or numpy.random.RandomState instance.
    """
    targets = set()
    while len(targets) < m:
        x = rng.choice(seq)
        targets.add(x)
    return targets

@py_random_state(2)
def YJBT_graph(n, m, seed=None):
    """Returns a random graph according to the Barabási–Albert preferential
    attachment model.

    A graph of $n$ nodes is grown by attaching new nodes each with $m$
    edges that are preferentially attached to existing nodes with high degree.

    Parameters
    ----------
    n : int
        Number of nodes
    m : int
        Number of edges to attach from a new node to existing nodes
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    G : Graph

    Raises
    ------
    NetworkXError
        If `m` does not satisfy ``1 <= m < n``.

    References
    ----------
    .. [1] A. L. Barabási and R. Albert "Emergence of scaling in
       random networks", Science 286, pp 509-512, 1999.
    """

    if m < 1 or m >= n:
        raise nx.NetworkXError(
            f"Barabási–Albert network must have m >= 1 and m < n, m = {m}, n = {n}"
        )

    # Add m initial nodes (m0 in barabasi-speak)
    G = nx.empty_graph(m)

    node_strength_dict={x:0 for x in range(n)}
    # Target nodes for new edges
    targets = list(range(m))
    # List of existing nodes, with nodes repeated once for each adjacent edge
    repeated_nodes = []
    # Start adding the other n-m nodes. The first node is m.
    source = m
    while source < n:
        # Add edges to m nodes from the source.\
        sm=[source] * m
        targets_weight=0
        for t in targets:
            targets_weight+=repeated_nodes.count(t)
        k=zip(sm, targets)
        edges=[]
        for x in k:
            if targets_weight!=0:
                weight=repeated_nodes.count(x[1])/targets_weight
            else:
                weight=1/targets.__len__()
            edges.append((x[0], x[1], weight))
            node_strength_dict[x[0]] += weight
            node_strength_dict[x[1]] += weight
        G.add_weighted_edges_from(edges)

        #每增加一个节点，显示当前的网络形状
        pos = nx.spring_layout(G)
        nx.draw(G, pos)
        edge_lable = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_lable)
        nx.draw_networkx_labels(G, pos)
        plt.show()


        # Add one node to the list for each new edge just created.
        repeated_nodes.extend(targets)
        # And the new node "source" has m edges to add to the list.
        repeated_nodes.extend([source] * m)
        # Now choose m unique nodes from the existing nodes
        # Pick uniformly from repeated_nodes (preferential attachment)
        targets = _random_subset(repeated_nodes, m, seed)
        source += 1



    #显示度分布
    node_weight_dict={x:repeated_nodes.count(x) for x in repeated_nodes}
    node_weight_list=list(node_weight_dict.values())
    node_weight_list.sort()

    weight_distribute_dict={x:node_weight_list.count(x) for x in node_weight_list}
    plt.plot(weight_distribute_dict.keys(),weight_distribute_dict.values())
    plt.xlabel("weight")
    plt.ylabel("count")
    plt.show()

    node_strength_list = list(node_strength_dict.values())
    node_strength_list.sort()
    #显示强度分布
    strength_distribute_dict = {x: node_strength_list.count(x) for x in node_strength_list}
    plt.plot(strength_distribute_dict.keys(), strength_distribute_dict.values())
    plt.xlabel("strength")
    plt.ylabel("count")
    plt.show()
    return G

G=YJBT_graph(100,20)
