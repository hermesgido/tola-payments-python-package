from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="tola_payments",
    version="0.1.7",
    description="A python package to easy push payment integration with Tola Payments with Mpesa, TigoPesa, and AirtelMoney Tanzania",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["phonenumbers", "tanzania_mno", "python-decouple"],
)
