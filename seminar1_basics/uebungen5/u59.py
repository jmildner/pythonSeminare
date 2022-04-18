from tools import mytools as mt

print("Übung 5.9.2 - external functions")

number = mt.geti("enter number of item")
prize = mt.getf("enter prize  of item")
name = mt.gets("enter name   of item")

print(f"{number} pieces of {name} at {prize} $ cost {prize * number}")
