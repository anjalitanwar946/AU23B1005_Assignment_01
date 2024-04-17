def Get_name():
    name = input("name: ")
    return name

def get_tshirt():
    size=["s","m","l","xl"]
    brands=["Prada","LV","Gucci","Zudio","Balanciaga"]
    user=Get_name()
    brand_name= input("T-shirt brand you are looking for: ")
    user_size=input("enter size: ")
    if brand_name in brands:
        if user_size in size:
          print("Hi {user},Unfortunately the brand you are looking for is available in this size.")
        else:
            print(f"Hi {user},Unfortunately the brand you are looking for is un available in this size.")
    else:
     print(f"Hi {user},Unfortunately the brand you are looking for is un available.")
get_tshirt()
