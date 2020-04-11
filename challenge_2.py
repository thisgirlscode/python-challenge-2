def solve():
    int1 = ""
    int2 = ""
    while True:
        try:
            if int1 == "":
                int1 = int(input("insert an integer: "))
            else:
                int2 = int(input("insert another integer: "))
                break
        except Exception as e:
            print("An error occurred: {}".format(e))
            
    int_div = int1 // int2
    float_div = int1 / int2

    print ("The integer division of {} and {} is {} ".format(int1,int2,int_div))
    print ("The float division of {} and {} is {} ".format(int1,int2,float_div))

if __name__ == "__main__":
    solve()
