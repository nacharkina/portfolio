import sender_stand_request
import data

# Тест 1. Успешное создание пользователя. Параметр firstName состоит из 2 символов
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")


# Тест 2. Успешное создание пользователя. Параметр firstName состоит из 15 символов
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")


# Тест 3. Ошибка. Параметр firstName состоит из 1 символа
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")


# Тест 4. Ошибка. Параметр firstName состоит из 16 символов
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааa")


# Тест 5. Успешное создание пользователя. Параметр fisrsName состоит из английских букв
def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание пользователя. Параметр firstName состоит из русских букв
def test_create_user_russian_letter_in_first_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Ошибка. Параметр firstName состоит из слов с пробелами
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Человек и КО")


# Тест 8. Ошибка. Параметр firstName состоит из строки спецсимволов
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")


# Тест 9. Ошибка. Параметр firstName состоит из строки цифр
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


# Тест 10. Ошибка. В запросе нет параметра firstName
def test_create_user_no_first_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    user_body = data.user_body.copy()
    # Удаление параметра firstName из запроса
    user_body.pop("firstName")
    # Проверка полученного ответа
    negative_assert_no_firstname(user_body)


# Тест 11. Ошибка. Параметр состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert_no_firstname(user_body)


# Тест 12. Ошибка. Тип параметра firstName: число
def test_create_user_number_type_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(12)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_user(user_body)

    # Проверка кода ответа
    assert response.status_code == 400
