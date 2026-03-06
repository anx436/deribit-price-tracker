import pytest
from unittest.mock import AsyncMock, MagicMock, patch

class AsyncContextManagerMock(AsyncMock):
    """Proper async context manager mock."""
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

@pytest.mark.asyncio
async def test_deribit_get_index_price():
    from app.clients.deribit import DeribitClient
    
    client = DeribitClient()
    
    # Create proper async context manager mocks
    mock_response = AsyncContextManagerMock()
    mock_response.__aenter__.return_value = mock_response
    mock_response.json = AsyncMock(return_value={"result": {"index_price": 98765.43}})
    mock_response.raise_for_status = MagicMock()  # fix for warning: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited 
    
    mock_session = AsyncContextManagerMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.get = MagicMock(return_value=mock_response)
    
    with patch("aiohttp.ClientSession", return_value=mock_session):
        price = await client.get_index_price("btc_usd")
        
        assert price == 98765.43
        mock_session.get.assert_called_once_with(
            f"{client.base_url}/public/get_index_price",
            params={"index_name": "btc_usd"}
        )
