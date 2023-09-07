#output \' \" Line A Line B

#\\\' ==> \'

#\\\" ==> \"

print("\\\' \\\" Line A Line B")

# Basics: \' --> '

# \" --> "

# \\ --> \

print("this is \\\\ double backslash")

print("this is \/\/\/\/\/\/\ this is mountain")

print("/\\/\\/\\/\\/")

print("She is \t awesome") #with escape sequence

#  output \" \n \t \'

print("\\\" \\n \\t \\\'")

print("\\")

#raw string to print
#short cut for the above

print(r"hello ///.""'\\\\\ ")
print(f"hello ///.'\\\\\ ")

#print emojies
# this is the unicode of smiley U+1F600	, in the place of + replace 3 000 and at start backslash
print("\U0001F600")
