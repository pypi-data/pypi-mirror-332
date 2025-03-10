import pytest
from privydns.resolver import DNSResolver

resolver = DNSResolver()

def test_sync_doh():
    response = resolver.query("example.com", protocol="doh")
    assert response is not None
    assert len(response) > 0

@pytest.mark.asyncio
async def test_async_doh():
    response = await resolver.query("example.com", protocol="doh", async_mode=True)
    assert response is not None
    assert len(response) > 0

@pytest.mark.asyncio
async def test_async_invalid_protocol():
    with pytest.raises(ValueError):
        await resolver.query("example.com", protocol="invalid", async_mode=True)
