import random
customers = [{"id":"077","name":"Roma","age":23,"product":[]}]
id = random.expovariate(32)
check = input("Do you want buy something? ")
while check == "Yes" or check == "yes":
    account = input("Do you have account? ")
    if account == "Yes" or account == "yes":
        check_id = input("Enter id ")
        for a in customers:
            if check_id == a["id"]:
                new_products = input("Choice products ")
                a["product"].append(new_products)
                print(customers)
            elif check_id != a["id"]:
                print("error!! Please enter correct id or create new account")


    elif account == "No" or account == "no":
        new_cust = {}
        new_cust["id"] = id
        new_cust["name"] = input("Enter your name ")
        new_cust["age"] = int(input("Enter age "))
        new_cust["product"] = input("Choice product ").split(", ")
        customers.append(new_cust)
        print(customers)
    elif account == "exit":
        break





