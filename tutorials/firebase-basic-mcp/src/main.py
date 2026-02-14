"""
Entrypoint for the MCP server.

For this example we will use a subgraph api available to retrieve data from the
blockchain, and expose additional analytics tools to the user.

The subgraph can be found at: https://thegraph.com/explorer/subgraphs/HNCFA9TyBqpo5qpe6QreQABAA1kV8g46mhkCcicu6v2R
"""

# Third Party Imports
from mcp.server.fastmcp import FastMCP

# Local Imports
from .subgraph import get_uniswap_data  

# Server
mcp = FastMCP("Firebase-MCP-Tutorial")


# Resources definitions
@mcp.resource("uniswap-data://history")
async def resource_uniswap_data() -> list[dict]:
    """
    Get data from the uniswap subgraph.
    """
    # Get the data
    try:
        return await get_uniswap_data()
    except Exception as e:
        return f"Error: {e}"

# Tools definitions
@mcp.tool()
async def tool_basic_analytics() -> str:
    """
    Calculate basic analytics for a given address.
    """
    # Get the data
    try:
        data = await get_uniswap_data()
        # Calculate basic aggregations
        total_liquidity = sum([
            pos.get("totalValueLockedUSD")
            for pos in data
        ])
        total_volume = sum([
            pos.get("volumeUSD")
            for pos in data
        ])
        tx_count = sum([pos.get("txCount") for pos in data])
        # Calculate the average price
        average_price = total_volume / total_liquidity
        # Calculate the average volume
        average_volume = total_volume / tx_count
        # Return the result
        return f"Average Price: {average_price}, Average Volume: {average_volume}"
    except Exception as e:
        return f"Error: {e}"

# Entrypoint
if __name__ == "__main__":
    # Run the server
    mcp.run()
