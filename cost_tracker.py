import sys
cost ={}

while True:
    a=input("name=")
    
    if a=='1':
        break
    
    b=input("price=")
    cost[a]=b

print(cost)

out_path='output.txt'
with open(out_path,'w') as f:
    og=sys.stdout
    sys.stdout=f
    for a,b in cost.items():
        print(f"Name:{a} Price:{b}")