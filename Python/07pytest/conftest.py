import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp():
    return smtplib.SMTP("smtp.163.com")
