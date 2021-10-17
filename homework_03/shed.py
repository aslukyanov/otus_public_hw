
import datetime

my_duty_week = ["day", "day", "night", "night", "free_after_night", "second_day_free", "third_day_free", "free_before_day"] * 45 + ["day", "day", "night", "night", "free_after_night"]
	    
def get_my_shed(day, month) :
    #month, day
    expected_date = datetime.date(2021, month, day)
    expected_day = int(f"{expected_date:%j}")
    return my_duty_week[expected_day - 1], expected_date.strftime('%A')



if __name__ == "__main__" :
    print(get_my_shed(20, 10))


