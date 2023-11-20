import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# fungsi sinusial dan kosinusial
def sin(x):
    return sum(factorial(i) / (factorial(2 * i + 1) * (-1) ** i) * (x ** (2 * i + 1)) for i in range(n))

def cos(x):
    return sum(factorial(i) / (factorial(2 * i)) * (-1) ** i * (x ** (2 * i)) for i in range(n))

# fungsi faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# pengaturan
st.title('Progam Deret Taylor')

# mengambil input pengguna
n = st.slider('Derajat tertinggi (n)', 1, 100, 50)
x = st.slider('Nilai x', -10.0, 10.0, 0.0)

# menghitung deret Taylor
sin_taylor = sin(x)
cos_taylor = cos(x)

# menggambar fungsi asli dan hasil deret Taylor
fig, ax = plt.subplots()
ax.plot(x_values, sin_values, label='sin(x)')
ax.plot(x_values, cos_values, label='cos(x)')
ax.plot(x, sin_taylor, 'ro', label='sin(x) Taylor')
ax.plot(x, cos_taylor, 'bo', label='cos(x) Taylor')

# menampilkan hasil
st.pyplot(fig)
st.caption("AFIF GANTENG")