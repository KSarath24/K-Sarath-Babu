s= input("Enter any character: ");
if s == '0':
    exit();
else:
    if((s>='a' and s<='z') or (s>='A' and s<='Z')):
    	print("Alphabet");
    else:
    	print("Not alphabet");
