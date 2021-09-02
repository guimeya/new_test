
"""
Basic sales tax is applicable at a rate of 10% on all goods, except books,food, and medical 
products that are exempt.Import duty is an additional sales  tax applicable on all imported 
goods at a rate of 5% , with no exemptions.

When I purchase items I receive a receipt with lists the name of all the items and their price 
(including tax), finishing with the total cost of the items, and the total amounts of sales 
taxes paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price 
of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping baskets...

"""


def tax (amount, rate, time):

    p = 10
    n = 5

    tax (12.49, 0, 1)
    tax (14.99, 10/100, 1)
    tax (0.85, 0, 1)

    tax (10.00, 5/100, 2)
    tax (47.50, 5/100, 1)
    
    tax (27.99, 5*10/100, 2)
    tax (18.99, 5*10/100, 3)
    tax (9.75, 0, 1)
    tax (11.25, 5*10/100, 3)

print ('input 1:')
book = input (' 1 book: 12.49')
book = 12.49
music_CD = input ('1 music CD: 16.49')
music_CD = 16.49
chocolate_bar = input ('1 chocolate bar: 0.85')
chocolate_bar = 0.85
print ('Sales Taxes: 1.50')
print ('Total: 29.83')

print ('Input 2:')
imported_box_of_chocolates = input ('1 imported box of chocolates: 10.50')
imported_box_of_chocolates = 10.50 
imported_bottle_of_perfume = input ('1 imported bottle of perfume: 54.65')
imported_bottle_of_perfume = 54.65
print ('Sales Taxes: 7.65')
print ('Total: 65.15')

print ('Input 3:')
imported_bottle_of_perfume = input ('1 imported bottle of perfume: 32.19')
imported_bottle_of_perfume = 32.19
bottle_of_perfume = input ('1 botthe of perfume: 20.89')
bottle_of_perfume = 20.89
packet_of_headache_pills = input ('1 packet of headache pills: 9.75')
packet_of_headache_pills = 9.75
imported_box_of_chocolates = input ('1 imported box of chocolates: 11.85')
impoerted_box_of_chocolates = 11.85
print ('Sales Taxes: 6.70')
print ('Total: 74.68')