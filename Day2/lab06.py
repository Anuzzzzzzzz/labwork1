"""
You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
run to university. You jog the first mile at 7mph; then run the next two at15mph; before
jogging the last at 7mph again. Will this be quicker or slower than the bus?
    """

#distance of university and bus speed
university_distance_in_miles = 4
bus_speed = 25

#total time for all 10 stops
stop_time = 10*2

#Time taken by bus to reach university
time_by_bus = university_distance_in_miles / bus_speed

total_time_taken_by_bus = (time_by_bus*60) +stop_time

print(f"Total time required by bus to reach university is {total_time_taken_by_bus} minutes")

#Time taken by jogging to university
walking_speed_first_mile = 7
time_taken_to_cover_first_mile  = 1/walking_speed_first_mile

walking_speed_second_mile = 15
time_taken_to_cover_second_mile = 1 / walking_speed_second_mile

walking_speed_third_mile = 15
time_taken_to_cover_third_mile  = 1 / walking_speed_third_mile

walking_speed_fourth_mile = 7
time_taken_to_cover_fourth_mile = 1/ walking_speed_fourth_mile

total_time_taken_by_walking = (time_taken_to_cover_first_mile + time_taken_to_cover_second_mile + time_taken_to_cover_third_mile + time_taken_to_cover_fourth_mile)*60

print(f"Total time taken by walking is {total_time_taken_by_walking}")

if (total_time_taken_by_bus > total_time_taken_by_walking):
    print("walking is faster than bus.")
else:
    print("Bus is faster than walking")