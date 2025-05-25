def compare(a:int, b:int, x:list) -> list:
    if a<b:
        x.append(a)
    else:
        x.append(b)
    

def two_array_main(arr1:list, arr2:list) -> list:
    new_arr=[]
    for i in range(max(len(arr1), len(arr2))):
        compare(arr1[i], arr2[i], new_arr)
    return new_arr

print(two_array_main([1,2,3],[100,200,300]))