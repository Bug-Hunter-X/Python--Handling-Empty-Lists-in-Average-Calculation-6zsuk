def calculate_average(numbers):
    if not numbers:
        return float('nan')  # Return NaN for empty list
    return sum(numbers) / len(numbers)

# Example usage with empty list
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # Output: nan

# Example usage with numbers
my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}") # Output: 30.0