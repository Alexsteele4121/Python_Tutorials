my_lucky_number = 4


def get_evens(numbers):
    results = []
    for number in numbers:
        if number % 2 == 0:
            results.append(number)
    return results


def get_odds(numbers):
    results = []
    for number in numbers:
        if number % 2:
            results.append(number)
    return results
