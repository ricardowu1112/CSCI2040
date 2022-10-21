def roman_to_decimal(str1, str2):
    index = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    deximal_num1 = 0
    deximal_num2 = 0
    str1 = str1.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                  "CCCC").replace(
        "CM", "DCCCC")
    str2 = str2.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                  "CCCC").replace(
        "CM", "DCCCC")
    for char1 in str1:
        deximal_num1 += index[char1]
    for char2 in str2:
        deximal_num2 += index[char2]
    assert (deximal_num1 and deximal_num2 <= 9999), "Over the range"
    if deximal_num2 > deximal_num1:
        return deximal_num1
    else:
        return deximal_num2
        return deximal_num2