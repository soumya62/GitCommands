VOWELS=("a","e","i","o","u")
msg=input("Enter ur msg:")
new_msg=""
for letter in msg:
        if letter not in VOWELS:
                new_msg+=letter
print(new_msg)
