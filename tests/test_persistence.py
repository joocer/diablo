import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from diablo import Graph
import diablo
from graph_data import build_graph, graph_is_as_expected
import shutil
from pathlib import Path

def test_save_graph():
    # test the save and read of diablo native graphs

    TEST_FOLDER = 'TEST_PERISTENCE'

    if Path(TEST_FOLDER).exists():
        shutil.rmtree(TEST_FOLDER)

    graph = build_graph()
    graph.save(TEST_FOLDER)

    del graph

    g = diablo.load(TEST_FOLDER)
    graph_is_as_expected(g)

    if Path(TEST_FOLDER).exists():
        shutil.rmtree(TEST_FOLDER)

def test_networkx():

    graph = build_graph()

    n = graph.to_networkx()
    graph_is_as_expected(n)

def test_read_graphml():

    graph = diablo.read_graphml('tests/data/test.graphml')
    graph_is_as_expected(graph)

if __name__ == "__main__":

    test_save_graph()
    test_networkx()
    test_read_graphml()
    
    print('okay')
