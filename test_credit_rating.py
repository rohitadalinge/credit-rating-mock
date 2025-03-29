import unittest
from credit_rating import calculate_credit_rating


class TestCreditRating(unittest.TestCase):

    def test_aaa_rating(self):
        mortgages = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 720,
                "loan_amount": 100000,
                "property_value": 200000,
                "annual_income": 80000,
                "debt_amount": 10000,
                "loan_type": "fixed",
                "property_type": "single_family"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")

    def test_bbb_rating(self):
        mortgages = [
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            },
            {
                "credit_score": 670,
                "loan_amount": 170000,  # Adjusted to reduce LTV
                "property_value": 200000,
                "annual_income": 50000,
                "debt_amount": 15000,
                "loan_type": "adjustable",
                "property_type": "single_family"  # Changed to reduce risk
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")

    def test_c_rating(self):
        mortgages = [
            {
                "credit_score": 600,
                "loan_amount": 300000,
                "property_value": 250000,
                "annual_income": 50000,
                "debt_amount": 30000,
                "loan_type": "adjustable",
                "property_type": "condo"
            },
            {
                "credit_score": 620,
                "loan_amount": 200000,
                "property_value": 180000,
                "annual_income": 40000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")

    def test_invalid_mortgage_missing_key(self):
        invalid_mortgage = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                # Missing 'loan_type'
                "property_type": "single_family"
            }
        ]
        with self.assertRaises(ValueError):
            calculate_credit_rating(invalid_mortgage)

    def test_empty_mortgages(self):
        with self.assertRaises(ValueError):
            calculate_credit_rating([])


if __name__ == '__main__':
    unittest.main()