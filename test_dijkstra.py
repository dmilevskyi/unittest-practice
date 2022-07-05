import unittest

from dijkstra import Graph


class DijkstraTest(unittest.TestCase):
    def setUp(self):

        self.graph = Graph(
            [
                ("a", "b", 7),
                ("a", "c", 9),
                ("a", "f", 14),
                ("b", "c", 10),
                ("b", "d", 15),
                ("c", "d", 11),
                ("c", "f", 2),
                ("d", "e", 6),
                ("e", "f", 9),
                ("f", "g", float("inf"))
            ]
        )

    def test(self):
        self.assertEqual(['a', 'b'], list(self.graph.dijkstra("a", "b")))

    def test_shortest_route(self):
        self.assertEqual(['a', 'c', 'f', 'e'], list(self.graph.dijkstra("a", "e")))

    def test_no_path(self):
        self.assertEqual(['g'], list(self.graph.dijkstra("a", "g")))

    def test_same_cost(self):
        self.assertEqual(['e', 'f'], list(self.graph.dijkstra("e", "f")))

    def test_non_existent_vertices(self):
        with self.assertRaises(KeyError) as context:
            list(self.graph.dijkstra("a", "z"))

        self.assertFalse('There is undefined vertices' in context.exception)