def read_file():    
    f = open("password.csv", "r")
    all_lines = f.readlines()
    all_password = []
    for line in all_lines:
        clean_data = line.strip()
        data = clean_data.split(",")
        all_password.append(data)
    f.close()
    return all_password
all_applicants = read_file()
print(all_password)