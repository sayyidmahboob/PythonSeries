# Strings are immutable
string = "Ye ek string hai."
print(string)  # Output: Ye ek string hai.
print(type(string))  # Output: <class 'str'>

# STRING METHODS

# Upper case
string = "ye ek string hai."
stringUpperCase = string.upper()
print("\nUpper case:", stringUpperCase)

# Lower case
string = "YE EK DUSRI STRING HAI"
stringLowerCase = string.lower()
print("Lower case:", stringLowerCase)

# Title case
string = "ye ek string hai."
stringTitleCase = string.title()
print("Title case:", stringTitleCase)

# Capitalize
string = "ye ek string hai."
stringCapitalize = string.capitalize()
print("Capitalize:", stringCapitalize)

# Strip (Remove spaces from both ends)
string = "    ye ek string hai jisme spaces hain.    "
stringStrip = string.strip()
print("\nStrip (remove spaces):", stringStrip)

# Lstrip (Remove spaces from the left)
string = "        ye ek string hai."
stringLstrip = string.lstrip()
print("Lstrip (remove left spaces):", stringLstrip)

# Rstrip (Remove spaces from the right)
string = "ye ek string hai.          "
stringRstrip = string.rstrip()
print("Rstrip (remove right spaces):", stringRstrip)

# Split (Convert string to a list of words)
string = "ye ek string hai."
stringSplit = string.split()
print("\nSplit into list:", stringSplit)

# Join (Convert list back to string)
words = ["ye", "ek", "string", "hai."]
stringJoin = " ".join(words)
print("Join list into string:", stringJoin)

# Find (Find substring in a string)
string = "ye ek string hai."
stringFind = string.find("dhundho")  # Substring not found
stringFind2 = string.find("ye")  # Substring found
print("\nFind 'dhundho':", stringFind)  # Output: -1
print("Find 'ye':", stringFind2)  # Output: 0

# Replace (Replace substring in a string)
string = "ye ek string hai."
stringReplace = string.replace("ye", "ye nahi")
print("\nReplace 'ye' with 'ye nahi':", stringReplace)

# Count (Count occurrences of a substring)
string = "ye ek string hai hai hai."
stringCount = string.count("hai")
print("\nCount 'hai':", stringCount)  # Output: 3

# Isdigit (Check if string contains only digits)
string = "12345"
string2 = "ye ek string hai."
stringIsDigit = string.isdigit()
stringIsNotDigit = string2.isdigit()
print("\nIsdigit check (string 1):", stringIsDigit)  # Output: True
print("Isdigit check (string 2):", stringIsNotDigit)  # Output: False

# Isalpha (Check if string contains only alphabets)
string = "yeekstringhai"
string2 = "yeekstringhai123"
stringIsAlpha = string.isalpha()
stringIsNotAlpha = string2.isalpha()
print("\nIsalpha check (string 1):", stringIsAlpha)  # Output: True
print("Isalpha check (string 2):", stringIsNotAlpha)  # Output: False

# Startswith (Check if string starts with a specific substring)
string = "ye ek string hai."
print("\nStartswith 'ye':", string.startswith("ye"))  # Output: True
print("Startswith 'ek':", string.startswith("ek"))  # Output: False

# Endswith (Check if string ends with a specific substring)
string = "ye ek string hai."
print("\nEndswith 'hai.':", string.endswith("hai."))  # Output: True
print("Endswith 'string':", string.endswith("string"))  # Output: False

# Center (Center align the string and pad with spaces)
string = "hello"
print("\nCenter aligned (width 20):", string.center(20))
print("Center aligned with '-':", string.center(20, '-'))

# Zfill (Pad the string with zeroes)
number = "123"
print("\nZfill (width 5):", number.zfill(5))  # Output: "00123"

# Isalnum (Check if string contains only alphabets and digits)
string = "Python123"
string2 = "Python 123"
print("\nIsalnum check (string 1):", string.isalnum())  # Output: True
print("Isalnum check (string 2):", string2.isalnum())  # Output: False

# Isspace (Check if string contains only spaces)
string = "   "
string2 = "Hello World"
print("\nIsspace check (string 1):", string.isspace())  # Output: True
print("Isspace check (string 2):", string2.isspace())  # Output: False

# Swapcase (Swap uppercase to lowercase and vice versa)
string = "Ye Ek String Hai."
print("\nSwapcase:", string.swapcase())  # Output: "yE eK sTRING hAI."

# Partition (Split the string into three parts: before, match, after)
string = "Python is awesome"
print("\nPartition by 'is':", string.partition("is"))  
# Output: ('Python ', 'is', ' awesome')

# Rfind (Find the last occurrence of a substring)
string = "ye ek string hai, aur ye ek example hai."
print("\nRfind 'ye':", string.rfind("ye"))  # Output: Last 'ye' index

# Format (Insert values dynamically into a string)
name = "Syed"
age = 27
print("\nFormat example:", "Mera naam {} hai aur meri umar {} saal hai.".format(name, age))
# Output: Mera naam Syed hai aur meri umar 25 saal hai.