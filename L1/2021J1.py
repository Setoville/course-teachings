boiling_point = input()
pressure = (5 * int(boiling_point)) - 400

print(pressure)
if pressure > 100:
    print(-1)
elif pressure < 100:
    print(1)
else:
    print(0)
