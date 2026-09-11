inventory=0
while True:
    #inputing quantity
    quantity=input("Enter a stock quantity or type (quit) to leave: ")
    #check if integer or not
    if not quantity.isdigit() and not quantity.lower()=="quit":
        print("ERROR! Please key in an integer")
        continue
    #quit statement
    if quantity.lower()=="quit":
        break
     #converts quantity to integer
    quantity=int(quantity)
    inventory+=quantity
print(inventory)