import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Set page config
st.set_page_config(
    page_title="XYZ Indicator Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk responsivitas dan alignment
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        max-width: 100%;
    }
    .main-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
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
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .small-metric-card {
        background: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .chart-container, .small-chart-container {
        background: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .chart-container h5, .small-chart-container h5 {
        margin: 0 0 5px 0;
        font-size: 0.8rem;
        color: #2c3e50;
    }
    @media (max-height: 800px) {
        .chart-container,
        .small-chart-container,
        .metric-card,
        .small-metric-card {
            height: 120px;
        }
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

# First row - Main metrics
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.2])
with col1:
    st.markdown("""
    <div class="metric-card" style="border-left-color: #27ae60;">
        <h4>Revenue</h4>
        <div style="font-size: 1.8rem; color: #27ae60;">$20M</div>
        <div style="color: #27ae60;">📈 12% From Last Month</div>
        <div style="color: #7f8c8d;">Target $100M</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card" style="border-left-color: #f1c40f;">
        <h4>Expense</h4>
        <div style="font-size: 1.8rem; color: #e67e22;">$8.5M</div>
        <div style="color: #e67e22;">📈 5% From Last Month</div>
        <div style="color: #7f8c8d;">Target $50M</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card" style="border-left-color: #16a085;">
        <h4>Productivity Index</h4>
        <div style="font-size: 1.8rem; color: #16a085;">1.88</div>
        <div style="color: #16a085;">📈 15% From Last Month</div>
        <div style="color: #7f8c8d;">Target 2.93</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card" style="border-left-color: #7f8c8d;">
        <h4>🔧 Manpower Fulfilment</h4>
        <div style="font-size: 1.8rem; color: #2c3e50;">102 of 122</div>
        <div style="color: #7f8c8d;">67%</div>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown('<div class="chart-container"><h5>🧑‍💼 Recruitment Funnel</h5>', unsafe_allow_html=True)
    funnel_fig = go.Figure(go.Funnel(
        y=["Qualified Pool", "HC Interview", "User Interview", "Offering", "Successful Hire"],
        x=[100, 70, 40, 25, 20],
        marker={"color": ["#3498db", "#9b59b6", "#e74c3c", "#f39c12", "#27ae60"]}
    ))
    funnel_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(funnel_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Second row - Performance metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="small-metric-card">
        <h5>👥 Number of Customer</h5>
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">153</div>
        <div style="color: #27ae60;">↗️ 3 From Last Month</div>
        <div style="color: #7f8c8d;">Target 225</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown('<div class="small-chart-container"><h5>Product Churn Rate</h5>', unsafe_allow_html=True)
    churn_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=7,
        number={'font': {'size: 18'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 20], 'tickfont': {'size': 8}},
            'bar': {'color': "#e74c3c"},
            'steps': [
                {'range': [0, 5], 'color': "#27ae60"},
                {'range': [5, 10], 'color': "#f39c12"},
                {'range': [10, 20], 'color': "#e74c3c"}
            ]
        }
    ))
    churn_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(churn_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="small-metric-card">
        <h5>Average Product CSAT</h5>
        <div style="font-size: 1.8rem; font-weight: bold; color: #2c3e50;">4.0</div>
        <div style="color: #f1c40f;">★★★★☆</div>
        <div style="color: #7f8c8d;">Target 4.45</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown('<div class="small-chart-container"><h5>Product NPS</h5>', unsafe_allow_html=True)
    nps_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=70,
        number={'font': {'size': 18}},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100], 'tickfont': {'size': 8}},
            'bar': {'color': "#9b59b6"},
            'steps': [
                {'range': [0, 50], 'color': "#ecf0f1"},
                {'range': [50, 100], 'color': "#d5dbdb"}
            ]
        }
    ))
    nps_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(nps_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Third row - Charts
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    st.markdown('<div class="chart-container"><h5>📊 Employee Competency Fulfillment</h5>', unsafe_allow_html=True)
    _, sit_data, comp_data = generate_sample_data()
    comp_df = pd.DataFrame(comp_data)
    comp_fig = go.Figure()
    colors = ['#f1c40f', '#27ae60', '#3498db', '#2c3e50']
    for i, cat in enumerate(['Jr', 'Mid', 'Sr', 'Expert']):
        comp_fig.add_trace(go.Bar(name=cat, y=comp_df['Role'], x=comp_df[cat], orientation='h',
                                  marker_color=colors[i], text=comp_df[cat], textposition='inside'))
    comp_fig.update_layout(barmode='stack', showlegend=True, legend=dict(orientation="h", y=1.02),
                           xaxis={'tickfont': {'size': 8}}, yaxis={'tickfont': {'size': 8}})
    comp_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(comp_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="small-chart-container"><h5>🚚 On Time Delivery</h5>', unsafe_allow_html=True)
    delivery_fig = go.Figure(go.Indicator(mode="gauge+number", value=92, number={'font': {'size': 16}},
                             gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#27ae60"}}))
    delivery_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(delivery_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="small-chart-container"><h5>⚠️ Defect Rate</h5>', unsafe_allow_html=True)
    defect_fig = go.Figure(go.Indicator(mode="gauge+number", value=5, number={'font': {'size': 16}},
                           gauge={'axis': {'range': [None, 15]}, 'bar': {'color': "#e74c3c"}}))
    defect_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(defect_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="small-chart-container"><h5>📋 SLA Achievement</h5>', unsafe_allow_html=True)
    sla_fig = go.Figure(go.Indicator(mode="gauge+number", value=95, number={'font': {'size': 16}},
                        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#27ae60"}}))
    sla_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(sla_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Bottom row - Final charts
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="chart-container"><h5>📈 Deployment Success Rate</h5>', unsafe_allow_html=True)
    dep_fig = go.Figure(go.Scatter(x=sit_data["Month"], y=sit_data["Quality Score"], mode='lines+markers'))
    dep_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0), xaxis={'tickfont': {'size': 8}})
    st.plotly_chart(dep_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="chart-container"><h5>📊 SIT Quality Index</h5>', unsafe_allow_html=True)
    sit_fig = go.Figure(go.Bar(x=sit_data["Month"], y=sit_data["Quality Score"], marker_color='#16a085'))
    sit_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0), xaxis={'tickfont': {'size': 8}})
    st.plotly_chart(sit_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="chart-container"><h5>🔄 Talent Turnover Rate</h5>', unsafe_allow_html=True)
    turnover_fig = go.Figure(go.Indicator(mode="gauge+number", value=7, number={'font': {'size': 16}}))
    turnover_fig.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(turnover_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align:center; color:#7f8c8d; padding:10px;'>© XYZ Indicator Dashboard - Business Intelligence Platform</div>", unsafe_allow_html=True)
