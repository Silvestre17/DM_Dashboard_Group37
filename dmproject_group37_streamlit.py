# =============================================================================
# Data Mining | Project 2024 | MSc in Data Science and Advanced Analytics
# Group: 37
#        André Silvestre, 20240502 | Filipa Pereira, 20240509  | Umeima Mahomed, 20240543
# =============================================================================
# streamlit run dmproject_group37_streamlit.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import dmproject_dashboard_functions
import plotly.express as px
import plotly.graph_objects as go
from pickle import dump , load
from sklearn.preprocessing import StandardScaler

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# ---- Streamlit Page Config ----
st.set_page_config(page_title='ABCDEats',
                   page_icon='https://upload.wikimedia.org/wikipedia/en/6/69/NOVA_IMS_Logo.png',
                   layout='wide',
                   initial_sidebar_state='expanded',
                   menu_items={
                       'Report a bug': 'mailto:20240502@novaims.unl.pt',
                       'About': "# DM Project | Group 37 | 2024/25"
                   })

# ---- CSS Styling ----
with open('style.css') as f:
    st.markdown(f'''<style>{f.read()}
                    /* Change the slider color | Sources: https://discuss.streamlit.io/t/how-to-change-st-sidebar-slider-default-color/3900/2 
                                                           https://discuss.streamlit.io/t/customizing-the-appearance-of-tabs/48913 */
                    .stTabs [data-baseweb="tab"] {{
                        color: #869721;
                    }}

                    .stTabs [data-baseweb="tab-highlight"] {{
                        background-color: #869721;
                    }}

                    button[kind="secondary"] {{
                        border: 1px solid #869721;
                    }}

                    button[kind="secondary"]:hover {{
                        font-weight: bold;
                        color: #869721;
                        border: 2px solid #869721;
                    }}

            </style>''', unsafe_allow_html=True)

st.logo(image='static/640px-HD_transparent_picture.png', icon_image='static/NOVAIMS_Logo.png')

# =============================================================================
# -----------------------------
# Banner Image (Top of the Page)
st.markdown("""
    <style>
        .h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 {
            font-weight: bold !important;
        }
        
        .banner {
            width: 117%;
            display: block;
            margin-left: -100px;
            margin-top: -60px;
        }
        .banner img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        @media (max-width: 768px) {
            .banner {
                width: 110%;
                display: block;
                margin-left: -20px;
                margin-top: -60px;
            }
            
            .banner img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
    </style>

    <!-- Banner Image -->
    <div class="banner">
        <img src='./app/static/ABCDEats_Banner.png' alt="Banner Image">
    </div>
    """, unsafe_allow_html=True)

# -----------------------------

# =============================================================================
# Resumo do Trabalho
st.markdown("""
    <style>
        @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css");
            
        .team h1,
        .team h2,
        .team h3,
        .team h4,
        .team h5,
        .team h6 {
            color: #3d392d;
            font-weight: bold;
        }
    
        .team .font-weight-medium {
            font-weight: 700;
        }
    
        .team .bg-light {
            background-color: #f4f8fa !important;
        }
    
        .team .subtitle-title {
            color: rgb(190, 214, 47);
            line-height: 24px;
            font-size: 26px;
            font-weight: 700;
            margin-top: -10px;
        }
    
        .team .subtitle-names {
            color: rgb(190, 214, 47);
            line-height: 24px;
            font-size: 14px;
            font-weight: 600;
        }
    
        .team ul {
            margin-top: 30px;
        }
    
        .team h5 {
            line-height: 22px;
            font-size: 18px;
        }
    
        .team ul li a {
            color: #8d97ad;
            padding-right: 15px;
            -webkit-transition: 0.1s ease-in;
            -o-transition: 0.1s ease-in;
            transition: 0.1s ease-in;
        }
    
        .team ul li a:hover {
            -webkit-transform: translate3d(0px, -5px, 0px);
            transform: translate3d(0px, -5px, 0px);
            color: #ff141e;
        }
    
        .team .title {
            margin: 30px 0 0 0;
        }
    
        .team .subtitle {
            margin: 0 0 20px 0;
            font-size: 13px;
        }
        
        .st-emotion-cache-1629p8f a {
            display: none;
            pointer-events: none;
        }
        
        .st-emotion-cache-1629p8f h1, .st-emotion-cache-1629p8f h2, .st-emotion-cache-1629p8f h3, .st-emotion-cache-1629p8f h4,
        .st-emotion-cache-1629p8f h5, .st-emotion-cache-1629p8f h6, .st-emotion-cache-1629p8f span {
            font-weight: bolder;
        }
        
    </style>
    
    <!-- Bibliotecas de Icons-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
            integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
            integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js"
            integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
            crossorigin="anonymous"></script>
        
    <div class="py-5 team">
        <div class="container" style="margin-top: -80px">
            <div class="row justify-content-center" style="margin-bottom: -40px">
                <div class="col-md-7 text-center">
                    <h1 class="mb-0 title-contactos"></h1>
                    <p class="subtitle-title">Customer Segmentation | Motivation</p>
                </div>
                <br><br>
                <p style="text-align: justify; margin: auto;"><br>
                    In an increasingly competitive market, businesses have been aiming to better understand their customers, offering products and services that closely align with their needs. <br>
                    By partitioning their customers into groups, they are able to tailor their strategies and improve satisfaction, loyalty, and profits. This practice, which is becoming more essential, is supported by many studies that highlight the importance of customer segmentation as a foundation for lasting client relationships. <br>
                    When executed effectively, segmentation enables a more comprehensive outline of resource allocation, allowing for more impactful investments in areas that yield the greatest return. <br> <br>
                    This web application provides an <b>user-friendly</b> and <b>interactive platform</b> to explore the <i>ABCDEats</i> dataset in a 90-day period and perform customer segmentation analysis, aiding in the identification of distinct customer segments based on diverse factors such as region, age, ordering behavior, and cuisine preferences. <br>                
                </p>
                <div class="col-md-7 text-center">
                    <h1 class="mb-0 title-contactos"></h1>
                    <p class="subtitle-title" style="color: #869721;">Web Application Features</p>
                </div>
            </div>
            <br>
            <style>
                .ol-custom {
                    counter-reset: item;
                    list-style-type: none;
                }
                .li-custom {
                    counter-increment: item;
                    margin-bottom: 10px;
                }
                .li-custom:before {
                    content: counter(item) ". ";
                    font-weight: bold;
                    color: #869721;
                    font-size: 18px;
                }
            </style>
            <p style="text-align: justify; margin: auto;"><br>
                <ol class="ol-custom" style="margin-left: 5rem;margin-right: 5rem;">
                    <li class="li-custom"><b>Interactive Visualizations:</b> presents key insights and segmentation results through various charts and graphs, facilitating easy interpretation of complex data.</li>
                    <li class="li-custom"><b>Interactive Filtering:</b> allows users to refine the dataset based on multiple user-defined criteria.</li>
                    <li class="li-custom"><b>Customer Segmentation:</b> enables the identification of distinct customer segments using diverse factors such as region, age, ordering behavior, and cuisine preferences.</li>
                </ol>
            </p>
            <hr/>
            <p style="text-align: center; margin: auto;"><br>
                Explore the app by selecting the <b><span style="color: #869721;">EDA</span></b> tab, and access the customer segmentation dashboard through the <b><span style="color: #869721;">Final Customer Segmentation</span></b> tab!<br>
            </p>
            </div>
        </div>
    </div>
    <footer class="footer" style="visibility: visible;">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <p class="company-name" style="color: #d3d3d3;">DM Project | Group 37 © 2024/25</p>
                </div>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# =============================================================================
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>""", unsafe_allow_html=True)

# =============================================================================
# --------------------------- Load Data ---------------------------
# Load the cleaned dataset
ABCDEats = pd.read_parquet('./DM2425_ABCDEats_ClusteringResults.parquet')

# Load the scaler
scaler = load(open('./scaler.pkl', 'rb'))

# Reverse the scaling transformation
metric_cols = ['customer_age', 'vendor_count', 'product_count', 'chain_count', 'first_order', 'last_order', 
               'CUI_American', 'CUI_Asian', 'CUI_Beverages', 'CUI_Cafe', 'CUI_Chicken Dishes', 'CUI_Chinese', 'CUI_Desserts', 'CUI_Healthy', 'CUI_Indian', 'CUI_Italian', 'CUI_Japanese', 'CUI_Noodle Dishes', 'CUI_OTHER', 'CUI_Street Food / Snacks', 'CUI_Thai', 
               'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
               'HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23', 
               'order_count', 'days_between_orders', 'days_between_orders_per_order', 'CUI_Total_Amount_Spent', 'CUI_Total_Food_Types', 'CUI_Avg_Amount_Spent']
ABCDEats_metrics_inverse = scaler.inverse_transform(ABCDEats[metric_cols])

# Replace the original columns with the inverse-scaled values
ABCDEats[metric_cols] = ABCDEats_metrics_inverse

# # Metrics that need to be converted to integers
int_cols = ['customer_age', 'vendor_count', 'product_count', 'chain_count', 'first_order', 'last_order', 
            'HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23',
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'order_count', 'days_between_orders', 'CUI_Total_Food_Types']
ABCDEats[int_cols] = ABCDEats[int_cols].astype(int)

# Replace the 'customer_age_group' values with the corresponding age ranges
# {'15-28': 1, '29-41': 2, '42-54': 3, '55-67': 4, '68-80': 5}
ABCDEats['customer_age_group'] = ABCDEats['customer_age_group'].replace({1: '15-28', 2: '29-41', 3: '42-54', 4: '55-67', 5: '68-80'})

################## ABCDEats - Data Summary ##################
# 1. `customer_id`: Unique identifier for each customer.
# 2. `customer_region`: Geographic region where the customer is located.
# 3. `customer_age`: Age of the customer.
# 4. `vendor_count`: Number of unique vendors the customer has ordered from.
# 5. `product_count`: Total number of products the customer has ordered.
# 6. `is_chain`: Number of orders placed at a chain restaurant.
# 7. `first_order`: Number of days from the start of the dataset when the customer first placed an order.
# 8. `last_order`: Number of days from the start of the dataset when the customer most recently placed an order.
# 9. `last_promo`: The category of the promotion or discount most recently used by the customer.
# 10. `payment_method`: Method most recently used by the customer to pay for their orders.
# 11-25. `CUI_American`, `CUI_Asian`, `CUI_Chinese`, `CUI_Italian`, etc.: The amount in monetary units spent by the customer from the indicated type of cuisine.
# 26-32. `DOW_0` to `DOW_6`: Number of orders placed on each day of the week (`0` = Sunday, `6` = Saturday).
# 33-56. `HR_0` to `HR_23`: Number of orders placed during each hour of the day (`0` = midnight, `23` = 11 PM).
# +1. `Number of Orders`: Corresponds to the sum of the variables `DOW_0` to `DOW_6`.
# +2. `customer_region_buckets`: Aggregated `customer_region` into buckets `2`, `4`, `8`, and `U`.
# +3. `customer_age_group`: Age ranges grouped into buckets: `15-28`, `29-41`, `42-54`, `55-67`, `68-80`.
# +4. `days_between_orders`: Calculated as the difference between `last_order` and `first_order`.
# +5. `days_between_orders_per_order`: Represents the quotient between `days_between_orders` and `order_count`.
# +6. `last_promo_bin`: Binary variable; takes the value `0` for `'NO PROMO'` and `1` otherwise.
# +7. `CUI_Total_Amount_Spent`: Total spending across all cuisines during the study period (90 days) for each customer.
# +8. `CUI_Most_Spent_Cuisine`: Name of the cuisine where the customer spent the most money.
# +9. `CUI_Total_Food_Types`: Count of different types of cuisines ordered.
# +10. `CUI_Avg_Amount_Spent`: Quotient of `CUI_Total_Amount_Spent` by `order_count`.
# +11. `CUI_NOTAsian_Italian_OTHER_NOTSnack_PC`: Principal component representing a combination of non-Asian, non-Italian, non-snack cuisines.
# +12. `CUI_American_Cafe_Japanese_PC`: Principal component representing a combination of American, Cafe, and Japanese cuisines.
# +13. `CUI_Chicken_Chinese_Noodle_PC`: Principal component representing a combination of Chicken, Chinese, and Noodle cuisines.
# +14. `CUI_Healthy_NOTAmerican_PC`: Principal component representing a combination of healthy, non-American cuisines.
# +15. `CUI_Indian_PC`: Principal component representing Indian cuisine.
# +16. `CUI_Japanese_NOTBeverages_PC`: Principal component representing Japanese cuisine excluding beverages.
# +17. `CUI_Beverages_Thai_PC`: Principal component representing a combination of Beverages and Thai cuisines.
# +18. `HR_Lunch_Dinner_PC`: Principal component representing orders placed during lunch and dinner hours.
# +19. `HR_LateNight_Breakfast_PC`: Principal component representing orders placed during late-night and breakfast hours.
# +20. `HR_Evening_PC`: Principal component representing orders placed during evening hours.
# +21. `HR_AfternoonSnack_PC`: Principal component representing orders placed during afternoon snack hours.


# =============================================================================
# ------------------------------- Sidebar Filters -----------------------------
# Filtros
# Definições do botão 'Filtrar' - https://docs.streamlit.io/develop/concepts/design/buttons
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

if 'filtros_button' in st.session_state and st.session_state.filtros_button is True:
    st.session_state.running = True
else:
    st.session_state.running = False   

# Initialize the session state variables
if 'cuisine' not in st.session_state:
    st.session_state.cuisine = []
if 'dow' not in st.session_state:
    st.session_state.dow = []
if 'hr' not in st.session_state:
    st.session_state.hr = []
if 'start_date_fo' not in st.session_state:
    st.session_state.start_date_fo = None
if 'end_date_fo' not in st.session_state:
    st.session_state.end_date_fo = None
if 'region' not in st.session_state:
    st.session_state.region = []
if 'age_group' not in st.session_state:
    st.session_state.age_group = []
if 'payment_method' not in st.session_state:
    st.session_state.payment_method = []
if 'vendor_count' not in st.session_state:
    st.session_state.vendor_count = []
if 'product_count' not in st.session_state:
    st.session_state.product_count = []
if 'chain_count' not in st.session_state:
    st.session_state.chain_count = []
if 'last_promo' not in st.session_state:
    st.session_state.last_promo = []

# Apply filters
@st.cache_data
def apply_filters(filters=None):
    
    # Case when no filters are applied
    if filters is None:
        return ABCDEats
    
    # Create a copy of the original dataset
    data = ABCDEats.copy()
        
    # Filter by Cuisine | 'CUI_American', 'CUI_Asian', 'CUI_Chinese', 'CUI_Italian', etc. > 0
    if filters['cuisine']:
        data = data[(data[cuisine].sum(axis=1) > 0)]
        
    # Filter by DOW (Day of the Week) | 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
    if filters['dow']:
        data = data[(data[dow].sum(axis=1) > 0)]
        
    # Filter by HR (Hour of the Day) | 'HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23'
    if filters['hr']:
        data = data[(data[hr].sum(axis=1) > 0)]
    
    # Filter by first_order and last_order
    if filters['start_date_fo'] and filters['end_date_fo']:
        data = data[(data['first_order'] >= start_date_fo) & (data['first_order'] <= end_date_fo)]
   
    # Filter by Region | 'customer_region'
    if filters['region']:
        data = data[data['customer_region_buckets'].isin(region)]
        
    # Filter by Age Group | 'customer_age_group'
    if filters['age_group']:
        data = data[data['customer_age_group'].isin(age_group)]

    # Filter by Payment Method | 'payment_method'
    if filters['payment_method']:
        data = data[data['payment_method'].isin(payment_method)]
        
    # Filter by Vendor Count | 'vendor_count'
    if filters['vendor_count']:
        data = data[data['vendor_count'].isin(vendor_count)]
        
    # Filter by Product Count | 'product_count'
    if filters['product_count']:
        data = data[data['product_count'].isin(product_count)]
        
    # Filter by Chain | 'chain_count'
    if filters['chain_count']:
        data = data[data['chain_count'].isin(chain_count)]
        
    # Filter by Last Promo | 'last_promo'
    if filters['last_promo']:
        data = data[data['last_promo'].isin(last_promo)]
        
    # Return the filtered dataset         
    return data


with st.sidebar:
    st.markdown('## Filters')
    st.write('<p style="font-size:10px"><b>Note:</b> The filters will be applied to the dataset when the <b><span style="color: #869721;">Filter</span></b> button is clicked <b>&</b> Multiple selections are treated as <b>OR</b>', unsafe_allow_html=True)
    
    # Filter by Cuisine | 'CUI_American', 'CUI_Asian', 'CUI_Chinese', 'CUI_Italian', etc.
    cuisine_cols = ['CUI_American', 'CUI_Asian', 'CUI_Beverages', 'CUI_Cafe', 'CUI_Chicken Dishes', 'CUI_Chinese', 'CUI_Desserts', 'CUI_Healthy', 'CUI_Indian', 'CUI_Italian', 'CUI_Japanese', 'CUI_Noodle Dishes', 'CUI_OTHER', 'CUI_Street Food / Snacks', 'CUI_Thai']
    cuisine = st.multiselect('Select Cuisine', ABCDEats[cuisine_cols].columns, default=st.session_state.cuisine)
    st.write('<p style="font-size:10px"><b>Note:</b> The filter will consider customers who have spent more than 0 monetary units on the selected cuisine.', unsafe_allow_html=True)
    
    # Filter by DOW (Day of the Week) | 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
    dow = st.multiselect('Select Day of the Week', ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], default=st.session_state.dow)
    st.write('<p style="font-size:10px"><b>Note:</b> The filter will consider customers who have placed orders on the selected day(s) of the week.', unsafe_allow_html=True)
    
    # Filter by HR (Hour of the Day) | 'HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23'
    hr = st.multiselect('Select Hour of the Day', ['HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23'], default=st.session_state.hr)
    st.write('<p style="font-size:10px"><b>Note:</b> The filter will consider customers who have placed orders during the selected hour(s) of the day.', unsafe_allow_html=True)
    
    # Filter by Date | First Order & Last Order
    start_date_fo, end_date_fo = dmproject_dashboard_functions.init_sidebar_dates_pickers(data_frame_datetime=ABCDEats['first_order'], 
                                                                                          start_default=st.session_state.start_date_fo,
                                                                                          end_default=st.session_state.end_date_fo)
    
    # Filter by Region | 'customer_region'
    region = st.multiselect('Select Region', sorted(ABCDEats['customer_region_buckets'].unique()), default=st.session_state.region)
    
    # Filter by Age Group | 'customer_age_group'
    age_group = st.multiselect('Select Age Group', sorted(ABCDEats['customer_age_group'].unique()), default=st.session_state.age_group)
    
    # Filter by Payment Method | 'payment_method'
    payment_method = st.multiselect('Select Payment Method', ABCDEats['payment_method'].unique(), default=st.session_state.payment_method)
    
    # Filter by Vendor Count | 'vendor_count'
    vendor_count = st.multiselect('Select Vendor Count', sorted(ABCDEats['vendor_count'].unique()), default=st.session_state.vendor_count)
    
    # Filter by Product Count | 'product_count'
    product_count = st.multiselect('Select Product Count', sorted(ABCDEats['product_count'].unique()), default=st.session_state.product_count)
    
    # Filter by Chain | 'chain_count'
    chain_count = st.multiselect('Select Chain', sorted(ABCDEats['chain_count'].unique()), default=st.session_state.chain_count)
    
    # Filter by Last Promo | 'last_promo'
    last_promo = st.multiselect('Select Last Promo', ABCDEats['last_promo'].unique(), default=st.session_state.last_promo)
    
    if st.button("Filter", on_click=click_button, key='filtros_button'):
        # Store the filter values in the session state
        st.session_state.cuisine = cuisine
        st.session_state.dow = dow
        st.session_state.hr = hr
        st.session_state.start_date_fo = start_date_fo
        st.session_state.end_date_fo = end_date_fo
        st.session_state.region = region
        st.session_state.age_group = age_group
        st.session_state.payment_method = payment_method
        st.session_state.vendor_count = vendor_count
        st.session_state.product_count = product_count
        st.session_state.chain_count = chain_count
        st.session_state.last_promo = last_promo
        
        # Apply filters
        ABCDEats = apply_filters({
        'cuisine': cuisine if cuisine else None,
        'dow': dow if dow else None,
        'hr': hr if hr else None,
        'start_date_fo': start_date_fo if start_date_fo else None,
        'end_date_fo': end_date_fo if end_date_fo else None,
        'region': region if region else None,
        'age_group': age_group if age_group else None,
        'payment_method': payment_method if payment_method else None,
        'vendor_count': vendor_count if vendor_count else None,
        'product_count': product_count if product_count else None,
        'chain_count': chain_count if chain_count else None,
        'last_promo': last_promo if last_promo else None
        })

    st.divider()
    
    # Notes about the project
    st.markdown('## About')
    
    st.write('''
             <p style="font-size: 14px; text-align: justify;">
                <b>Disclaimer:</b> This web application was developed as part of the Data Mining project for the MSc in Data Science and Advanced Analytics at NOVA IMS.<br><br>
                The data used in this application is synthetic and does not represent real customer information. <br><br>
            </p>
            ''', unsafe_allow_html=True)


# =============================================================================
# --------------------------- Main Content ---------------------------
# Tabs

tab1, tab2 = st.tabs(['EDA', 'Final Customer Segments'])

with tab1:
    st.write("### EDA | Exploratory Data Analysis")
    
    # Cards | Number of Customers, Total Orders, Total Amount Spent
    col1, col2, col3 = st.columns(3)
    
    # Number of Customers
    dmproject_dashboard_functions.create_card(col1, 'bi bi-person', [243, 251, 201], [0, 0, 0], 'Number of Customers', ABCDEats.index.nunique())
    
    # Total Orders
    dmproject_dashboard_functions.create_card(col2, 'bi bi-cart', [176, 197, 51], [0, 0, 0], 'Total Orders', round(ABCDEats['order_count'].sum()))
    
    # Total Amount Spent
    dmproject_dashboard_functions.create_card(col3, 'bi bi-cash-coin', [67, 75, 18], [255, 255, 255], 'Total Amount Spent (Monetary Units)', f"{ABCDEats['CUI_Total_Amount_Spent'].sum():,.2f}")
        
    # --------------------------------------------------------------------------------------------
    
    # Define the color palette
    color_palette = {
        "first_order": "#869721",  # Base green
        "last_order": "#4A5500", # Darker green
        "customer_age": "#869721",  # Base green
        "vendor_count": "#A3B75D",  # Softer green
        "product_count": "#C3D87B",  # Light green
        "chain_count": "#6F8D1B",  # Darker green
        "CUI_Total_Amount_Spent": "#5A7500",  # Olive green
        "customer_region": "#869721",  # Consistent green
        "last_promo": "#98A62D",  # Muted green
        "payment_method": "#D6E7A5",  # Pale green
        "customer_region_palette": {
            2: "#7B8F3A", 
            4: "#A4C173", 
            8: "#E1F2B5", 
            0: "#dfdfdf"
        },
        "last_promo_palette": {
            'NO PROMO': "#dfdfdf", 
            'DELIVERY': "#A3B75D", 
            'DISCOUNT': "#C3D87B", 
            'FREEBIE': "#6F8D1B"
        },
        "payment_method_palette": {
            'CASH': "#5A7500", 
            'CARD': "#A4C173", 
            'DIGI': "#D6E7A5",
        }
    }
    
    # LineChart | first_order, last_order
    # Group by 'first_order' and count the number of customers for each day
    df_first_order = ABCDEats.groupby('first_order').size().reset_index(name='first_order_count')
    # Group by 'last_order' and count the number of customers for each day
    df_last_order = ABCDEats.groupby('last_order').size().reset_index(name='last_order_count')

    # Create a complete list of days from 0 to 90
    all_days = pd.DataFrame({'day': range(91)})

    # Merge the dataframes to ensure all days are present (using 'day' as the key)
    df_first_order_merged = pd.merge(all_days, df_first_order, left_on='day', right_on='first_order', how='left')
    df_last_order_merged = pd.merge(all_days, df_last_order, left_on='day', right_on='last_order', how='left')

    # Fill NaN values with 0 for those days when no orders were made
    df_first_order_merged['first_order_count'] = df_first_order_merged['first_order_count'].fillna(0)
    df_last_order_merged['last_order_count'] = df_last_order_merged['last_order_count'].fillna(0)

    # Create the Plotly line chart
    fig_linechart = go.Figure()
    fig_linechart.add_trace(go.Scatter(x=df_first_order_merged['day'],
                                     y=df_first_order_merged['first_order_count'],
                                     mode='lines',
                                     name='First Order',
                                     line=dict(color=color_palette["first_order"], width=2)))
    fig_linechart.add_trace(go.Scatter(x=df_last_order_merged['day'],
                                    y=df_last_order_merged['last_order_count'],
                                     mode='lines',
                                     name='Last Order',
                                     line=dict(color=color_palette["last_order"], width=2)))

    # Update layout
    fig_linechart.update_layout(title='Number of First and Last Orders by Day',
                                xaxis_title='Day',
                                yaxis_title='Number of Orders',
                                font=dict(family="Arial", size=12, color="black"),
                                showlegend=True)
    fig_linechart.update_traces(hovertemplate='<b>Day</b>: %{x}<br><b>Number of Orders</b>: %{y}')

    # Display the chart in Streamlit
    st.plotly_chart(fig_linechart)
    
    # --------------------------------------------------------------------------------------------

    # Create a layout with two columns
    col1, col2, col3 = st.columns(3)

    # Distribution of Customer Age
    fig_age = px.histogram(ABCDEats,
                           x='customer_age',
                           nbins=30,
                           title='Distribution of Customer Age',
                           color_discrete_sequence=[color_palette["customer_age"]],
                           labels={"customer_age": "Customer Age", "count": "Number of Customers"})
    fig_age.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_age.layout.yaxis.title.text = 'Number of Customers'
    fig_age.update_traces(hovertemplate='<b>Customer Age</b>: %{x}<br><b>Number of Customers</b>: %{y}')
    col1.plotly_chart(fig_age)

    # Distribution of Vendor Count
    fig_vendor = px.histogram(ABCDEats,
                              x='vendor_count',
                              title='Distribution of Vendor Count',
                              color_discrete_sequence=[color_palette["vendor_count"]],
                              labels={"vendor_count": "Vendor Count", "count": "Number of Customers"})
    fig_vendor.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_vendor.layout.yaxis.title.text = 'Number of Customers'
    fig_vendor.update_traces(hovertemplate='<b>Vendor Count</b>: %{x}<br><b>Number of Customers</b>: %{y}')
    col2.plotly_chart(fig_vendor)

    # Distribution of Product Count
    fig_product = px.histogram(ABCDEats,
                            x='product_count',
                            title='Distribution of Product Count',
                            color_discrete_sequence=[color_palette["product_count"]],
                            labels={"product_count": "Product Count", "count": "Number of Customers"})
    fig_product.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_product.layout.yaxis.title.text = 'Number of Customers'
    fig_product.update_traces(hovertemplate='<b>Product Count</b>: %{x}<br><b>Number of Customers</b>: %{y}')
    col3.plotly_chart(fig_product)

    # Distribution of Total Amount Spent
    fig_total_amount = px.histogram(ABCDEats,
                                    x='CUI_Total_Amount_Spent',
                                    title='Distribution of Total Amount Spent',
                                    color_discrete_sequence=[color_palette["CUI_Total_Amount_Spent"]],
                                    labels={"CUI_Total_Amount_Spent": "Total Amount Spent", "count": "Number of Customers"})
    fig_total_amount.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_total_amount.layout.yaxis.title.text = 'Number of Customers'
    fig_total_amount.update_traces(hovertemplate='<b>Total Amount Spent</b>: %{x}<br><b>Number of Customers</b>: %{y}')
    
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig_total_amount)

    # Create the box plot for Customer Age by Region
    # Convert the customer_region_buckets = 'U' to 0
    ABCDEats['customer_region_buckets'] = ABCDEats['customer_region_buckets'].replace('U', '0')

    # Create the box plot for Customer Age by Region
    fig_age_region = px.box(ABCDEats,
                            x='customer_region_buckets',
                            y='customer_age',
                            title='Customer Age by Region',
                            color_discrete_sequence=[color_palette["customer_region"]],
                            labels={"customer_region_buckets": "Customer Region", "customer_age": "Customer Age"},
                            category_orders={"customer_region_buckets": ["2", "4", "8", "U"]})
    fig_age_region.update_layout(xaxis = dict(tickmode = 'array', tickvals = [0, 2, 4, 8], ticktext = ['Unknown', '2', '4', '8']),
                                 font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_age_region.update_traces(hovertemplate='<b>Customer Region</b>: %{x}<br><b>Customer Age</b>: %{y}')
    col2.plotly_chart(fig_age_region)
    
    # Bar chart of Customer Region (% with hovertemplate 'n')
    fig_region = px.bar(pd.DataFrame(ABCDEats['customer_region_buckets'].value_counts(normalize=True) * 100).round(2).reset_index(),
                        x='customer_region_buckets',
                        y='proportion',
                        title='Distribution of Customer Region',
                        color='customer_region_buckets',
                        color_discrete_sequence=[color_palette["customer_region_palette"][2], color_palette["customer_region_palette"][4], color_palette["customer_region_palette"][8], color_palette["customer_region_palette"][0]],
                        labels={"customer_region_buckets": "Customer Region", "proportion": "% of Customers"},
                        category_orders={"customer_region_buckets": ["2", "4", "8", "0"]})
    fig_region.update_layout(xaxis = dict(tickmode = 'array', tickvals = [0, 2, 4, 8], ticktext = ['Unknown', '2', '4', '8']),
                             font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_region.update_traces(hovertemplate='<b>Customer Region</b>: %{x}<br><b>% of Customers</b>: %{y}')
    col1, col2 = st.columns([0.3, 0.7])
    col1.plotly_chart(fig_region)
    
    # Scatter plot of Total Amount Spent vs. Number of Orders by Region
    fig_scatter = px.scatter(ABCDEats,
                            x='order_count',
                            y='CUI_Total_Amount_Spent',
                            title='Total Amount Spent vs. Number of Orders by Customer Region',
                            color='customer_region_buckets',
                            color_discrete_sequence=[color_palette["customer_region_palette"][2], color_palette["customer_region_palette"][4], color_palette["customer_region_palette"][8], color_palette["customer_region_palette"][0]],
                            labels={"order_count": "Number of Orders", "CUI_Total_Amount_Spent": "Total Amount Spent", "customer_region_buckets": "Customer Region"},
                            category_orders={"customer_region_buckets": ["2", "4", "8", "0"]})
    fig_scatter.for_each_trace(lambda trace: trace.update(name=trace.name.replace("0", "Unknown")))
    fig_scatter.update_layout(legend_title_text='Customer Region',
                              legend=dict(title=dict(text='Customer Region'), yanchor="middle", y=0.5),
                              font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_scatter.update_traces(hovertemplate='<b>Number of Orders</b>: %{x}<br><b>Total Amount Spent</b>: %{y}')
    col2.plotly_chart(fig_scatter)

    # Bar chart of Last Promo Used
    fig_promo = px.bar(pd.DataFrame(ABCDEats['last_promo'].map({'NO PROMO': 'No Promo', 'DELIVERY': 'Delivery', 'DISCOUNT': 'Discount', 'FREEBIE': 'Freebie'}).value_counts(normalize=True) * 100).round(2).reset_index(),
                       x='last_promo',
                       y='proportion',
                       title='Distribution of Last Promo Used',
                       color='last_promo',
                       color_discrete_sequence=[color_palette["last_promo_palette"]['NO PROMO'], color_palette["last_promo_palette"]['DELIVERY'], color_palette["last_promo_palette"]['DISCOUNT'], color_palette["last_promo_palette"]['FREEBIE']],
                       labels={"last_promo": "Last Promo Used", "proportion": "% of Customers"},
                       category_orders={"last_promo": ["NO PROMO", "DELIVERY", "DISCOUNT", "FREEBIE"]})
    fig_promo.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_promo.update_traces(hovertemplate='<b>Last Promo Used</b>: %{x}<br><b>% of Customers</b>: %{y}')                      
    col1.plotly_chart(fig_promo)
    
    # Scatter plot of Total Amount Spent vs. Number of Orders by Last Promo Used
    fig_scatter_promo = px.scatter(ABCDEats,
                                    x='order_count',
                                    y='CUI_Total_Amount_Spent',
                                    title='Total Amount Spent vs. Number of Orders by Last Promo Used',
                                    color='last_promo',
                                    color_discrete_sequence=[color_palette["last_promo_palette"]['NO PROMO'], color_palette["last_promo_palette"]['DELIVERY'], color_palette["last_promo_palette"]['DISCOUNT'], color_palette["last_promo_palette"]['FREEBIE']],
                                    labels={"order_count": "Number of Orders", "CUI_Total_Amount_Spent": "Total Amount Spent", "last_promo": "Last Promo Used"},
                                    category_orders={"last_promo": ["NO PROMO", "DELIVERY", "DISCOUNT", "FREEBIE"]})
    fig_scatter_promo.update_layout(legend_title_text='Last Promo Used',
                                    legend=dict(title=dict(text='Last Promo Used'), yanchor="middle", y=0.5),
                                    font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_scatter_promo.update_traces(hovertemplate='<b>Number of Orders</b>: %{x}<br><b>Total Amount Spent</b>: %{y}')
    col2.plotly_chart(fig_scatter_promo)
    
    # Bar chart of Payment Methods
    fig_payment_method = px.bar(pd.DataFrame(ABCDEats['payment_method'].value_counts(normalize=True) * 100).round(2).reset_index(),
                                x='payment_method',
                                y='proportion',
                                title='Distribution of Payment Methods',
                                color = 'payment_method',
                                color_discrete_sequence=[color_palette["payment_method_palette"]['CASH'], color_palette["payment_method_palette"]['CARD'], color_palette["payment_method_palette"]['DIGI']],
                                labels={"payment_method": "Payment Method", "proportion": "% of Customers"},
                                category_orders={"payment_method": ABCDEats['payment_method'].value_counts().index})
    fig_payment_method.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_payment_method.update_traces(hovertemplate='<b>Payment Method</b>: %{x}<br><b>% of Customers</b>: %{y}')
    col1.plotly_chart(fig_payment_method)
    
    # Scatter plot of Total Amount Spent vs. Number of Orders by Payment Method
    fig_scatter_payment = px.scatter(ABCDEats,
                                     x='order_count',
                                     y='CUI_Total_Amount_Spent',
                                     title='Total Amount Spent vs. Number of Orders by Payment Method',
                                     color='payment_method',
                                     color_discrete_sequence=[color_palette["payment_method_palette"]['CASH'], color_palette["payment_method_palette"]['CARD'], color_palette["payment_method_palette"]['DIGI']],
                                     labels={"order_count": "Number of Orders", "CUI_Total_Amount_Spent": "Total Amount Spent", "payment_method": "Payment Method"},
                                     category_orders={"payment_method": ABCDEats['payment_method'].value_counts().index})
    fig_scatter_payment.update_layout(legend_title_text='Payment Method',
                                      legend=dict(title=dict(text='Payment Method'), yanchor="middle", y=0.5),
                                      font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_scatter_payment.update_traces(hovertemplate='<b>Number of Orders</b>: %{x}<br><b>Total Amount Spent</b>: %{y}')
    col2.plotly_chart(fig_scatter_payment)
        
    # ------------------------------------------------------------------------------------------------
    # Barplot chain_count/order_count by customer_region_buckets
    # Add a new column 'chain_count/order_count' to the dataset
    ABCDEats['chain_count/order_count'] = ABCDEats['chain_count'] / (ABCDEats['order_count'])

    # Ensure that 'customer_region_buckets' is not 'U', and replace it with '0'
    ABCDEats['customer_region_buckets'] = ABCDEats['customer_region_buckets'].replace('U', '0')
    ABCDEats['customer_region_buckets'] = pd.Categorical(ABCDEats['customer_region_buckets'], categories=['2', '4', '8', '0'], ordered=True)

    # Calculate the min and max values of the 'chain_count/order_count' variable
    min_val = ABCDEats['chain_count/order_count'].min()
    max_val = ABCDEats['chain_count/order_count'].max()

    # Create a color scale using plotly.colors
    custom_scale = [
        [0, "#cde3a7"],  # Start with a lighter color
        [1, "#4A5500"]  # End with a darker color
    ]
        
    # Create the bar plot
    fig_chain = px.bar(ABCDEats.groupby(['chain_count/order_count', 'customer_region_buckets']).size().reset_index(name='mean').round(3),
                       x='customer_region_buckets',
                       y='mean',
                       color='chain_count/order_count',
                       custom_data = ['chain_count/order_count'],
                       color_continuous_scale=custom_scale,
                       title='Number of Orders by Chain and Customer Region',
                       labels={"customer_region_buckets": "Customer Region", "mean": "Number of Orders", "chain_count/order_count": "% Chain Count/Order Count"},
                       category_orders={"customer_region_buckets": ["2", "4", "8", "0"]})
    fig_chain.update_layout(font=dict(family="Arial", size=12, color="black"), 
                            legend_title_text='% Chain Count/Order Count',
                            showlegend=True)
    fig_chain.update_traces(hovertemplate='<b>Number of Orders</b>: %{y}<br><b>% Chain/Order</b>: %{customdata[0]:.2%}')
    st.plotly_chart(fig_chain)
    
    # --------------------------------------------------------------------------------------------
    # ScatterPlot of Average Amount Spent, Order Count, Total Food Types
    fig_scatter_cuisine = px.scatter(ABCDEats,
                                    x='order_count',
                                    y='CUI_Avg_Amount_Spent',
                                    custom_data='CUI_Total_Food_Types',
                                    title='Average Amount Spent vs. Number of Orders by Most Spent Cuisine',
                                    color='CUI_Most_Spent_Cuisine',
                                    color_discrete_sequence=px.colors.qualitative.Light24,
                                    labels={"order_count": "Number of Orders", "CUI_Avg_Amount_Spent": "Average Amount Spent",  "CUI_Most_Spent_Cuisine": "Most Spent Cuisine"},
                                    category_orders={"CUI_Most_Spent_Cuisine": ABCDEats['CUI_Most_Spent_Cuisine'].value_counts().index},
                                    height=600)
    fig_scatter_cuisine.update_layout(font=dict(family="Arial", size=12, color="black"), 
                                      legend=dict(title=dict(text='Most Spent Cuisine'), yanchor="middle", y=0.5),
                                      showlegend=True)
    fig_scatter_cuisine.update_traces(hovertemplate='<b>Number of Orders</b>: %{x}<br><b>Average Amount Spent</b>: %{y}<br><b>Total Food Types</b>: %{customdata[0]}')
    st.plotly_chart(fig_scatter_cuisine, use_container_width=True)
        
    # Table of Average Amount Spent, Order Count, Most Spent Cuisine
    fig_table_cuisine = pd.DataFrame(ABCDEats.groupby('CUI_Most_Spent_Cuisine').agg({'order_count': 'sum', 'CUI_Avg_Amount_Spent': 'mean', 'CUI_Total_Amount_Spent': 'sum', 'CUI_Total_Food_Types': 'mean'}).reset_index())
    fig_table_cuisine = fig_table_cuisine.rename(columns={'CUI_Most_Spent_Cuisine': 'Most Spent Cuisine', 'order_count': 'Total Orders', 'CUI_Avg_Amount_Spent': 'Average Amount Spent', 'CUI_Total_Amount_Spent': 'Total Amount Spent', 'CUI_Total_Food_Types': 'Mean Food Types'})
    fig_table_cuisine['n'] = ABCDEats['CUI_Most_Spent_Cuisine'].value_counts().values
    fig_table_cuisine = fig_table_cuisine.sort_values(by='n', ascending=False)
    fig_table_cuisine['Average Amount Spent'] = fig_table_cuisine['Average Amount Spent'].round(2)
    fig_table_cuisine['Total Amount Spent'] = fig_table_cuisine['Total Amount Spent'].round(2).map('{:,.2f}'.format)
    fig_table_cuisine['Mean Food Types'] = fig_table_cuisine['Mean Food Types'].round(2)
    fig_table_cuisine = fig_table_cuisine.set_index('Most Spent Cuisine')

    # Convert the pandas DataFrame to HTML
    table_html = fig_table_cuisine[['n','Total Orders', 'Average Amount Spent', 'Total Amount Spent', 'Mean Food Types']].to_html(escape=True, classes='styled-table')

    # Drop 2nd row of the table
    table_html = table_html.replace('''<tr>
      <th>Most Spent Cuisine</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>''', '')
    
    # Replace the column names
    table_html = table_html.replace(
        '''<tr style="text-align: right;">
      <th></th>
      <th>n</th>
      <th>Total Orders</th>
      <th>Average Amount Spent</th>
      <th>Total Amount Spent</th>
      <th>Mean Food Types</th>
    </tr>''', 
        '''<tr style="text-align: right;">
            <th>Most Spent Cuisine</th>
            <th>Number of Customers</th>
            <th>Total Orders</th>
            <th>Average Amount Spent</th>
            <th>Total Amount Spent</th>
            <th>Mean Food Types</th>
        </tr>''')

    # Apply custom styles
    st.markdown(f"""
        <style>
            .styled-table {{
                width: 80%;
                margin: 0 auto;
                border-collapse: collapse;
                font-size: 0.9em;
                font-family: sans-serif;
                min-width: 400px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                height: 100%;
            }}
            .styled-table th,
            .styled-table td {{
                padding: 12px 15px;
                text-align: center;
                border-bottom: 1px solid #dddddd;
            }}
            .styled-table thead tr {{
                    background-color: #4A5500;
                    color: #ffffff;
                    text-align: left;
                }}
            .styled-table tbody tr:nth-of-type(even) {{
                background-color: #f5f5f5;
            }}
            
            .styled-table tbody tr:last-of-type {{
                border-bottom: 4px solid #4A5500;
            }}
        </style><div style='display: flex; justify-content: center; align-items: center; height: 900px;'>{table_html}</div>""", unsafe_allow_html=True)
        
    # --------------------------------------------------------------------------------------------
    # Sunburst Chart of ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], HR_0:HR_23
    
    # Create a new column for the 'Most Common DOW' name
    ABCDEats['Most_Common_DOW'] = ABCDEats[['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']].idxmax(axis=1)
    
    # Create a new column for the 'Most Common HR' name
    ABCDEats['Most_Common_HR'] = ABCDEats[['HR_0', 'HR_1', 'HR_2', 'HR_3', 'HR_4', 'HR_5', 'HR_6', 'HR_7', 'HR_8', 'HR_9', 'HR_10', 'HR_11', 'HR_12', 'HR_13', 'HR_14', 'HR_15', 'HR_16', 'HR_17', 'HR_18', 'HR_19', 'HR_20', 'HR_21', 'HR_22', 'HR_23']].idxmax(axis=1).str.replace('HR_', '')
               
    fig_sunburst = px.sunburst(ABCDEats,
                               path=['Most_Common_DOW', 'Most_Common_HR'],
                               title='Most Common Day of the Week and Hour of the Day',
                               labels={"Most_Common_DOW": "Day of the Week", "Most_Common_HR": "Hour of the Day"},
                               width=1600, height=1000)
    fig_sunburst.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_sunburst.update_traces(hovertemplate='<b>Day of the Week/Hour of the Day</b>: %{id}<br><b>Number of Customers</b>: %{value}')
    st.plotly_chart(fig_sunburst, use_container_width=True)
           
    # --------------------------------------------------------------------------------------------
    
with tab2:
    st.write("### Final Customer Segments")
    
    # Display Overall Customer Segments Results [Clustering - 5 Clusters]
    clusters_palette = {
        0: "#2C3E1F",
        1: "#7B8F3A",  
        2: "#ADC178", 
        3: "#F0E5CB",  
        4: "#909090"  
    }
    
    # Filter the dataset based on 'Cluster' column
    cluster_data = ABCDEats.copy()
    
    # Apply sidebar filters
    cluster_data = apply_filters({
        'cuisine': st.session_state.cuisine if st.session_state.cuisine else None,
        'dow': st.session_state.dow if st.session_state.dow else None,
        'hr': st.session_state.hr if st.session_state.hr else None,
        'start_date_fo': st.session_state.start_date_fo if st.session_state.start_date_fo else None,
        'end_date_fo': st.session_state.end_date_fo if st.session_state.end_date_fo else None,
        'region': st.session_state.region if st.session_state.region else None,
        'age_group': st.session_state.age_group if st.session_state.age_group else None,
        'payment_method': st.session_state.payment_method if st.session_state.payment_method else None,
        'vendor_count': st.session_state.vendor_count if st.session_state.vendor_count else None,
        'product_count': st.session_state.product_count if st.session_state.product_count else None,
        'chain_count': st.session_state.chain_count if st.session_state.chain_count else None,
        'last_promo': st.session_state.last_promo if st.session_state.last_promo else None
        })
    
    # Create a new column for the 'Cluster' name
    cluster_data['Cluster Name'] = cluster_data['merged_labels'].map({0: 'Cluster 1', 1: 'Cluster 2', 2: 'Cluster 3', 3: 'Cluster 4', 4: 'Cluster 5'})
    
    # Create a new column for the 'Cluster' color
    cluster_data['Cluster Color'] = cluster_data['merged_labels'].map(clusters_palette)
    
    # Create a filter for the 'Cluster Name' (multiselect)
    cluster_name = st.multiselect('Select Cluster', cluster_data['Cluster Name'].unique(), default=sorted(cluster_data['Cluster Name'].unique().tolist()))
    
    # Filter the dataset based on the selected 'Cluster Name'
    cluster_data = cluster_data[cluster_data['Cluster Name'].isin(cluster_name)]
    
    # Display the number of customers in the selected cluster(s)
    col1, col2 = st.columns(2)
    dmproject_dashboard_functions.create_card(col1, 'bi bi-person', [243, 251, 201], [0, 0, 0], 'Number of Customers in Selected Cluster(s)', cluster_data.shape[0])
    
    # Display the percentage of customers in the selected cluster(s)
    dmproject_dashboard_functions.create_card(col2, 'bi bi-percent', [176, 197, 51], [0, 0, 0], 'Percentage of Customers in Selected Cluster(s)', round(cluster_data.shape[0] / ABCDEats.shape[0], 4) * 100)
    
    # --------------------------------------------------------------------------------------------
    
    # Create a layout with two columns
    col1, col2 = st.columns(2)
    
    # Create a bar chart of the number of customers by cluster
    freq_cluster = cluster_data['Cluster Name'].value_counts().reset_index()
    freq_cluster.columns = ['Cluster Name', 'count']
    freq_cluster['% of Total'] = freq_cluster['count'] / freq_cluster['count'].sum() * 100
    freq_cluster['% of Total'] = freq_cluster['% of Total'].round(2)    
    fig_cluster_bar = px.bar(freq_cluster,
                             x='Cluster Name',
                             y='count',
                             custom_data=['% of Total'],
                             title='Number of Customers by Cluster',
                             color='Cluster Name',
                             color_discrete_sequence=clusters_palette,
                             labels={"count": "Cluster", "Cluster Name": "Number of Customers"},
                             category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_bar.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_bar.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Number of Customers</b>: %{y}<br><b>% of Customers</b>: %{customdata[0]}%')
    col1.plotly_chart(fig_cluster_bar)
    
    # Scatter plot of Total Amount Spent vs. Number of Orders by Cluster
    fig_scatter_cluster = px.scatter(cluster_data,
                                    x='order_count',
                                    y='CUI_Total_Amount_Spent',
                                    title='Total Amount Spent vs. Number of Orders by Cluster',
                                    color='Cluster Name',
                                    color_discrete_sequence=clusters_palette,
                                    labels={"order_count": "Number of Orders", "CUI_Total_Amount_Spent": "Total Amount Spent", "Cluster Name": "Cluster"},
                                    category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_scatter_cluster.update_layout(legend_title_text='Cluster',
                                    legend=dict(title=dict(text='Cluster'), yanchor="middle", y=0.5),
                                    font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_scatter_cluster.update_traces(hovertemplate='<b>Number of Orders</b>: %{x}<br><b>Total Amount Spent</b>: %{y:.2f}')
    col2.plotly_chart(fig_scatter_cluster)
        
    # --------------------------------------------------------------------------------------------
    # Time Series Plot | First Order by Cluster
    first_order_cluster = cluster_data.groupby(['Cluster Name', 'first_order']).size().reset_index(name='first_order_count')

    # Create a complete list of days from 0 to 90
    all_days = pd.DataFrame({'day': range(91)})
    
    # Create a Area Chart of the number of first orders by cluster
    fig_first_order_cluster = px.area(first_order_cluster,
                                    x='first_order',
                                    y='first_order_count',
                                    title='Number of First Orders by Cluster',
                                    color='Cluster Name',
                                    color_discrete_sequence=clusters_palette,
                                    labels={"first_order": "Day", "first_order_count": "Number of Orders", "Cluster Name": "Cluster"},
                                    category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_first_order_cluster.update_layout(font=dict(family="Arial", size=12, color="black"), 
                                          legend=dict(title=dict(text='Cluster'), yanchor="middle", y=0.5),
                                          showlegend=True)
    fig_first_order_cluster.update_traces(hovertemplate='<b>Day</b>: %{x}<br><b>Number of First Orders</b>: %{y}')
    col1.plotly_chart(fig_first_order_cluster, use_container_width=True)
    
    # Time Series Plot | Last Order by Cluster
    last_order_cluster = cluster_data.groupby(['Cluster Name', 'last_order']).size().reset_index(name='last_order_count')
    
    # Create a complete list of days from 0 to 90
    all_days = pd.DataFrame({'day': range(91)})
                            
    # Create a Area Chart of the number of last orders by cluster
    fig_last_order_cluster = px.area(last_order_cluster,
                                    x='last_order',
                                    y='last_order_count',
                                    title='Number of Last Orders by Cluster',
                                    color='Cluster Name',
                                    color_discrete_sequence=clusters_palette,
                                    labels={"last_order": "Day", "last_order_count": "Number Orders", "Cluster Name": "Cluster"},
                                    category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_last_order_cluster.update_layout(font=dict(family="Arial", size=12, color="black"), 
                                         legend=dict(title=dict(text='Cluster'), yanchor="middle", y=0.5),
                                         showlegend=True)
    fig_last_order_cluster.update_traces(hovertemplate='<b>Day</b>: %{x}<br><b>Number of Last Orders</b>: %{y}')
    col2.plotly_chart(fig_last_order_cluster, use_container_width=True)
      


    # --------------------------------------------------------------------------------------------
    
    # Create a layout with four columns [Bar Chart, Bar Chart, Bar Chart, Bar Chart]
    col1, col2, col3, col4 = st.columns(4)
    
    # Create a bar chart of the average 'order_count' by cluster
    fig_cluster_order = px.bar(cluster_data.groupby('Cluster Name')['order_count'].mean().reset_index(),
                               x='Cluster Name',
                               y='order_count',
                               title='Average Number of Orders by Cluster',
                               color='Cluster Name',
                               color_discrete_sequence=clusters_palette,
                               labels={"Cluster Name": "Cluster", "order_count": "Average Number of Orders"},
                               category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_order.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_order.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Number of Orders</b>: %{y:.2f}')  
    col1.plotly_chart(fig_cluster_order)
    
    # Create a bar chart of the average 'chain_count' by cluster
    fig_cluster_chain = px.bar(cluster_data.groupby('Cluster Name')['chain_count'].mean().reset_index(),
                               x='Cluster Name',
                               y='chain_count',
                               title='Average Chain Count by Cluster',
                               color='Cluster Name',
                               color_discrete_sequence=clusters_palette,
                               labels={"Cluster Name": "Cluster", "chain_count": "Average Chain Count"},
                               category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_chain.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_chain.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Chain Count</b>: %{y:.2f}')
    col2.plotly_chart(fig_cluster_chain)
    
    # Create a bar chart of the average 'product_count' by cluster
    fig_cluster_product = px.bar(cluster_data.groupby('Cluster Name')['product_count'].mean().reset_index(),
                                x='Cluster Name',
                                y='product_count',
                                title='Average Product Count by Cluster',
                                color='Cluster Name',
                                color_discrete_sequence=clusters_palette,
                                labels={"Cluster Name": "Cluster", "product_count": "Average Product Count"},
                                category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_product.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_product.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Product Count</b>: %{y:.2f}')
    col3.plotly_chart(fig_cluster_product)
    
    # Create a bar chart of the average 'vendor_count' by cluster
    fig_cluster_vendor = px.bar(cluster_data.groupby('Cluster Name')['vendor_count'].mean().reset_index(),
                                x='Cluster Name',
                                y='vendor_count',
                                title='Average Vendor Count by Cluster',
                                color='Cluster Name',
                                color_discrete_sequence=clusters_palette,
                                labels={"Cluster Name": "Cluster", "vendor_count": "Average Vendor Count"},
                                category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_vendor.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_vendor.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Vendor Count</b>: %{y:.2f}')
    col4.plotly_chart(fig_cluster_vendor)
    
    # --------------------------------------------------------------------------------------------
    
    # Create a bar chart of the average 'CUI_Avg_Amount_Spent' by cluster
    fig_cluster_avg = px.bar(cluster_data.groupby('Cluster Name')['CUI_Avg_Amount_Spent'].mean().reset_index(),
                                x='Cluster Name',
                                y='CUI_Avg_Amount_Spent',
                                title='Average Amount Spent by Cluster',
                                color='Cluster Name',
                                color_discrete_sequence=clusters_palette,
                                labels={"Cluster Name": "Cluster", "CUI_Avg_Amount_Spent": "Average Amount Spent"},
                                category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_avg.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_avg.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Amount Spent</b>: %{y:.2f}')
    col1.plotly_chart(fig_cluster_avg)
    
    # Create a bar chart of the average 'CUI_Total_Amount_Spent' by cluster
    fig_cluster_bar = px.bar(cluster_data.groupby('Cluster Name')['CUI_Total_Amount_Spent'].mean().reset_index(),
                             x='Cluster Name',
                             y='CUI_Total_Amount_Spent',
                             title='Average Total Amount Spent by Cluster',
                             color='Cluster Name',
                             color_discrete_sequence=clusters_palette,
                             labels={"Cluster Name": "Cluster", "CUI_Total_Amount_Spent": "Average Total Amount Spent"},
                             category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_bar.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_bar.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Total Amount Spent</b>: %{y:.2f}')
    col2.plotly_chart(fig_cluster_bar)
    
    # Create a bar chart of the average 'CUI_Total_Food_Types' by cluster
    fig_cluster_food = px.bar(cluster_data.groupby('Cluster Name')['CUI_Total_Food_Types'].mean().reset_index(),
                                x='Cluster Name',
                                y='CUI_Total_Food_Types',
                                title='Average Total Food Types by Cluster',
                                color='Cluster Name',
                                color_discrete_sequence=clusters_palette,
                                labels={"Cluster Name": "Cluster", "CUI_Total_Food_Types": "Average Total Food Types"},
                                category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_food.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_food.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Total Food Types</b>: %{y:.2f}')
    col3.plotly_chart(fig_cluster_food)    
    
    # Create a bar chart of the average 'customer_age' by cluster
    fig_cluster_age = px.bar(cluster_data.groupby('Cluster Name')['customer_age'].mean().reset_index(),
                                x='Cluster Name',
                                y='customer_age',
                                title='Average Customer Age by Cluster',
                                color='Cluster Name',
                                color_discrete_sequence=clusters_palette,
                                labels={"Cluster Name": "Cluster", "customer_age": "Average Customer Age"},
                                category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_cluster_age.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_cluster_age.update_traces(hovertemplate='<b>Cluster</b>: %{x}<br><b>Average Customer Age</b>: %{y:.2f}')
    col4.plotly_chart(fig_cluster_age)
    
    # --------------------------------------------------------------------------------------------
    
    clusters_palette_names = {'Cluster 1': '#2C3E1F', 'Cluster 2': '#7B8F3A', 'Cluster 3': '#ADC178', 'Cluster 4': '#F0E5CB', 'Cluster 5': '#909090'}
        
    # Sunburst Plot | Customer Region, Last Promo, and Payment Method by Cluster
    fig_sunburst_cluster = px.sunburst(cluster_data,
                             path=['Cluster Name', 'customer_region_buckets', 'last_promo', 'payment_method'],
                             title='Sunburst Plot of Customer Region, Last Promo, and Payment Method by Cluster',
                             color='Cluster Name',
                             color_discrete_sequence=['#7B8F3A', '#F0E5CB', '#ADC178', '#2C3E1F', '#909090'],
                             labels={"Cluster Name": "Cluster", "customer_region_buckets": "Customer Region", "payment_method": "Payment Method", "last_promo": "Last Promo"},
                             height=1000)
    fig_sunburst_cluster.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=False)
    fig_sunburst_cluster.update_traces(hovertemplate='<b>Cluster/Customer Region/Last Promo/Payment Method</b>: %{id}<br><b>Number of Customers</b>: %{value}')
    st.plotly_chart(fig_sunburst_cluster, use_container_width=True)
    
    # --------------------------------------------------------------------------------------------
    # Barplot chain_count/order_count by Cluster
    # Add a new column 'chain_count/order_count' to the dataset
    cluster_data['chain_count/order_count'] = cluster_data['chain_count'] / (cluster_data['order_count'])
        
    # Create the bar plot
    fig_chain_cluster = px.bar(cluster_data.groupby(['chain_count/order_count', 'Cluster Name']).size().reset_index(name='mean').round(3),
                               x='Cluster Name',
                               y='mean',
                               color='chain_count/order_count',
                               custom_data = ['chain_count/order_count'],
                               color_continuous_scale=custom_scale,
                               title='Number of Orders by Chain and Cluster',
                               labels={"mean": "Number of Orders", "chain_count/order_count": "% Chain Count/Order Count", "Cluster Name": "Cluster"},
                               category_orders={"Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]})
    fig_chain_cluster.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_chain_cluster.update_traces(hovertemplate='<b>Number of Orders</b>: %{y}<br><b>% Chain/Order</b>: %{customdata[0]:.2%}')
    st.plotly_chart(fig_chain_cluster)    
    
    # --------------------------------------------------------------------------------------------
    # Funnel Chart | Most Spent Cuisine by Cluster
    funnel_cluster = cluster_data.groupby(['Cluster Name', 'CUI_Most_Spent_Cuisine']).size().reset_index()
    funnel_cluster.columns = ['Cluster Name', 'CUI_Most_Spent_Cuisine', 'number_of_customers']
    funnel_cluster = funnel_cluster.sort_values(by='number_of_customers', ascending=False)
    
    # Create a funnel chart of the most spent cuisine by cluster
    fig_funnel_cluster = px.funnel(funnel_cluster,
                                   x='number_of_customers',
                                   y='CUI_Most_Spent_Cuisine',
                                   title='Most Spent Cuisine by Cluster',
                                   color='Cluster Name',
                                   color_discrete_sequence=['#2C3E1F', '#7B8F3A', '#ADC178', '#F0E5CB', '#909090'],
                                   labels={"number_of_customers": "Number of Customers", "CUI_Most_Spent_Cuisine": "Most Spent Cuisine", "Cluster Name": "Cluster"},
                                   category_orders={"CUI_Most_Spent_Cuisine": cluster_data['CUI_Most_Spent_Cuisine'].value_counts().index[::-1],
                                                    "Cluster Name": ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]},
                                   height=1600)
    
    fig_funnel_cluster.update_layout(font=dict(family="Arial", size=12, color="black"), showlegend=True)
    fig_funnel_cluster.update_traces(hovertemplate='<b>Number of Customers</b>: %{x:.2f}<br><b>Most Spent Cuisine</b>: %{y}')
    st.plotly_chart(fig_funnel_cluster, use_container_width=True)