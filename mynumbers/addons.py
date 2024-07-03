def get_divisors(number, sqrt):
    first_divs = []
    last_divs = []

    for i in range(1, int(sqrt) + 1):
        if (number % i) == 0 and (number // i) == i:
            first_divs.append(i)
        elif (number % i) == 0:
            first_divs.append(i)
            last_divs.append(number // i)
    
    return first_divs + last_divs[::-1]


def generate_number_info(number):
    import json

    sqrt = number ** 0.5
    divisors = get_divisors(number, sqrt)
    is_even = number % 2 == 0
    return {'sqrt': sqrt, 'divisors': json.dumps(divisors), 'is_even': is_even}