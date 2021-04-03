import os
from PIL import Image




# part 3
U = os.getlogin()

os.chdir(f"C:\\Users\\{U}\\Desktop\\wallpapers")


listdir = os.listdir()

for sth in listdir :
	img = Image.open(sth)
	x, y = img.size
	img.close()
	if x > y :
		# print(f"\n\n{sth} : windows size")
		if os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\windows"):
			pass
		else :
			os.mkdir("windows")

		if os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\windows_bad"):
			pass
		else :
			os.mkdir("windows_bad")

		if x > 1.7*y :
			# print("good size for background")
			os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\windows\\{sth[:-4]}-good{sth[-4:]}")
		else :
			os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\windows_bad\\{sth[:-4]}-bad{sth[-4:]}")
			# # print("bad size for background")
			# os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\windows\\{sth[:-4]}-bad{sth[-4:]}")
	elif x < y :
		# print(f"\n\n{sth} : phone size")
		if os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\phone"):
			pass
		else :
			os.mkdir("phone")

		if 1.7*x < y :
			# print("good size for background")
			os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\phone\\{sth[:-4]}-good{sth[-4:]}")
		else :
			# print("bad size for background")
			os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\phone\\{sth[:-4]}-bad{sth[-4:]}")
	elif x == y :
		# print(f"\n\n{sth} : squared size !!")
		if os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\squared"):
			pass
		else :
			os.mkdir("squared")

		os.rename(sth,f"C:\\Users\\{U}\\Desktop\\wallpapers\\squared\\{sth[:-4]}-squared{sth[-4:]}")






