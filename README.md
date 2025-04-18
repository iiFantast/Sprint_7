# Sprint_7
Проект для тестирования приложения http://qa-scooter.praktikum-services.ru

директория api_handlers содержит методы для тестирования эндпоинтов
директория test_data содержит данные для тестирования эндпоинтов
директория tests содержит тесты
директория allure_report содержит сформированный отчет allure

установка зависимостей:
pip install -r requirements.txt

запуск тестов:
pytest tests --alluredir=allure_result

открытие сформированного allure-отчета:
allure open allure_report