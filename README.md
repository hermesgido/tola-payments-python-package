
# Tola Payments Python Package


A python package to easy push payment integration with Tola Payments with Mpesa, TigoPesa, and AirtelMoney Tanzania. You can easily charge a customer's phone number with a specified amount, and the package will handle the necessary details to make the payment using the Tola Mobile API. No need to integrate each MNO individualy.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Tola Payments package.

Installation To install the Tola Payments package, run the following command:

```bash
pip install tola_payments
```

## Configuration

To use the package, you need to set up your Tola Mobile API credentials in a .env file. Add the following variables to your .env file: To use the Tola Payments package, you first need to import it into your Python code. Here's an example:


```env
TOLA_USERNAME = "my_username"
TOLA_PASSWORD = "my_password"
VODA_TARGET = "my_voda_target"
TIGO_TARGET = "my_tigo_target"
AIRTEL_TARGET = "my_airtel_target"
TOLA_LIVE_URL = "my_tola_live_url"
```

Next, create an instance of the TolaPayments class, providing your Tola Mobile API credentials:

```python
from tolapyments import TolaPayments
tolapayments = TolaPayments(is_sandbox=True)
```


Note that the is_sandbox parameter specifies whether you're using the Tola Mobile sandbox environment or the live environment. If you're using the sandbox environment, set is_sandbox to True. Otherwise, set it to False and provide the live API URL via the TOLA_LIVE_URL environment variable.

To charge a customer, call the charge_customer method on your TolaPayments instance, passing in the customer's phone number, the amount to charge, and a source reference

```python
response =tolapayments.charge_costomer(amount="1000",phone_number="+25561189850", sourcereference='4546f56543poF66')

print(response.text)
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
