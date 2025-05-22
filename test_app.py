import pytest
from dash.testing.application_runners import import_app

# Note: Use `pip install pytest dash[testing]` to install test dependencies


def test_header_exists(dash_duo):
    """
    Tests if the H1 header with the text 'Pink Morsel Sales' exists.
    """
    app = import_app("app")
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales"
    dash_duo.wait_for_element(
        "#pink-morsel-graph", timeout=10
    )  # Wait for graph to render


def test_graph_exists(dash_duo):
    """
    Tests if the graph element with id 'pink-morsel-graph' exists.
    """
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-graph", timeout=10)
    assert dash_duo.find_element("#pink-morsel-graph")


def test_region_picker_exists(dash_duo):
    """
    Tests if the region picker radio items element with id 'region-radio' exists.
    """
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element(
        "#region-radio", timeout=10
    )  # Wait for radio items to render
    assert dash_duo.find_element("#region-radio")
