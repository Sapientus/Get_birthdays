from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    weekday = {                  #Here we create a dictionary to iterate only routine days
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday"
        }

    user_birthday_dict = {day: [] for day in weekday.values()}

    if not users:
        return {}

    today = date.today()
    next_week = today + timedelta(days=7) #here we define the next new week
       
    for user in users:
        user_birthday = user["birthday"].replace(year=today.year) #we modify the birthday to the current year

        if today > user_birthday:
            user_birthday = user_birthday.replace(year=today.year+1) #it checks if BD already was in the current year

        if today<=user_birthday<=next_week:    #my favourite part, we finally check days of week here
            day_of_week = user_birthday.strftime("%A")
            if day_of_week not in weekday.values():
                day_of_week = "Monday"
            user_birthday_dict[day_of_week].append(user["name"])

        
    user_birthday_dict = {day: names for day, names in user_birthday_dict.items() if names}

    return user_birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")