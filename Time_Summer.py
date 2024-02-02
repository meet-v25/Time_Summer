digits = ["0","1","2","3","4","5","6","7","8","9"]; 


def sum_durations(a,b): # -> "(H)*MMSS" : str
    a,b = str(a),str(b); l_a,l_b = len(a),len(b); 
    
    if  (l_a < 3): secs_a = int(a);         mins_a = 0;                   hors_a = 0; 
    elif(l_a < 5): secs_a = int(a[l_a-2:]); mins_a = int(a[:l_a-2]);      hors_a = 0; 
    else:          secs_a = int(a[l_a-2:]); mins_a = int(a[l_a-4:l_a-2]); hors_a = int(a[:l_a-4]); 

    if  (l_b < 3): secs_b = int(b);         mins_b = 0;                   hors_b = 0; 
    elif(l_b < 5): secs_b = int(b[l_b-2:]); mins_b = int(b[:l_b-2]);      hors_b = 0; 
    else:          secs_b = int(b[l_b-2:]); mins_b = int(b[l_b-4:l_b-2]); hors_b = int(b[:l_b-4]); 

    secs_tot = secs_a + secs_b; 
    mins_tot = mins_a + mins_b; 
    hors_tot = hors_a + hors_b; 

    # res = result
    secs_res = "00" + str( (secs_tot % 60) ); 
    mins_res = "00" + str( (mins_tot + (secs_tot//60)) % 60 ); 
    hors_res = "00" + str( hors_tot + ((mins_tot + (secs_tot//60)) // 60) ); 

    resulting_time = hors_res[-2:] + mins_res[-2:] + secs_res[-2:]; 
    return resulting_time;  # -> "(H)*MMSS"


def parse_input_duration(x):
    try:            # If input is of the form "time*multiplier" , eg. "130*7" i.e. 7 times of 1 mins 30 secs
        if(x.count("*")!=1): raise; 
        pos = x.index("*"); 
        res = "000000"; tiime = int(x[:pos].strip()); multiplier = int(x[pos+1:].strip()); 
        for i in range(multiplier): res = sum_durations(res,tiime); 
        return res; 
    
    except:         # Otherwise, remove everything except digits
        res = ""; 
        for i in x: res += (i in digits)*i; 
        return res; 


def Time_Summer():

    print("\nKeep entering your times in (H)*MMSS format. When you want to exit, press 'Enter' without entering anything. ( (x)* denotes any number of x's. )\n"); 
    print("Only 'digits' (and single '*' denoting mult) in your input are considered. All other characters are ignored.\n"); 

    fin = "000000"; 
    parsed_input = parse_input_duration(input("Enter here : ")); l = len(parsed_input); 
    while(l!=0):
        fin = sum_durations(fin,parsed_input); 
        parsed_input = parse_input_duration(input("Enter here : ")); l = len(parsed_input); 

    l_fin = len(fin); hors_fin = int(fin[:l_fin-4]); mins_fin = int(fin[l_fin-4:l_fin-2]); secs_fin = int(fin[l_fin-2:]); 
    print(f"\nStandard Total  =  {hors_fin} {mins_fin} {secs_fin}  =  {hors_fin} Hours {mins_fin} Minutes {secs_fin} Seconds . \n"); 
    input("\nPress Enter to Exit."); print(); 


if(__name__ == "__main__"):
    Time_Summer(); 

