"""Command line interface for DeepWiki utilities."""

import argparse
from .analyze import parse_call_graph


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Analyze Python call graphs")
    parser.add_argument("source", help="Path to Python source file")
    args = parser.parse_args(argv)

    edges = parse_call_graph(args.source)
    if not edges:
        print("No function calls found.")
        return
    print("Function call dependencies:")
    for caller, callee in edges:
        print(f"{caller} -> {callee}")


if __name__ == "__main__":
    main()
