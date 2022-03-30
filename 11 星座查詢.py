day = input("輸入月及日為：").split()
month = int(day[0])
date = int(day[1])
if month == 1 and date >= 21 or month == 2 and date <= 18:
    print("Aquarius 水瓶座")
elif month == 2 and date >= 19 or month == 3 and date <= 20:
    print("Pisces 雙魚座")
elif month == 3 and date >= 21 or month == 4 and date <= 20:
    print("Aries 牡羊座")
elif month == 4 and date >= 21 or month == 5 and date <= 21:
    print("Taurus 金牛座")
elif month == 5 and date >= 19 or month == 6 and date <= 21:
    print("Gemini 雙子座")
elif month == 6 and date >= 19 or month == 7 and date <= 22:
    print("Cancer 巨蟹座")
elif month == 7 and date >= 19 or month == 8 and date <= 23:
    print("Leo 獅子座")
elif month == 8 and date >= 19 or month == 9 and date <= 23:
    print("Virgo 處女座")
elif month == 9 and date >= 19 or month == 10 and date <= 23:
    print("Libra 天秤座")
elif month == 10 and date >= 19 or month == 11 and date <= 22:
    print("Scorpio 天蠍座")
elif month == 11 and date >= 19 or month == 12 and date <= 21:
    print("Sagittarius 射手座")
elif month == 12 and date >= 19 or month == 1 and date <= 20:
    print("Capricorn 摩蠍座")

