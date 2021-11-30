'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
done = False
while not done:
    user = int(input("Choose a month 1-12 or any other number to quit:"))
    if 1 <= user <= 12:
        print(months[((int(user)-1)*3):(int(user)*3)])
    else:
        done = True
print("Goodbye")
