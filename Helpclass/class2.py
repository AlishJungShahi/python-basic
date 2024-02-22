#creat fuction for BIM claculate
def BIMcalculate():
    
    #create variable to get input form user
    weight = eval(input("Enter the weight of object\n")) # prompting the user to enter the weight 
    hight = eval(input("Enter the hight of object\n")) # prompting the user to enter the hight 
    
    #calculating the BIM by using formula bim = 
    bim = weight/(hight*hight)
    
    #display the calculate BIM
    #print(bim)
    
    if bim < 18.5:
        print("underweight")
    if bim <= 18.5 and bim > 25:
        print("normal")
    if bim >= 25 and bim<30:
        print("underweight")
    if bim >= 30:
        print("obesity")
        
#call the function to execute it        
BIMcalculate()