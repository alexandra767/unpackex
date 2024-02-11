def f(*args,**kwargs):
    print("Named:", kwargs)

f(galleons=100, sickeles=50, knuts=25)



















"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) *29 + knuts

coins = [100, 50, 25] list
 *coins passes in individual numbers (unpacks)
print(total(*coins),"Knuts")

coins = {"galleons": 100, "sickles": 50 , "knuts": 25}

#** for dictionary
print(total(**coins), "Knuts")


# print(total(galleons=100, sickles=50, knuts=25), "Knuts")
"""

