#Agenda 
# Project - Hotel Billing system

db = {1:'Poha', 2:"Idli", 3:"Dosa", 4:"Vada Pav", 5:"Tea", 6:"Coffee", 7:"Upma"}
price = {1:25, 2:20, 3:40, 4:15, 5:10, 6:15, 7:30}

items = []
qty = []

while True:
    print("""Hotel Menu
        1. Poha         - 25
        2. Idli         - 20
        3. Dosa         - 40 
        4. Vada Pav     - 15
        5. Tea          - 10
        6. Coffee       - 15
        7. Upma         - 30""")

    i = int(input("Enter item number: "))
    q = int(input("Enter quantity: "))
    items.append(i)
    qty.append(q)
    print(items)
    print(qty)

    c = input("Do you want to order more? (y/n): ")
    if c == 'n':
        print("Your order is being processed...")
        print("bill...")
        print('*'*100)
        print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format("Item No", "Item Name", "Quantity", "Price", "Total"))
        print('*'*100)

        sum = 0
        for i in range(len(items)):
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(i+1, db[items[i]], qty[i], price[items[i]], qty[i]*price[items[i]]))
            sum = sum + qty[i]*price[items[i]]
        print('*'*100)
    print(f'Total Amount: {sum}')    
    cgst = sum * (9/100)
    print(f'CGST: ', cgst)
    sgst = sum * (9/100)
    print(f'SGST: ', sgst)
    g_total = sum + cgst + sgst
    print(f'Grand Total: {g_total}')




    