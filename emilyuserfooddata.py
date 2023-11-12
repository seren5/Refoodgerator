def user_food():
    food_item = input("Please input the food item you'd like to store in lowercase and non-plural (Check your spelling! Our varieties are limited to the general categories, such as cabbage) ")
    expiry_time(food_item)
    return food_item



def expiry_time(item):
    exit_menu = False
    while not exit_menu:
        expiry_year = input("Please input the expiration year (in numbers) of the food item: ")
        if " " in expiry_year:
            print("Error: Please provide only one number without a space. ")
            continue

        length_expiry_year = len(expiry_year)
        if length_expiry_year > 4 or length_expiry_year < 4:
             print("Error: Please provide a valid year in numbers. ")
             continue
        exit_menu = True

    expiry_year = int(expiry_year)

    if expiry_year % 4 == 0 or expiry_year % 400 == 0:
        expiry_year = expiry_year-2000
        expiry_year_days = ((expiry_year)/4)*366 + (3*(expiry_year)/4)*365
        feb_days = 29
    else:
        expiry_year = expiry_year-2000
        expiry_year_days = ((expiry_year)/4)*366 + (3*(expiry_year)/4)*365
        feb_days = 28

    jan_days = 31
    mar_days = 31
    apr_days = 30
    may_days = 31
    jun_days = 30
    jul_days = 31
    aug_days = 31
    sep_days = 30
    oct_days = 31
    nov_days = 30
    dec_days = 31
    
    exit_menu2 = False
    while not exit_menu2:
        expiry_month = (input("Please input the expiration month (in numbers) of the food item: "))
        if " " in expiry_month:
            print("Error: Please provide only one number without a space. ")
            continue

        length_expiry_month = len(expiry_month)
        if length_expiry_month > 2:
             print("Error: Please provide a valid month in numbers. ")

        expiry_month = int(expiry_month)
        if expiry_month < 1 or expiry_month > 12:
            print("Error: You did not provide a number for a month. ")
            continue

        exit_menu2 = True
    

    if expiry_month == 1:
        expiry_month_days = jan_days
    elif expiry_month == 2:
        expiry_month_days = jan_days + feb_days
    elif expiry_month == 3:
        expiry_month_days = jan_days + feb_days + mar_days
    elif expiry_month == 4:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days
    elif expiry_month == 5:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days
    elif expiry_month == 6:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days
    elif expiry_month == 7:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days
    elif expiry_month == 8:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days
    elif expiry_month == 9:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days
    elif expiry_month == 10:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days
    elif expiry_month == 11:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days + nov_days
    elif expiry_month == 12:
        expiry_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days + nov_days + dec_days

    expiry_day = int(input("Please input the expiration day of the food item: "))
    
    days_expiry = expiry_year_days + expiry_month_days + expiry_day


    from datetime import date
    today = date.today()
    today = str(today)
    
    this_year = int(today[:4])
    this_month = today[5:7]
    this_day = today[8:]
    this_day_days = int(this_day)
    
    if this_year % 400 == 0 or this_year % 4 == 0:
        this_year = this_year - 2000
        this_year_days = ((this_year)/4)*366 + (3*(this_year)/4)*365
    else:
        this_year = this_year - 2000
        this_year_days = ((this_year)/4)*366 + (3*(this_year)/4)*365
   
    if "1" in this_month:
        this_month_days = jan_days
    elif "2" in this_month:
            this_month_days = jan_days + feb_days
    elif "3" in this_month:
            this_month_days = jan_days + feb_days + mar_days
    elif "4" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days
    elif "5" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days
    elif "6" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days
    elif "7" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days
    elif "8" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days
    elif "9" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days
    elif "10" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days
    elif "11" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days + nov_days
    elif "12" in this_month:
            this_month_days = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days + nov_days + dec_days

    today_in_days = this_year_days + this_month_days + this_day_days

    days_until_expiry = int(days_expiry - today_in_days - 303.25)

    print(f"{days_until_expiry} days until expiration.")
    return days_until_expiry

user_food()
