import pandas as pd
import statistics
from module_fix_2 import Module

modul = Module()

print("Interpolasi Fraktal 4 titik".center(80, "*"))

n_data = 4

x0 = float(input("Masukkan nilai x0 : "))
y0 = float(input("Masukkan nilai y0 : "))
x1 = float(input("Masukkan nilai x1 : "))
y1 = float(input("Masukkan nilai y1 : "))
x2 = float(input("Masukkan nilai x2 : "))
y2 = float(input("Masukkan nilai y2 : "))
x3 = float(input("Masukkan nilai x3 : "))
y3 = float(input("Masukkan nilai y3 : "))
x_data_pure = [x0, x1, x2, x3]
y_data_pure = [y0, y1, y2, y3]

data_input = pd.DataFrame({"x":x_data_pure, "y":y_data_pure})
print(f"Input data yang dimasukkan :\n{data_input}\n")

n_result = int(input("Masukkan banyak data yang ingin di generate : "))
x_data, x_generate, y_data, y_generate = modul.generate_data(x_data_pure, y_data_pure, n_result)

data_generate = pd.DataFrame({"x_generate":x_generate, "y_generate":y_generate})
data_use = pd.DataFrame({"x_use":x_data, "y_use":y_data})
print(f"\nData yang digenerate :\n{data_generate}\n")
print(f"Data yang dihasilkan :\n{data_use}\n")

a, e = modul.a_and_e_value(x_data_pure, x0, x3)
d = 0.5
c, f = modul.c_and_f_value(x_data_pure, y_data_pure, x0, x3, y0, y3, d)

val_matrix = pd.DataFrame({"a_value":a, "e_value":e, "d_value":d, "c_value":c, "f_value":f}, index=[1, 2, 3])
print(f"Nilai a, e, d, c dan f :\n{val_matrix}\n")

matriks1 = modul.matrix1(a, c, d)
print(f"Matriks 1 : {matriks1}\n")
matriks2 = modul.matrix2(e, f)
print(f"Matriks 2 : {matriks2}\n")
matriks3, num = modul.matrix3(x_data_pure, x_generate, y_generate)
print(f"Matriks 3 : {matriks3}\n")
print(f"Nomor matriks : {num}\n")
matriks_result = modul.matrix_result(matriks1, matriks2, matriks3, num)
print(f"Matriks result : {matriks_result}")
y_result = [value[1, 0] for value in matriks_result]
y_result_data = y_data_pure.copy()
y_result_data.extend(y_result)
data_result = pd.DataFrame({"x_result":x_data, "y_result":y_result_data})
print(f"Data prediksi yang dihasilkan dengan interpolasi fraktal :\n{data_result}")

modul.tampil_grafik(x_data, y_data, y_result_data)

mse = modul.mape(y_data, y_result_data)
data_result_with_mse = pd.DataFrame({"x_asli":x_data, "y_asli":y_data, "x_hasil": x_data, "y_hasil":y_result_data, "mse":mse})
print(f"Nilai yang dihasilkan :\n{data_result_with_mse}")
print(f"Nilai mape yaitu : {statistics.mean(mse)}")
