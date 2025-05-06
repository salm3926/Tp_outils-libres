def sum_positive(numbers):
    if any(n < 0 for n in numbers):
        raise ValueError("Negative numbers not allowed")
    return sum(numbers)
