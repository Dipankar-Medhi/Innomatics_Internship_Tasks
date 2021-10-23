import math

numTickets = float(input())
studWaiting = float(input())
mean = studWaiting * float(input())
std = math.sqrt(studWaiting) * float(input())

print(round(0.5*(1+math.erf((numTickets - mean)/(std * math.sqrt(2)))), 4))
