class Edge(object):
    def __init__(self, vertices, weight):
        self.vertices = vertices
        self.weight = weight

    def __eq__(self, other):
        return (
                type(self) == type(other)
                and set(self.vertices) == set(other.vertices)
                and self.weight == other.weight
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.vertices[0]) ^ hash(self.vertices[1])


def load_graph(graph_arr):
    graph = []

    v_starts = graph_arr[:graph_arr[0] - 1]
    for i in range(len(v_starts) - 1):
        vertice_neighbors = []

        for j in range(v_starts[i] - 1, v_starts[i + 1] - 1, 2):
            vertice_neighbors.append(tuple(graph_arr[j:j+2]))

        graph.append(vertice_neighbors)

    return graph


def dump_graph(edges, graph_size):
    graph_arrs = [[] for _ in range(graph_size)]

    for edge in edges:
        graph_arrs[edge.vertices[0] - 1].append(edge.vertices[1])
        graph_arrs[edge.vertices[1] - 1].append(edge.vertices[0])

    for idx in range(graph_size):
        graph_arrs[idx] = sorted(graph_arrs[idx])
        graph_arrs[idx].append(0)

    edges_weight = sum(edge.weight for edge in edges)

    return graph_arrs, edges_weight


def find_edges(graph):
    edges = set()

    for idx, vertice_neighbors in enumerate(graph):
        for vertice in vertice_neighbors:
            edges.add(Edge((idx + 1, vertice[0]), vertice[1]))

    return sorted(list(edges), key=lambda edge: edge.weight)


def find_min_span_tree(graph):
    edges = find_edges(graph)
    visited_vertices = set()
    min_span_tree = []

    while len(visited_vertices) < len(graph):
        for edge in edges:
            if (
                    len(visited_vertices.intersection(set(edge.vertices))) == 1
                    or len(visited_vertices) == 0
            ):
                min_span_tree.append(edge)
                visited_vertices.update(edge.vertices)
                break

    return min_span_tree


def main():
    with open('../In1_1.txt', 'r') as reader:
        arr_size = int(reader.readline())

        graph_arr = []
        while len(graph_arr) < arr_size:
            graph_arr.extend(int(_) for _ in reader.readline().split())

    graph = load_graph(graph_arr)
    min_span_tree = find_min_span_tree(graph)

    graph_arrs, tree_weight = dump_graph(min_span_tree, len(graph))

    with open('out.txt', 'w+') as writer:
        for arr in graph_arrs:
            writer.write(" ".join([str(e) for e in arr]) + '\n')

        writer.write(str(tree_weight))


if __name__ == "__main__":
    main()
