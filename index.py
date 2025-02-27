import streamlit as st

conversion_factors = {
    "Plane Angle": {
        "Degree": 1.0,
        "Radian": 57.2958,
        "Gradian": 0.9,
        "Arcsecond": 1 / 3600
    },

    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    },

    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    },

    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x - 32) * 5/9,
        "Kelvin": lambda x: x - 273.15
    },

    "Speed": {
        "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704
    },

    "Time": {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0
    },

    "Volume": {
        "Liter": 1.0,
        "Milliliter": 0.001,
        "Cubic meter": 1000.0,
        "Gallon (US)": 3.78541
    },

    "Pressure": {
        "Pascal": 1.0,
        "Kilopascal": 1000.0,
        "Bar": 100000.0
    },

    "Energy": {
        "Joule": 1.0,
        "Kilojoule": 1000.0,
        "Calorie": 4.184
    },

    "Power": {
        "Watt": 1.0,
        "Kilowatt": 1000.0
    },

    "Fuel Economy": {
        "Miles per gallon (US)": 1.0,
        "Kilometers per liter": 0.425144
    },

    "Data Transfer Rate": {
        "Bits per second": 1.0,
        "Kilobits per second": 1000.0,
        "Megabits per second": 1e6
    },

    "Digital Storage": {
        "Bit": 1.0,
        "Byte": 8.0,
        "Kilobyte": 8000.0,
        "Megabyte": 8e6
    },

    "Force": {
        "Newton": 1.0,
        "Dyne": 1e-5,
        "Kilogram-force": 9.80665
    },

    "Torque": {
        "Newton meter": 1.0,
        "Dyne centimeter": 1e-7,
        "Foot pound": 1.35582
    },

    "Frequency": {
        "Hertz": 1.0,
        "Kilohertz": 1000.0,
        "Megahertz": 1e6,
        "Gigahertz": 1e9
    },

    "Electric Charge": {
        "Coulomb": 1.0,
        "Milliampere hour": 3.6,
        "Ampere hour": 3600.0
    },

    "Electric Current": {
        "Ampere": 1.0,
        "Milliampere": 0.001,
        "Kiloampere": 1000.0
    },

    "Voltage": {
        "Volt": 1.0,
        "Millivolt": 0.001,
        "Kilovolt": 1000.0
    },

    "Resistance": {
        "Ohm": 1.0,
        "Kiloohm": 1000.0,
        "Megaohm": 1e6
    },

    "Capacitance": {
        "Farad": 1.0,
        "Microfarad": 1e-6,
        "Nanofarad": 1e-9
    },

    "Magnetic Flux": {
        "Weber": 1.0,
        "Maxwell": 1e-8,
        "Tesla meter squared": 1.0
    },

    "Illuminance": {
        "Lux": 1.0,
        "Foot-candle": 10.764
    },

    "Luminance": {
        "Candela per square meter": 1.0,
        "Nit": 1.0
    },

    "Radioactivity": {
        "Becquerel": 1.0,
        "Curie": 3.7e10
    },

    "Sound Level": {
        "Decibel": 1.0,
        "Bel": 10.0
    }
}



def convert_units(value, from_unit, to_unit, category):
    factors = conversion_factors.get(category, {})

    if category == "Temperature":
        base_value = factors[from_unit](value)  
        return factors[to_unit](base_value)  
    
    return (value * factors[from_unit]) / factors[to_unit]  



st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("📏 Universal Unit Converter")


conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

with col2:
   st.markdown("""<h2 style='text-align: center;'>⇄</h2>""", unsafe_allow_html=True)

with col3: 
    to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

try:
    if st.button("Click to Convert"):
     value2 = convert_units(value1, from_unit, to_unit, conversion_type)
     st.markdown(f"<p style='text-align: center; font-size: 28px; color: green;'>Result : {from_unit} to {to_unit} = {value2:.4f}  </p> ", unsafe_allow_html=True)


except Exception as e:
    st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)