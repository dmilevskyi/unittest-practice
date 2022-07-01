# Практическое занятие

В результате успешного выполнения практического задания студент будет уметь:

* описывать тесты к функции c помощью библиотеки `unittest`;
* запускать автоматические тесты;

## Требования к программному обеспечению

* Операционная система: Windows, MacOS или Linux;
* Python 3.10 или старше
* Любой текстовый редактор

## Установка unittest

`unittest` — стандартный пакет Python и не требует установки.

## Тесты в документации

Рассмотрим файл `dijkstra.py` — это реализация [алгоритма Дейкстры](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%94%D0%B5%D0%B9%D0%BA%D1%81%D1%82%D1%80%D1%8B):


```python
# Source: http://rosettacode.org/
from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])


class Graph:
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))

        # pp(neighbours)

        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        # pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
```

А также заготовку тестов к алгоритму (файл `test_dijkstra.py`):

```python
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
```

Запустить тесты можно командой из консоли:

    python -m unittest -v

Отчет будет на консоли:

```text
test (test_dijkstra.DijkstraTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Новые тесты

Запишите новые тесты в файле `test_dijkstra.py`:

* проверка, что между двумя маршрутами выбирается кратчайший;
* проверка, что будет если между двумя вершинами нет пути;
* провека, что будет если между двумя вершинами есть два пути с одинаковой стоимостью;
* проверка, что алгоритм выкидывает исключение при попытке построить маршрут между несуществующими вершинами;

Проверьте, что все тесты выполняются. 

Произвольным образом внесите несколько логических ошибок в файл `dijkstra.py` и убедитесь, что тест их обнаруживает. Синтаксические ошибки вносить нельзя.

Отчет о запуске (текст консольного вывода) сохраните в файл `unittest_report.txt`.

## Отчет

Для отчета по практическому заданию необходимо:

1. Создать публичный репозиторий на GitHub на основе репозитория https://github.com/1irs/unittest-practice Можно воспользоваться страницей Generate: https://github.com/1irs/unitteset-practice/generate для создания своего репозитория по шаблону.
2. В отдельном коммите дописать тесты и добавить файл `unittest_report.txt`
3. Прислать ссылку на репозиторий на obrizan@1irs.net
