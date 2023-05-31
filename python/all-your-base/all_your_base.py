def rebase(input_base, digits, output_base):
    #Create empty lists for result and converted digits
    result = []
    new_digits = []

    #Raise exceptions when input or output base are less than 2
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    #Convert number from decimal to non-decimal base
    if input_base == 10 and output_base != 10:
        number = create_number(digits)
        if number == 0:
            result.append(0)
        while number >= 1:
            result.append (number % output_base)
            number /= output_base
            number = int(number)
        result.reverse()
        return result

    #Convert number from non-decimal to decimal base
    if input_base != 10 and output_base == 10:
        if not digits:
            result.append(0)
            return result
        for index,i in enumerate(digits):
            if i < 0 or i >= input_base:
                raise ValueError("all digits must satisfy 0 <= d < input base")
            else:
                new_digits.append(i*input_base**(len(digits)-1-index))
                result = list(map(int, str(sum(new_digits))))
        return result

    #Convert number from one non-decimal base to another non-decimal base
    if input_base != 10 and output_base != 10:
        if not digits:
            result.append(0)
        for index,i in enumerate(digits):
            if i < 0 or i > input_base:
                raise ValueError("all digits must satisfy 0 <= d < input base")
            else:
                new_digits.append(i*input_base**(len(digits)-1-index))
        base_ten = sum(new_digits)
        if base_ten == 0:
            result.append(0)
        while base_ten >= 1:
            result.append (base_ten % output_base)
            base_ten /= output_base
            base_ten = int(base_ten)
        result.reverse()
        return result


def create_number(digits):
    num = ''
    for digit in digits:
        num += str(digit)
    number = int(num)
    return number