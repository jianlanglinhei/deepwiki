import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from deepwiki.analyze import parse_call_graph


def test_parse_call_graph(tmp_path):
    src = tmp_path / "sample.py"
    src.write_text(
        """
        def a(x):
            return b(x)
        def b(x):
            return x
        def c(x):
            return a(x)
        """
    )
    edges = set(parse_call_graph(str(src)))
    assert ("a", "b") in edges
    assert ("c", "a") in edges
