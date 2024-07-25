#art 


logo="""
  ___________
  \         /
   )_______(
   |"""""""|_.-._,.---------.,_.-._
   |       | | |               | | ''-.
   |       |_| |_             _| |_..-'
   |_______| '-' `'---------'` '-'
   )"""""""(
  /_________\
  `'-------'`
 .-------------.
/_______________\

"""


#main

import os
# from art import logo
print(logo)
print(" Welcome To Secret Auction BID ")

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  #{dhana,120;annamalai,230}
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The Winner is {bidder} with the highest bid of {highest_bid}")

while not bidding_finished:
  name=input("What is your name ? \n :")
  price=int(input("What is your bidding price ? \n :"))
  bids[name]=price
  continue_bid =input("Are there any other bidders ? 'yes' or 'no' :").lower()
  if continue_bid == "no" :
    bidding_finished = True
    find_highest_bidder(bids)
  elif continue_bid == "yes" :
    os.system('clear')



