"""
Functions related with the subgraph api.
"""

# Standard Library Imports
import os
# Third Party Imports
from dotenv import load_dotenv
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Retrieve the environment variables
load_dotenv()

# Constants
API_URL = f"https://gateway.thegraph.com/api/{os.getenv('SUBGRAPH_API_KEY')}/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"

# Client
transport = AIOHTTPTransport(
    url=API_URL,
    headers={
        "Content-Type": "application/json",
    }
)
client = Client(transport=transport)

# Queries
QUERY_GET_UNISWAP_DATA_FOR_ADDRESS = gql(
    """
    query {
        positions(first: 10) {
            id
            pool {
                id
                token0 {
                    id
                    symbol
                }
                token1 {
                    id
                    symbol
                }
                txCount
                totalValueLockedUSD
                volumeUSD
            }
        }
    }
    """
)

# Functions
async def get_uniswap_data() -> list[dict]:
    """
    Get data from the uniswap subgraph.
    """
    # Execute the query
    result = await client.execute_async(
        QUERY_GET_UNISWAP_DATA_FOR_ADDRESS
    )
    # Handle if the query fails
    if result.get("errors"):
        raise Exception(result.get("errors"))
    # Format the result
    result = [
        {
            "token0": pos.get("pool").get("token0").get("symbol"),
            "token1": pos.get("pool").get("token1").get("symbol"),
            "txCount": int(pos.get("pool").get("txCount")),
            "totalValueLockedUSD": float(pos.get("pool").get("totalValueLockedUSD")),
            "volumeUSD": float(pos.get("pool").get("volumeUSD"))
        }
        for pos in result.get("positions")
    ]
    # Return the result
    return result
