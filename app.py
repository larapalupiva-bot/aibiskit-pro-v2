import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI KEAMANAN & API ---
# Gantilah "rahasia-aibiskit-2026" dengan password keinginan Anda untuk pembeli
PASSWORD_AKSES = "aibis2026" 

# Mengambil API Key dari Streamlit Secrets secara otomatis
try:
    GEMINI_API_KEY = st.secrets["AIzaSyD1bc4QKiq_WAGr6qfFqNI7Lwg97vHWz5A"]
    genai.configure(api_key=GEMINI_API_KEY)
    # Menggunakan model gemini-1.5-flash untuk kecepatan dan biaya termurah
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Konfigurasi API Belum Benar. Pastikan GEMINI_API_KEY sudah ada di Settings > Secrets.")

# --- 2. LOGIKA KITAB STANDAR AIBISKIT (POIN 1-13 + ANTI-TELEPORTASI) ---
def aibiskit_cleaner(user_input, mode="video"):
    # Di sini saya sudah memasukkan aturan agar ikan tidak muncul tiba-tiba (Occlusion Logic)
    standard_rules = """
    STRICT RULES FOR ASMR REALISM:
    1. 30/70 Framing Rule: Foreground covers max 30%.
    2. Zero-Drift: Fixed Tripod Shot, No Zoom, No Panning.
    3. Organic Material: Subsurface scattering, micro-pores, realistic mass.
    4. Still-Water Protocol: Micro-particles only, strictly NO large scuba bubbles.
    5. Motion Scale: 2 (Subtle movement).
    6. Occlusion Persistence: Entities MUST enter from frame edges or from behind static anchors. 
       PROHIBIT sudden appearing/disappearing (No teleporting).
    7. Impact Reaction: Symmetrical slicing with realistic recoil.
    """
    
    if mode == "video":
        prompt = f"Act as AIBisKit Engine. Convert this into a professional ASMR VIDEO prompt: {user_input}. {standard_rules}"
    else:
        prompt = f"Act as AIBisKit Engine. Convert this into a professional ASMR PHOTO prompt: {user_input}. {standard_rules} Focus on hyper-realistic textures and soft light fall-off."
    
    return prompt

# --- 3. TAMPILAN ANTARMUKA (USER INTERFACE) ---
st.set_page_config(page_title="AIBisKit Pro v2.0", layout="centered")

# Sidebar Tutorial untuk Pembeli
with st.sidebar:
    st.title("🎨 AIBisKit Pro")
    st.markdown("---")
    st.success("✅ Engine: Gemini 1.5 Flash Active")
    st.info("""
    **Cara Pakai:**
    1. Masukkan Password Akses.
    2. Ketik objek (Misal: Ikan Karang).
    3. Klik Generate.
    4. Copy hasil ke Runway/Luma/DALL-E.
    """)
    st.write("---")
    st.caption("Standardized by AIBisKit Logic © 2026")

# Halaman Login
st.title("🚀 AIBisKit: Professional ASMR Tool")
password_input = st.text_input("Masukkan Kunci Akses Pembeli:", type="password")

if password_input == PASSWORD_AKSES:
    st.write("### Akses Diterima. Silakan buat prompt Anda:")
    
    # Input dari User
    user_query = st.text_input("Apa yang ingin Anda visualisasikan?", placeholder="Contoh: Potong jeruk nipis segar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔥 Generate PROMPT VIDEO"):
            if user_query:
                with st.spinner("Mengolah Fisika Video..."):
                    final_request = aibiskit_cleaner(user_query, "video")
                    response = model.generate_content(final_request)
                    st.subheader("Copy Prompt Video:")
                    st.code(response.text)
                    st.caption("Gunakan di: Runway Gen-3, Luma Dream Machine, atau Kling.")
            else:
                st.warning("Masukkan deskripsi dulu!")

    with col2:
        if st.button("📸 Generate PROMPT FOTO"):
            if user_query:
                with st.spinner("Mengolah Tekstur Mikro..."):
                    final_request = aibiskit_cleaner(user_query, "photo")
                    response = model.generate_content(final_request)
                    st.subheader("Copy Prompt Foto:")
                    st.code(response.text)
                    st.caption("Gunakan di: Midjourney, DALL-E 3, atau Leonardo AI.")
            else:
                st.warning("Masukkan deskripsi dulu!")

else:
    if password_input != "":
        st.error("Kunci Akses Salah! Silakan hubungi Admin.")
    st.info("Akses Terkunci. Masukkan password untuk menggunakan AIBisKit.")
