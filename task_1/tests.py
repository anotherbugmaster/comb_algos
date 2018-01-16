from task_1 import find_min_span_tree, find_edges, Edge


class TestFindEdges(object):
    def test_find_edges(self):
        graph = [
            [(2, 25), (3, 4)],
            [(1, 25), (3, 0)],
            [(1, 4), (2, 0), (4, 7)],
            [(3, 7)],
        ]

        expected_edges = [
            Edge((2, 3), 0),
            Edge((1, 3), 4),
            Edge((3, 4), 7),
            Edge((1, 2), 25),
        ]

        assert find_edges(graph) == expected_edges


class TestFindMinSpanTree(object):
    def test_find_min_span_tree(self):
        graph = [
            [(2, 25), (3, 4)],
            [(1, 25), (3, 0)],
            [(1, 4), (2, 0), (4, 7)],
            [(3, 7)],
        ]

        expected_min_span_tree = {
            Edge((1, 3), 4),
            Edge((2, 3), 0),
            Edge((4, 3), 7),
        }

        assert find_min_span_tree(graph) == expected_min_span_tree
