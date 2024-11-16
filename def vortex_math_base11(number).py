def vortex_math_base11(number):
    sum_digits = sum(int(digit) for digit in str(number))
    return sum_digits % 11 or 11

number = 123456
vortex_result = vortex_math_base11(number)
print(f"Vortex Math Base 11 result for {number}: {vortex_result}")