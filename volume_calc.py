#%% 부피 계산

length = float(input("length:"))
width = float(input("width:"))
height = float(input("height:"))

volume = length*width*height

print("부피는",volume, "입니다.")

#
#
#

# %% 택배 요금 계산

# 80cm 이하 : 5000
# 80 ~ 100cm : 8000
# 100 ~ 120cm : 10000
# 120 ~ 160cm : 13000
# 160cm 초과 : 배송 불가

length = float(input("length:"))
width = float(input("width:"))
height = float(input("height:"))

total_length = (length + width + height)


if total_length <= 80:
    charge = 5000
elif total_length <= 100:
    charge = 8000
elif total_length <= 120:
    charge = 10000
elif total_length <= 160:
    charge = 13000
else:
    charge = "배송 불가"

print("총 길이는", total_length, "입니다.")
print("요금은", charge, "입니다.")
