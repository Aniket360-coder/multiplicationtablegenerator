while True:
    try:
        a = int(input("enter: "))
    except Exception as e:
        continue
    else:
        if str(a) == "q":
            break
        a= str(a)
        if  a.isnumeric()==True:
            for i in range(1,11):
                print(f"{int(a)} * {int(i)} = {int(a)*int(i)}")
            print()
            continue
        
        
