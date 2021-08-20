print("DOMESTIC CHARGES")
Present_units=float(input("Enter Present_units="))
Previous_units=float(input("Enter Previous_units="))
units=Present_units-Previous_units
print(units)
if 0<=units<=75:
    if 0<=units<=50:
        customer_charges=25.00
        bill=units*1.45+customer_charges
    elif 51<=units<=75:
        customer_charges=30.00
        bill=50*1.45+(units-50)*2.6+customer_charges
elif 0<=units<=225:
    if 0<=units<=50:
        customer_charges=35.00
        bill=units*2.60+customer_charges
    elif 51<=units<=100:
        customer_charges=40.00
        bill=50*2.60+(units-50)*2.60+customer_charges
    elif 101<=units<=200:
        customer_charges=45.00
        bill=100*2.60+(units-100)*3.60+customer_charges
    elif 201<=units<=225:
        customer_charges=50.00
        bill=100*2.60+100*3.60+(units-200)*6.90+customer_charges
elif 0<=units<=500:
    if 0<=units<=50:
        customer_charges=35.00
        bill=units*2.65+customer_charges
    elif 51<=units<=100:
        customer_charges=40.00
        bill=50*2.65+(units-50)*3.35+customer_charges
    elif 101<=units<=200:
        customer_charges=45.00
        bill=50*2.65+50*3.35+(units-100)*5.40+customer_charges
    elif 201<=units<=300:
        customer_charges=50.00
        bill=50*2.65+50*3.35+100*5.40+(units-200)*7.10+customer_charges
    elif 301<=units<=400:
        customer_charges=55.00
        bill=50*2.65+50*3.35+100*5.40+100*7.10+(units-300)*7.95+customer_charges
    elif 401<=units<=500:
        customer_charges=55.00
        bill=50*2.65+50*3.35+100*5.40+100*7.10+100*7.95+(units-400)*8.50+customer_charges
elif units>500:
    customer_charges=55.00
    bill=50*2.65+50*3.35+100*5.40+100*7.10+100*7.95+100*8.50+(units-500)*9.95+customer_charges
print("Power Bill:{:.2f}".format(bill))     
    
    
        
        
