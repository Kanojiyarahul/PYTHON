lines=int(input("enter no of lines in square:"))
rows=0
while rows < lines:
    cols=0
    while cols < lines:
        print("*", end=" ")
        cols+=1
    print()
    rows+=1