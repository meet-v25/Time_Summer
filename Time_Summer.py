def Time_Summer():

    print("\nKeep entering your times in (H)*MMSS format. When you want to exit, press 'Enter' without entering anything. ( (x)* denotes any number of x's. )\n"); 
    print("Only 'digits' in your input are considered. All other characters are ignored.\n"); 

    nos = ["0","1","2","3","4","5","6","7","8","9"]; 
    hrs=mns=scs = hh=mm=ss = 0 ; 

    def extract_digits(x):
        y = ""; 
        for i in x:
            if(i in nos): y += i; 
        return y; 
    
    x = extract_digits(input("Enter here : ")); l = len(x); 
    while(l!=0):
        if  (l<3): ss += int(x); 
        elif(l<5): mm += int(x[:l-2]); ss += int(x[l-2:]); 
        else:      hh += int(x[:l-4]); mm += int(x[l-4:l-2]); ss += int(x[l-2:]); 
        x = extract_digits(input("Enter here : ")); l = len(x); 

    scs = ss % 60; scs = str(scs); 
    mns = (mm + (ss//60)) % 60; mns = str(mns); 
    hrs = hh + (mm + (ss//60)) // 60; hrs = str(hrs); 

    if(len(hrs)<2): print("\nStandard Total =", "0"+hrs, "0"*(2-len(mns))+mns, "0"*(2-len(scs))+scs, "=", "0"+hrs, "Hours", "0"*(2-len(mns))+mns, "Minutes", "0"*(2-len(scs))+scs, "Seconds", "\n"); 
    else:           print("\nStandard Total =",     hrs, "0"*(2-len(mns))+mns, "0"*(2-len(scs))+scs, "=",     hrs, "Hours", "0"*(2-len(mns))+mns, "Minutes", "0"*(2-len(scs))+scs, "Seconds", "\n"); 

    exit = input("\nPress Enter to Exit."); print(); 

Time_Summer(); 
