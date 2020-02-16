amount = input('string')
transform = amount.maketrans
amount = amount.translate(transform('.,', '.,'))
print(amount)