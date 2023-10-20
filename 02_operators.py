# Python divides the operators in the following groups:
# (1) Arithmetic operators (2) Assignment operators (3) Comparison operators (4) Logical operators (5) Identity operators (6) Membership operators (7) Bitwise operators

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# "+" is used for Addition. For example,	x + y	
# "-" is used for Subtraction. For example,	x - y		
# "*" is used for Multiplication. For example,	x * y		
# "/" is used for Division. For example,	x / y	
# "%" is used for Modulus. For example,	x % y		
# "**" is used for Exponentiation. For example,	x ** y	
# "//" is used for Floor Division. For example,	x // y		

# Python Assignment Operators
# Assignment operators are used to assign values to variables:
# "=" is used for assigning value to a variable. For example, x = 5.	
# "+="      means    x += 3     or      x = x + 3.	
# "-="      means 	 x -= 3	    or      x = x - 3.	
# "*="      means    x *= 3     or      x = x * 3.
# "/="      means    x /= 3	    or      x = x / 3.
# "%="      means    x %= 3	    or      x = x % 3.
# "//="	    means    x //= 3	or      x = x // 3.
# "**="	    means    x **= 3	or      x = x ** 3.	
# "&="      means	 x &= 3	    or      x = x & 3.
# "|="      means    x |= 3	    or      x = x | 3.	
# "^="      means	 x ^= 3     or     	x = x ^ 3.	
# ">>="     means	 x >>= 3	or      x = x >> 3.	
# "<<="	    means    x <<= 3	or      x = x << 3.	


# Python Comparison Operators
# Comparison operators are used to compare two values.
# "=="	means   Equal	                    i.e,    x == y	
# "!="	means   Not equal	                i.e.    x != y	
# ">""	means   Greater than	            i.e.    x > y	
# "<"	means   Less than	                i.e.    x < y	
# ">="	means   Greater than or equal to	i.e.    x >= y	
# "<="  means 	Less than or equal to       	i.e.    x <= y

# Python Logical Operators
# Logical operators are used to combine conditional statements:
# and 	Returns True if both statements are true	
# or	Returns True if one of the statements is true
# not	Reverse the result, returns False if the result is true	 
	
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is 	    Returns True if both variables are the same object		
# is not	Returns True if both variables are not the same object		

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object.
# in 	    Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y	

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers.
# # & 	AND	Sets each bit to 1 if both bits are 1		
# |	OR	Sets each bit to 1 if one of two bits is 1		
# ^	XOR	Sets each bit to 1 if only one of two bits is 1		
# ~	NOT	Inverts all the bits		
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off		
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	

# Operator Precedence
# Operator precedence describes the order in which operations are performed.
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR	
# If two operators have the same precedence, the expression is evaluated from left to right.
