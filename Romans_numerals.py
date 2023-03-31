def convert_to_roman_numeral(n):
    if not isinstance(n, int) or n < 1:
        return "XXX"
    
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                      50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    result = ''
    for value, numeral in roman_numerals.items():
        while n >= value:
            result += numeral
            n -= value
            
    return result
