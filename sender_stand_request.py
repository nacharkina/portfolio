import configuration
import requests
import data
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "Длина должна быть не менее 2 и не более 15 символов"

def negative_assert_no_firstname(user_body):

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"