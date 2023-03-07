from setuptools import setup, find_packages

setup(
    name="tola_payments",
    version="0.1.2",
    description="A python package to easy push payment integration with Tola Payments with Mpesa, TigoPesa, and AirtelMoney Tanzania",
    packages=find_packages(),
    install_requires=["phonenumbers", "tanzania_mno", "python-decouple"],
)
