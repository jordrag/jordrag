activation_key = input()
command = input().split(">>>")

while True:
    if command[0] == "Generate":
        break
    else:
        if command[0] == "Contains":
            if command[1] in activation_key:
                print(f"{activation_key} contains {command[1]}")
            else:
                print(f"Substring not found!")
        elif command[0] == "Flip":
            mid_string = activation_key[int(command[2]):int(command[3])]
            if command[1] == "Upper":
                mid_string = mid_string.upper()
            elif command[1] == "Lower":
                mid_string = mid_string.lower()
            activation_key = activation_key[:int(command[2])] + mid_string + activation_key[int(command[3]):]
            print(activation_key)
        elif command[0] == "Slice":
            activation_key = activation_key[:int(command[1])] + activation_key[int(command[2]):]
            print(activation_key)

        command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
