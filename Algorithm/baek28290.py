string_input = input()

ans_dict = {"fdsajkl;": 'in-out', "jkl;fdsa": 'in-out',
            "asdf;lkj": 'out-in', ";lkjasdf": 'out-in',
            "asdfjkl;": "stairs", ";lkjfdsa":  "reverse"}

print(ans_dict.get(string_input, 'molu'))