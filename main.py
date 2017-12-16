print ("enter 10 numbers in sorted order:");

data=[];
for i in range(0,10):
    temp=int(input("enter numbers:"));
    data.append(temp);

def sort_check(data):
    if len(data)<=1:
        return True;
    return data[0]<=data[1] and sort_check(data[1:]);
    
if sort_check(data):
    print ('data is sorted');
else:
    print ('data not sorted');
    