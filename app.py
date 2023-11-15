import streamlit as st
import pandas as pd
import plotly.express as px

# the layout Variables
st.set_page_config(page_title="Beauty Bytes: Omni Channel Dashboard", 
                   page_icon="/static/logo.png",
                   initial_sidebar_state="expanded",
                   )

hero = st.container()
topRow = st.container()
midRow = st.container()
chartRow = st.container()
footer = st.container()

# # Load the data
# superSales = pd.read_csv('data/superSales.csv')
# Load the new data
# ics_data = pd.read_csv('data/ics_segments_data-2.csv')
ics_data = pd.read_csv('data/ics_segments_data-2.csv', encoding='ISO-8859-1')  # or try 'cp1252', 'utf-16'
ics_data['Date'] = pd.to_datetime(ics_data['Date'])

# CSS styles
# Custom styling for top and down
st.markdown(
    """
    <style>
    .top-stats {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0 40px 0;
        width: 100%;
        height: 40px;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stat {
        flex: 1; 

        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background-color: #111;

        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .stat p {
        padding-top: 8px;
    }
    .stat p {
        color: #bbb;
        font-size: 12px;
    }
    .stat span {
        color: #ddd;
        font-size: 24px;
        font-family: serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown(f'''
        <style>
        section[data-testid="stSidebar"] {{
                width: 500px;
                background-color: #000b1a;
                }}
        section[data-testid="stSidebar"] h1 {{
                color: #e3eefc;
                }}
        section[data-testid="stSidebar"] p {{
                color: #ddd;
                text-align: left;
                }}
        section[data-testid="stSidebar"] svg {{
                fill: #ddd;
                }}
        </style>
    ''',unsafe_allow_html=True)
    st.title(":anchor: About the dataset")
    st.markdown("As consumer preferences continue to evolve rapidly, the skincare industry is witnessing significant growth and heightened market competition. Through this dashboard, we aim to transform complex data into clear and insightful visualizations, offering a deeper understanding of these dynamic consumer trends.")

    # The Selectbox for ICS Segments
    ics_segments = ics_data['ICS Segment'].unique()
    selected_segment = st.selectbox('Select ICS Segment', ['Choose a Segment'] + list(ics_segments))
    if selected_segment == 'Choose a Segment':
        chosen_segment_data = ics_data
    else:
        chosen_segment_data = ics_data[ics_data['ICS Segment'] == selected_segment]    
    
    # # The Selectbox
    # Product_lines = superSales['Product_line'].unique()
    # line = st.selectbox('',['Choose the Product Line'] + list(Product_lines))
    # if line == 'Choose the Product Line':
    #     chosen_line = superSales
    # else:
    #     chosen_line = superSales[superSales['Product_line'] == line]

    # Customizing the select box
    
    st.markdown(f'''
    <style>
        .stSelectbox div div {{
                background-color: #fafafa;
                color: #333;
        }}
        .stSelectbox div div:hover {{
                cursor: pointer
        }}
        .stSelectbox div div .option {{
                background-color: red;
                color: #111;
        }}
        .stSelectbox div div svg {{
                fill: black;
        }}
    </style>
    ''', unsafe_allow_html=True)

# The Hero Section
with hero:
    st.markdown("""<div style="position:relative; margin: auto; text-align: center;">
              <img src="/static/logo.png" width=56>
            </div>""", unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; position:relative; top:40%;">Beauty Bytes: Omni Channel Dasbhoard</h1>', unsafe_allow_html=True)

# The Top Row
with topRow:
    # Calculate KPIs for the selected segment
    avg_purchase_value = chosen_segment_data['Average Purchase Value'].mean()
    purchase_frequency = chosen_segment_data['Purchase Frequency'].mean()
    preferred_channel = chosen_segment_data['Preferred Purchase Channel'].mode()[0]
    peak_purchase_time = chosen_segment_data['Peak Purchase Time'].mode()[0]
    avg_stickiness = chosen_segment_data['Stickiness'].mean()

    # # the logo
    # st.markdown("""<div style="position:relative; margin: auto; text-align: center;">
    #           <img src="https://www.ranklogos.com/wp-content/uploads/2014/10/The-Estee-Lauder-Companies-Logo.jpg" width=56>
    #         </div>""", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="subheader">KPIs</div>
        <div class="top-stats">
            <div class="stat">
                <p>Average Purchase Value<br><span> %.2f </span></p>
            </div>
            <div class="stat">
                <p>Purchase Frequency<br><span> %.2f </span></p>
            </div>
            <div class="stat">
                <p>Preferred Channel<br><span> %s </span></p>
            </div>
            <div class="stat">
                <p>Peak Purchase Time<br><span> %s </span></p>
            </div>
            <div class="stat">
                <p>Average Stickiness<br><span> %.2f </span></p>
            </div>
        </div>
        """ % (avg_purchase_value, purchase_frequency, preferred_channel, peak_purchase_time, avg_stickiness),
        unsafe_allow_html=True
    )    

    # # the header
    # st.markdown('<h1 style="text-align:center; position:relative; top:40%;">Super Store DATA</h1>', unsafe_allow_html=True)


# # The Rows
# with topRow:

#     # Calculate the total number of invoices
#     total_invoices = chosen_line.shape[0]

#     # Calculate the average rating and number of ratings
#     average_rating = chosen_line['Rating'].mean()

#     # Find the most active time for invoices
#     most_active_time = chosen_line['Order_time'].mode()[0]
#     # the result is 2:14 PM so I'll type it by hand for now.

   
# with midRow:
#     # Calculate the total income, costs, and profit
#     depts_income = chosen_line['Total_price'].sum()
#     depts_costs = chosen_line['costs'].sum()
#     depts_profit = depts_income - depts_costs

# The Mid Row
# with midRow:
#     st.markdown("Mid Row content can be added here.")

    # st.markdown(
    #     """
    #     <div class="top-stats">
    #         <div class="stat" style="background-color: #093b09;">
    #             <p>Income<br><span>&pound; %.1f</span></p>
    #         </div>
    #         <div class="stat" style="background-color: #4e0000;">
    #             <p>Costs<br><span>&pound; %.1f</span></p>
    #         </div>
    #         <div class="stat" style="background-color: #000062;">
    #             <p>Profit<br><span>&pound; %.1f</span></p>
    #         </div>
    #     </div>
    #     """ % (depts_income, depts_costs, depts_profit),
    #     unsafe_allow_html=True
    # )



# with chartRow:
#     # Filter for the month
#     superSales['Order_date'] = pd.to_datetime(superSales['Order_date'])
#     mar_data = (superSales['Order_date'].dt.month == 3)
#     lineQuantity = chosen_line[(mar_data)]

#     # Quantity for each day
#     quantity_per_day = lineQuantity.groupby('Order_date')['Quantity'].sum().reset_index()

#     # some space
#     st.markdown('<div></div>', unsafe_allow_html=True)
    
#     # Create a line chart for Quantity over the last month using Plotly
#     fig_quantity = px.line(
#         quantity_per_day, 
#         x='Order_date', 
#         y='Quantity', 
#         title='Total Sales for ICS'
#     )
#     fig_quantity.update_layout(
#         margin_r=100,
#     )
#     st.plotly_chart(fig_quantity)

# The Chart Row
with chartRow:
    # Create a line chart for Stickiness over time
    if selected_segment != 'Choose a Segment':
        stickiness_data = chosen_segment_data.groupby('Date')['Stickiness'].mean().reset_index()
        fig_stickiness = px.line(
            stickiness_data, 
            x='Date', 
            y='Stickiness', 
            title=f'Stickiness over time for ICS: {selected_segment}'
        )
        fig_stickiness.update_layout(margin_r=100)
        st.plotly_chart(fig_stickiness)
    else:
        st.markdown("Please select an ICS Segment to view the stickiness trend.")

with footer:
    st.markdown("---")
    st.markdown(
        """
        <style>
            p {
                font-size: 16px;
                text-align: center;
            }
            a {
                text-decoration: none;
                color: #00a;
                font-weight: 600;
            }
        </style>

        """, unsafe_allow_html=True
        )
