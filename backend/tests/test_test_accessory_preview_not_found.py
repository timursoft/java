@pytest.mark.asyncio
def test_accessory_preview_not_found(async_client: AsyncClient):
    accessory_id = "non_existing_id"
    response = await async_client.get(f"/api/accessories/{accessory_id}/preview")
    assert response.status_code == 404, "Expected status code 404 for non-existing accessory preview"