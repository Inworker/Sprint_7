import allure
import pytest
import scooter_api


class TestCreateOrder:

    @pytest.mark.parametrize('Color', ['BlACK', 'GREY'])
    @allure.description('При создании заказа можно указать 1 из цветов')
    def test_create_order_black_or_grey(self, Color):
        body = scooter_api.CreateOrder.generate_data_order(self)  # Генерация данных для курьера
        create_order2 = scooter_api.CreateOrder()
        create_order2.change_color(body, Color)
        responce_order = create_order2.create_order(create_order2.change_color(body, Color))
        assert 201 == responce_order.status_code and responce_order.json()["track"] != []

    @allure.description('При создании заказа можно указать оба цвета')
    def test_create_order_black_or_grey(self):
        body = scooter_api.CreateOrder.generate_data_order(self)  # Генерация данных для курьера
        create_order2 = scooter_api.CreateOrder()
        body_with_color = create_order2.add_color(body, "GREY")  # Добавление цвета
        response_order = create_order2.create_order(body_with_color)  # Создание заказа с указанным цветом
        assert 201 == response_order.status_code and response_order.json()["track"] != []

    @allure.description('Можно не указывать цвет')
    def test_create_order_null_color(self):
        body = scooter_api.CreateOrder.generate_data_order(self)  # Генерация данных для курьера
        create_order2 = scooter_api.CreateOrder()
        deleted_color_body = create_order2.delete_color(body)
        responce_order = create_order2.create_order(deleted_color_body)
        assert 201 == responce_order.status_code and responce_order.json()["track"] != []
