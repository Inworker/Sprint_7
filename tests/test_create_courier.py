import helper
import scooter_api
# from ... import scooter_api
import pytest
import allure


class TestCreateCurrier:

    @allure.description('Успешное создание курьера')
    def test_success_create_currier(self):
        create_currier2 = scooter_api.CreateCurrier()
        response_currier_request = create_currier2.create_currier(create_currier2.generate_currier_data())
        assert 201 == response_currier_request.status_code and response_currier_request.json()["ok"]

    @allure.description('Создание курьеров с одинаковым логином')
    def test_create_courier_same_login(self):
        create_currier2 = scooter_api.CreateCurrier()  # создаем экземпляр класса CreateCurrier
        body = create_currier2.generate_currier_data()  # Сгенерировал данные курьера
        body_login = create_currier2.get_login_from_body(
            body)  # Cгенерировал данные курьера и положил body в переменную
        create_currier2.create_currier(body)  # создал курьера

        create_currier3 = scooter_api.CreateCurrier()  # создаем новый экземпляр класса CreateCurrier
        body2 = create_currier3.generate_currier_data2()  # сгенерировал еще одного курьера
        create_currier3.change_login_first_currier(body2, body_login)
        response_currier_request = create_currier2.create_currier(body2)  # Получил ответ, что такой логин уже есть
        assert 409 == response_currier_request.status_code and response_currier_request.json()[
            "message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.description('Создание 2 одинаковых курьеров')
    def test_create_same_courier(self):
        body = scooter_api.CreateCurrier.generate_currier_data(self)  # Сгенерировал данные курьера
        create_currier2 = scooter_api.CreateCurrier()
        create_currier2.create_currier(body)
        response_currier_request = create_currier2.create_currier(body)  # Создал абсолютно такого же куьера
        assert 409 == response_currier_request.status_code and response_currier_request.json()[
            "message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    @allure.description('Не заполнен логин или пароль')
    def test_create_not_all_required_fields_are_filled_in(self, key, value):
        body = helper.ChangeTestDataHelper.change_data_courier(self, key, value)  # Сгенерировал данные курьера
        create_currier2 = scooter_api.CreateCurrier()
        response_currier_request = create_currier2.create_currier(body)
        assert 400 == response_currier_request.status_code and response_currier_request.json()[
            "message"] == "Недостаточно данных для создания учетной записи"

    @allure.description('Создание курьера с пустыми параметрами')
    def test_create_courier_all_null_parametr(self):
        create_currier2 = scooter_api.CreateCurrier()
        response_currier_request = create_currier2.create_currier(create_currier2.generate_null_currier_data())
        assert 400 == response_currier_request.status_code and response_currier_request.json()[
            "message"] == "Недостаточно данных для создания учетной записи"
