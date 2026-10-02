import streamlit as st

def load_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        /* ANIMATED COLOR BREEZE BACKGROUND FOR WHOLE WEBSITE */
        @keyframes colorBreeze {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            background: linear-gradient(-45deg, #fffdf8, #fef3c7, #fde68a, #fcd34d, #fff7ed, #fef08a) !important;
            background-size: 400% 400% !important;
            animation: colorBreeze 16s ease infinite !important;
            color: #451a03 !important;
        }

        /* STREAMLIT CONTAINER ADJUSTMENT */
        .main .block-container {
            max-width: 100% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            padding-top: 1rem !important;
            overflow: visible !important;
        }

        /* BRAND HEADER */
        .brand-header {
            text-align: center;
            padding: 10px 0 20px 0;
        }
        
        .brand-logo {
            font-size: 2.8rem;
            font-family: 'Playfair Display', serif;
            font-weight: 800;
            letter-spacing: 3px;
            color: #78350f;
            text-transform: uppercase;
            text-shadow: 2px 2px 10px rgba(217, 119, 6, 0.15);
        }

        .brand-sub {
            font-size: 0.82rem;
            letter-spacing: 4px;
            color: #b45309;
            text-transform: uppercase;
            font-weight: 700;
        }

        /* FULL HORIZONTAL NAVIGATION RIBBON CONTAINER */
        div[data-testid="stRadio"] {
            width: 100% !important;
            margin-bottom: 30px !important;
        }

        /* LIGHT CREAMY GLASS STRIP (FULL WIDTH) */
        div[data-testid="stRadio"] > div {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            justify-content: space-between !important;
            align-items: center !important;
            background: linear-gradient(135deg, rgba(255, 253, 245, 0.95), rgba(254, 243, 199, 0.9)) !important;
            padding: 8px 12px !important;
            border-top: 2px solid rgba(245, 158, 11, 0.3) !important;
            border-bottom: 2px solid rgba(245, 158, 11, 0.3) !important;
            box-shadow: 0 8px 25px rgba(217, 119, 6, 0.1) !important;
            backdrop-filter: blur(12px) !important;
            border-radius: 16px !important;
            box-sizing: border-box !important;
        }

        /* HIDE ALL RADIO BUTTON CIRCLES / DOTS / SVG ICONS COMPLETELY */
        div[data-testid="stRadio"] input[type="radio"],
        div[data-testid="stRadio"] div[role="radio"] > div:first-child,
        div[data-testid="stRadio"] label > div:first-child,
        div[data-testid="stRadio"] svg,
        div[data-testid="stRadio"] circle {
            display: none !important;
            width: 0 !important;
            height: 0 !important;
            visibility: hidden !important;
            opacity: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* NAVIGATION ITEM TABS */
        div[data-testid="stRadio"] label {
            flex: 1 1 0% !important;
            text-align: center !important;
            justify-content: center !important;
            padding: 12px 16px !important;
            border-radius: 12px !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            margin: 0 4px !important;
            white-space: nowrap !important;
            background: transparent !important;
        }

        div[data-testid="stRadio"] label p {
            color: #78350f !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            margin: 0 !important;
            text-align: center !important;
            width: 100% !important;
        }

        /* HOVER STATE */
        div[data-testid="stRadio"] label:hover {
            background: rgba(254, 243, 199, 0.8) !important;
        }

        /* ACTIVE SELECTED TAB PILL */
        div[data-testid="stRadio"] label[data-checked="true"],
        div[data-testid="stRadio"] label:has(input:checked) {
            background: linear-gradient(135deg, #d97706 0%, #b45309 100%) !important;
            box-shadow: 0 4px 15px rgba(180, 83, 9, 0.25) !important;
        }

        div[data-testid="stRadio"] label[data-checked="true"] p,
        div[data-testid="stRadio"] label:has(input:checked) p {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        /* SIDEBAR STYLES */
        [data-testid="stSidebar"] {
            background: rgba(255, 252, 245, 0.88) !important;
            backdrop-filter: blur(12px) !important;
            border-right: 2px solid rgba(245, 158, 11, 0.3) !important;
        }

        .cart-3d-box {
            background: linear-gradient(145deg, #ffffff, #fef3c7);
            border-radius: 16px;
            padding: 18px;
            border: 2px solid #f59e0b;
            box-shadow: 0 10px 20px rgba(217, 119, 6, 0.12);
            text-align: center;
        }

        /* PRODUCT CARDS */
        .product-card-frame {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 24px;
            border: 2px solid rgba(245, 158, 11, 0.3);
            box-shadow: 0 12px 30px rgba(180, 83, 9, 0.08);
            margin-bottom: 20px;
        }

        .product-badge {
            display: inline-block;
            background: linear-gradient(90deg, #d97706, #f59e0b);
            color: white;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }

        .product-card-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: #78350f;
        }

        .product-card-price {
            font-size: 1.8rem;
            font-weight: 800;
            color: #d97706;
            margin: 8px 0;
        }

        /* BUTTONS */
        .stButton > button {
            background: linear-gradient(90deg, #d97706 0%, #f59e0b 100%) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100%;
            padding: 10px 20px !important;
            box-shadow: 0 6px 18px rgba(217, 119, 6, 0.25) !important;
        }

        /* FOOTER */
        .footer-container {
            background-color: #291205;
            color: #fef3c7;
            padding: 35px;
            border-radius: 20px;
            margin-top: 50px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)