bank1 = ['tiger', 'grass', 'goat']
bank2 = []
print ("bank1 has",bank1)
print ("bank2 has",bank2)
print("Moving goat to bank2")
bank1.remove('goat')
bank2.append('goat')
print ("bank1 has",bank1)
print ("bank2 has",bank2)
bank1.remove('grass')
bank2.append('grass')
bank2.remove('goat')
bank1.append('goat')
print("We move grass to bank2 and take goat back to bank1")
print ("bank1 has",bank1)
print ("bank2 has",bank2)
bank1.remove('tiger')
bank2.append('tiger')
print("We move the tiger to bank2")
print ("bank1 has",bank1)
print ("bank2 has",bank2)
print("We move goat to bank2")
bank1.remove('goat')
bank2.append('goat')
print ("bank1 has",bank1)
print ("bank2 has",bank2)