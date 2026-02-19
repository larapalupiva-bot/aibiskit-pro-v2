import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI KEAMANAN & API ---
# Gantilah "rahasia-aibiskit-2026" dengan password keinginan Anda
PASSWORD_AKSES = "aibis2026" 
GEMINI_API_KEY = "AIzaSyD1bc4QKiq_WAGr6qfFqNI7Lwg97vHWz5A"

# Konfigurasi AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. LOGIKA KITAB STANDAR AIBISKIT (POIN 1-13) ---
def aibiskit_cleaner(user_input, mode="video"):
    standard_rules = """
    Rules: 1. 30/70 Framing. 2. Locked-off Fixed Tripod Shot (No Zoom/Drift). 
    3. Organic Texture (Subsurface scattering). 4. Soft Fall-off Lighting. 
    5. Still-Water Protocol (Micro-particles, No scuba bubbles). 
    6. Motion Scale 2. 7. Symmetrical Slicing. 8. Occlusion Persistence.
    """
    
    if mode == "video":
        prompt = f"Act as AIBisKit Engine. Transform this into a professional ASMR VIDEO prompt: {user_input}. {standard_rules}"
    else:
        prompt = f"Act as AIBisKit Engine. Transform this into a professional ASMR PHOTO prompt: {user_input}. {standard_rules} Focus on micro-pores and macro detail."
    
    return prompt

# --- 3. TAMPILAN ANTARMUKA (UI) ---
st.set_page_config(page_title="AIBisKit Pro - Official Tool", layout="wide")

# Sidebar Help (SOP Singkat)
with st.sidebar:
    st.title("🎨 AIBisKit v2.0")
    st.write("---")
    st.success("Status: Locked-Off System Active")
    st.markdown("""
    **SOP Input:**
    1. Sebutkan Subjek (Ikan, Sabun, Apel).
    2. Sebutkan Lokasi (Hutan, Dapur).
    3. Pilih Gaya (Claymation, Realistis).
    """)
    st.write("---")
    st.caption("AIBisKit © 2026 - Target: 100+ Users")

# Gerbang Password
st.title("🚀 AIBisKit Professional Tool")
password_input = st.text_input("Masukkan Kunci Akses Pembeli:", type="password")

if password_input == PASSWORD_AKSES:
    st.balloons()
    st.write("### Selamat Datang, Partner AIBisKit! 👋")
    
    # Input Utama
    user_query = st.text_input("Apa yang ingin Anda buat hari ini?", placeholder="Contoh: Ikan di terumbu karang Belang-Belang")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔥 Generate PROMPT VIDEO"):
            with st.spinner("Mencuci prompt sesuai standar..."):
                final_request = aibiskit_cleaner(user_query, "video")
                response = model.generate_content(final_request)
                st.subheader("Copy Prompt Video Ke Generator (Runway/Luma):")
                st.code(response.text)
                st.warning("Gunakan Negative Prompt: (zoom), (drifting), (large bubbles), (shaky)")

    with col2:
        if st.button("📸 Generate PROMPT FOTO"):
            with st.spinner("Menyusun detail mikro..."):
                final_request = aibiskit_cleaner(user_query, "photo")
                response = model.generate_content(final_request)
                st.subheader("Copy Prompt Foto Ke Generator (Midjourney/DALL-E):")
                st.code(response.text)
                st.info("Tips: Hasil terbaik gunakan aspect ratio 16:9")

else:
    if password_input != "":
        st.error("Kunci Akses Salah! Silakan hubungi admin untuk aktivasi.")
    st.info("Silakan masukkan Kunci Akses untuk membuka fitur AIBisKit.")
