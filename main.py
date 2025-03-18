import streamlit as st

# Title of the app
st.title("Unit Converter")

# Conversion type selection
conversion_type = st.selectbox(
    "Select Conversion Type:",
    ["Select", "Length", "Weight", "Temperature"],
    index=0
)


# Function to convert length
def convert_length(value, from_unit, to_unit):
    conversions = {
        ("Meters", "Kilometers"): value / 1000,
        ("Kilometers", "Meters"): value * 1000,
        ("Meters", "Feet"): value * 3.28084,
        ("Feet", "Meters"): value / 3.28084,
    }
    return conversions.get((from_unit, to_unit), value)  # No conversion if same unit


# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    conversions = {
        ("Kilograms", "Pounds"): value * 2.20462,
        ("Pounds", "Kilograms"): value / 2.20462,
        ("Kilograms", "Grams"): value * 1000,
        ("Grams", "Kilograms"): value / 1000,
    }
    return conversions.get((from_unit, to_unit), value)


# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        return value


# Show conversion options after a type is selected
if conversion_type != "Select":
    st.subheader(f"{conversion_type} Converter")

    if conversion_type == "Length":
        units = ["Meters", "Kilometers", "Feet"]
    elif conversion_type == "Weight":
        units = ["Kilograms", "Pounds", "Grams"]
    else:  # Temperature
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units, key="from_unit")
    with col2:
        to_unit = st.selectbox("To", units, key="to_unit")

    if st.button("Swap Units"):
        from_unit, to_unit = to_unit, from_unit

    value = st.number_input("Enter value", value=0.0, key="input_value")

    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    else:
        result = convert_temperature(value, from_unit, to_unit)

    st.text_input("Converted value", value=f"{result} {to_unit}", disabled=True)
