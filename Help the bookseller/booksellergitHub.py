from collections import defaultdict


def stock_list(books, categories):
    """Counts total number of books per category"""
    if not books:
        return ''

    stock = defaultdict(int)
    str_stock = list()

    for book in books:
        code, quantity = book.split()
        for category in categories:
            if code.startswith(category):
                stock[category] += int(quantity)

    for category in categories:
        str_stock.append('({} : {})'.format(category, stock[category]))

    return ' - '.join(str_stock)

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

print(stock_list(b, c))
