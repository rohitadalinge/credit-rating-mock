def calculate_credit_rating(mortgages):
    """
    Calculates the credit rating for a collection of mortgages in an RMBS.

    Args:
        mortgages: A list of dictionaries, each representing a mortgage.

    Returns:
        str: The credit rating ("AAA", "BBB", or "C").

    Raises:
        ValueError: If any mortgage is invalid or input is empty.
    """


    if not mortgages:
        raise ValueError("No mortgages provided")

    total_risk = 0
    sum_credit_scores = 0

    for mortgage in mortgages:
        validate_mortgage(mortgage)

        # Calculate LTV risk
        loan_amount = mortgage['loan_amount']
        property_value = mortgage['property_value']
        ltv = (loan_amount / property_value) * 100
        if ltv > 90:
            total_risk += 2
        elif ltv > 80:
            total_risk += 1

        # Calculate DTI risk
        debt_amount = mortgage['debt_amount']
        annual_income = mortgage['annual_income']
        dti = (debt_amount / annual_income) * 100
        if dti > 50:
            total_risk += 2
        elif dti > 40:
            total_risk += 1

        # Credit score adjustment
        credit_score = mortgage['credit_score']
        sum_credit_scores += credit_score
        if credit_score >= 700:
            total_risk -= 1
        elif credit_score < 650:
            total_risk += 1

        # Loan type adjustment
        if mortgage['loan_type'] == 'fixed':
            total_risk -= 1
        else:
            total_risk += 1

        # Property type adjustment
        if mortgage['property_type'] == 'condo':
            total_risk += 1

    average_credit = sum_credit_scores / len(mortgages)

    # Average credit adjustment
    if average_credit >= 700:
        total_risk -= 1
    elif average_credit < 650:
        total_risk += 1

    # Determine final rating
    if total_risk <= 2:
        return "AAA"
    elif 3 <= total_risk <= 5:
        return "BBB"
    else:
        return "C"


def validate_mortgage(mortgage):
    
    """Validates mortgage dictionary for required keys and valid values."""
    required_keys = [
        'credit_score', 'loan_amount', 'property_value', 'annual_income',
        'debt_amount', 'loan_type', 'property_type'
    ]
    for key in required_keys:
        if key not in mortgage:
            raise ValueError(f"Missing required key: {key}")


    credit_score = mortgage['credit_score']
    if not isinstance(credit_score, int) or not (300 <= credit_score <= 850):
        raise ValueError(f"Invalid credit_score: {credit_score}")

    loan_amount = mortgage['loan_amount']
    if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
        raise ValueError(f"Invalid loan_amount: {loan_amount}")

    property_value = mortgage['property_value']
    if not isinstance(property_value, (int, float)) or property_value <= 0:
        raise ValueError(f"Invalid property_value: {property_value}")

    annual_income = mortgage['annual_income']
    if not isinstance(annual_income, (int, float)) or annual_income <= 0:
        raise ValueError(f"Invalid annual_income: {annual_income}")

    debt_amount = mortgage['debt_amount']
    if not isinstance(debt_amount, (int, float)) or debt_amount < 0:
        raise ValueError(f"Invalid debt_amount: {debt_amount}")

    loan_type = mortgage['loan_type']
    if loan_type not in ['fixed', 'adjustable']:
        raise ValueError(f"Invalid loan_type: {loan_type}")

    property_type = mortgage['property_type']
    if property_type not in ['single_family', 'condo']:
        raise ValueError(f"Invalid property_type: {property_type}")