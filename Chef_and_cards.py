times=int(input())
points=[]
for i in range(times):
    inputs=int(input())
    chef=[]
    morty=[]
    for ii in range(inputs):
        cards=input().split()
        chef_point=[]
        morty_point=[]
        chef_card=cards[0]
        morty_card=cards[1]
        for a in chef_card:
            chef_point.append(int(a))
        for b in morty_card:
            morty_point.append(int(b))
        if(sum(chef_point)>sum(morty_point)):
            chef.append(1)
        if(sum(chef_point)<sum(morty_point)):
            morty.append(1)
    if(sum(chef)>sum(morty)):
        points.append(0)
        points.append(sum(chef))
    if(sum(chef)<sum(morty)):
        points.append(1)
        points.append(sum(morty))
    if(sum(chef)==sum(morty)):
        points.append(2)
        points.append(sum(chef))
for point in range(0,len(points),2):
    print(int(points[point]),int(points[point+1]))
