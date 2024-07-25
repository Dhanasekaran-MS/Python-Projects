stu_hei=input("Input list of students height : ").split()
#getting values and storing in list with typecasting
for i in range(0,len(stu_hei)):
  stu_hei[i]=int(stu_hei[i])
print(stu_hei)
#total height using for
tot_hei=0
for n in stu_hei:
  tot_hei+=n
print(f"total height = {tot_hei}")
#no.of stu using for loop
tot_stu=0
for x in stu_hei:
  tot_stu+=1
print(f"Total students = {tot_stu}")
average=(tot_hei/tot_stu)
print(f"Average Height = {average}")
r_average=round(tot_hei/tot_stu)
print(f"rounded Average Height = {r_average}")
