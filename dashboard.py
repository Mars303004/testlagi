import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Simulasi data
data = {
    "Revenue": {"value": 20_000_000, "target": 100_000_000, "change": 12},
    "Expense": {"value": 8_500_000, "target": 50_000_000, "change": 5},
    "Productivity Index": {"value": 1.88, "target": 2.93, "change": 15},
    "Manpower Fulfillment": {"value": 102, "target": 122},
    "Number Active Customer": {"value": 153, "target": 225, "change": 3},
    "Product Churn Rate": {"value": 7, "target": 0, "change": None},
    "Average Product CSAT": {"value": 4.0, "target": 4.45, "change": None},
    "Product NPS": {"value": 70, "target": 90, "change": None},
    "On Time Product Delivery Rate": {"value": 92, "target": None, "change": None},
    "Defect Rate": {"value": 5, "target": 0, "change": None},
    "SLA Achievement": {"value": 95, "target": None, "change": None},
    "Deployment Success Rate": {"value": [80, 82, 81, 83, 84, 85, 86, 85, 84, 83, 82, 81], "target": None, "change": None},
    "Talent Turnover Rate": {"value": 7, "target": None, "change": 5},
}

# Fungsi untuk membuat KPI Card
def kpi_card(title, value, target, change, icon=None):
    col1, col2 = st.columns([1, 4])
    with col1:
        if icon:
            st.image(icon, width=30)
    with col2:
        st.metric(
            label=title,
            value=f"{value}%",
            delta=f"{change}%" if change else None,
            delta_color="inverse" if change and change > 0 else "off"
        )
        if target:
            st.write(f"Target: {target}%")
        st.progress(value / 100)

# Header
st.title("XYZ Indicator")
st.date_input("Select Month", key="selected_month")

# Row 1: Revenue, Expense, Productivity Index, Manpower Fulfillment
col1, col2, col3, col4 = st.columns(4)
with col1:
    kpi_card("Revenue", data["Revenue"]["value"], data["Revenue"]["target"], data["Revenue"]["change"], icon="💰")
with col2:
    kpi_card("Expense", data["Expense"]["value"], data["Expense"]["target"], data["Expense"]["change"], icon="💸")
with col3:
    kpi_card("Productivity Index", data["Productivity Index"]["value"], data["Productivity Index"]["target"], data["Productivity Index"]["change"], icon="📈")
with col4:
    st.metric(label="Manpower Fulfillment", value=f"{data['Manpower Fulfillment']['value']} of {data['Manpower Fulfillment']['target']}")
    # Funnel Chart
    labels = ['Qualified Pool', 'HC Interview', 'User Interview', 'Offering', 'Successful Hire']
    values = [100, 70, 40, 25, 20]
    colors = ['#FF6B6B', '#FFD166', '#1E8449', '#00BFFF', '#8E44AD']
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Row 2: Number Active Customer, Product Churn Rate, Average Product CSAT, Product NPS
col1, col2, col3, col4 = st.columns(4)
with col1:
    kpi_card("Number Active Customer", data["Number Active Customer"]["value"], data["Number Active Customer"]["target"], data["Number Active Customer"]["change"], icon="👥")
with col2:
    st.metric(label="Product Churn Rate", value=f"{data['Product Churn Rate']['value']}%", delta=f"{data['Product Churn Rate']['value']}%")
    # Gauge Chart for Churn Rate
    fig, ax = plt.subplots()
    ax.set_title("Product Churn Rate")
    ax.pie([data['Product Churn Rate']['value'], 100 - data['Product Churn Rate']['value']], colors=['red', 'green'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['Product Churn Rate']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)
with col3:
    st.metric(label="Average Product CSAT", value=data["Average Product CSAT"]["value"], delta=f"{data['Average Product CSAT']['value']}/5")
    # Star Rating
    stars = "⭐" * int(data["Average Product CSAT"]["value"])
    st.write(stars)
with col4:
    st.metric(label="Product NPS", value=f"{data['Product NPS']['value']}%", delta=f"{data['Product NPS']['value']}%")
    # Gauge Chart for NPS
    fig, ax = plt.subplots()
    ax.set_title("Product NPS")
    ax.pie([data['Product NPS']['value'], 100 - data['Product NPS']['value']], colors=['purple', 'white'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['Product NPS']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)

# Row 3: On Time Product Delivery Rate, Defect Rate, SLA Achievement, Deployment Success Rate
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="On Time Product Delivery Rate", value=f"{data['On Time Product Delivery Rate']['value']}%", delta=f"{data['On Time Product Delivery Rate']['value']}%")
    # Circle Gauge
    fig, ax = plt.subplots()
    ax.set_title("On Time Product Delivery Rate")
    ax.pie([data['On Time Product Delivery Rate']['value'], 100 - data['On Time Product Delivery Rate']['value']], colors=['green', 'white'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['On Time Product Delivery Rate']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)
with col2:
    st.metric(label="Defect Rate", value=f"{data['Defect Rate']['value']}%", delta=f"{data['Defect Rate']['value']}%")
    # Circle Gauge
    fig, ax = plt.subplots()
    ax.set_title("Defect Rate")
    ax.pie([data['Defect Rate']['value'], 100 - data['Defect Rate']['value']], colors=['red', 'green'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['Defect Rate']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)
with col3:
    st.metric(label="SLA Achievement", value=f"{data['SLA Achievement']['value']}%", delta=f"{data['SLA Achievement']['value']}%")
    # Circle Gauge
    fig, ax = plt.subplots()
    ax.set_title("SLA Achievement")
    ax.pie([data['SLA Achievement']['value'], 100 - data['SLA Achievement']['value']], colors=['green', 'white'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['SLA Achievement']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)
with col4:
    st.metric(label="Deployment Success Rate", value=f"{sum(data['Deployment Success Rate']['value'])/len(data['Deployment Success Rate']['value'])}%", delta=f"{sum(data['Deployment Success Rate']['value'])/len(data['Deployment Success Rate']['value'])}%")
    # Line Chart
    fig, ax = plt.subplots()
    ax.plot(range(1, 13), data['Deployment Success Rate']['value'])
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.set_ylabel("Success Rate (%)")
    st.pyplot(fig)

# Row 4: SIT Quality Index, Talent Turnover Rate
col1, col2 = st.columns(2)
with col1:
    st.metric(label="SIT Quality Index", value="85", delta="+5")
    # Bar Chart
    fig, ax = plt.subplots()
    ax.bar(["Dev", "Mid", "Sr", "Expert"], [85, 89, 85, 89])
    ax.set_ylabel("Score")
    st.pyplot(fig)
with col2:
    st.metric(label="Talent Turnover Rate", value=f"{data['Talent Turnover Rate']['value']}%", delta=f"{data['Talent Turnover Rate']['change']}%")
    # Circle Gauge
    fig, ax = plt.subplots()
    ax.set_title("Talent Turnover Rate")
    ax.pie([data['Talent Turnover Rate']['value'], 100 - data['Talent Turnover Rate']['value']], colors=['red', 'green'], wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{data['Talent Turnover Rate']['value']}%", ha='center', va='center', fontsize=14)
    st.pyplot(fig)
