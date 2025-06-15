def is_float(value):
    if value.count('.') > 1:
        return False
    if value.replace('.', '', 1).replace('-', '', 1).isdigit():
        return True
    return False


def safe_divide(numerator, denominator):
    if not is_float(numerator) or not is_float(denominator):
        return "Error: Please enter numeric values only."

    num = float(numerator)
    denom = float(denominator)

    if denom == 0:
        return None

    result = num / denom
    return f"The result of the division is {result}"
