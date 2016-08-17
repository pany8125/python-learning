items = ["December 22, 2015", "Bread", 8.4]
print(items[0])


date,item,price = ["December 22, 2015", "Bread", 8.4]
print(date)
print(item)
print(price)

dateA,*itemA,priceA = ["December 22, 2015", "abc", "Bread", 8.4]
print(dateA)
print(itemA)
print(priceA)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([12,65,76,25,67,38,96,98,66,44])
drop_first_last([12,65,76,25])
drop_first_last([12,65,76])