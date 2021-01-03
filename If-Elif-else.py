age = int(input("Please enter your age: "))

if age > 17:
    print("You can see an R-rated movie")

elif age < 18 and age > 14:
    print("You can see an MA-rated movie.")

else:
    print("You can only see a G or PG-rated movie.")
