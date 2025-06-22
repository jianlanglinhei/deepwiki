"""Simple code analysis utilities."""

import ast
import networkx as nx
from typing import List, Tuple


def parse_call_graph(source_path: str) -> List[Tuple[str, str]]:
    """Parse a Python file and return function call edges.

    Parameters
    ----------
    source_path: str
        Path to the Python source file.

    Returns
    -------
    List[Tuple[str, str]]
        List of (caller, callee) pairs representing calls between
        defined functions.
    """

    with open(source_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code, filename=source_path)
    G = nx.DiGraph()

    func_defs = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    for func in func_defs:
        G.add_node(func.name)

    for func in func_defs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                caller = func.name
                callee = node.func.id
                if callee in G.nodes:
                    G.add_edge(caller, callee)

    return list(G.edges())
