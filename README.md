# Django russian financial validators

l10n russian validators for INN, bank account number

[![Build Status](https://travis-ci.org/zhelyabuzhsky/django-ru-validators.svg?branch=master)](https://travis-ci.org/zhelyabuzhsky/django-ru-validators)

## Install

```bash
$ pip install django-ru-validators
```

## Usage

```python
from django import forms
from django.core.exceptions import ValidationError
from django_ru_validators import validate_inn, BankAccountNumberValidator

from bank.payment_orders.models import PaymentOrder


class PaymentOrderForm(forms.ModelForm):
    class Meta:
        model = PaymentOrder
        fields = ("recipient_inn", "recipient_account_number", "recipient_bik")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["recipient_inn"].validators.append(validate_inn)

    def clean(self):
        cleaned_data = super().clean()
        recipient_account_number = cleaned_data.get("recipient_account_number")
        recipient_bik = cleaned_data.get("recipient_bik")
        try:
            BankAccountNumberValidator(recipient_bik)(recipient_account_number)
        except ValidationError:
            msg = "Wrong combination of account number and bik of bank"
            self.add_error("recipient_account_number", msg)
            self.add_error("recipient_bik", msg)

        return cleaned_data
``` 

## Development

Install dependencies with

```bash
$ pip install --requirement requirements.txt
```

Run tests with

```bash
$ python setup.py test
```
