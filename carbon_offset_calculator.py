import streamlit as st

# Set wide layout and page name at the beginning
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Define emission factors for various countries
EMISSION_FACTORS = {
    "France": {
        "Transportation": 0.103,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.060,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Smoking": 0.01,  # kgCO2 per cigarette
        "Plants": -22  # kg/tree/year
    },
    # Add other countries (India, Pakistan, etc.) as needed...
}

# Carbon offset costs (in USD per ton of CO2)
OFFSET_COSTS = {
    "Reforestation": 10,  # USD per ton CO2
    "Renewable Energy": 15,  # USD per ton CO2
    "Methane Capture": 20,  # USD per ton CO2
}

# Streamlit app code
st.title("Carbon Calculator ⚠️")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["France", "Hungary", "India", "Italy", "Pakistan"])

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🚗 Daily car distance (in km)")
    distance = st.slider("Distance", 0.0, 120.0, key="Car_distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

    st.subheader("🌳 Number of Trees Planted (per month)")
    Plants = st.number_input("Plants", 0, key="Plants_input")

with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 120.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

with col3:
    st.subheader("🚌 Daily Public Transport Use (in km)")
    Bus_Travel = st.slider("Distance", 0.0, 100.0, key="Bus_distance_input")
    
    st.subheader("🚬 Number of cigarettes per day")
    cigarette = st.number_input("Cigarette", 0, key="cigarette_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly
if Bus_Travel > 0:
    Bus_Travel = Bus_Travel * 365  # Convert to yearly
if cigarette > 0:
    cigarette = cigarette * 365  # Convert to yearly
if Plants > 0:
    Plants = Plants  # No need for conversion for planted trees

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste
cigarette_emissions = EMISSION_FACTORS[country]["Smoking"] * cigarette
Bus_Emissions = EMISSION_FACTORS[country]["Bus"] * Bus_Travel
C02_Saving = EMISSION_FACTORS[country]["Plants"] * Plants

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)
cigarette_emissions = round(cigarette_emissions / 1000, 2)
Bus_emissions = round(waste_emissions / 1000, 2)
CO2_Saving = round(C02_Saving / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions + Bus_Emissions + cigarette_emissions + C02_Saving, 2
)

# When the button is clicked, we show the results
if st.button("Calculate CO2 Emissions"):
    # Display results
    st.header("Your Carbon Footprint")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Private Transport: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        st.info(f"🚌 Public Transport: {Bus_Emissions} tonnes CO2 per year")
        st.info(f"🚬 Cigarettes: {cigarette_emissions} tonnes CO2 per year")
       
    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.info(f"☺️ CO2 Saved: {abs(CO2_Saving)} tonnes CO2 per year")

    # Carbon offset calculation
    st.subheader("Calculate your Carbon Offset Cost")
    offset_type = st.selectbox("Choose Offset Method:", list(OFFSET_COSTS.keys()))

    offset_cost_per_ton = OFFSET_COSTS[offset_type]
    total_offset_cost = total_emissions * offset_cost_per_ton

    st.success(f"The cost to offset your carbon footprint via {offset_type} is: ${total_offset_cost:.2f}")

# Button to toggle tips display
if st.button("Tips to reduce your carbon footprint"):
    st.session_state.show_tips = True

# Show tips if button clicked
if 'show_tips' in st.session_state and st.session_state.show_tips:
    st.header("Carbon Reduction Tips ⚡")
    st.write("""
    1. **Use Public Transport or Bike**: Reduce emissions by opting for buses, trains, or biking instead of driving.
    2. **Switch to Renewable Energy**: Power your home with renewable sources like solar or wind to cut electricity-related emissions.
    3. **Reduce Meat Consumption**: Eating plant-based meals can significantly lower your carbon footprint.
    4. **Minimize Waste**: Recycle, compost, and reduce single-use plastics to reduce emissions from waste management.
    """)
