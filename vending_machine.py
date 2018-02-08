soda = ["Pepsi","Coke","Sprite"]
chips = ["Dpritos","Fritos"]
candy = ["Snickers","M&M","Twizzlers"]

while True:
    choice = input("would you liek a soda, soe chips , or a candy?").lower()
    try:
        if choice == 'soda':
            snack = soda.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
          print("Sorry i didnt understand")
          continue 
    except IndexError:
        print ("We're all out of {}!".format(choice))
    else:
        print ("Here are your {}: {}".format(choice, snack))
        #try3