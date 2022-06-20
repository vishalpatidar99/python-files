# Python Program for compound interest
price,rate,time=10000,10.25,5
amount=price*(pow((1+rate/100),time))
CI=amount-price
print(CI)