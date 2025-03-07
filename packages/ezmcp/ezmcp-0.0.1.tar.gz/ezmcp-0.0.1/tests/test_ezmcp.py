import pytest

from ezmcp import TextContent, ezmcp


@pytest.fixture
def app():
    """Create a test ezmcp application."""
    return ezmcp("test-app")


def test_app_initialization():
    """Test that the ezmcp application initializes correctly."""
    app = ezmcp("test-app")
    assert app.name == "test-app"
    assert app.sse_path == "/messages"
    assert app.sse_endpoint == "/sse"
    assert app.docs_url == "/docs"
    assert app.debug is False


def test_tool_registration(app):
    """Test that tools can be registered correctly."""

    @app.tool(description="Test tool")
    async def test_tool(param1: str, param2: int = 0):
        return [TextContent(type="text", text=f"Test: {param1}, {param2}")]

    assert "test_tool" in app.tools
    assert app.tools["test_tool"]["schema"].name == "test_tool"
    assert app.tools["test_tool"]["schema"].description == "Test tool"

    # Check that parameters are correctly extracted
    params = app.tools["test_tool"]["params"]
    assert "param1" in params
    assert params["param1"].required is True
    assert "param2" in params
    assert params["param2"].required is False
    assert params["param2"].default == 0


def test_tool_schema_generation(app):
    """Test that tool schemas are generated correctly."""

    @app.tool(description="Test tool")
    async def test_tool(param1: str, param2: int = 0):
        return [TextContent(type="text", text=f"Test: {param1}, {param2}")]

    schema = app.tools["test_tool"]["schema"]

    # Check input schema
    input_schema = schema.inputSchema
    assert input_schema["type"] == "object"
    assert "param1" in input_schema["required"]
    assert "param2" not in input_schema["required"]

    # Check properties
    properties = input_schema["properties"]
    assert properties["param1"]["type"] == "string"
    assert properties["param2"]["type"] == "integer"


def test_starlette_app_creation(app):
    """Test that the Starlette application is created correctly."""
    starlette_app = app.get_app()
    assert starlette_app is not None

    # Check routes
    routes = starlette_app.routes
    assert len(routes) == 3  # SSE endpoint, messages mount, and docs

    # Check SSE endpoint
    sse_route = routes[0]
    assert sse_route.path == "/sse"

    # Check messages mount
    messages_mount = routes[1]
    assert messages_mount.path == "/messages"  # Starlette removes trailing slash

    # Check docs endpoint
    docs_route = routes[2]
    assert docs_route.path == "/docs"


def test_docs_disabled():
    """Test that the docs endpoint can be disabled."""
    app = ezmcp("test-app", docs_url=None)
    starlette_app = app.get_app()

    # Check routes
    routes = starlette_app.routes
    assert len(routes) == 2  # Only SSE endpoint and messages mount

    # Check route paths
    paths = [route.path for route in routes]
    assert "/docs" not in paths
