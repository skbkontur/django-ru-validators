# Django russian financial validators

l10n russian validators for INN, bank account number

[![Build Status](https://travis-ci.org/skbkontur/django-ru-validators.svg?branch=master)](https://travis-ci.org/skbkontur/django-ru-validators)

## Install

```bash
$ pip install django-ru-validators
```

## Usage

```python
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django_ru_validators import validate_inn, BankAccountNumberValidator


class PaymentOrder(models.Model):
    recipient_inn = models.CharField(validators=[validate_inn])
    recipient_account_number = models.CharField()
    recipient_bank = models.CharField()


class PaymentOrderForm(forms.ModelForm):
    class Meta:
        model = PaymentOrder
        fields = ("recipient_inn", "recipient_account_number", "recipient_bik")

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
