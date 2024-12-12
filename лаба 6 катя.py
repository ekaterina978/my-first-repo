import unittest

class TestBankAccount(unittest.TestCase):
    def test_create_account_with_valid_balance(self):
        """Тест создания счёта с норм начальным балансом."""
        account = BankAccount("13131", 500.0)
        self.assertEqual(account.getBalance(), 500.0)

    def test_create_account_with_invalid_balance(self):
        """Тест создания счёта с некоректым начальным балансом."""
        with self.assertRaises(ValueError):
            BankAccount(13131"", -500.0)

    def test_deposit_valid_amount(self):
        """Тест успешного пополнения счёта."""
        account = BankAccount("13131", 400.0)
        account.deposit(50.0)
        self.assertEqual(account.getBalance(), 450.0)

    def test_deposit_invalid_amount(self):
        """Тест пополнения счёта с неправильной суммой."""
        account = BankAccount("13131", 100.0)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid_amount(self):
        """Тест успешного снятия средств."""
        account = BankAccount("13131", 300.0)
        account.withdraw(50.0)
        self.assertEqual(account.getBalance(), 250.0)

    def test_withdraw_insufficient_funds(self):
        """Тест снятия средств, превышающих баланс."""
        account = BankAccount("13131", 200.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(300.0)
        self.assertEqual(str(context.exception), "Нет денег")

    def test_withdraw_invalid_amount(self):
        """Тест снятия некорректной суммы."""
        account = BankAccount("13131", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)

    def test_balance_after_operations(self):
        """Тест проверки баланса после операций."""
        account = BankAccount("13131", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.getBalance(), 120.0)

    def test_create_account_with_default_balance(self):
        """Тест создания счёта с балансом по умолчанию."""
        account = BankAccount("13131")
        self.assertEqual(account.getBalance(), 0.0)

if name == "__main__":
    unittest.main()
