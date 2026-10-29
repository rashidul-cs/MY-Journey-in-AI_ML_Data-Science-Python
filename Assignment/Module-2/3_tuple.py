
tuple1 = (
    1,
    2,
    3,
    6.7,
    8.8,
    9.4,
    "a",
    "b",
    "c",
    "mango",
    "banana",
    "apple",
)
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12 = tuple1

tuple2 = (
    1,
    2,
    3,
    6.7,
    8.8,
    4.4,
    "a",
    "b",
    "c",
    "mango",
    "banana",
    "zebra",
)

is_equal = tuple1 == tuple2
is_greater = tuple1 > tuple2
is_less = tuple1 < tuple2

print("Tuple 1 and Tuple 2 are equal:", is_equal)
print("Tuple 1 > Tuple 2:", is_greater)
print("Tuple 1 < Tuple 2:", is_less)
