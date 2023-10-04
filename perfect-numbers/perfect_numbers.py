def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = []
    perfect = 'perfect'
    abundant = 'abundant'
    deficient = 'deficient'
    for i in range(1,number):
        if number%i == 0:
            divisors.append(i)
    aliquot = sum(divisors)
    if aliquot == number:
        return perfect
    if aliquot > number:
        return abundant
    if aliquot < number:
        return deficient