def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3

flow = flow_rate(weight_diff, time_diff)
print(f"{flow:.3} kg per second")
print("{0:.3} kg per second".format(flow))
print("{0:.3f} kg per second".format(flow))
