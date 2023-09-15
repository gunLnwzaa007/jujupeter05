#return not values
#หมายถึง การสิ้นสุดหรือจบการทำงานของ Block scope การทำงานหนึ่งๆ

def A():
    print("KKK")
    print("LLL")
    return
    print("JJJ")

def B(x):
    return
    print(f"X is {x}")


A()
B(252)
