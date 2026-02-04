@pytest.mark.asyncio
def test_accessory_preview_success(async_client: AsyncClient):
    accessory_id = "hat_123"
    response = await async_client.get(f"/api/accessories/{accessory_id}/preview")
    assert response.status_code == 200, "Expected status code 200 when previewing an accessory"
    data = response.json()
    assert "preview_url" in data, "Response should contain 'preview_url' key"