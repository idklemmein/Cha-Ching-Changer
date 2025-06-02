def is_valid_number(user_input):
    input_clean = user_input.replace(".", "").replace("-", "")
    if len(input_clean) > 7:
        return False, "Amount must be 7 digits or fewer"
    try:
        amount = float(user_input)
        if amount <= 0:
            return False, "Amount must be greater than 0"
        return True, ""
    except ValueError:
        return False, "Please enter a valid number"

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number to validate (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting Input Validator.")
            break

        valid, message = is_valid_number(user_input)
        if valid:
            print("✓ Valid input.\n")
        else:
            print(f"✗ Invalid input: {message}\n")