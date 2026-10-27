# # Bank Transaction Processor

# Create functions to:
# Deposit money.
# Withdraw money.
# Check the current balance.
# Record a transaction.
# Generate a transaction summary.



# --- Account State ---
def create_account(opening_balance=0.0, daily_withdrawal_limit=1000.0):

    """Initializes and returns an account dictionary."""
    if opening_balance < 0:
        raise ValueError("Opening balance cannot be negative.")
    return {
        "balance": float(opening_balance),
        "history": [],
        "daily_limit": float(daily_withdrawal_limit),
        "withdrawn_today": 0.0,
    }
my_account = create_account(opening_balance=3200.0, daily_withdrawal_limit=1000.0)
print("Account created:", my_account)

print( create_account(opening_balance=3200.0, daily_withdrawal_limit=1000.0))


def withdraw_money(account, amount):
    """Processes a withdrawal and updates the account state."""
    if amount <= 0:
        return "Withdrawal amount must be greater than zero."

    remaining_limit = account["daily_limit"] - account["withdrawn_today"]
    if amount > remaining_limit:
        return f"Declined: Exceeds daily limit. Remaining limit today: ${remaining_limit:.2f}"

    if amount > account["balance"]:
        return f"Declined: Insufficient balance. Available: ${account['balance']:.2f}"

    account["balance"] -= amount
    account["withdrawn_today"] += amount

    return f"Success: Withdrew ${amount:.2f}. New balance: ${account['balance']:.2f}"

result2 = withdraw_money(my_account, 700.0)
print(result2)



