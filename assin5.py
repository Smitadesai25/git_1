#WAP to input bank account number , acount holder name , gender , birth date , city and opening balance. 
#Add 3% of available balance as interest amount for the
#  current year and show total available balance.

bank_acount_number = int (input("enter bank account number :"))
account_holder_name = input("enter account holder name : ")
gender = input("Enter the gender :")
birht_date = input("enter your birht date:")
city = input("Enter the city name: ")
opening_balance = int(input("Enter the opening balance :"))

intrest_amount = (opening_balance * (3/100))
print("Interest amount:" , intrest_amount)
total_available_blance = (intrest_amount + opening_balance)
print("Total available balance is :", total_available_blance)

