@pytest.mark.asyncio
def test_select_accessory_unavailable(async_client: AsyncClient):
    accessory_id = "unavailable_id"
    response = await async_client.post(f"/api/accessories/select", json={"accessory_id": accessory_id})
    assert response.status_code == 400, "Expected status code 400 for selecting an unavailable accessory"