def admin():
    print("""
                👍You can change or add items and price of your items.👍
    """)
    print("       \n    Enter Order for order. \n  ")

    while True:
        item_admin = input("Enter your item : ")
        item_admin = item_admin[0].upper() + item_admin[1:].lower()
        if item_admin == "Order":
            customer()
        elif item_admin == "E":
            quit()
        else:
            new_price = int(input("Price : "))
            item_list.append(item_admin)
            price_list.append(new_price)


admin_custome = input("""You are admin or customer : 

                1.admin
                2.customer    

        Enter here : """)

admin_custome_modified = admin_custome[0].upper() + admin_custome[1:].lower()
if admin_custome_modified == "Customer" or admin_custome_modified == "2":
    customer()
elif admin_custome_modified == "Admin" or admin_custome_modified == "1":

    for i in range(3):
        paasWord = input("Enter your Paasword : ")
        if paasWord == "chitkara@22":
            menuAsDict()
        else:
            print("\n                          ❌❌ Sorry ! Invalid paasword ❌❌\n ")
else:
    print("\n                                    ❌❌ Invalid input ❌❌\n ")
