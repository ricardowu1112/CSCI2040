import math


def check_invalid(n):
    triangle = [a for a in n if a < max(n)]
    for char in n:
        if (isinstance(char, int) or isinstance(char, float)) != True:
            return True
        if char <= 0:
            return True
    if len(n) != 3:
        return True
    if triangle[0] + triangle[1] <= max(n):
        return True
    return False


def is_obtuse_triangle(n):
    triangle = [a for a in n if a < max(n)]
    if (triangle[0] ** 2 + triangle[1] ** 2 < (max(n)) ** 2) and (check_invalid(n) != True):
        return True
    else:
        return False


def area(n):
    if check_invalid(n) == True:
        print("This is not a valid Triangle")
    else:
        s = perimeter(n) / 2
        area = math.sqrt(s * (s - n[0]) * (s - n[1]) * (s - n[2]))
        return area


def perimeter(n):
    if check_invalid(n) == True:
        print("This is not a valid Triangle")
    else:
        s = (n[0] + n[1] + n[2])
        return s