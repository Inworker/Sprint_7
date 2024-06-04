import allure
import scooter_api


class TestGetOrderList:
    @allure.description("Получен список заказов")
    def test_get_orders_list(self):
        body = scooter_api.GetOrder.get_body_for_order_list(self)
        responce_data = scooter_api.GetOrder.get_orders_list(body)  # Получение списка заказов
        assert 200 == responce_data.status_code and responce_data.json()["orders"] != "[]"
