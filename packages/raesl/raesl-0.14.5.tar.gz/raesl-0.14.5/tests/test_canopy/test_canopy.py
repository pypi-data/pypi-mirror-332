from pathlib import Path

from ragraph.io.canopy import to_canopy

from raesl import datasets
from raesl.canopy import add_canopy_annotations


def test_canopy(tmpdir, gendir, inspect):
    graph = datasets.get("pump")
    add_canopy_annotations(graph)

    if inspect:
        outfile = Path(gendir) / "pump-canopy-test.json"
    else:
        outfile = Path(tmpdir) / "pump-canopy-test.json"

    to_canopy(graph, outfile)

    graph = datasets.get("rally-car")
    add_canopy_annotations(graph)

    if inspect:
        outfile = Path(gendir) / "rally-car-test.json"
    else:
        outfile = Path(tmpdir) / "rally-car-test.json"

    to_canopy(graph, outfile)
