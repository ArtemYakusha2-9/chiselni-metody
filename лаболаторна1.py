# 1)Визначити, яка рівність точніша;
# √66 = 8.12 7/3 = 2.33
import math as m
x_actual_sqrt = m.sqrt(66)  # точне значення для √66
x_actual_fraction = 7/3  # точне значення для 7/3
x_measured_sqrt = 8.12  # виміряне значення для √66
x_measured_fraction = 2.33  # виміряне значення для 7/3


# обчислення абсолютної похибки
absolute_error_sqrt = x_measured_sqrt - x_actual_sqrt
absolute_error_fraction = x_measured_fraction - x_actual_fraction

# обчислення відносної похибки
relative_error_sqrt = (absolute_error_sqrt / x_actual_sqrt) * 100
relative_error_fraction = (absolute_error_fraction / x_actual_fraction) * 100

# виведення результатів
print("абсолютна похибка для √66:", abs(absolute_error_sqrt))
print("відносна похибка для √66:", str(abs(relative_error_sqrt)) + '%')
print("абсолютна похибка для 7/3:", abs(absolute_error_fraction))
print("відносна похибка для 7/3:", str(abs(relative_error_fraction)) + '%')

# порівняння точності
if absolute_error_sqrt < absolute_error_fraction:
    print("√66 є точнішою")
elif absolute_error_sqrt > absolute_error_fraction:
    print("7/3 є точнішою")
else:
    print("обидві рівності мають однакову точність")


# 2)

# а)
# Нехай x=13.5726+-0.0072.За умовою ∆x = 0.0072
delta_x = 0.0072
# 13.5726 = 1*10^1+3*10^0+5*10^(-1)+7*10^(-2)+2*10^(-3)+6*10^(-4)
# Щоб знайти кількість правильних значущих цифр у вузькому розумінні, перевіримо послідовно виконання умови для  n=1, 2, 3…
n = 1
while delta_x <= 0.5 * 10**(1-n+1):
    n += 1
print("2a)  Отже, правильними значущими цифрами у вузькому розумінні наближеного числа 13.5726 будуть " + str(n) + ' цифри - 1, 3, 5, 7 (тобто n = ' + str(n) + """); 
Відповідь: n=""" + str(n))

# б)
# Нехай х=3.87683; 𝛿х=0,33%.
absolute_error = 3.87683*0.0033  #Абсолютна похибка 𝛥х=х⋅𝛿х
# 3.87683 = 3*10^0+8*10^(-1)+7*10^(-2)+6*10^(-3)+8*10^(-4)+3*10^(-5)
x = 1
while absolute_error <= 1 * 10**(1-x+1):
    x += 1
print("2б)  Це означає, що у числі 3.87683 правильними у широкому розумінні є " + str(x) + ' цифри 3, 8, 7, 6.')

#3)
#a)
#Оскільки всі три цифри числа х=26.3 правильні у вузькому розумінні, то гранична абсолютна похибка 𝛥𝑥 ≤ 0,5⋅0,001=0,0005
marginal_relative_error = 0.0005/26.3  #шукаем граничну відносну похибку
round_marginal_relative_error = round(marginal_relative_error, 5)
round_percent_marginal_relative_error = round_marginal_relative_error * 100
print("∆x = 0.0005, 𝛿х = " + str(marginal_relative_error) + '(' + str(round_percent_marginal_relative_error) + "%)")

#б)
#Оскільки всі п’ять цифр числа х=4.8556 правильні у широкому розумінні, то гранична абсолютна похибка 𝛥𝑥 ≤ 1∙0.001=0.001
marginal_relative_error = 0.001/4.8556  #шукаем граничну відносну похибку
round_marginal_relative_error = round(marginal_relative_error, 5)
round_percent_marginal_relative_error = round_marginal_relative_error * 100
print("∆x = 0.001, 𝛿х = " + str(marginal_relative_error) + '(' + str(round_percent_marginal_relative_error) + "%)")



