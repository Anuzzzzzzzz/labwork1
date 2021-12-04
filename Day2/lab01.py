#convert seconds to day, hours, minutes and seconds
user_input=int(input("Enter seconds to convert into day"))
day=(((user_input/60)/60)/24)
print(f"total day for given seconds:{day}")
hour=((user_input/60)/60)
print(f"total hours for given seconds:{hour}")
minute=(user_input/60)
print(f"total minutes for givem seconds:{minute}")

