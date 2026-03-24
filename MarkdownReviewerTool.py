from smolagents import Tool, tool
from doc import filestr

@tool
def markdown_specifications_documentation_tool():
    """A tool to source markdown specifications and documentation."""

    return filestr