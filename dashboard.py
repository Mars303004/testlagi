import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="XYZ Indicator Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
    
    .main-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        margin-bottom: 15px;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin: 0;
    }
    
    .metric-card {
        background: white;
        padding: 12px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid;
        margin-bottom: 10px;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .metric-card.revenue { border-left-color: #27ae60; }
    .metric-card.expense { border-left-color: #f1c40f; }
    .metric-card.productivity { border-left-color: #16a085; }
    .metric-card.manpower { border-left-color: #7f8c8d; }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 5px 0;
        line-height: 1;
    }
    
    .metric-change {
        color: #27ae60;
        font-size: 0.75rem;
        margin-bottom: 5px;
    }
    
    .metric-target {
        color: #7f8c8d;
        font-size: 0.7rem;
        margin-bottom: 8px;
    }
    
    .progress-bar {
        background-color: #ecf0f1;
        border-radius: 8px;
        height: 6px;
        overflow: hidden;
    }
    
    .progress-bar-fill {
        height: 100%;
        border-radius: 8px;
        transition: width 0.3s ease;
    }
    
    .progress-green { background-color: #27ae60; }
    .progress-yellow { background-color: #f1c40f; }
    .progress-teal { background-color: #16a085; }
    .progress-gray { background-color: #7f8c8d; }
    
    .small-metric-card {
        background: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        height: 90px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .stars {
        color: #f1c40f;
        font-size: 1rem;
        margin: 2px 0;
    }
    
    .chart-container {
        background: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        height: 140px;
        display: flex;
        flex-direction: column;
    }
    
    .chart-container h5 {
        margin: 0 0 5px 0;
        font-size: 0.8rem;
        color: #2c3e50;
    }
    
    .small-chart-container {
        background: white;
        padding: 8px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        height: 120px;
        display: flex;
        flex-direction: column;
    }
    
    .small-chart-container h5 {
        margin: 0 0 3px 0;
        font-size: 0.75rem;
        color: #2c3e50;
    }
    
    /* Responsive font sizes */
    @media (max-width: 1200px) {
        .main-title { font-size: 2rem; }
        .metric-value { font-size: 1.5rem; }
    }
    
    @media (max-width: 768px) {
        .main-title { font-size: 1.5rem; }
        .metric-value { font-size: 1.2rem; }
        .metric-card { height: 120px; }
        .chart-container { height: 120px; }
    }
</style>
""", unsafe_allow_html=True)

# Generate sample data
@st.cache_data
def generate_sample_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    deployment_success = [85, 87, 89, 91, 88, 92, 94, 96, 93, 95, 97, 98]
    
    sit_quality_data = {
        'Month': months,
        'Quality Score': [78, 82, 85, 88, 91, 89, 93, 96, 94, 97, 95, 98]
    }
    
    competency_data = {
        'Role': ['Dev', 'QA', 'SA', 'BA', 'PM'],
        'Jr': [15, 20, 25, 30, 20],
        'Mid': [35, 30, 25, 20, 25],
        'Sr': [30, 25, 30, 25, 30],
        'Expert': [20, 25, 20, 25, 25]
    }
    
    return deployment_success, sit_quality_data, competency_data

# Header
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<h1 class="main-title">XYZ Indicator</h1>', unsafe_allow_html=True)
with col2:
    selected_month = st.selectbox("", ["December 2025", "November 2025", "October 2025"], key="month_selector")

# First row - Main metrics (4 cards + recruitment funnel)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.2])

with col1:
    st.markdown("""
    <div class="metric-card revenue">
        <div>
            <h4 style="margin: 0; font-size: 0.8rem;">Revenue</h4>
            <div class="metric-value" style="color: #27ae60;">$20M</div>
            <div class="metric-change">📈 12% From Last Month</div>
            <div class="metric-target">Target $100M</div>
        </div>
        <div>
            <div class="progress-bar">
                <div class="progress-bar-fill progress-green" style="width: 20%;"></div>
            </div>
            <div style="font-size: 0.7rem; color: #7f8c8d; margin-top: 2px;">20%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card expense">
        <div>
            <h4 style="margin: 0; font-size: 0.8rem;">Expense</h4>
            <div class="metric-value" style="color: #e67e22;">$8.5M</div>
            <div class="metric-change">📈 5% From Last Month</div>
            <div class="metric-target">Target $50M</div>
        </div>
        <div>
            <div class="progress-bar">
                <div class="progress-bar-fill progress-yellow" style="width: 17%;"></div>
            </div>
            <div style="font-size: 0.7rem; color: #7f8c8d; margin-top: 2px;">17%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card productivity">
        <div>
            <h4 style="margin: 0; font-size: 0.8rem;">Productivity Index</h4>
            <div class="metric-value" style="color: #16a085;">1.88</div>
            <div class="metric-change">📈 15% From Last Month</div>
            <div class="metric-target">Target 2.93</div>
        </div>
        <div>
            <div class="progress-bar">
                <div class="progress-bar-fill progress-teal" style="width: 64%;"></div>
            </div>
            <div style="font-size: 0.7rem; color: #7f8c8d; margin-top: 2px;">64%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card manpower">
        <div>
            <h4 style="margin: 0; font-size: 0.8rem;">🔧 Manpower Fulfilment</h4>
            <div class="metric-value" style="color: #2c3e50;">102</div>
            <div style="color: #7f8c8d; font-size: 0.9rem;">of 122</div>
        </div>
        <div>
            <div class="progress-bar">
                <div class="progress-bar-fill progress-gray" style="width: 67%;"></div>
            </div>
            <div style="font-size: 0.7rem; color: #7f8c8d; margin-top: 2px;">67%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown('<div class="chart-container"><h5>🧑‍💼 Recruitment Funnel</h5>', unsafe_allow_html=True)
    funnel_fig = go.Figure(go.Funnel(
        y = ["Qualified Pool", "HC Interview", "User Interview", "Offering", "Successful Hire"],
        x = [100, 70, 40, 25, 20],
        textinfo = "value+percent initial",
        textfont = {"size": 10},
        marker = {"color": ["#3498db", "#9b59b6", "#e74c3c", "#f39c12", "#27ae60"]}
    ))
    funnel_fig.update_layout(height=120, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(funnel_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Second row - Performance metrics (4 small cards)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="small-metric-card">
        <h5 style="margin: 0; font-size: 0.75rem;">👥 Number of Customer</h5>
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50; margin: 5px 0;">153</div>
        <div style="color: #27ae60; font-size: 0.7rem;">↗️ 3 From Last Month</div>
        <div style="color: #7f8c8d; font-size: 0.65rem;">Target 225</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="small-chart-container"><h5>Product Churn Rate</h5>', unsafe_allow_html=True)
    churn_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 7,
        number = {'font': {'size': 20}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 20], 'tickfont': {'size': 8}},
            'bar': {'color': "#e74c3c"},
            'steps': [
                {'range': [0, 5], 'color': "#27ae60"},
                {'range': [5, 10], 'color': "#f39c12"},
                {'range': [10, 20], 'color': "#e74c3c"}
            ]
        }
    ))
    churn_fig.update_layout(height=85, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(churn_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="small-metric-card">
        <h5 style="margin: 0; font-size: 0.75rem;">Average Product CSAT</h5>
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50; margin: 5px 0;">4.0</div>
        <div class="stars">★★★★☆</div>
        <div style="color: #7f8c8d; font-size: 0.65rem;">Target 4.45</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown('<div class="small-chart-container"><h5>Product NPS</h5>', unsafe_allow_html=True)
    nps_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 70,
        number = {'font': {'size': 20}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 100], 'tickfont': {'size': 8}},
            'bar': {'color': "#9b59b6"},
            'steps': [
                {'range': [0, 50], 'color': "#ecf0f1"},
                {'range': [50, 100], 'color': "#d5dbdb"}
            ]
        }
    ))
    nps_fig.update_layout(height=85, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(nps_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Third row - Employee Competency + Bottom metrics
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    st.markdown('<div class="chart-container" style="height: 160px;"><h5>📊 Employee Competency Fulfillment</h5>', unsafe_allow_html=True)
    deployment_success, sit_quality_data, competency_data = generate_sample_data()
    
    competency_df = pd.DataFrame(competency_data)
    competency_fig = go.Figure()
    
    colors = ['#f1c40f', '#27ae60', '#3498db', '#2c3e50']
    categories = ['Jr', 'Mid', 'Sr', 'Expert']
    
    for i, cat in enumerate(categories):
        competency_fig.add_trace(go.Bar(
            name=cat,
            y=competency_df['Role'],
            x=competency_df[cat],
            orientation='h',
            marker_color=colors[i],
            text=competency_df[cat],
            textposition='inside',
            textfont={'size': 10}
        ))
    
    competency_fig.update_layout(
        barmode='stack',
        xaxis_title="",
        yaxis_title="",
        height=140,
        margin=dict(l=0,r=0,t=0,b=0),
        legend=dict(orientation="h", yanchor="top", y=1, xanchor="center", x=0.5, font={'size': 8}),
        showlegend=True,
        xaxis={'tickfont': {'size': 8}},
        yaxis={'tickfont': {'size': 8}}
    )
    
    st.plotly_chart(competency_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="small-chart-container" style="height: 160px;"><h5>🚚 On Time Product Delivery Rate</h5>', unsafe_allow_html=True)
    delivery_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 92,
        number = {'font': {'size': 18}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 100], 'tickfont': {'size': 8}},
            'bar': {'color': "#27ae60"},
            'steps': [
                {'range': [0, 70], 'color': "#ecf0f1"},
                {'range': [70, 100], 'color': "#d5dbdb"}
            ]
        }
    ))
    delivery_fig.update_layout(height=120, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(delivery_fig, use_container_width=True)
    st.markdown("<div style='text-align: center; color: #7f8c8d; font-size: 0.65rem;'>Last Month 91%</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="small-chart-container" style="height: 160px;"><h5>⚠️ Defect Rate</h5>', unsafe_allow_html=True)
    defect_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 5,
        number = {'font': {'size': 18}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 15], 'tickfont': {'size': 8}},
            'bar': {'color': "#e74c3c"},
            'steps': [
                {'range': [0, 3], 'color': "#27ae60"},
                {'range': [3, 8], 'color': "#f39c12"},
                {'range': [8, 15], 'color': "#e74c3c"}
            ]
        }
    ))
    defect_fig.update_layout(height=120, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(defect_fig, use_container_width=True)
    st.markdown("<div style='text-align: center; color: #7f8c8d; font-size: 0.65rem;'>Last Month 7% | Target= 0%</div></div>", unsafe_allow_html=True)

with col4:
    st.markdown('<div class="small-chart-container" style="height: 160px;"><h5>📋 SLA Achievement</h5>', unsafe_allow_html=True)
    sla_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 95,
        number = {'font': {'size': 18}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 100], 'tickfont': {'size': 8}},
            'bar': {'color': "#27ae60"},
            'steps': [
                {'range': [0, 80], 'color': "#ecf0f1"},
                {'range': [80, 100], 'color': "#d5dbdb"}
            ]
        }
    ))
    sla_fig.update_layout(height=120, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(sla_fig, use_container_width=True)
    st.markdown("<div style='text-align: center; color: #7f8c8d; font-size: 0.65rem;'>Last Month 95%</div></div>", unsafe_allow_html=True)

# Bottom row - Three charts
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="chart-container" style="height: 160px;"><h5>📈 Deployment Success Rate</h5>', unsafe_allow_html=True)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    deployment_fig = go.Figure(go.Scatter(
        x=months,
        y=deployment_success,
        mode='lines+markers',
        line=dict(color='#3498db', width=2),
        marker=dict(size=4)
    ))
    deployment_fig.update_layout(
        height=135,
        xaxis_title="",
        yaxis_title="",
        yaxis=dict(range=[80, 100], tickfont={'size': 8}),
        xaxis={'tickfont': {'size': 8}},
        margin=dict(l=0,r=0,t=0,b=0)
    )
    st.plotly_chart(deployment_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container" style="height: 160px;"><h5>📊 SIT Quality Index</h5>', unsafe_allow_html=True)
    sit_df = pd.DataFrame(sit_quality_data)
    sit_fig = go.Figure(go.Bar(
        x=sit_df['Month'],
        y=sit_df['Quality Score'],
        marker_color='#16a085'
    ))
    sit_fig.update_layout(
        height=135,
        xaxis_title="",
        yaxis_title="",
        xaxis={'tickfont': {'size': 8}},
        yaxis={'tickfont': {'size': 8}},
        margin=dict(l=0,r=0,t=0,b=0)
    )
    st.plotly_chart(sit_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="chart-container" style="height: 160px;"><h5>🔄 Talent Turnover Rate</h5>', unsafe_allow_html=True)
    turnover_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 7,
        number = {'font': {'size': 18}},
        title = {'text': "100 employees", 'font': {'size': 10}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 20], 'tickfont': {'size': 8}},
            'bar': {'color': "#e74c3c"},
            'steps': [
                {'range': [0, 5], 'color': "#27ae60"},
                {'range': [5, 10], 'color': "#f39c12"},
                {'range': [10, 20], 'color': "#e74c3c"}
            ]
        }
    ))
    turnover_fig.update_layout(height=115, margin=dict(l=0,r=0,t=15,b=0))
    st.plotly_chart(turnover_fig, use_container_width=True)
    st.markdown("<div style='text-align: center; color: #27ae60; font-size: 0.65rem;'>📉 5% From Last Month</div></div>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; padding: 10px; font-size: 0.8rem;'>XYZ Indicator Dashboard - Business Intelligence Platform</div>",
    unsafe_allow_html=True
)
