##
## EPITECH PROJECT, 2023
## B-CNA-410-PAR-4-1-trade-hugo.mouraud
## File description:
## action
##

import sys

def actions(dollars, current_closing_prices):
    previous_closing_price = current_closing_prices[-2]
    current_closing_price = current_closing_prices[-1]

    # Stocker le prix de clôture précédent pour réduire les accès répétitifs
    affordable = dollars / current_closing_price
    momentum = current_closing_price - previous_closing_price #variation des prix
    print(f'momentum = {momentum}, dollard {dollars}, ', file=sys.stderr)

    if momentum > 5 and dollars >= 100:
        print(f'buy USDT_BTC {0.5 * affordable }', flush=True)
    elif momentum < -5 and self.botState.stacks["USDT"] >= 0.5:
         print(f'sell USDT_BTC {0.5 * affordable }', flush=True)
         print(f'momentum: {momentum}, BTC stack: {self.botState.stacks["BTC"]}, Dollars {dollars}', file=sys.stderr)
    else:
        print("no_moves", flush=True)