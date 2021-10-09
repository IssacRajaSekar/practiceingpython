def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
bidding_continues = True
while bidding_continues:
  print("welcome to the secret aucation!!!")
  secret_aucation = {}
  name = input("What is your name? ")
  bid_amount = int(input("How much you are bitting? "))
  secret_aucation[name] = bid_amount
  should_continue = input("Are there any other bitters? Type yes or no: ").lower()
  if should_continue == "no":
    bidding_continues = False
    find_highest_bidder(secret_aucation)

