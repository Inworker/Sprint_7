import allure
import pytest
import data
import scooter_api


class TestLoginCurrier:

    @allure.description('Авторизация возвращает id')
    def test_sucess_login(self):
        body = scooter_api.CreateCurrier.generate_currier_data(self)  # Генерация данных курьера
        scooter_api.CreateCurrier.create_currier(self, body)  # Дернуть ручку
        login_currier2 = scooter_api.LoginCurrier()  # Создать экземпляр класса
        login_currier2.delete_firstName(body)  # Вызвать метод delete_firstName от экземпляра класса
        response_login = login_currier2.login_currier(body)  # Дернуть ручку без аргументов
        assert 200 == response_login.status_code and response_login.json()["id"] != []

    @pytest.mark.parametrize('key, value', [('login', data.fake.user_name()), ('password', data.fake.password())])
    @allure.description('Неверно указан логин или пароль')
    def test_wrong_login_or_password(self, key, value):
        body = scooter_api.CreateCurrier.generate_currier_data(self)  # Генерация данных курьера
        scooter_api.CreateCurrier.create_currier(self, body)  # Дернуть ручку
        login_currier2 = scooter_api.LoginCurrier()
        login_currier2.delete_firstName(body)  # Вызвать метод delete_firstName от экземпляра класса
        login_currier2.change_login_or_password(body, key, value)
        response_login = login_currier2.login_currier(body)  # Дернуть ручку
        assert 404 == response_login.status_code and response_login.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize('key, value', [('login', ""), ('password', "")])
    @allure.description('Не заполнен логин или пароль')
    def test_without_login_or_password(self, key, value):
        body = scooter_api.CreateCurrier.generate_currier_data(self)  # Генерация данных курьера
        scooter_api.CreateCurrier.create_currier(self, body)  # Дернуть ручку
        login_currier2 = scooter_api.LoginCurrier()
        login_currier2.delete_firstName(body)
        login_currier2.change_login_or_password(body, key, value)
        response_login = login_currier2.login_currier(body)  # Дернуть ручку
        assert 400 == response_login.status_code and response_login.json()["message"] == "Недостаточно данных для входа"
