def Get_name():
    name = input(name: )
    return name

def get_tshirt():
    size=["s","m","l","xl"]
   brands=["Prada","LV","Gucci","Zudio","Balanciaga"]
    user=Get_name()
    brand_name= input("T-shirt brand you are looking for: ")
    user_size=input("enter size: ")
    if brand_name in brands and user_size in size:
     print("Hi {user},Unfortunately the brand you are looking for is available.")
    else:
     print(f"Hi {user},Unfortunately the brand you are looking for is un available.")
get_tshirt()
