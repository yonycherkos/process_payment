# Coding exercise:

Write a Flask Web API with only 1 method called “ProcessPayment” that receives a request
like this

    - CreditCardNumber (mandatory, string, it should be a valid credit card number)
    - CardHolder: (mandatory, string)
    - ExpirationDate (mandatory, DateTime, it cannot be in the past)
    - SecurityCode (optional, string, 3 digits)
    - Amount (mandatoy decimal, positive amount)
    
The response of this method should be 1 of the followings based on

    - Payment is processed: 200 OK
    - The request is invalid: 400 bad request
    - Any error: 500 internal server error
    
The payment could be processed using different payment providers (external services)
called:

    - PremiumPaymentGateway
    - ExpensivePaymentGateway
    - CheapPaymentGateway.

The payment gateway that should be used to process each payment follows the next set of
business rules:

    a) If the amount to be paid is less than £20, use CheapPaymentGateway.
    b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
    Otherwise, retry only once with CheapPaymentGateway.
    c) If the amount is > £500, try only

PremiumPaymentGateway and retry up to 3 times
in case payment does not get processed.
Recommendations:

    - The classes should be written in such way that they are easy to test.
    - Write as many tests as you think is enough to be certain about your solution works -
    Use SOLID principles.
    - Decouple the logic the prediction logic from the API as much as possible

## How to run the project
Have `pipenv` installed in your system

run the following command to do so.

   1. clone the project from git on your system, run git clone https://github.com/yonycherkos/process_payment
   2. cd `process_payment`
   3. activate the virtual environment, inside the project run command `source env/bin/activate`
   4. exporting the FLASK_APP environment variable, run commamnd `export FLASK_APP=app.py`
   5. run command to run the flask server `flask run`
   6. To exit server run `ctrl+c`
   7. To exit the virtual env run command in terminal `deactivate`
   
 ## How to test the application
 
   1. run the server first using above step
   2. run comands: `pytest test/test_process_payment.py`

