from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Server", host="0.0.0.0", port=8000)


@mcp.tool()
def add_notes_to_file(content: str) -> str:
    """
    Appends the provided content as a new line to user's local notes.
    Args:
        content (str): The content to be added to the file.
    Returns:
        str: A confirmation message indicating success or failure.
    """
    import os
    filename = os.path.join(os.path.dirname(__file__), 'notes.txt')
    try: 
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        return f"Note added to {filename}."
    
    except Exception as e:
        return f"Failed to add note: {str(e)}"

@mcp.tool()
def read_notes_from_file() -> str:
    """
    Reads and returns the content of the user's local notes.
    Returns:
        str: The content of the file or an error message if the file cannot be read.
    """
    import os
    filename = os.path.join(os.path.dirname(__file__), 'notes.txt')
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content if content else "The notes file is empty."
    
    except FileNotFoundError:
        return f"The file {filename} does not exist."
    
    except Exception as e:
        return f"Failed to read notes: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
