
import streamlit as st

import numpy as np
from bokeh.plotting import figure, show
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource

st.set_page_config(layout="wide")



def parabola(A0, B0, C0, x01, x02, cm2):
        x = np.linspace(-5, 5, 5000)
        y0 = A0*(x-x01)**2 + B0*(x-x02) + C0 

        source_0 = ColumnDataSource(data=dict(x=x, y=y0))

        p = figure(title='Common Tangents Finder', plot_width=800, plot_height=700, x_axis_label='x', y_axis_label='y', y_range=(-1, 0), x_range=(0, 1))
        p.line(x, y0,  line_color='blue', line_width=2, legend_label='Parabola 1')
        
        hover = HoverTool(tooltips=[('x', '$x'), ('y', '$y')], mode='mouse', point_policy='snap_to_data')
        p.add_tools(hover)
        p.legend.location = 'bottom_center'
        p.legend.click_policy = 'hide'
        p.legend.label_text_font_size = '15pt'
        p.title.align = 'center'

        cm2.bokeh_chart(p)


cm1, cm2 = st.columns(2)
c1, c2, c3, c4, c5 = cm1.columns(5)

A0 = c1.slider("A0", min_value=-25.0, max_value=25.0, value=15.0, step=0.0001)
B0 = c2.slider("B0", min_value=-5.0, max_value=5.0, value=0.0, step=0.0001)
C0 = c3.slider("C0", min_value=-5.0, max_value=5.0, value=-0.602, step=0.0001)
x01 = c4.slider("x01", min_value=-1.0, max_value=1.0, value=0.667, step=0.0001)
x02 = c5.slider("x02", min_value=-1.0, max_value=1.0, value=0.667, step=0.0001)

parabola(A0,B0,C0,x01,x02, cm2)
