import math

def calc(height,width,cover):
  area=height*width
  paint_can=area/cover
  print(f"The actual paint can needed : {paint_can}")
  print(f"The number of paint can needed to buy : {math.ceil(paint_can)}")

test1=int(input("Enter the height of the wall in meters : "))
test2=int(input("Enter the width of the wall in meters : "))
test3=int(input("Enter how much sq.m that 1 can can cover : "))

calc(height=test1,width=test2,cover=test3)
