@pytest.mark.asyncio
def test_get_accessories_success(async_client: AsyncClient):
    response = await async_client.get("/api/accessories")
    assert response.status_code == 200, "Expected status code 200 when retrieving accessories"
    data = response.json()
    assert "categories" in data, "Response should contain 'categories' key"
    assert len(data["categories"]) > 0, "Categories should not be empty"