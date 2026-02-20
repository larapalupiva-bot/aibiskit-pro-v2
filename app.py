import streamlit as st
import google.generativeai as genai

# --- 1. INISIALISASI (Bagian Paling Penting) ---
PASSWORD_AKSES = "rahasia-aibiskit-2026" 

# Sistem pengecekan kunci API yang lebih kuat
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Inisialisasi model secara global agar tidak kena NameError
        model = genai.GenerativeModel('gemini-1.5-flash')
        api_aktif = True
    except Exception as e:
        st.error(f"Gagal menginisialisasi AI: {e}")
        api_aktif = False
else:
    st.error("Kunci API tidak ditemukan di Secrets!")
    api_aktif = False

# --- 2. LOGIKA STANDAR AIBISKIT ---
def aibiskit_cleaner(user_input, mode="video"):
    standard_rules = """
    STRICT RULES: 1. 30/70 Framing. 2. Fixed Tripod (No Zoom/Drift). 
    3. Organic Texture. 4. Soft Fall-off Lighting. 
    5. Still-Water Protocol (Micro-particles, No large scuba bubbles). 
    6. Motion Scale 2. 7. Occlusion Persistence (No teleporting).
    """
    if mode == "video":
        return f"ASMR VIDEO prompt: {user_input}. {standard_rules}"
    return f"ASMR PHOTO prompt: {user_input}. {standard_rules}"

# --- 3. ANTARMUKA PENGGUNA ---
st.title("🚀 AIBisKit Professional Tool")
pass_input = st.text_input("Masukkan Kunci Akses:", type="password")

if pass_input == PASSWORD_AKSES:
    if api_aktif:
        user_query = st.text_input("Apa yang ingin Anda visualisasikan?", placeholder="Contoh: potong jeruk nipis")
        
        if st.button("🔥 Generate PROMPT VIDEO"):
            if user_query:
                final_request = aibiskit_cleaner(user_query, "video")
                # Memanggil model hanya jika api_aktif bernilai True
                response = model.generate_content(final_request)
                st.subheader("Hasil Prompt Video:")
                st.code(response.text)
            else:
                st.warning("Isi deskripsi dulu!")
    else:
        st.error("Aplikasi tidak bisa berjalan tanpa API Key yang benar di Secrets.")
else:
    if pass_input != "":
        st.error("Password Salah!")
