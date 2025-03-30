# Arithmetic Operators
num1 = 15  # Pehla number
num2 = 6  # Doosra number
print("Arithmetic Operators:")
print("Jod (Addition):", num1 + num2)
print("Ghatana (Subtraction):", num1 - num2)
print("Guna (Multiplication):", num1 * num2)
print("Bhaag (Division):", num1 / num2)
print("Shesh (Modulus):", num1 % num2)
print("Power lagana (Exponentiation):", num1 ** num2)
print("Poora Bhaag (Floor Division):", num1 // num2)

# Assignment Operators
value = 10  # Ek value
print("\nAssignment Operators:")
print("Shuruaati value (Initial value):", value)
value += 5
print("5 jod kar (Add and assign):", value)
value -= 3
print("3 ghata kar (Subtract and assign):", value)
value *= 2
print("2 guna kar ke (Multiply and assign):", value)
value /= 4
print("4 se divide kar ke (Divide and assign):", value)
value %= 5
print("Shesh assign karo (Modulus and assign):", value)

# Comparison Operators
umar1 = 18  # Pehli umar
umar2 = 25  # Doosri umar
print("\nComparison Operators:")
print("Kya umar1 aur umar2 same hain? (==):", umar1 == umar2)
print("Kya umar1 aur umar2 alag hain? (!=):", umar1 != umar2)
print("Kya umar1 zyada hai umar2 se? (>):", umar1 > umar2)
print("Kya umar1 kam hai umar2 se? (<):", umar1 < umar2)
print("Kya umar1 zyada ya barabar hai? (>=):", umar1 >= umar2)
print("Kya umar1 kam ya barabar hai? (<=):", umar1 <= umar2)

# Logical Operators
true_value = True  # Sahi value
false_value = False  # Galat value
print("\nLogical Operators:")
print("Sahi aur galat dono (AND):", true_value and false_value)
print("Koi ek sahi ho (OR):", true_value or false_value)
print("Ulta kar do (NOT):", not true_value)

# Identity Operators
list1 = [1, 2, 3]  # Ek list
list2 = [1, 2, 3]  # Dusri list
list3 = list1  # Wahi list
print("\nIdentity Operators:")
print("Kya list1 aur list2 ek jaise hain? (is):", list1 is list2)
print("Kya list1 aur list3 ek hi hain? (is):", list1 is list3)
print("Kya list1 aur list2 alag hain? (is not):", list1 is not list2)

# Membership Operators
numbers = [10, 20, 30, 40]
print("\nMembership Operators:")
print("Kya 20 list mein hai? (in):", 20 in numbers)
print("Kya 50 list mein nahi hai? (not in):", 50 not in numbers)

# Bitwise Operators
bit_num1 = 5  # Pehla binary number (0101)
bit_num2 = 3  # Dusra binary number (0011)
print("\nBitwise Operators:")
print("Bitwise AND (Aur):", bit_num1 & bit_num2)
print("Bitwise OR (Ya):", bit_num1 | bit_num2)
print("Bitwise XOR (XOR):", bit_num1 ^ bit_num2)
print("Bitwise NOT (Ulta):", ~bit_num1)
print("Left Shift (Bayein khisako):", bit_num1 << 1)
print("Right Shift (Dayein khisako):", bit_num1 >> 1)

# Ternary Operator
umar1 = 18
umar2 = 25
badi_umar = umar1 if umar1 > umar2 else umar2
print("\nTernary Operator:")
print("Sabse badi umar hai (Ternary):", badi_umar)