class Main(): 
    
    def Subfields():
        list = [1,2,3,4,5,6]
        for Sub in list:
            if Sub == 1:
                print ("Machine Learning")
            elif Sub == 2:
                print ("Neural Networks")
            elif Sub == 3:
                print ("Vision")
            elif Sub == 4:
                print ("Robotics")
            elif Sub == 5:
                print ("Speech Processing")
            else:
                print ("Natural Language Processing")
    Subfields()

    def OddEven():
        Number = int(input("Please enter a number:"))
        if Number % 2 == 0:
            Datum = "The number you entered is an even number"
        else:
            Datum = "The number you entered is an odd number"
        return Datum
        Datum = OddEven()
        print (Datum)    
    
    def Eligible():  
        Gender = input("Please enter your gender i.e., M if you are a male or F if you are a female:")
        if Gender == "M":
            print ("Good. You entered the correct letter")
        elif Gender == "F":
            print ("Good. You entered the correct letter")
        else:
            print ("Please enter either M or F only")
            Value = input ("Please enter the correct letter:")
            Value = Gender
        Age = int(input("Please enter your age"))
        if Gender == "M":
            if Age >= 21:
                Output = "As per our government norms you are eligible for marriage"
            else:
                Output = "As per our government norms you are not eligible for marriage"
        else:
            if Age >= 18:
                Output = "As per our government norms you are eligible for marriage"
            else:
                Output = "As per our government norms you are not eligible for marriage"
        return Output
        Output = Eligible()
        print (Output)

    def Percentage():        
        Subject1 = int(input("Please enter the marks for subject 1:"))
        Subject2 = int(input("Please enter the marks for subject 2:"))
        Subject3 = int(input("Please enter the marks for subject 3:"))
        Subject4 = int(input("Please enter the marks for subject 4:"))
        Subject5 = int(input("Please enter the marks for subject 5:"))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print ("The total for the five subjects is:", Total)        
        Percentage = Total * 100 / 500
        print ("The percentage for the five subjects is:", Percentage)
        
    def Triangle():         
         print ("Determine the area or perimeter of the triangle.") 
         print ("What do you want to calculate?")    
         Value = input ("Press A for area or P for perimeter:")
         if Value == "A":
             print ("Good. You entered the correct letter")
         elif Value == "P":
             print ("Good. You entered the correct letter")
         else:
             print ("Please enter either A or P only")
             Value1 = input ("Please enter the correct letter:")
             Value = Value1
         if Value == "A":
             Height = int(input("Enter the height of the triangle:"))
             Breadth = int(input("Enter the breadth of the triangle:"))        
             Area = (Height * Breadth) / 2
             Output = Area
         else:
             Height1 = int(input("Enter the height1 of the triangle:"))
             Height2 = int(input("Enter the height2 of the triangle:"))
             Breadth = int(input("Enter the breadth of the triangle:"))
             Perimeter = Height1 + Height2 + Breadth
             Output = Perimeter                         
         if Value == "A":
             print ("The area of the triangle is:", Output)
         else:
             print ("The perimeter of the triangle is:", Output)
              

