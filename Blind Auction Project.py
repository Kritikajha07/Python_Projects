# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)

bids={}
def find_highest_bidder(bidding_dictionary):
    highest_bidder=0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount=int(bidding_dictionary[bidder])
        if bid_amount>highest_bidder:
            highest_bidder=bid_amount
            winner= bidder
    print(f"the highest bidder is {winner} with a bid of $ {highest_bidder} ")


continue_bidding=True
while continue_bidding:
    name = input("What's your name? ")
    price = input("what's your bid: $ ")
    bids[name]=price
    new=input("Are there any other bidders? type 'yes' or 'no' ").lower()
    if  new=="no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif new=="yes":
        continue_bidding=True
        print("\n"*100)




