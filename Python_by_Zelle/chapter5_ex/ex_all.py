# Chapter 5 exercises from Zelle's python book. SaidakbarP 12/25/2019
# exercise 1
#     Converts day month and year numbers into two date formats

def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    #date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    #date2 = monthStr+" " + str(day) + ", " + str(year)

    print("The date is {0}/{1}/{2} or {3} {1}, {2}".format(month, day, year, monthStr))

#main()

#ex2
def quiz():
    grades = ['F', 'F', 'D', 'C', 'B', 'A']
    score = int(input("Enter score 0-5: "))
    print("The grade is:", grades[score])

#quiz()

# ex4
def acronym():
    txt = input("Enter the text you want an acronym for: ")
    list_ = txt.upper().split()
    acr = []
    for word in list_:
        acr.append(word[0])
    print("".join(acr))

#acronym()
# ex 5
def name_number():
    txt = input("Enter your name: ")
    txt = txt.upper()
    s = 0
    for ch in txt:
        s = s + (ord(ch)-64)
    print("sum of characters: ",s)

#name_number()

#ex 7
def Caesar():
    txt = input("Enter the plaintext to be ciphered: ")
    key = int(input("Enter the key to shift the letters (0-26): "))
    key = abs(key) % 26 # works only for positive numbers. Any bigger value >26 are circled back to 0-26 range
    ciphertext = ""

    for ch in txt:
        ciphertext = ciphertext + chr(ord(ch) + key)

    print(ciphertext)
    print()
    print("decrypting the text:")
    plain = ""
    for ch in ciphertext:
        plain = plain + chr(ord(ch)-key)
    print(plain)
#Caesar()

# ex 11
def chaos():
    x1 = float(input("Enter the first number: "))
    x2 = float(input("Enter the second number: "))
    x1_list = []
    x2_list = []
    for i in range(10):
        x1 = 3.9*x1*(1-x1)
        x1_list.append(x1)

        x2 = 3.9*x2*(1-x2)
        x2_list.append(x2)

    print("index {:^8.2f}    {:^8.2f}".format(x1, x2))
    print("-"*26)
    for i in range(1, 11):
        print("{0:^5} {1:^8.6f}    {2:^8.6f}".format(i, x1_list[i-1], x2_list[i-1]))

#chaos()
# ex 13 chaos from file to file
def chaosf():
    infile = open("chaos_values.txt")
    x1s, x2s = infile.read().split()
    infile.close()

    x1 = float(x1s)
    x2 = float(x2s)
    x1_list = []
    x2_list = []
    for i in range(10):
        x1 = 3.9*x1*(1-x1)
        x1_list.append(x1)

        x2 = 3.9*x2*(1-x2)
        x2_list.append(x2)
    outfile = open("chaos_out.txt", "w")
    print("index {:^8.2f}    {:^8.2f}".format(float(x1s), float(x2s)), file = outfile)
    print("-"*26, file = outfile)
    for i in range(1, 11):
        print("{0:^5} {1:^8.6f}    {2:^8.6f}".format(i, x1_list[i-1], x2_list[i-1]), file = outfile)
    outfile.close()
#chaosf()
# ex14 word count
def word_count():
    txt = open("chaos_out.txt", "r")
    l = 0
    w = 0
    ch = 0
    for line in txt:
        l = l + 1 # count lines
        w = w + len(line.split()) # count words
        ch = ch + len(line) # count characters
    print(l, w, ch)
#word_count()
# ex16 histogram
import random
def quiz_histogram():
    scores = open("scores.txt", "w")
    for n in range(1000):
        print(random.randint(0,10), file = scores) # creates 1000 random scores
    scores.close()

    hist = open("scores.txt", "r")
    list_ = [0,0,0,0,0,0,0,0,0,0,0] # 10 slots for counting each score
    for line in hist:
        scr = int(line[:-1])
        list_[scr] = list_[scr] + 1
    print(list_)
quiz_histogram()
