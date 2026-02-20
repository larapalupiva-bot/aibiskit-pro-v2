import streamlit as st
import google.generativeai as genai

# --- 1. INISIALISASI ---
PASSWORD_AKSES = "rahasia-aibiskit-2026" 

if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # OTOMATIS: Mencari model yang mendukung generateContent
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # Mengutamakan Flash, jika tidak ada pakai model pertama yang tersedia
            selected_model = next((m for m in available_models if "flash" in m), available_models[0])
            model = genai.GenerativeModel(selected_model)
            api_aktif = True
        else:
            st.error("Tidak ada model Gemini yang ditemukan di akun Anda.")
            api_aktif = False
    except Exception as e:
        st.error(f"Koneksi API Gagal: {e}")
        api_aktif = False
else:
    st.error("GEMINI_API_KEY tidak ditemukan di Secrets!")
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
        return f"Transform to ASMR VIDEO prompt: {user_input}. {standard_rules}"
    return f"Transform to ASMR PHOTO prompt: {user_input}. {standard_rules}"

# --- 3. ANTARMUKA PENGGUNA ---
st.title("🚀 AIBisKit Professional Tool")
pass_input = st.text_input("Masukkan Kunci Akses:", type="password")

if pass_input == PASSWORD_AKSES:
    if api_aktif:
        user_query = st.text_input("Apa yang ingin Anda visualisasikan?", placeholder="Contoh: potong jeruk nipis")
        
        if st.button("🔥 Generate PROMPT VIDEO"):
            if user_query:
                try:
                    final_request = aibiskit_cleaner(user_query, "video")
                    response = model.generate_content(final_request)
                    st.subheader(f"Hasil Prompt (Model: {selected_model}):")
                    st.code(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Isi deskripsi dulu!")
    else:
        st.error("Cek kembali pengaturan Secrets Anda.")
else:
    if pass_input != "":
        st.error("Password Salah!")
