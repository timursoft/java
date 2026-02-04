@pytest.mark.asyncio
def test_get_accessories_unauthorized(async_client: AsyncClient):
    response = await async_client.get("/api/accessories")
    assert response.status_code == 401, "Expected status code 401 for unauthorized access"