# test_hello_add.py
import pytest
import requests
import json

url = "http://127.0.0.1:5000"


def test_payment_no_data():
    # testing when request body has no data
    card_data = {}
    response = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data),
                             headers={"Content-Type": "application/json"})
    assert response.status_code == 400


def test_payment_invalid_argument():
    # testing api when request body has invalid argument, as compared to argument which is required
    card_data = dict(CreditCardNumbers="1234123412341234", CardHoldewr="yonathan cherkos",
                     SecurityCode="111", ExpirationDate="2020/1/1", Amount=222.2)
    response = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400


def test_payment_ext_invalid_credit_card_info():
    # testing for various cases when CreditCardNumber value is different, checking validity of credit
    # card numbers
    card_data_1 = {"CreditCardNumber": "qwer123456ijiojw", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2020/1/1", "Amount": 333.3}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 333.3}
    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_2), headers={"Content-Type": "application/json"})

    assert response_1.status_code == 400
    assert response_2.status_code == 200


def test_valid_input_data_for_various_amount():
    # testing the cases where for different amount input different external payment method invoke
    card_data_1 = {"CreditCardNumber": "1234567890123456", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 19}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 333}
    card_data_3 = {"CreditCardNumber": "1234567890123456", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 666}

    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_2), headers={"Content-Type": "application/json"})
    response_3 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_3), headers={"Content-Type": "application/json"})

    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200


def test_payment_ext_exp_date():
    # testing the ExpirationDate different case, when date is more then present and when date is past of present date
    card_data_1 = {"CreditCardNumber": "qwer123456ijiojw", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2019/11/12", "Amount": 333.3}

    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(
        card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})

    assert response_1.status_code == 200
    assert response_2.status_code == 400


def test_security_code():
    # testing for SecurityCode cases
    card_data_1 = {"CreditCardNumber": "qwer123456ijiojw", "CardHolder": "yonathan cherkos", "SecurityCode": "111",
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_2 = {"CreditCardNumber": "qwer123456ijiojw",
                   "CardHolder": "yonathan cherkos", "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_3 = {"CreditCardNumber": "qwer123456ijiojw", "CardHolder": "yonathan cherkos", "SecurityCode": 444,
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}

    response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1),
                               headers={"Content-Type": "application/json"})

    response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    response_3 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_3),
                               headers={"Content-Type": "application/json"})
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 400
