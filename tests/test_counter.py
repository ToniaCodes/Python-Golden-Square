from lib.counter import *

def test_initial_count():
    counter = Counter()
    assert counter.count == 0

def test_add_method():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_report_method():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

    counter.add(10)
    assert counter.report() == "Counted to 10 so far."