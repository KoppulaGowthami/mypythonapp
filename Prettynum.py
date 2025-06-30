# Find the given number(0-99) is pretty number or not.
# the number should be in either prefix or suffix
# pretty number:-7
# i/p:72    27
# o/p:YES   YES
# i/p:43
# o/p:NO
num=int(input("Enter number to check"))
if num%10==7 or num/10==7:
    print("lucky num")
else:
    print("Not a lucky num")
