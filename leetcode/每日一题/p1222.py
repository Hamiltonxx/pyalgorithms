def queensAttacktheKing(queens, king):
    ans = []
    x,y = king
    for i in range(x,-1,-1):
        if [i,y] in queens:
            ans.append([i,y])
            break
    for i in range(x,8):
        if [i,y] in queens:
            ans.append([i,y])
            break
    for j in range(y,-1,-1):
        if [x,j] in queens:
            ans.append([x,j])
            break
    for j in range(y,8):
        if [x,j] in queens:
            ans.append([x,j])
            break
    while x>=0 and y>=0:
        x-=1;y-=1
        if [x,y] in queens:
            ans.append([x,y])
            break
    x,y = king
    while x<8 and y<8:
        x+=1; y+=1
        if [x,y] in queens:
            ans.append([x,y])
            break
    x,y = king
    while x>=0 and y<8:
        x-=1; y+=1
        if [x,y] in queens:
            ans.append([x,y])
            break
    x,y = king
    while x<8 and y>=0:
        x+=1; y-=1
        if [x,y] in queens:
            ans.append([x,y])
            break
    return ans 
