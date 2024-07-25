row1=["1","1","1"]
row2=["2","2","2"]
row3=["3","3","3"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you wamt to put the treasure ? : ")
horizontal=int(position[0])   #column in row
vertical=int(position[1])  #row
selected_row=map[vertical-1]  #gets row from vertical
selected_row[horizontal-1]='x'  #gets column from sel row
print(selected_row)
print(f"\n{row1}\n{row2}\n{row3}")
