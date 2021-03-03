import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from data_sets import words_10, albums_25, words_10_ordered
from diablo import Index

def test_index_iterating_keys_and_values():

    index = Index(order=2)

    for word in words_10:
        index.insert(word[:1], word)

    k = [k for k,v in index.items()]
    v = [v for k,v in index.items()]

    # we should have 10 keys in alphabetical order
    assert len(k) == 10
    assert k == ['A', 'C', 'E', 'I', 'P', 'P', 'S', 'S', 'S', 'S']

    # we should have 10 values in alphabetical order
    assert len(v) == 10
    assert v == ['Aurora', 'Clinomania', 'Euphoria', 'Idyllic', 'Petrichor', 'Pluviophile', 'Serendipity', 'Supine', 'Solitude', 'Sequoia']

    # we should have 6 keys (deduplicated) in alphabetical order
    assert list(index.keys()) == ['A', 'C', 'E', 'I', 'P', 'S']


def test_look_up():

    index = Index(order=2)

    for album in albums_25:
        index.insert(album['artist'], album['album'])

    # look up on item with a 'clashing' key returns multiple items
    assert index.retrieve('Eagles') == ['Eagles/Their Greatest Hits 1971-1975', 'Hotel California']
    # also test can get back single items
    assert index.retrieve('Fleetwood Mac') == ['Rumours']
    # also test we get back nothing when there is no match
    assert index.retrieve('Flight of the Conchords') is None


if __name__ == "__main__":
    test_index_iterating_keys_and_values()
    test_look_up()

    print('okay')
