import random
com=random. randint (1,100)
tries=0
while True:
    tries=tries+1
    hum=int(input("Enter a number  between 1-100"))  

    if hum==com:
        print(f"congralutation correct guessing and you won {tries} tries")    
        

    elif hum > com:
           print("number is lower")

    elif hum < com:
             print("number is higher")
  


