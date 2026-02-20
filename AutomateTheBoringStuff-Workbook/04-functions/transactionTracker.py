
def after_transaction(balance, cost):
    if balance + cost < 0:
        return balance
    else:
        return balance + cost
    