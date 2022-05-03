import game


def main():
    name = str(input("Enter the name: "))
    price = str(input("Enter you'r price: "))
    game.bid_game(name, price)

main()
