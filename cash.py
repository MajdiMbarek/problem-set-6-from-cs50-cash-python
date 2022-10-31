

def main():
    count = 0
   
    while True:
        try :
            change = float(input("Change owed: "))
            if change > 0 :
                break
        except ValueError:
            print("This is not a number!")
    cent = round(change * 100)
    while cent >= 25:
        cent -= 25
        count += 1
    while cent >= 10:
        cent -= 10
        count += 1
    while cent >= 5:
        cent -= 5
        count += 1
    while cent >= 1:
        cent -= 1
        count += 1

    print(count)
   


main()