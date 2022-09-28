"""def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read(13)
        print(read_data)
read_file("my_file_0.txt")"""

"""def write_file(filename="", text=""):
    with open(filename, mode ="w", encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)"""

"""def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8")as f:
        append_file = f.write(text)
        return append_file
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)"""

"""import json
def to_json_string(my_obj):
    file = json.dumps(my_obj)
    return file
my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))"""
"""import json
def from_json_string(my_str):
    file = json.loads(my_str)
    return file
s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
"""{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}"""
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
""" {"is_active": true, 12 } """
"""
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))"""
import json
def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding="utf-8") as f:
        write_data = f.write(json.dumps(my_obj))
filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
