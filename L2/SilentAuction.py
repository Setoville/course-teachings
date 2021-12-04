N = int(input())

# for i in range(N):
i = 0

highest_bidder_name = ''
max_bid_amount = 0

# N = 3
# i = 0
while i < N:
    if i == 0:
        break
    name = input()

    #name = "grace"
    #name = "william"
    bid = int(input())
    #bid = 100
    #bid = 95
    #max_bid_amount = 0
    if bid > max_bid_amount:
        #highest_bidder_name = "g race"
        highest_bidder_name = name
        #max_bid_amount = 100
        max_bid_amount = bid
    i = i + 1

print(highest_bidder_name)
