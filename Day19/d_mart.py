# Dmart Billing System
dmart_db = {1: 'Rice', 2: 'Sugar', 3: 'Oil', 4: 'Soap', 5: 'Shampoo', 6: 'Biscuits', 7: 'Milk'}
dmart_price = {1: 50, 2: 40, 3: 120, 4: 30, 5: 90, 6: 25, 7: 60}

items = []
qty = []

while True:
    print(""" 
        Dmart Menu
          1. Rice       -50
          2. Sugar      -40
          3. Oil        -120
          4. Soap       -30
          5. Shampoo    -90
          6. Biscuits   -25
          7. Milk       -60 """)
    
    i = int(input("Enter Item Number: "))
    q = int(input("Enter quantity: "))

    items.append(i)
    qty.append(q)

    c = input("Do you want to order more? (y/n): ")
    if c == 'n':
        print("Bill.......")
        print("*"*100)
        print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format("Item Code", "Item Name", "Quantity", "Price", "Total"))
        print("*"*100)

        sum = 0
        for i in range(len(items)):
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(i+1, dmart_db[items[i]], qty[i], dmart_price[items[i]], qty[i]*dmart_price[items[i]]))

            sum += qty[i]*dmart_price[items[i]]
        print("*"*100)
        print(f'Total Amount: {sum}')    
        cgst = sum * (9/100)
        print(f'CGST: ', cgst)
        sgst = sum * (9/100)
        print(f'SGST: ', sgst)
        g_total = sum + cgst + sgst
        print(f'Grand Total: {g_total}')    
