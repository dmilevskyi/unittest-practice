import unittest

from dijkstra import Graph


class DijkstraTest(unittest.TestCase):
    def setUp(self) -> None:

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
            ]
        )

    def test(self):
        self.assertEqual(['a', 'b'], list(self.graph.dijkstra("a", "b")))
