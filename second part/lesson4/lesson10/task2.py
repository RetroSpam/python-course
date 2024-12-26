def get_background_color(current_hour):
    if 6 <= current_hour < 18:
        return "Light_mode"
    else:
        return "Dark_mode"


print(get_background_color(10))
print(get_background_color(20))
print(get_background_color(5))