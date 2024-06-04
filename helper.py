import allure
import scooter_api


class ChangeTestDataHelper:
    @allure.step('# Сгенерировал данные курьера ')
    def change_data_courier(self, key, value):
        body = scooter_api.CreateCurrier.generate_currier_data(self)
        body[key] = value
        return body
