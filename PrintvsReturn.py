#Mini Excerise: print() vs return
#Write two functions that do the same extact calculation, but behav differently

def calculate_total(price, tax):
    total = (price * tax) + price
    print(total)

def calculate_total_return(price, tax):
    return (price * tax) + price 

calculate_total(100, 0.08)

total = calculate_total_return(100,0.08)
print("Your total is: ", total)

def increase_total(total, tax):
    return (total * tax) + total

new_total = increase_total(total, 0.02)

print("Your total with a 2% increase: $ ", new_total)


