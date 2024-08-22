immutable_var = (1, 2, True, "weather", 8, 74)
print(immutable_var)
#   immutable_var[1] = 50 # TypeError: 'tuple' object does not support item assignment
mutable_list = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
mutable_list.remove("monday")
mutable_list.extend(["days", 2, True])
print(mutable_list)