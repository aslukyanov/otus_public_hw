
import datetime

my_duty_week = ["day", "day", "night", "night", "free_after_night", "second_day_free", "third_day_free", "free_before_day"] * 45 + ["day", "day", "night", "night", "free_after_night"]
	    
def get_my_shed(day, month) :
    #month, day
    expected_date = datetime.date(2021, month, day)
    expected_day = int(f"{expected_date:%j}")
    return my_duty_week[expected_day - 1], expected_date.strftime('%A')

def get_period_of_sched(day1, month1, day2, month2) :
    return_lst = []
    start_date = datetime.date(2021, month1, day1)
    start_day = int(f"{start_date:%j}")

    end_date = datetime.date(2021, month2, day2)
    end_day = int(f"{end_date:%j}")
    for i in range(start_day, end_day + 1) :
        current_date = datetime.datetime.strptime("2021" + "-" + str(i), "%Y-%j").strftime("%d-%m")
        current_day = datetime.date(2021, int(current_date.split("-")[1]), int(current_date.split("-")[0])).strftime('%A')
        #print(current_date, current_day, my_duty_week[i - 1])
        result = current_date + " is " + current_day + " - " + my_duty_week[i - 1]
        return_lst.append(result)

    return return_lst


if __name__ == "__main__" :
    #print(get_my_shed(20, 10))
    print(get_period_of_sched(16, 10, 26, 10))













