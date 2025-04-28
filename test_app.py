from dash import html, dcc
from app import app


def test_header_exists():
    """
    Tests if the H1 header exists in the app layout.
    """
    # Check if any component in the layout's children is an H1
    assert any(isinstance(child, html.H1) for child in app.layout.children)


def test_graph_exists():
    """
    Tests if the graph element with id 'pink-morsel-graph' exists in the app layout.
    """
    # Check if any component in the layout's children is a Graph with the correct ID
    assert any(
        isinstance(child, dcc.Graph) and child.id == "pink-morsel-graph"
        for child in app.layout.children
    )


def test_region_picker_exists():
    """
    Tests if the region picker radio items element with id 'region-radio' exists in the app layout.
    """
    # Check if any component in the layout's children is RadioItems with the correct ID
    assert any(
        isinstance(child, dcc.RadioItems) and child.id == "region-radio"
        for child in app.layout.children
    )
