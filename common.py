a=[2,4,1,6]
b=[2,0,2,5,3,6]

def common_end(a,b):
    if a[0] == b[0] or a[-1] == b[-1] :
        return True
    else:
        return False

print(common_end())