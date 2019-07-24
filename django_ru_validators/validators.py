from django.core.exceptions import ValidationError


def validate_inn(value):
    _INN_TEST_WEIGHTS_10 = (2, 4, 10, 3, 5, 9, 4, 6, 8, 0)
    _INN_TEST_WEIGHTS_12_0 = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0, 0)
    _INN_TEST_WEIGHTS_12_1 = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0)

    def _check_inn_organization(inn):
        if len(inn) != 10:
            return False

        res = 0
        for i, char in enumerate(inn):
            res += int(char) * _INN_TEST_WEIGHTS_10[i]
        res = res % 11 % 10

        return res == int(inn[-1])

    def _check_inn_person(inn):
        if len(inn) != 12:
            return False

        res1 = 0
        for i, char in enumerate(inn):
            res1 += int(char) * _INN_TEST_WEIGHTS_12_0[i]
        res1 = res1 % 11 % 10

        res2 = 0
        for i, char in enumerate(inn):
            res2 += int(char) * _INN_TEST_WEIGHTS_12_1[i]
        res2 = res2 % 11 % 10

        return (res1 == int(inn[-2])) and (res2 == int(inn[-1]))

    def _check_inn(inn):
        if len(inn) == 10:
            return _check_inn_organization(inn)
        elif len(inn) == 12:
            return _check_inn_person(inn)

        return False

    if not _check_inn(value):
        raise ValidationError(
            "%(value)s является неверным ИНН", params={"value": value}
        )


class BankAccountNumberValidator:
    _BANK_ACC_TEST_WEIGHTS = ((7, 1, 3) * 8)[:-1]

    bik = None

    def __init__(self, bik=None):
        if bik is not None:
            self.bik = bik

    def _check_bank_number(self, anumber):
        if not isinstance(anumber, str) and not anumber.isdigit():
            return False

        if len(anumber) != 23:
            return False

        res = 0
        for i, char in enumerate(anumber):
            res += int(char) * self._BANK_ACC_TEST_WEIGHTS[i]
        return (res % 10) == 0

    def _check_bank_account_number(self, account, bik):
        return (
            account
            and bik
            and len(account) == 20
            and len(bik) == 9
            and self._check_bank_number(bik[-3:] + account)
        )

    def __call__(self, value):
        if not self._check_bank_account_number(value, self.bik):
            raise ValidationError(
                "%(value)s является неверным номером счёта", params={"value": value}
            )

    def __eq__(self, other):
        return isinstance(other, BankAccountNumberValidator) and self.bik == other.bik
