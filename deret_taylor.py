import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def taylor_series(func, x0, n_terms):
    x = sp.symbols('x')
    taylor = sp.series(func, x, x0, n_terms).removeO()
    return taylor

def plot_taylor_series(func, x0, n_terms, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 1000)
    y_vals_func = func(x_vals)
    y_vals_taylor = [taylor_series(func, x0, n_terms).subs('x', val) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals_func, label='Function')
    plt.plot(x_vals, y_vals_taylor, label=f'Taylor Series (n={n_terms})', linestyle='--')
    plt.scatter([x0], [func(x0)], color='red', marker='o', label=f'Expansion point (x={x0})')
    plt.legend()
    plt.title('DERET TAYLOR')
    plt.xlabel('x')
    plt.ylabel('y')
    st.pyplot()

def main():
    st.title('DERET TAYLOR')

    st.sidebar.header('Input Parameters')
    func_str = st.sidebar.text_input('Masukkan Fungsi (e.g., sin(x), cos(x)):')
    x0 = st.sidebar.number_input('Enter the expansion point (x0):', value=0.0)
    n_terms = st.sidebar.number_input('Enter the number of terms in the series:', min_value=1, value=4)
    x_range = st.sidebar.slider('Select the x-axis range:', -10.0, 10.0, (-5.0, 5.0))

    try:
        func = sp.sympify(func_str)
        plot_taylor_series(func, x0, n_terms, x_range)
    except sp.SympifyError:
        st.error('Invalid function. Please enter a valid mathematical expression.')

if __name__ == '__main__':
    main()
