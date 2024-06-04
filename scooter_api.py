import allure
import requests

import data
import urls


class CreateCurrier:
    @allure.step('Вызов ручки Создания курьера')
    def create_currier(self, body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @allure.step('Генерация тестовых данных для 1-го курьера, все параметры заполнены')
    def generate_currier_data(self):
        return data.TestDataCurrier.CREATE_COURIER_BODY.copy()

    @allure.step('Генерация тестовых данных для 2-го курьера, все параметры заполнены')
    def generate_currier_data2(self):
        return data.TestDataCurrier.CREATE_COURIER_BODY2

    @allure.step('Генерация тестовых данных для 2-го курьера, все параметры заполнены')
    def generate_second_currier_data(self):
        return data.TestDataCurrier.create_courier_body.copy()

    @allure.step('Генерация тестовых данных для создания курьера с пустыми параметрами')
    def generate_null_currier_data(self):
        return data.TestDataCurrier.NULL_BODY

    @allure.step('Cоздал курьера и положил в переменную логин')
    def get_login_from_body(self, body):
        return body['login']

    @allure.step('Заменил его логин на 1-го курьера')
    def change_login_first_currier(self, key, value):
        body = key['login'] = value
        return body


class LoginCurrier:
    @allure.step('Вызов ручки авторизации курьера')
    def login_currier(self, body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=body)

    @allure.step('Удалить поле "firstname"')
    def delete_firstName(self, body):
        body.pop('firstName')

    @allure.step('Заменить параметр "логин или пароль"')
    def change_login_or_password(self, body, key, value):
        body[key] = value


class CreateOrder:
    @allure.step('Вызов ручки создания заказа')
    def create_order(self, body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDERS_ENDPOINT, json=body)

    @allure.step('Генерация данных для заказа')
    def generate_data_order(self):
        return data.TestDataCreateOrder.DATA_ORDER

    @allure.step('Заменить параметр "Цвет"')
    def change_color(self, body, Color):
        body['color'][0] = Color

    @allure.step('Добавить цвет')
    def add_color(self, body, color):
        body["color"].append(color)  # Добавить цвет

    @allure.step('Удалить цвет')
    def delete_color(self, body):
        body["color"] = []  # Удалить цвет


class GetOrder:
    @allure.step('Вызов ручки поулчения списка заказов')
    def get_orders_list(body):
        return requests.get(urls.BASE_URL + urls.GET_ORDER_LIST_ENDPOINT, json=body)

    @allure.step('Получить боди для списка заказаов')
    def get_body_for_order_list(self):
        return data.TestDataGetListOrder.PARAMS_ORDERS
