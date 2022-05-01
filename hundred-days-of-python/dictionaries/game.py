def highest_bidder(record):
    highest_bid = 0
    winner = ""
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(winner)

def bid_game():
    game_on = True
    bids = {}
    while game_on:
        name = str(input("Enter the name: "))
        price = int(input("Enter you'r price: $"))
        bids[name] = price
        answer = input("Are there any other bidders? Type 'yes or no'").lower()
        if answer == "no":
            game_on = False
      
        
    highest_bidder(bids)

bid_game()