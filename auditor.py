inventory=0
failed_entry=0
while True:
    #inputing quantity
    quantity=input("Enter a stock quantity or type (quit) to leave: ")
    #check if integer or not
    if not quantity.isdigit() and not quantity.lower()=="quit":
        print("ERROR! Please key in an integer")
        failed_entry+=1
        continue
    #quit statement
    elif quantity.lower()=="quit":
        break
     #converts quantity to integer
    quantity=int(quantity)
    inventory+=quantity
    #check if inventory exceeds 500
    if inventory>500:
        print("ALERT! U have exceeded 500 units. OVERSTOCK!")
        break
#print total units and failed entries
print("Total units processed: "+str(inventory))
print("Number of failed/rejected entries: "+str(failed_entry))