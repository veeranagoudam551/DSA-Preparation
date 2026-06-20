#Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
#Time complexity:0(1)
#Space complexity:0(1)
day=int(input("enter the day number(From 1 to 7):"))
match day:
    case 1 :
        print("Monday")
    case 2 :
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 :
        print("saturday")
    case 7 :
        print("sunday")
    case _ :
        print("invalid")