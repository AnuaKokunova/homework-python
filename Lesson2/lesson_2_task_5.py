# -*- coding: utf-8 -*-

month_to_season_as_str = input ("Номер месяца : ")
month_to_season = int(month_to_season_as_str)


if (month_to_season == 1 or month_to_season == 2 or month_to_season == 12 ) :
    print ("Зима")

elif (month_to_season == 3 or month_to_season == 4 or month_to_season == 5) :
    print ("Весна")

elif (month_to_season == 6 or month_to_season == 7 or month_to_season == 8 ) :
    print ("Лето")

elif (month_to_season == 9 or month_to_season == 10 or month_to_season == 11) :
    print ("Осень")


