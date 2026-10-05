cost_price=500
selling_price=650

if selling_price > cost_price:
    profit=selling_price-cost_price
    print("profit is",profit)
elif cost_price > selling_price:
    loss=cost_price-selling_price
    print("loss is ",loss)  
else:
    print("no profit no loss")  