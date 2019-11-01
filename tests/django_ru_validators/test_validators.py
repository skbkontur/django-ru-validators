import pytest
from django.core.exceptions import ValidationError

from django_ru_validators import BankAccountNumberValidator, validate_inn


@pytest.mark.parametrize(
    "inn",
    [
        "9109000140",
        "9204563745",
        "2502039781",
        "2004000870",
        "0103006692",
        "9721072801",
        "773711807351",
        "010403374502",
    ],
)
def test_validate_inn_correct(inn):
    validate_inn(inn)


@pytest.mark.parametrize("inn", ["2109000140", "710403374602"])
def test_validate_inn_wrong(inn):
    with pytest.raises(ValidationError) as error_context:
        validate_inn(inn)
    assert f"{inn} является неверным ИНН" in error_context.value


@pytest.mark.parametrize(
    "bik,account_number",
    [
        ("044525593", "40817810108670017419"),
        ("046577964", "40702810138030000017"),
        ("046577674", "40702810116480034147"),
        ("044525225", "40702810638050013199"),
        ("046577795", "47426810863032003088"),
        ("046577795", "40802810363030003088"),
        ("046577674", "40502810216020102982"),
    ],
)
def test_validate_bank_account_number_correct(bik, account_number):
    validator = BankAccountNumberValidator(bik)
    validator(account_number)


@pytest.mark.parametrize(
    "bik,account_number",
    [
        ("0445255931", "40817810108670017419"),
        ("044525593", "408178101086700174191"),
        ("04452559", "40817810108670017419"),
        ("044525593", "4081781010867001741"),
        ("0445255931", "408178101086700174191"),
        ("044525593", "40817810108170017419"),
        ("046577795", "40502810216020102982"),
    ],
)
def test_validate_bank_account_number_wrong(bik, account_number):
    with pytest.raises(ValidationError) as error_context:
        validator = BankAccountNumberValidator(bik)
        validator(account_number)
    assert f"{account_number} является неверным номером счёта" in error_context.value


@pytest.mark.parametrize(
    "bik,account_number",
    [
        ("044525000", "40101810045250010041"),
        ("045004001", "40101810900000010001"),
        ("044030001", "40101810200000010001"),
        ("043510001", "40101810335100010001"),
    ],
)
def test_validate_bank_corr_account_number_correct(bik, account_number):
    validator = BankAccountNumberValidator(bik)
    validator(account_number)


@pytest.mark.parametrize(
    "bik,account_number",
    [("044525000", "40101810045250011041"), ("044030001", "40702810400000105745"),],
)
def test_validate_bank_corr_account_number_wrong(bik, account_number):
    with pytest.raises(ValidationError) as error_context:
        validator = BankAccountNumberValidator(bik)
        validator(account_number)
    assert f"{account_number} является неверным номером счёта" in error_context.value
