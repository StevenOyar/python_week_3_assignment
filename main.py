def calculate_discount(price, discount_percent):
    # Check if discount is equal to 20% or  greater
    if discount_percent >= 20:
        # Apply discount: reduce price by discount percentage
        return price * (1 - discount_percent / 100)
    else:
        # Return original price if discount is below 20%
        return price


# Get user input for original price and convert to float
price = float(input("Enter your original price: "))

# Get user input for discount percentage and convert to float
discount_percent = int(input("discount percentage: "))


# Calculate final price using the function
total_price = calculate_discount(price, discount_percent)

# Print formatted result with 2 decimal places
if discount_percent >= 20:
    print(
        f"Final total price after a discount of {discount_percent}% is  appliedd is Ksh.{total_price:.2f}"
    )
else:
    print(
        f"Final total price after {discount_percent}% discount was not applied is Ksh.{total_price:.2f}"
    )
