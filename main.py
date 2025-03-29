import json
from credit_rating import calculate_credit_rating

def main():
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)
        rating = calculate_credit_rating(data['mortgages'])
        print(f"Credit Rating: {rating}")
    except ValueError as err:
        print(f"Error processing input data: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()