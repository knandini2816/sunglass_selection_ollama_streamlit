import streamlit as st

# ==========================================================
# PAGE SETTINGS
# ==========================================================

st.set_page_config(
    page_title="LUXE VISION",
    page_icon="🕶️",
    layout="wide"
)

# ==========================================================
# CSS DESIGN
# ==========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #d6a75655 0%, transparent 25%),
        radial-gradient(circle at 90% 20%, #7b5e3b44 0%, transparent 25%),
        linear-gradient(135deg, #17120d, #2a1e16, #3b2a20, #14110e);

    color: #f7ead7;
}

header {
    visibility: hidden;
}

/* MAIN TITLE */

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 900;
    letter-spacing: 8px;
    color: #f4d58d;

    text-shadow:
        0 0 8px #d6a756,
        0 0 20px #d6a756,
        0 0 40px #8b642d;

    margin-top: 20px;
    margin-bottom: 5px;
}

/* SUBTITLE */

.subtitle {
    text-align: center;
    color: #e8c98c;
    font-size: 18px;
    letter-spacing: 7px;
    margin-bottom: 45px;
    text-transform: uppercase;
}

/* SECTION TITLE */

.section-title {
    color: #f0c674;
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 2px;

    margin-top: 40px;
    margin-bottom: 20px;

    text-shadow: 0 0 10px #9d6f32;
}

/* GLASS CARD */

.glass-card {
    background:
        linear-gradient(
            145deg,
            rgba(255,239,210,0.12),
            rgba(40,25,15,0.55)
        );

    backdrop-filter: blur(18px);

    border: 1px solid #c89b4b66;

    border-radius: 25px;

    padding: 28px;

    box-shadow:
        0 15px 40px #00000066,
        inset 0 1px 0 #ffffff22;
}

/* INPUT */

.stTextInput input {

    background: #f8efe2 !important;

    color: #241b14 !important;

    border: 2px solid #b88a43 !important;

    border-radius: 14px !important;

    padding: 14px !important;

    font-size: 17px !important;
}

.stTextInput input:focus {

    border-color: #e7bd69 !important;

    box-shadow:
        0 0 12px #d6a75688 !important;
}

/* SELECT BOX */

.stSelectbox > div > div {

    background: #f8efe2 !important;

    color: #241b14 !important;

    border: 2px solid #b88a43 !important;

    border-radius: 14px !important;
}

/* LABELS */

label {

    color: #f2d49b !important;

    font-weight: 700 !important;

    font-size: 16px !important;
}

/* BUTTON */

.stButton button {

    width: 100%;

    height: 55px;

    border-radius: 15px;

    border: 1px solid #e1b65e;

    color: #20160f !important;

    font-size: 16px;

    font-weight: 900;

    letter-spacing: 1px;

    background:
        linear-gradient(
            135deg,
            #f5d99a,
            #c79643,
            #f1cf82
        );

    box-shadow:
        0 8px 25px #00000066,
        0 0 15px #d6a75633;

    transition: 0.3s;
}

.stButton button:hover {

    transform: translateY(-3px);

    background:
        linear-gradient(
            135deg,
            #ffe6a9,
            #d4a64f,
            #ffe09a
        );

    box-shadow:
        0 12px 30px #00000088,
        0 0 25px #e2b75e88;
}

/* SUCCESS */

.stSuccess {

    background: #27351f !important;

    border: 1px solid #8cae68 !important;

    border-radius: 15px;

    color: #e9f4d9 !important;
}

/* ERROR */

.stError {

    background: #3a211c !important;

    border: 1px solid #b86d55 !important;

    border-radius: 15px;
}

/* FOOTER */

.footer {

    text-align: center;

    margin-top: 60px;

    padding: 25px;

    color: #bda981;

    font-size: 13px;

    letter-spacing: 4px;

    border-top: 1px solid #c99a4a33;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #17120d;
}

::-webkit-scrollbar-thumb {

    background: #b88a43;

    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🕶️ LUXE VISION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✦ SEE THE WORLD DIFFERENTLY ✦</div>',
    unsafe_allow_html=True
)


# ==========================================================
# CUSTOMER PROFILE
# ==========================================================

st.markdown(
    '<div class="section-title">👤 CREATE YOUR VISION PROFILE</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Full Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "Email Address",
        placeholder="example@gmail.com"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="+91 XXXXX XXXXX"
    )


with col2:

    face_shape = st.selectbox(
        "Choose Your Face Shape",
        [
            "Select face shape",
            "Oval",
            "Round",
            "Square",
            "Heart",
            "Diamond",
            "Rectangle"
        ]
    )

    frame_color = st.selectbox(
        "Preferred Frame Color",
        [
            "Black",
            "Gold",
            "Silver",
            "Brown",
            "Transparent",
            "Blue",
            "Pink"
        ]
    )

    budget = st.selectbox(
        "Your Budget",
        [
            "Under ₹2,000",
            "₹2,000 - ₹5,000",
            "₹5,000 - ₹10,000",
            "₹10,000 - ₹25,000",
            "Above ₹25,000"
        ]
    )


# ==========================================================
# BRAND SELECTION
# ==========================================================

st.markdown(
    '<div class="section-title">✨ CHOOSE YOUR BRAND</div>',
    unsafe_allow_html=True
)

brand = st.selectbox(
    "Select Brand",
    [
        "Ray-Ban",
        "Oakley",
        "Gucci",
        "Prada",
        "Persol",
        "No Preference"
    ]
)


# ==========================================================
# FIND YOUR PERFECT STYLE
# ==========================================================

st.markdown(
    '<div class="section-title">✨ FIND YOUR PERFECT STYLE</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    usage = st.selectbox(
        "Where will you mainly use your sunglasses?",
        [
            "Daily Wear",
            "Driving",
            "Travel",
            "Sports & Outdoor",
            "Beach & Vacation",
            "Fashion & Events"
        ]
    )


with col2:

    lens_type = st.selectbox(
        "Choose Your Lens Type",
        [
            "UV Protection",
            "Polarized",
            "Anti-Glare",
            "Photochromic",
            "Blue Light Protection"
        ]
    )


# ==========================================================
# STYLE PREFERENCE
# ==========================================================

st.markdown(
    '<div class="section-title">💫 YOUR STYLE PREFERENCE</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    frame_style = st.selectbox(
        "Frame Style",
        [
            "Aviator",
            "Round",
            "Wayfarer",
            "Square",
            "Cat-Eye",
            "Sports"
        ]
    )


with col2:

    lens_color = st.selectbox(
        "Lens Color",
        [
            "Black",
            "Brown",
            "Grey",
            "Blue",
            "Green",
            "Gradient"
        ]
    )


with col3:

    fit = st.selectbox(
        "Preferred Fit",
        [
            "Small",
            "Medium",
            "Large",
            "Oversized"
        ]
    )


# ==========================================================
# COMPLETE REGISTRATION
# ==========================================================

st.markdown(
    '<div class="section-title">🚀 COMPLETE YOUR REGISTRATION</div>',
    unsafe_allow_html=True
)

if st.button("✨ REGISTER & SAVE MY STYLE"):

    if not name or not email or not phone:

        st.error(
            "⚠️ Please complete your name, email and phone number."
        )

    elif face_shape == "Select face shape":

        st.error(
            "⚠️ Please select your face shape."
        )

    else:

        st.success(
            f"""
            🎉 Welcome to LUXE VISION, {name}!

            Your style profile has been created successfully.

            ━━━━━━━━━━━━━━━━━━━━━

            👤 PERSONAL DETAILS

            📧 Email: {email}

            📱 Phone: {phone}

            ━━━━━━━━━━━━━━━━━━━━━

            😎 FACE SHAPE

            {face_shape}

            ━━━━━━━━━━━━━━━━━━━━━

            🎨 FRAME COLOR

            {frame_color}

            ━━━━━━━━━━━━━━━━━━━━━

            💰 BUDGET

            {budget}

            ━━━━━━━━━━━━━━━━━━━━━

            ✨ BRAND

            {brand}

            ━━━━━━━━━━━━━━━━━━━━━

            🌎 MAIN USAGE

            {usage}

            ━━━━━━━━━━━━━━━━━━━━━

            🔍 LENS TYPE

            {lens_type}

            ━━━━━━━━━━━━━━━━━━━━━

            🕶️ FRAME STYLE

            {frame_style}

            🎨 LENS COLOR

            {lens_color}

            📐 FIT

            {fit}

            ━━━━━━━━━━━━━━━━━━━━━

            Thank you for choosing LUXE VISION! 🕶️
            """
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">

        🕶️ LUXE VISION

        &nbsp; • &nbsp;

        PREMIUM EYEWEAR EXPERIENCE

        &nbsp; • &nbsp;

        SEE THE WORLD DIFFERENTLY

    </div>
    """,
    unsafe_allow_html=True
)