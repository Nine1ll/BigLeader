import sys                                            
                                                      
while True:                                           
    name, age, weight = sys.stdin.readline().split()  
    if name == '#':                                   
        break                                         
    else:                                             
        age = int(age)                                
        weight = int(weight)                          
        if age > 17 or weight >= 80:                  
            print(name+" Senior")                     
        else:                                         
            print(name+" Junior")                     