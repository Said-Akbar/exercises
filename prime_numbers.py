import numpy as np
def prime_numbers(n):
    bool_table = [True]*(n+1)
    steps=int(n**(1/2)) 
    
    for i in np.arange(2,steps): # prime number calculation up to n
        #print(i, bool_table[i])
        if bool_table[i]==True:
            sumx=0
            x=0
            itr_table = []
            
            while sumx<n:
                sumx=i**2+x*i
                x+=1
                itr_table.append(sumx)
                
            if itr_table[-1]>=len(bool_table): itr_table.pop()

            for j in itr_table[:-1]:
                bool_table[j]=False
                
    indices = np.array(np.arange(0,n+1))
    prime = indices[bool_table][1:-1]