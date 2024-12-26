import streamlit as st

# Sample data for emission factors (in kg CO2 per unit)
emission_factors = {
    "Electricity (kWh)": 0.5,  # kg CO2 per kWh
    "Gasoline (liters)": 2.31,  # kg CO2 per liter
    "Diesel (liters)": 2.68,  # kg CO2 per liter
    "Waste (kg)": 0.5,  # kg CO2 per kg of waste
}

# Carbon offset costs (in USD per ton of CO2)
offset_costs = {
    "Reforestation": 10,  # USD per ton CO2
    "Renewable Energy": 15,  # USD per ton CO2
    "Methane Capture": 20,  # USD per ton CO2
}

# Function to calculate carbon footprint
def calculate_carbon_footprint(activities):
    total_emissions = 0
    for activity, amount in activities.items():
        factor = emission_factors.get(activity)
        if factor:
            total_emissions += amount * factor
    return total_emissions / 1000  # Convert from grams to tons

# Function to calculate offset cost
def calculate_offset_cost(emissions, offset_type):
    cost_per_ton = offset_costs.get(offset_type, 0)
    return emissions * cost_per_ton

# Streamlit UI elements
st.title("Carbon Offset Calculator")

# Input fields for various activities
electricity = st.number_input("Electricity (kWh):", min_value=0.0, value=0.0)
gasoline = st.number_input("Gasoline (liters):", min_value=0.0, value=0.0)
diesel = st.number_input("Diesel (liters):", min_value=0.0, value=0.0)
waste = st.number_input("Waste (kg):", min_value=0.0, value=0.0)

# Dropdown for selecting offset type
offset_type = st.selectbox("Choose Offset Type:", ["Reforestation", "Renewable Energy", "Methane Capture"])

# Button to calculate the results
if st.button("Calculate"):
    # Prepare activities data
    activities = {
        "Electricity (kWh)": electricity,
        "Gasoline (liters)": gasoline,
        "Diesel (liters)": diesel,
        "Waste (kg)": waste,
    }
    
    # Calculate carbon footprint
    emissions = calculate_carbon_footprint(activities)
    st.write(f"Total CO2 Emissions: {emissions:.2f} tons")
    
    # Calculate offset cost
    offset_cost = calculate_offset_cost(emissions, offset_type)
    st.write(f"Offset Cost ({offset_type}): ${offset_cost:.2f}")
