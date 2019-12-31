# exercises from chapter 7. 12/28/2019 SaidakbarP
# ex1. overtime
def overtime():
    h = int(input("Enter hours: "))
    r = float(input("Enter rate: "))
    w = 0
    if h>40:
        w = 40*r + h%40*1.5*r
    else:
        w = h*r
    return w
# ex11. leap year
def leap_year(y):
    if y%4 == 0 or y%400==0:
        return True
    return False

def date_validation(strdate):
    max_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        month, day, year = strdate.split('/')
        month, day, year = int(month), int(day), int(year)
        if 0<month<=12 and 0<day<=max_month[month-1] and year>0:
            print('Valid date:', strdate)
        else:
            print('Invalid date:', strdate)
            print("Check day, month. Use format: MM/DD/YYYY")
    except:
        print("Enter date only in MM/DD/YYYY format!")

def main():
    #print(round(overtime()))
    #print(leap_year(1804))
    date_validation(input("Enter date MM/DD/YYYY: "))

if __name__=="__main__":
    main()
