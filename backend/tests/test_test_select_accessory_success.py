@pytest.mark.asyncio
def test_select_accessory_success(async_client: AsyncClient):
    accessory_id = "hat_123"
    response = await async_client.post(f"/api/accessories/select", json={"accessory_id": accessory_id})
    assert response.status_code == 200, "Expected status code 200 when selecting an accessory"
    data = response.json()
    assert data["selected"] == accessory_id, "Response should confirm the selected accessory ID"