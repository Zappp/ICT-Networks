import random

crc_key = [1, 0, 1, 1, 1, 1, 1, 1]
ki_long = len(crc_key)
n = 0.1


def open_file(file_name):
    with open(file_name, "rb") as f:
        data = f.read()

    return data


def new_file(new_file_name, bin_data, attribute):
    file = open(new_file_name, attribute)
    file.write(bin_data)
    file.close()


def data_string(data):
    bin_str_list = []	
    [bin_str_list.append((bin(i)[2:])) for i in data]
    bin_str = ''.join(bin_str_list)

    return bin_str


def parity_bit(data):
    return (data_string(data).count('1')) % 2


def sum_bit(data):
    return (data_string(data).count('1')) % 100


def noise_operation(byte):
    noise = random.randrange(0, 256)
    byte_and = byte ^ noise

    return byte_and


def bit_operation(data):
    len_data = len(data)
    byte_arr = bytearray(data)

    random_list = (random.sample(range(len_data), int(len_data * n)))
    for k in random_list:
        byte_arr[k] = noise_operation(byte_arr[k])

    noised_data = bytes(byte_arr)

    return noised_data


def xor(a, b):
    if a == b:
        return 0
    else:
        return 1


def division(list1, list2):
    reminder = []
    while len(list2) <= len(list1) and len(list1) > 0:
        if list1[0] == 1:
            del list1[0]
            for i in range(len(list2) - 1):
                list1[i] = xor(list1[i], list2[i + 1])
            if len(list1) > 0:
                reminder.append(1)
        else:
            del list1[0]
            reminder.append(0)
    # list1 is now output list
    return list1


##################################################################
# MAIN

data = open_file("input_data.txt")
new_file("output_data.txt", data, "wb")

parity_bit_ = parity_bit(data)
sum_bit_ = sum_bit(data)

# crc on clear data

data_list_string = list(data_string(data))
data_list_int = list(map(int, data_list_string))

for i in range(ki_long - 1):
    data_list_int.append(0)

crc_list_int = division(data_list_int, crc_key)
crc_list_string = list(map(str, crc_list_int))

crc_data_list_string = data_list_string + crc_list_string
crc_data_list_int = list(map(int, crc_data_list_string))

crc_check_list_int = division(crc_data_list_int, crc_key)
crc_check_list_string = list(map(str, crc_check_list_int))
crc_ = "".join(crc_check_list_string)

###

new_file("output_data.txt", str(parity_bit_), "a")
new_file("output_data.txt", str(sum_bit_), "a")
new_file("output_data.txt", crc_, "a")

###

x = len(str(parity_bit_))
y = len(str(sum_bit_))
z = len(crc_)

new_data = open_file("output_data.txt")
noised_data = bit_operation(new_data[:-(x + y + z)])

# crc on noised data

noised_data_list_string = list(data_string(noised_data))
crc_noised_data_list_string = noised_data_list_string + crc_list_string
crc_noised_data_list_int = list(map(int, crc_noised_data_list_string))

crc_check_noised_list_int = division(crc_noised_data_list_int, crc_key)
crc_check_noised_list_string = list(map(str, crc_check_noised_list_int))

crc_noised = "".join(crc_check_noised_list_string)

###

print(parity_bit(noised_data))
print(sum_bit(noised_data))
print(crc_noised)
