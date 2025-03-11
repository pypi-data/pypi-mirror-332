from functools import singledispatch
from treestyle import Formatter


class DictFormatter(Formatter):
    def get_field_value(self, obj, k):
        return obj[k]

    def fields(self, node):
        if isinstance(node, dict):
            return list(node)

        if isinstance(node, list):
            return list(range(len(node)))

        return None


def test_simple(snapshot):
    d = {"a": 1, "b": 2}
    f = DictFormatter()
    assert f.format(d) == snapshot


def test_nested(snapshot):
    d = {"a": 1, "b": {"c": 3}}
    f = DictFormatter()
    assert f.format(d) == snapshot


def test_nested_list(snapshot):
    d = {"a": 1, "b": [{"c": 3}]}
    f = DictFormatter()
    assert f.format(d) == snapshot


def test_compact(snapshot):
    d = {"a": 1, "b": {"c": 3}}
    f = DictFormatter(compact=True)
    assert f.format(d) == snapshot
