import streamlit as st
import streamlit.components.v1 as components
from styles import load_css

# 1. Page Configuration
st.set_page_config(
    page_title="Nalanda Honey | Premium Raw Artisanal Honey",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
load_css()

# 2. Session State Cart Initialization
if "cart" not in st.session_state:
    st.session_state.cart = {}

PRODUCTS = {
    "honey_500g": {
        "name": "Nalanda Raw Honey",
        "weight": "500g (17.6 oz)",
        "price": 209.00,
        "badge": "Handcrafted Harvest",
        "description": "Pure raw wildflower honey featuring natural floral aromas and active enzymes. Ideal for daily tea, warm drinks, and breakfasts."
    },
    "honey_1kg": {
        "name": "Nalanda Raw Honey",
        "weight": "1kg (35.2 oz)",
        "price": 399.00,
        "badge": "Best Value Family Pack",
        "description": "Our flagship 1kg glass jar harvest. Cold-extracted, unheated, and unfiltered to retain maximum purity and golden caramel flavor."
    }
}

def add_to_cart(product_key, qty):
    if product_key in st.session_state.cart:
        st.session_state.cart[product_key] += qty
    else:
        st.session_state.cart[product_key] = qty
    product = PRODUCTS[product_key]
    st.toast(f"Added {qty}x {product['name']} ({product['weight']}) to cart! 🐝", icon="🛒")

# 3. Sidebar Shopping Cart
st.sidebar.markdown("""
    <div class="sidebar-brand-box">
        <div style="font-size:2rem;">🐝</div>
        <div style="font-family:'Playfair Display'; font-size:1.4rem; font-weight:800; color:#78350f;">NALANDA HONEY</div>
        <div style="font-size:0.75rem; color:#b45309; letter-spacing:1px; font-weight:600;">PURE ARTISANAL HARVEST</div>
    </div>
""", unsafe_allow_html=True)

total_items = sum(st.session_state.cart.values())
total_amount = sum(st.session_state.cart[key] * PRODUCTS[key]["price"] for key in st.session_state.cart)

st.sidebar.markdown(f"""
    <div class="cart-3d-box">
        <div style="font-size: 2.2rem; margin-bottom: 5px;">🛒</div>
        <h3 style="margin:0; font-family:'Playfair Display'; color:#78350f; font-size:1.2rem;">Your Shopping Cart</h3>
        <p style="color:#b45309; font-weight:600; margin:5px 0;">{total_items} Jar(s) Selected</p>
        <div style="font-size:1.4rem; font-weight:800; color:#d97706; margin:8px 0;">₹{total_amount:.2f}</div>
    </div>
""", unsafe_allow_html=True)

if total_items > 0:
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Selected Items:**")
    for key, qty in st.session_state.cart.items():
        if qty > 0:
            p = PRODUCTS[key]
            st.sidebar.caption(f"• {qty}x {p['name']} ({p['weight']}) - ₹{p['price'] * qty:.2f}")

st.write("")
if total_items > 0:
    if st.sidebar.button("Checkout Now"):
        st.sidebar.balloons()
        st.sidebar.success("Thank you for ordering Nalanda Premium Honey!")
        st.session_state.cart = {}
    
    if st.sidebar.button("Clear Cart"):
        st.session_state.cart = {}
        st.rerun()
else:
    st.sidebar.caption("Your cart is currently empty.")

# 4. Header Banner
st.markdown("""
    <div class="brand-header">
        <div class="brand-sub">Est. 2021 • Unfiltered & Raw</div>
        <div class="brand-logo">Nalanda Honey</div>
    </div>
""", unsafe_allow_html=True)

# Full-Width Elegant Golden Ribbon Navigation
navigation = st.radio(
    "Navigation Menu",
    ["Our Honey Showcase", "Why Nalanda?", "Recipes", "Contact Us"],
    horizontal=True,
    label_visibility="collapsed"
)

# 5. Helper Function for 3D Interactive Three.js Jar
def generate_3d_jar_code(weight_text):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; background: transparent; }}
            canvas {{ width: 100%; height: 100%; display: block; }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    </head>
    <body>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0, 7);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.body.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.enableZoom = false;

            const ambientLight = new THREE.AmbientLight(0xfffbeb, 1.2);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0xffffff, 1.6);
            dirLight.position.set(5, 10, 7);
            scene.add(dirLight);

            const pointLight = new THREE.PointLight(0xf59e0b, 2.5, 10);
            pointLight.position.set(0, 0, 2);
            scene.add(pointLight);

            const labelCanvas = document.createElement('canvas');
            labelCanvas.width = 512;
            labelCanvas.height = 256;
            const ctx = labelCanvas.getContext('2d');

            ctx.fillStyle = '#fffcf5';
            ctx.fillRect(0, 0, 512, 256);
            ctx.strokeStyle = '#d97706';
            ctx.lineWidth = 10;
            ctx.strokeRect(15, 15, 482, 226);

            ctx.fillStyle = '#78350f';
            ctx.font = 'bold 36px serif';
            ctx.textAlign = 'center';
            ctx.fillText('NALANDA HONEY', 256, 110);

            ctx.fillStyle = '#b45309';
            ctx.font = '18px sans-serif';
            ctx.fillText('PREMIUM RAW & UNFILTERED', 256, 150);
            ctx.fillText('NET WT. {weight_text}', 256, 185);

            const labelTexture = new THREE.CanvasTexture(labelCanvas);

            const jarGroup = new THREE.Group();

            const glassGeo = new THREE.CylinderGeometry(1.2, 1.1, 2.2, 32);
            const glassMat = new THREE.MeshPhysicalMaterial({{
                color: 0xd97706,
                transmission: 0.6,
                opacity: 0.9,
                transparent: true,
                roughness: 0.1,
                metalness: 0.1,
                ior: 1.5
            }});
            const glassBody = new THREE.Mesh(glassGeo, glassMat);
            jarGroup.add(glassBody);

            const honeyGeo = new THREE.CylinderGeometry(1.12, 1.02, 1.9, 32);
            const honeyMat = new THREE.MeshStandardMaterial({{
                color: 0xf59e0b,
                roughness: 0.2,
                metalness: 0.2,
                emissive: 0x78350f,
                emissiveIntensity: 0.2
            }});
            const honeyCore = new THREE.Mesh(honeyGeo, honeyMat);
            honeyCore.position.y = -0.1;
            jarGroup.add(honeyCore);

            const lidGeo = new THREE.CylinderGeometry(1.25, 1.25, 0.4, 32);
            const lidMat = new THREE.MeshStandardMaterial({{
                color: 0xb45309,
                metalness: 0.8,
                roughness: 0.3
            }});
            const lid = new THREE.Mesh(lidGeo, lidMat);
            lid.position.y = 1.3;
            jarGroup.add(lid);

            const labelGeo = new THREE.CylinderGeometry(1.21, 1.21, 1.1, 32, 1, true, -Math.PI/2.5, (2*Math.PI)/2.5);
            const labelMat = new THREE.MeshBasicMaterial({{ map: labelTexture, side: THREE.DoubleSide }});
            const label = new THREE.Mesh(labelGeo, labelMat);
            label.position.y = 0.05;
            jarGroup.add(label);

            scene.add(jarGroup);

            function animate() {{
                requestAnimationFrame(animate);
                jarGroup.rotation.y += 0.008;
                controls.update();
                renderer.render(scene, camera);
            }}
            animate();

            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """

# 6. Focal Carousel HTML
HORIZONTAL_FOCAL_CAROUSEL_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap');

    * { box-sizing: border-box; }
    body {
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: 'Plus Jakarta Sans', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow: hidden;
    }

    .carousel-container {
        position: relative;
        width: 100%;
        max-width: 900px;
        height: 310px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        position: absolute;
        width: 380px;
        height: 230px;
        background: linear-gradient(145deg, #2a1b12, #180d07);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 22px;
        padding: 28px 32px;
        color: #fef3c7;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        transition: all 0.7s cubic-bezier(0.25, 1, 0.5, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        cursor: pointer;
    }

    .card-icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
    }

    .card-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: #fbbf24;
        margin: 0 0 10px 0;
    }

    .card-text {
        font-size: 0.92rem;
        color: #fde68a;
        line-height: 1.55;
        margin: 0;
        opacity: 0.9;
    }

    .card.center {
        transform: translateX(0) scale(1);
        opacity: 1;
        filter: blur(0px);
        z-index: 10;
        border-color: #f59e0b;
        box-shadow: 0 25px 50px rgba(217, 119, 6, 0.35), 0 0 20px rgba(245, 158, 11, 0.2);
    }

    .card.left {
        transform: translateX(-260px) scale(0.82);
        opacity: 0.3;
        filter: blur(5px);
        z-index: 5;
    }

    .card.right {
        transform: translateX(260px) scale(0.82);
        opacity: 0.3;
        filter: blur(5px);
        z-index: 5;
    }

    .card.hidden {
        transform: translateX(0) scale(0.6);
        opacity: 0;
        filter: blur(10px);
        z-index: 1;
    }

    .indicators {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 10px;
    }

    .dot {
        width: 10px;
        height: 10px;
        background-color: rgba(217, 119, 6, 0.3);
        border-radius: 50%;
        transition: all 0.4s ease;
        cursor: pointer;
    }

    .dot.active {
        width: 28px;
        height: 10px;
        border-radius: 10px;
        background-color: #d97706;
        box-shadow: 0 0 10px rgba(217, 119, 6, 0.6);
    }
</style>
</head>
<body>

<div class="carousel-container" id="carousel">
    <div class="card center" onclick="setIndex(0)">
        <div class="card-icon">🍯</div>
        <div class="card-title">100% Raw & Unfiltered</div>
        <div class="card-text">Preserving active natural pollens, aromatic nectar, and living beneficial enzymes.</div>
    </div>
    <div class="card right" onclick="setIndex(1)">
        <div class="card-icon">🐝</div>
        <div class="card-title">Ethically Sourced</div>
        <div class="card-text">Gentle extraction methods that protect bee colonies and natural flower reserves.</div>
    </div>
    <div class="card hidden" onclick="setIndex(2)">
        <div class="card-icon">🌿</div>
        <div class="card-title">Pure Origin Guaranteed</div>
        <div class="card-text">Zero added sugars, artificial preservatives, high-fructose corn syrup, or fillers.</div>
    </div>
    <div class="card left" onclick="setIndex(3)">
        <div class="card-icon">✨</div>
        <div class="card-title">Rich Golden Taste</div>
        <div class="card-text">Smooth, aromatic amber caramel floral notes packed in every single spoonful.</div>
    </div>
</div>

<div class="indicators">
    <div class="dot active" onclick="setIndex(0)"></div>
    <div class="dot" onclick="setIndex(1)"></div>
    <div class="dot" onclick="setIndex(2)"></div>
    <div class="dot" onclick="setIndex(3)"></div>
</div>

<script>
    const cards = document.querySelectorAll('.card');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;

    function renderCarousel() {
        cards.forEach((card, i) => {
            card.className = 'card';
            let pos = (i - currentIndex + cards.length) % cards.length;

            if (pos === 0) {
                card.classList.add('center');
            } else if (pos === 1) {
                card.classList.add('right');
            } else if (pos === cards.length - 1) {
                card.classList.add('left');
            } else {
                card.classList.add('hidden');
            }
        });

        dots.forEach((dot, i) => {
            dot.className = i === currentIndex ? 'dot active' : 'dot';
        });
    }

    function setIndex(index) {
        currentIndex = index;
        renderCarousel();
    }

    setInterval(() => {
        currentIndex = (currentIndex + 1) % cards.length;
        renderCarousel();
    }, 3500);
</script>

</body>
</html>
"""

# 7. Render Views
if navigation == "Our Honey Showcase":
    st.markdown("<h2 style='text-align: center; color: #78350f; font-family: Playfair Display; margin-bottom: 25px;'>Symmetrical Product Showcase</h2>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2)

    # --- PRODUCT 1: 500g Jar (₹209) ---
    with col_left:
        p1 = PRODUCTS["honey_500g"]
        st.markdown(f"""
            <div class="product-card-frame">
                <div>
                    <span class="product-badge">{p1['badge']}</span>
                    <div class="product-card-title">{p1['name']} ({p1['weight']})</div>
                    <div class="product-card-price">₹{p1['price']:.2f}</div>
                    <p style="color: #78350f; font-size: 0.92rem; line-height: 1.5; margin: 0;">
                        {p1['description']}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        components.html(generate_3d_jar_code("500g"), height=290)

        q1, b1 = st.columns([1, 1.8])
        with q1:
            qty_500 = st.number_input("Quantity", min_value=1, max_value=20, value=1, key="qty_500g")
        with b1:
            st.write("")
            st.write("")
            if st.button("🛒 Add 500g Jar", key="btn_500g"):
                add_to_cart("honey_500g", qty_500)

    # --- PRODUCT 2: 1kg Jar (₹399) ---
    with col_right:
        p2 = PRODUCTS["honey_1kg"]
        st.markdown(f"""
            <div class="product-card-frame">
                <div>
                    <span class="product-badge">{p2['badge']}</span>
                    <div class="product-card-title">{p2['name']} ({p2['weight']})</div>
                    <div class="product-card-price">₹{p2['price']:.2f}</div>
                    <p style="color: #78350f; font-size: 0.92rem; line-height: 1.5; margin: 0;">
                        {p2['description']}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        components.html(generate_3d_jar_code("1KG"), height=290)

        q2, b2 = st.columns([1, 1.8])
        with q2:
            qty_1k = st.number_input("Quantity", min_value=1, max_value=20, value=1, key="qty_1kg")
        with b2:
            st.write("")
            st.write("")
            if st.button("🛒 Add 1kg Jar", key="btn_1kg"):
                add_to_cart("honey_1kg", qty_1k)

    st.markdown("---")

    # Rotational Carousel Section
    st.markdown("<h2 style='text-align: center; color: #78350f; font-family: Playfair Display; margin: 30px 0;'>Why Nalanda Premium Raw Honey?</h2>", unsafe_allow_html=True)
    components.html(HORIZONTAL_FOCAL_CAROUSEL_HTML, height=360)

elif navigation == "Why Nalanda?":
    st.markdown("<h1 style='color: #78350f; font-family: Playfair Display; text-align: center;'>Our Legacy & Quality Standards</h1>", unsafe_allow_html=True)
    st.write("""
    At **Nalanda Honey**, we offer pure raw harvests in 500g and 1kg glass jars. 
    By preserving active pollens and live enzymes without heat processing, every jar brings rich natural flavor straight from our beehives to your doorstep.
    """)

elif navigation == "Recipes":
    st.markdown("<h1 style='color: #78350f; font-family: Playfair Display; text-align: center;'>Signature Recipes</h1>", unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    with r1:
        st.subheader("🐝 Warm Golden Honey Milk")
        st.write("Mix 1 tablespoon of Nalanda Premium Raw Honey into warm almond milk with a pinch of cinnamon.")
    with r2:
        st.subheader("🐝 Raw Honey Toast with Ricotta")
        st.write("Spread fresh ricotta on toasted sourdough and drizzle with warm Nalanda Raw Honey.")

elif navigation == "Contact Us":
    st.markdown("<h1 style='color: #78350f; font-family: Playfair Display; text-align: center;'>Contact Nalanda Honey</h1>", unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Inquiry")
        submit = st.form_submit_button("Submit Request")
        if submit:
            st.success("Thank you! The Nalanda Honey team will contact you shortly.")

# 8. Footer
st.markdown("""
    <div class="footer-container">
        <div class="footer-title">Nalanda Honey</div>
        <p style="font-size: 0.9rem; color: #fde68a;">Pure, Cold-Extracted Artisanal Raw Honey (500g & 1kg Harvests)</p>
        <p style="font-size: 0.8rem; margin-top: 15px; color: #d97706;">© 2026 Nalanda Honey. All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True)
