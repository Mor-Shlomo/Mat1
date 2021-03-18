def azerat(i):
     num=i
     if i>1:
         while (i>1):
             num=num*(i-1.0)
             i=i-1.0      
         return(num)
     else:
         return(1.0)




def power(x,y):
    if x==0 :
        return(0.0)
    else :
        j=0
        num=1.0
        while j<y:
            num=num*x
            j=j+1
    return(num)    


 
def exponent(a):
    result=0.0
    num=0.0    
    while num<50:
        result = result+(power(a,num+1.0))/(azerat(num+1.0)) 
        num = num+1.0
        new=1.0
        new=new+result
    return(new)    
    



def Ln(x):
    yn=0
    a= x-1.0
    while((yn-a)>0.001 or (a-yn)>0.001):
        yn=a
        a = a + 2*((x-exponent(a))/(x+exponent(a)))
    return(a)

def XtimesY(x:float,y:float) -> float:
    try:
        if(x>0):
            result=exponent(Ln(x)*y)
        return float('%0.6f' %result)
    except:
        return(0.0)



def sqrt(x:float,y:float) -> float:
    if (y>0 and x!=0):
            x=1/x
            a=(XtimesY(y,x))
            return float('%0.6f' %a)
    else:
        return(0.0)



def calculate(x):
    try:
        result=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        return float('%0.6f' %result)
    except:
        return (0.0)


