
import streamlit as st

import numpy as np
from bokeh.plotting import figure

from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Label, Title

import sympy as sym
from sympy import symbols, I, expand, Poly, simplify, re, im
st.set_page_config(layout="wide")

def Parabola(A0, B0, C0, x01, x02, A1, B1, C1, x11, x12, A2, B2, C2, x21, x22, x_coords, y_coords, column_no):

    x_coords =  list(map(float, x_coords))
    y_coords =  list(map(float, y_coords))
    x = np.linspace(-5, 5, 5000)
    y0 = A0*(x-x01)**2 + B0*(x-x02) + C0 
    y1 = A1*(x-x11)**2 + B1*(x-x12) + C1 
    y2 = A2*(x-x21)**2 + B2*(x-x22) + C2

    source_0 = ColumnDataSource(data=dict(x=x, y=y0))
    source_1 = ColumnDataSource(data=dict(x=x, y=y1))
    source_2 = ColumnDataSource(data=dict(x=x, y=y2))

    p = figure(title='Common Tangents Finder', plot_width=800, plot_height=700, x_axis_label='x', y_axis_label='y', y_range=(1.1*np.min(y_coords), 0), x_range=(0, 1))

    p.line(x, y0,  line_color='blue', line_width=2, legend_label='Parabola 1')
    p.line(x, y1,  line_color='red',  line_width=2,  legend_label='Parabola 2')
    p.line(x, y2,  line_color='green',line_width=2, legend_label='Parabola 3')


    palette = ['red', 'blue', 'green',]  # Adjust the number if needed
    for i in range(len(x_coords) - 1):
        if i % 2 == 0:
            color = palette[i % len(palette)]  # Cycle through the color palette

            p.segment(x_coords[i], y_coords[i], x_coords[i+1], y_coords[i+1], line_width=3, line_color=color, line_dash='dotted', legend_label =f"")
            p.circle(x_coords[i], y_coords[i], size=10, color=color, legend_label =f"")  # Match the circle color with the line color
            p.circle(x_coords[i+1], y_coords[i+1], size=10, color=color, legend_label =f"")  # Match the circle color with the line color


    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    for i in range(len(x_coords)):
        label = Label(x=x_coords[i], y=y_coords[i], text=f"{labels[i]}", text_font_size='22pt', text_color='black', x_offset=10, y_offset=-10, )
        p.add_layout(label)

    hover = HoverTool(tooltips=[('x', '$x'), ('y', '$y')], mode='mouse', point_policy='snap_to_data')

    p.add_tools(hover)
    p.add_layout(p.legend[0], 'right')
    p.legend.click_policy = 'hide'
    p.legend.label_text_font_size = '12pt'
    p.legend.location = 'top'
    p.title.align = 'center'
    p.title.text_font_size = "30pt"
    p.add_layout(p.title, 'above', )
    p.grid.grid_line_color = 'black'
    p.add_layout(Title(text="Parabola of form: A(x-xi)^2 + B(x-xi) + C",  text_font_size="20pt",  text_font_style="italic"), 'above')


    p.xaxis.axis_label_text_font_size = '24pt'
    p.xaxis.major_label_text_font_size = '22pt'

    p.yaxis.axis_label_text_font_size = '24pt'
    p.yaxis.major_label_text_font_size = '22pt'
    
    column_no.bokeh_chart(p)

cm1, cm2 = st.columns(2)  # main 2 columns column main 1 and column main 2

c1, c2, c3, c4, c5 = cm1.columns(5)
# c1, c2, c3, c4, c5 = st.columns(5)
A0 = c1.slider("A0", min_value=-50.0, max_value=50.0, value=15.0, step=0.0001)
B0 = c2.slider("B0", min_value=-5.0, max_value=5.0, value=0.0, step=0.0001)
C0 = c3.slider("C0", min_value=-5.0, max_value=5.0, value=-0.602, step=0.0001)
x01 = c4.slider("x01", min_value=-1.0, max_value=1.0, value=0.667, step=0.0001)
x02 = c5.slider("x02", min_value=-1.0, max_value=1.0, value=0.667, step=0.0001)

A1 = c1.slider("A1", min_value=-50.0, max_value=50.0, value=0.7069, step=0.0001)
B1 = c2.slider("B1", min_value=-5.0, max_value=5.0, value=0.1721, step=0.0001)
C1 = c3.slider("C1", min_value=-5.0, max_value=5.0, value=-0.7108, step=0.0001)
x11 = c4.slider("x11", min_value=-1.0, max_value=1.0, value=0.892, step=0.0001)
x12 = c5.slider("x12", min_value=-1.0, max_value=1.0, value=-0.2, step=0.0001)

A2 = c1.slider("A2", min_value=-50.0, max_value=50.0, value=4.1335, step=0.0001)
B2 = c2.slider("B2", min_value=-5.0, max_value=5.0, value=0.0123, step=0.0001)
C2 = c3.slider("C2", min_value=-5.0, max_value=5.0, value=-0.31477, step=0.0001)
x21 = c4.slider("x21", min_value=-1.0, max_value=1.0, value=0.0616, step=0.0001)
x22 = c5.slider("x22", min_value=-1.0, max_value=1.0, value=0.2, step=0.0001)




x, y, m, c  = symbols('x, y, m, c') 
L = m * x + c

P0 = expand(A0 *(x-x01 )**2 + B0 *(x-x02 ) + C0 )  # First Parabola in Ax^2 + Bx + C form
P1 = expand(A1 *(x-x11 )**2 + B1 *(x-x12 ) + C1 )  # Second Parabola  in Ax^2 + Bx + C form
P2 = expand(A2 *(x-x21 )**2 + B2 *(x-x22 ) + C2 )  # Third Parabola  in Ax^2 + Bx + C form

eq0 = sym.Eq(y, P0)  #eq0 ==> Equation 0 i.e. First Parabola in format y = Ax^2 + Bx + C
eq1 = sym.Eq(y, P1)  #eq1 ==> Equation 1 i.e. Second Parabola in format y = Ax^2 + Bx + C
eq2 = sym.Eq(y, P2)  #eq2 ==> Equation 2 i.e. Third Parabola in format y = Ax^2 + Bx + C

coeffs0 = Poly(P0, x).coeffs()  # Coefficients of First Parabola P0 
coeffs1 = Poly(P1, x).coeffs()  # Coefficients of Second Parabola P1  
coeffs2 = Poly(P2, x).coeffs()  # Coefficients of Third Parabola P2  

a0, b0, c0 =  coeffs0[0], coeffs0[1], coeffs0[2]   # First Parabola's coefficients a0 ==> A, b0 ==> B, c0 ==>c
a1, b1, c1 =  coeffs1[0], coeffs1[1], coeffs1[2]
a2, b2, c2 =  coeffs2[0], coeffs2[1], coeffs2[2]



## This function returns the equation of discriminant i.e. beta^2 - 4 * alpha * gamma as in above

def calculate(A,B,C):
    m, c = symbols('m, c') 
    alpha = A
    beta  = B - m
    gamma = C - c
    discriminant = beta**2 - 4* alpha * gamma
    equation = sym.Eq(discriminant,0)
    return equation

# First Calculation in the code 
# Tangent Between First and Second Parabola (P0 & P1)

D0 = calculate(a0,b0,c0)   ## Discriminant from 1st Parabola
D1 = calculate(a1,b1,c1)   ## Discriminant from 2st Parabola
result = sym.solve([D0,D1],(m,c))

## Here 1st Calculation in this code is done between First Parabola P0 & Second Parabola P1

m00, m01 =  result[0][0], result[1][0]   ## m01 == > '1' --> Second Slope of '0' First Calculation of slope in this code 
c00, c01 = result[0][1], result[1][1]

## 2 sets of common tangents lines equations are
L00 = m00 * x + c00
L01 = m01 * x + c01





eq_subs_00  = sym.Eq(P0-L00,0)    ## Equation after substituion of Tangent 1 in Parabola 1 as shown above
eq_subs_01  = sym.Eq(P0-L01,0)    ## Equation after substituion of Tangent 2 in Parabola 1

x_eq_01_0 = sym.solve([eq_subs_00],(x))   ## x_eq i.e. x-Point where Tangent 1 meet Parabola 1 
x_eq_01_0 = sym.re(x_eq_01_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_01_0 = m00 *x_eq_01_0 + c00              ## y_eq i.e. y-Point where Tangent 1 meet Parabola 1

x_eq_01_1 = sym.solve([eq_subs_01],(x))   ## x_eq i.e. x-Point where Tangent 2 meet Parabola 1 
x_eq_01_1 = sym.re(x_eq_01_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_01_1 = m01 *x_eq_01_1 + c01               ## y_eq i.e. y-Point where Tangent 2 meet Parabola 1

eq_subs_10  = sym.Eq(P1-L00,0)    ## Equation after substituion of Tangent 1 in Parabola 2 as shown above
eq_subs_11  = sym.Eq(P1-L01,0)    ## Equation after substituion of Tangent 2 in Parabola 2

x_eq_10_0 = sym.solve([eq_subs_10],(x))   ## x_eq i.e. x-Point where Tangent 1 meet Parabola 2 
x_eq_10_0 = sym.re(x_eq_10_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_10_0 = m00 *x_eq_10_0 + c00              ## y_eq i.e. y-Point where Tangent 1 meet Parabola 2

x_eq_10_1 = sym.solve([eq_subs_11],(x))   ## x_eq i.e. x-Point where Tangent 2 meet Parabola 2
x_eq_10_1 = sym.re(x_eq_10_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_10_1 = m01 *x_eq_10_1 + c01              ## y_eq i.e. y-Point where Tangent 2 meet Parabola 2



# Second Calculation in the code
# Tangent Between Second and Third Parabola (P1 & P2)

D1 = calculate(a1,b1,c1)   ## Discriminant from 2nd Parabola
D2 = calculate(a2,b2,c2)   ## Discriminant from 3rd Parabola
result = sym.solve([D1,D2],(m,c))

m10, m11 =  result[0][0], result[1][0]
c10, c11 = result[0][1], result[1][1]

## 2 sets of common tangents lines equations are
L10 = m10 * x + c10
L11 = m11 * x + c11

eq_subs_10  = sym.Eq(P1-L10,0)    ## Equation after substituion of Tangent 1 in 2nd Parabola 
eq_subs_11  = sym.Eq(P1-L11,0)    ## Equation after substituion of Tangent 2 in 2nd Parabola

x_eq_12_0 = sym.solve([eq_subs_10],(x))   ## x_eq i.e. x-Point where Tangent 1 meet 2nd Parabola
x_eq_12_0 = sym.re(x_eq_12_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_12_0 = m10 *x_eq_12_0 + c10              ## y_eq i.e. y-Point where Tangent 1 meet 2nd Parabola
y_eq_12_0 = sym.re(y_eq_12_0)               ## Taking real part if complex number arises in case 

x_eq_12_1 = sym.solve([eq_subs_11],(x))   ## x_eq i.e. x-Point where Tangent 2 meet 2nd Parabola
x_eq_12_1 = sym.re(x_eq_12_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_12_1 = m11 *x_eq_12_1 + c11              ## y_eq i.e. y-Point where Tangent 2 meet 2nd Parabola
y_eq_12_1 = sym.re(y_eq_12_1) 

eq_subs_20  = sym.Eq(P2-L10,0)    ## Equation after substituion of Tangent 1 in 3rd Parabola as shown above
eq_subs_21  = sym.Eq(P2-L11,0)    ## Equation after substituion of Tangent 2 in 3rd Parabola

x_eq_21_0 = sym.solve([eq_subs_20],(x))   ## x_eq i.e. x-Point where Tangent 1 meet 3rd Parabola
x_eq_21_0 = sym.re(x_eq_21_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_21_0 = m10 *x_eq_21_0 + c10              ## y_eq i.e. y-Point where Tangent 1 meet 3rd Parabola
y_eq_21_0 = sym.re(y_eq_21_0)               ## Taking real part if complex number arises in case 

x_eq_21_1 = sym.solve([eq_subs_21],(x))   ## x_eq i.e. x-Point where Tangent 2 meet 3rd Parabola
x_eq_21_1 = sym.re(x_eq_21_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_21_1 = m11 *x_eq_21_1 + c11              ## y_eq i.e. y-Point where Tangent 2 meet 3rd Parabola
y_eq_21_1 = sym.re(y_eq_21_1)                ## Taking real part if complex number arises in case 




# Third Calculation in the code
# Tangent Between Third and First Parabola (P2 & P0)

D2 = calculate(a2,b2,c2)   ## Discriminant from 3rd Parabola
D0 = calculate(a0,b0,c0)   ## Discriminant from 1st Parabola

result = sym.solve([D2,D0],(m,c))

m20, m21 =  result[0][0], result[1][0]
c20, c21 = result[0][1], result[1][1]

## 2 sets of common tangents lines equations are
L20 = m20 * x + c20
L21 = m21 * x + c21

## 2 set of x_eq & y_eq points at 3rd Parabola P2

eq_subs_20  = sym.Eq(P2-L20,0)    ## Equation after substituion of Tangent 1 in 3rd Parabola as shown above
eq_subs_21  = sym.Eq(P2-L21,0)    ## Equation after substituion of Tangent 2 in 3rd Parabola

x_eq_20_0 = sym.solve([eq_subs_20],(x))   ## x_eq i.e. x-Point where Tangent 1 meet 3rd Parabola
x_eq_20_0 = sym.re(x_eq_20_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_20_0 = m20 *x_eq_20_0 + c20              ## y_eq i.e. y-Point where Tangent 1 meet 3rd Parabola
y_eq_20_0 = sym.re(y_eq_20_0)               ## Taking real part if complex number arises in case 

x_eq_20_1 = sym.solve([eq_subs_21],(x))   ## x_eq i.e. x-Point where Tangent 2 meet 3rd Parabola
x_eq_20_1 = sym.re(x_eq_20_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_20_1 = m21 *x_eq_20_1 + c21              ## y_eq i.e. y-Point where Tangent 2 meet 3rd Parabola
y_eq_20_1 = sym.re(y_eq_20_1)               ## Taking real part if complex number arises in case 

## 2 set of x_eq & y_eq points at 1st Parabola P0

eq_subs_00  = sym.Eq(P0-L20,0)    ## Equation after substituion of Tangent 1 in 3rd Parabola as shown above
eq_subs_01  = sym.Eq(P0-L21,0)    ## Equation after substituion of Tangent 2 in 3rd Parabola

x_eq_02_0 = sym.solve([eq_subs_00],(x))   ## x_eq i.e. x-Point where Tangent 1 meet 3rd Parabola
x_eq_02_0 = sym.re(x_eq_02_0[0][0])         ## Taking real part if complex number arises in case 
y_eq_02_0 = m20 *x_eq_02_0 + c20              ## y_eq i.e. y-Point where Tangent 1 meet 3rd Parabola
y_eq_02_0 = sym.re(y_eq_02_0)               ## Taking real part if complex number arises in case 

x_eq_02_1 = sym.solve([eq_subs_01],(x))   ## x_eq i.e. x-Point where Tangent 2 meet 3rd Parabola
x_eq_02_1 = sym.re(x_eq_02_1[0][0])         ## Taking real part if complex number arises in case 
y_eq_02_1 = m21 *x_eq_02_1 + c21              ## y_eq i.e. y-Point where Tangent 2 meet 3rd Parabola
y_eq_02_1 = sym.re(y_eq_02_1)               ## Taking real part if complex number arises in case 




x_coords = [x_eq_01_0, x_eq_10_0, x_eq_01_1, x_eq_10_1, x_eq_12_0, x_eq_21_0,
            x_eq_12_1, x_eq_21_1, x_eq_20_0, x_eq_02_0, x_eq_20_1, x_eq_02_1]

y_coords = [y_eq_01_0, y_eq_10_0 ,y_eq_01_1, y_eq_10_1 ,y_eq_12_0, y_eq_21_0,
            y_eq_12_1, y_eq_21_1 ,y_eq_20_0, y_eq_02_0 ,y_eq_20_1, y_eq_02_1]


imaginary_count = 0
for i, val in enumerate(y_coords):
    if im(val) !=0:
        y_coords =  list(map(re, y_coords))
        imaginary_count += 1
for i, val in enumerate(x_coords):
    if im(val) !=0:
        x_coords =  list(map(re, x_coords))
        imaginary_count += 1

if imaginary_count>0:
    cm1.divider()
    cm1.title("Some point of tangency is detected in Complex Plane. So, taking  only real value.")


Parabola(A0,B0,C0,x01,x02,A1,B1,C1,x11,x12,A2,B2,C2,x21,x22, x_coords, y_coords, cm2)

cm1.divider()
cm1.write("EQUILIBRIUM POINTS:")
points = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
c1, c2, c3, c4, c5, c6,  = cm1.columns(6)
for i in range(len(x_coords)):
    if i<2: c1.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
    elif i<4 : c2.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
    elif i<6 : c3.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
    elif i<8 : c4.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
    elif i<10 : c5.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
    elif i<12 : c6.write(f'{points[i]}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')


####### Mathematical Explanation 
with st.expander('Mathematical Explanation'):
    cm1, cm2 = st.columns(2)
    cm1.title("Tangent Line and Parabola Intersection")
    cm1.markdown(" At the point of intersection between a line and a parabola, we can replace 'y' of the parabola with 'y' of the line as:")
    cm1.markdown(" $y ==> mx+c = Ax^2+Bx+C$")
    cm1.markdown("$y ==> Ax^2 + x(B-m) + (C-c)$")
    cm1.markdown("This equation has 2 roots for x:")
    cm1.markdown(" $x = \\frac{-\\beta \\pm \\sqrt{\\beta ^2 - 4 \\alpha \\gamma}}{2\\alpha}$")
    cm1.markdown("For a line to touch the parabola at only one point, i.e., to be tangent to the parabola:")
    cm1.markdown("The substituted equation (line to parabola) should have exactly one solution, which makes the discriminant zero, i.e.:")
    cm1.markdown(" $\\beta^2 - 4\\alpha \\gamma = 0$")
    cm1.markdown("In our case:")
    cm1.markdown(" $\\alpha = A$")
    cm1.markdown(" $\\beta = (B-m)$")
    cm1.markdown(" $\\gamma = (C-c)$")
    cm1.markdown("So,")
    cm1.markdown(" $\\beta^2 - 4\\alpha \\gamma$ == $ (B-m)^2 - 4A(C-c) = 0$")


    cm2.title("Tangent and Curve Intersection")
    cm2.markdown("At the point of intersection between a tangent and a curve, the equation of the tangent must satisfy the equation of the curve.")
    cm2.markdown("$y = mx + c$ and $y = Ax^2+Bx+C$ should be equal:")
    cm2.markdown("$y_{eq} ==> mx_{eq} + c = Ax_{eq}^2 + Bx_{eq} + C$")
    cm2.markdown("$y_{eq} ==> Ax_{eq}^2 + x_{eq}(B-m) + (C-c) = 0$")
    cm2.markdown("Now $x_{eq}$ has 2 roots, i.e.:")
    cm2.markdown("$x_{eq} = \\frac{B \\mp \\sqrt{B^2-4AC}}{2A}$")
    cm2.markdown("Similarly, by substituting $x_{eq}$ in $y = mx_{eq} + c$, we get:")
    cm2.markdown("$y_{eq} = m \\frac{B \\mp \\sqrt{B^2-4AC}}{2A} + c$")
    cm2.markdown("Then we get 2 sets of ($x_{eq}$, $y_{eq}$) points for 2 common tangents.")
    cm2.markdown("X equilibrium points notation: x_ab_c")
    cm2.markdown("a ==> X eq at Parabola")
    cm2.markdown("b ==> Tangent to Parabola")
    cm2.markdown("c ==> 1st or 2nd Point in Parabola a")
    cm2.markdown("E.g., x_20_1 means the 1st equilibrium point on parabola 2 for a tangent going from Parabola 2 to Parabola 0")