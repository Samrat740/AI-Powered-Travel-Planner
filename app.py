import streamlit as st
import google.generativeai as genai
import time

# ✅ Configure API Key
genai.configure(api_key="AIzaSyDHEtmaHRfAGRqBMphgYKw-M3VnEK9PDGk")

# ✅ Use a valid Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  

st.title("✈️ AI-Powered Travel Planner")

# User inputs
destination = st.text_input("Enter Your Destination:")
days = st.slider("Number of Days:", 1, 10, 3)
budget = st.selectbox("Select Budget Level:", ["Low", "Medium", "High"])

# ✅ Additional Specifications Dropdown
with st.expander("🛠️ Additional Specifications"):
    col1, col2 = st.columns(2)  # 2x2 Grid Layout

    with col1:
        interest_type = st.selectbox("Preferred Activities", ["Cultural", "Adventure", "Relaxation", "Food Tour", "Nightlife"])
        walking = st.selectbox("Walking Tolerance", ["High - Love exploring on foot!", "Moderate - Some walking is okay.", "Low - Prefer minimal walking."])

    with col2:
        diet = st.selectbox("Dietary Preferences", ["No Preference", "Veg-Food", "Non-Veg"])
        accommodation = st.selectbox("Accommodation Type", ["Budget", "Mid-range", "Luxury", "Near City Center", "Quiet Location"])

# Generate Itinerary Button
if st.button("Generate Itinerary"):
    user_prompt = f"""
    Plan a {days}-day trip to {destination} with a {budget} budget.
    User prefers {interest_type} activities, follows a {diet} diet,
    has {walking} walking tolerance, and wants {accommodation} accommodation.
    Provide a detailed structured itinerary.
    """

    # 🔄 Dynamic Loading Animation (HTML + CSS + Rotating Text)
    loading_html_template = """
    <div id="loading-overlay">
        <div class="loading-spinner"></div>
        <p id="loading-text">{message}</p>
    </div>
    <style>
        #loading-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            color: white;
            font-size: 20px;
            font-weight: bold;
        }}
        .loading-spinner {{
            width: 50px;
            height: 50px;
            border: 6px solid rgba(255, 255, 255, 0.3);
            border-top: 6px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
    """

    loading_messages = ["⏳ Planning your trip...", "🚀 Finding the best places...", "🌍 Creating your itinerary..."]
    
    loading_placeholder = st.empty()

    # Loop through messages and update the overlay dynamically
    for msg in loading_messages:
        loading_placeholder.markdown(loading_html_template.format(message=msg), unsafe_allow_html=True)
        time.sleep(1)  # Simulating processing time

    # Generate the response
    response = model.generate_content(user_prompt)

    # Remove the loading overlay
    loading_placeholder.empty()

    st.subheader("🗺️ Your AI-Generated Travel Itinerary:")
    st.write(response.text)

st.markdown("""
    <hr style="margin: 5px 0;">
    <p style='text-align: center; font-size: 14px; margin: 0;'>Developed by <b>Samrat Ghosh</b></p>
    <p style='text-align: center; font-size: 11px; margin: 0;'>Version <b>04.25.01</b></p>
""", unsafe_allow_html=True)

