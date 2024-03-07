text1='there'
print(f'Hi, {text1}')
print(text1[-4:-1])

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  

# len e.g. len(text1), replace, text1.count("e"), strip lstrip, rstrip(i.e trim)
# isalnum(), isalpha, isdigit, isupper, islower, stringwithspace is not alpha numeric 


#str,int, float
number=2.33
int_number=int(number)

#list: append, insert(index,value), del, split method to convert a string into list, "hi how".join(list )

# in, not in , type(2) is int, type(2) is not int
# tuple, dict, array, 

# if : elif: else:

# input("Input e if you want to exit")

# while count >0 :
# for count in range(10):
# for count in range(2,15): 15 exclusive
# for count in range(2,42,2): here 2 is increment value

#__init__.py package

"""
try:
    a=int(input("Enter your age"))
except Exception as e:  
    print("Exception occured",e)
else:
    print("no error in code")
finally:
    print("this is finally")
""" 

# python3 -m venv my_Python_venvs/my_Python_env1
#(mysqldemoenv) abhijitkurane@SEZ-MACB-34 mysqldemo % source mysqldemoenv/bin/activate        
# activating : source my_Python_venvs/my_Python_env1/bin/activate
# deactivate


#import pandas as pd
# df=pd.open_csv("txtfile")
# df.head(4), df.info(), df.describe()
# df['Total']=df['Order_Quantity'] * df['Order_Price']
# df.to_csv("update_csv.csv", index=False)