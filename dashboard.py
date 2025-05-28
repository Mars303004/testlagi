import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")
st.title("XYZ Indicator")
st.caption("\U0001F4C5 December 2025")

# --------- Helper Functions ---------
def kpi_card(title, value, target, percent, delta=None, bar_color="green"):
    st.markdown(f"""
        <div style='background-color:#f9f9f9; padding:20px; border-radius:15px;'>
            <h5>{title}</h5>
            <h2>{value}</h2>
            {'<span style="color:green;">⬆ ' + delta + '</span><br>' if delta else ''}
            <div style='font-size:14px;'>Target: {target}</div>
            <progress value='{percent}' max='100' style='width:100%; height:10px;'></progress>
            <div style='font-size:12px;'>{percent}%</div>
        </div>
    """, unsafe_allow_html=True)

def circular_gauge(label, value, color):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': label},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': color}}
    ))
    fig.update_layout(height=200, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

def line_chart(title):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    values = [90, 85, 88, 95, 93, 87, 89, 92, 94, 90, 91, 88]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=values, mode='lines+markers'))
    fig.update_layout(title=title, height=200, margin=dict(t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

def bar_chart(title):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    values = [80, 85, 82, 88, 91, 89, 90, 93, 94, 95, 97, 98]
    fig = go.Figure([go.Bar(x=months, y=values)])
    fig.update_layout(title=title, height=200, margin=dict(t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

# --------- Row 1 ---------
col1, col2, col3, col4, col5 = st.columns([1.2,1.2,1.2,1,1.4])
with col1:
    kpi_card("Revenue", "$20M", "$100M", 20, "12%")
with col2:
    kpi_card("Expense", "$8.5M", "$50M", 17, "5%")
with col3:
    kpi_card("Productivity Index", "1.88", "2.93", 64, "15%")
with col4:
    kpi_card("Manpower Fulfillment", "102", "122", 67)
with col5:
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:15px;'>
        <h5>Recruitment Funnel</h5>
        <ul style='font-size:13px; line-height:1.8;'>
            <li>Qualified Pool: 100</li>
            <li>HC Interview: 70</li>
            <li>User Interview: 50</li>
            <li>Offering: 25</li>
            <li>Successful Hire: 20</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --------- Row 2 ---------
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    kpi_card("Active Customer", "153", "225", 68, "3")
with col2:
    circular_gauge("Churn Rate", 7, "green")
with col3:
    st.markdown("<h5>Product CSAT</h5><h2>⭐ 4.0</h2><div>Target: 4.45</div>", unsafe_allow_html=True)
with col4:
    circular_gauge("Product NPS", 70, "purple")
with col5:
    st.markdown("""
        <h5>Employee Competency</h5>
        <img src='https://quickchart.io/chart?c={type:bar,horizontal:true,data:{labels:["Dev","SA","BA","PM"],datasets:[{label:"Jr",data:[90,90,85,85]},{label:"Mid",data:[85,85,90,90]},{label:"Sr",data:[90,90,90,90]},{label:"Expert",data:[98,98,98,98]}]}}' width='100%'>
    """, unsafe_allow_html=True)

# --------- Row 3 ---------
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    circular_gauge("On Time Delivery", 92, "green")
with col2:
    circular_gauge("Defect Rate", 5, "red")
with col3:
    circular_gauge("SLA Achievement", 95, "green")
with col4:
    line_chart("Deployment Success Rate")
with col5:
    bar_chart("SIT Quality Index")
with col6:
    circular_gauge("Talent Turnover", 7, "green")
    st.markdown("<h2 style='text-align:center;'>100 employees</h2><p style='color:red; text-align:center;'>↓ 5%</p>", unsafe_allow_html=True)

st.markdown("<br><hr><center>Designed by AI prompt · Streamlit</center>", unsafe_allow_html=True)
