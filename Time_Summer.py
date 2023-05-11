def Time_Summer():

    print("\nKeep entering your times in (H)*MMSS format. When you want to exit, press 'Enter' without entering anything else. ( (x)* denotes any number of x's. )\n"); 
    hrs=mns=scs = hh=mm=ss = 0 ; 

    x = input("Enter here : "); l = len(x); 
    while(l!=0):
        if  (l<3): ss += int(x); 
        elif(l<5): mm += int(x[:l-2]); ss += int(x[l-2:]); 
        else:      hh += int(x[:l-4]); mm += int(x[l-4:l-2]); ss += int(x[l-2:]); 
        x = input("Enter here : "); l = len(x); 

    scs = ss % 60; scs = str(scs); 
    mns = (mm + (ss//60)) % 60; mns = str(mns); 
    hrs = hh + (mm + (ss//60)) // 60; hrs = str(hrs); 

    if(len(hrs)<2): print("\nStandard Total =", "0"+hrs, "0"*(2-len(mns))+mns, "0"*(2-len(scs))+scs, "=", "0"+hrs, "Hours", "0"*(2-len(mns))+mns, "Minutes", "0"*(2-len(scs))+scs, "Seconds", "\n"); 
    else:           print("\nStandard Total =",     hrs, "0"*(2-len(mns))+mns, "0"*(2-len(scs))+scs, "=",     hrs, "Hours", "0"*(2-len(mns))+mns, "Minutes", "0"*(2-len(scs))+scs, "Seconds", "\n"); 

    exit = input("\nPress Enter to Exit."); print(); 

Time_Summer(); 