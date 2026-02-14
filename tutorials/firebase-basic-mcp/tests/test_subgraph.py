"""
Tests for the subgraph module.
"""

# Third Party Imports
import pytest
# Package Imports
from src.subgraph import get_uniswap_data

# Tests
@pytest.mark.asyncio
async def test_get_uniswap_data():
    """
    Test the get_uniswap_data function.
    """
    # Get the data
    data = await get_uniswap_data()
    print(data)