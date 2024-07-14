#AKASH
list1=[4,9,25,49,81,16,36,64]
def int_list(list1):
    
    even_num=[]
    odd_num=[]
    for i in list1:
        
        if i%2==0:
            
            
            even_num.append(i*i)
        else:
            
            odd_num.append(i)
    
    return even_num+odd_num
print(int_list(list1))
        
