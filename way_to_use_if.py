from abc import ABC, abstractmethod

# 1. Unnecessary else

def number_classification(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "zero"
    
def number_classification(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "zero"

print(number_classification(-1))

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_even(number):
    return number % 2 == 0

print(is_even(2))


# No, we can do better than this
condition = 1

if condition:
    number = 1
else:
    number = 2


# Just use a default vlue
condition = 1

number = 2
if condition:
    number = 1

print(number)

# 2. Value Assignments
def classify_temperature(temperature):
    message = ''
    if temperature >= 26:
        message = "Hot"
    elif temperature >= 15:
        message = "Warm"
    else:
        message = "Cold"
    return message

def classify_temperature(temperature):
    if temperature >= 26:
        return "Hot"
    if temperature >= 15:
        return "Warm"
    return "Cold"


print(classify_temperature(0))

# 3. Guard Clauses

# Using guard clauses

def my_function():
    if not condition:
        return  # or raise an Exception
    # Do something

def my_function_reverse_condition():
    if condition:
        # Do something
        return # or raise an Exception

def validate_input(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")
    if not input_list:
        raise ValueError("Input cannot be an empty list.")
    if not all(isinstance(item, float) for item in input_list):
        raise ValueError("All items in the list must be floats.")
    return True


# Using if-else statements
def validate_input(input_list):
    if isinstance(input_list, list):
        if input_list:
            if all(isinstance(item, float) for item in input_list):
                return True
            else:
                raise ValueError("All items in the list must be floats.")
        else:
            raise ValueError("Input cannot be an empty list.")
    else:
        raise TypeError("Input must be a list.")


# lots of if-elif
def determine_favorite_fruit(color):
    if color == "red":
        return "Strawberry"
    elif color == "yellow":
        return "Banana"
    elif color == "green":
        return "Honeydew"
    return "unknown"


# Dictionary is used
def determine_favorite_fruit_with_dict(color):
    color_to_fruit = {
        "red": "Strawberry",
        "yellow": "Banana",
        "green": "Honeydew",
    }
    return color_to_fruit.get(color, "unknown")


print(determine_favorite_fruit_with_dict("greenn"))

# 6. Strategy Pattern


def pay_with_credit_card(amount):
    print(f"Paying {amount} using credit card.")

def pay_with_paypal(amount):
    print(f"Paying {amount} using PayPal.")
    
def pay_with_stripe(amount):
    print(f"Paying {amount} using Stripe.")

def pay(amount, method):
    if method == "credit_card":
        pay_with_credit_card(amount)
    elif method == "paypal":
        pay_with_paypal(amount)
    elif method == "stripe":
        pay_with_stripe(amount)
    else:
        raise ValueError("Unsupported payment method")
    
pay(10, "credit_card")


# Define the abstract Strategy class
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    
# Define the concrete Strategy classes
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using credit card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

        
class StripePayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Stripe.")
        
        
# Define the Context class that will use the Strategy pattern
class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)


# Example usage
payment_context = PaymentContext(CreditCardPayment())
payment_context.pay(100)  # Output: Paying 100 using credit card.

payment_context.set_payment_strategy(PayPalPayment())
payment_context.pay(50)  # Output: Paying 50 using PayPal.

payment_context.set_payment_strategy(StripePayment())
payment_context.pay(150)  # Output: Paying 150 using Stripe.
