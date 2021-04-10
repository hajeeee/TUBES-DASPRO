# Haje Noorjamani
# Jurnal: 9/4/2021  : Read Data & Register
#         10/4/2021 : Login 

# READ DATA USER.CSV
filecsv = open("User.csv", "r")
raw_barisan = filecsv.readlines()
barisan = [baris.replace("\n", ";") for baris in raw_barisan]
filecsv.close()

def konversi_array_data_ke_real_values(array_data):
  arr_copy = array_data[:]
  for i in range(6):
    if(i == 0):
      arr_copy[i] = int(arr_copy[i])
  return arr_copy

def konversi_barisan_ke_arr_of_arr_data(barisan):
	z = []
	x = []
	b = ""
	for i in barisan:
		for j in i:
			if((j == ';')):
				x = x + [b]
				b = ""
			else:
				b = b+j
		if(b):
			x = x + [b]
		array_of_data = [data.strip() for data in x] 
		z = z+[array_of_data]
		x = []
	return z

raw_header = [barisan.pop(0)]
header = konversi_barisan_ke_arr_of_arr_data(raw_header)
array_of_array_data = konversi_barisan_ke_arr_of_arr_data(barisan)

head = []
for i in header:
	head=i
print(head)

datas = []
for a in array_of_array_data:
	array_data = konversi_array_data_ke_real_values(a)
	datas.append(array_data)
print(datas)

def konversi_datas_ke_string():
	string_data = ";".join(head) + "\n"
	for arr_data in datas:
		arr_data_all_string = [str(var) for var in arr_data]
		string_data += ";".join(arr_data_all_string)
		string_data += "\n"
	return string_data
datas_as_string = konversi_datas_ke_string()
print(datas_as_string)

def cekUsername(input_username):
	kons_cekUserName = 0
	for user in datas:
		if(user[2]==input_username):
			kons_cekUserName = kons_cekUserName + 1
		else:
			kons_cekUserName = kons_cekUserName
	
	if(kons_cekUserName == 0):
		return False
	else:
		return True

def cekPassword(password, username):
    kons_cekPassword = 0
    for user in datas:
        if(user[2]==username):
            if(user[3]==password):
                kons_cekPassword = kons_cekPassword + 1
            else:
                kons_cekPassword
    
    if(kons_cekPassword == 1):
        return True
    else:
        return False




# COMMAND

command = input('>> ')
if(command == 'register'):
    new_user_id = datas[-1][0] + 1
    register_nama = input("Masukan nama: ").title()
    register_username = input("Masukan username: ").lower()
    while(cekUsername(register_username)==True):
        print("Username sudah terdaftar. Gunakan username lain!")
        register_username = input("Masukan username: ").lower()
    register_password = input("Masukan password: ")
    register_alamat = input("Masukan alamat: ")
    new_user = [new_user_id, register_nama, register_username, register_password, register_alamat, 'User']

    print(new_user)

    datas.append(new_user)
    datas_as_string = konversi_datas_ke_string()
    f = open("User.csv", "w")
    f.write(datas_as_string)
    f.close()

    print(datas) 
elif(command == 'login'):
    login_username = input("Masukan username: ").lower()
    login_password = input("Masukan password: ")
    while(cekUsername(login_username)==False):
        print("Username belum terdaftar!")
        login_username = input("Masukan username: ").lower()
        login_password = input("Masukan password: ")
    while(cekPassword(login_password, login_username)==False):
        print("Password salah!")
        login_password = input("Masukan password: ")
    print('Halo '+login_username+'! Selamat datang di Kantong Ajaib.')