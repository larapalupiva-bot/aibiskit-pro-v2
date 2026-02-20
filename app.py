import streamlit as st

# --- 1. PENGATURAN KEAMANAN ---
# Ganti password ini untuk pembeli Anda
PASSWORD_AKSES = "rahasia-aibiskit-2026"

# --- 2. LOGIKA INTERNAL AIBISKIT (TANPA API) ---
def generate_manual_prompt(user_input, mode="video"):
    # Semua aturan Poin 1-13 disimpan di sini sebagai teks permanen
    rules = (
        "Rules: 1. 30/70 Framing. 2. Fixed Tripod Shot (No Zoom/Drift). "
        "3. Organic Texture (Subsurface scattering, micro-pores). "
        "4. Soft Fall-off Lighting (45-degree side lighting). "
        "5. Still-Water Protocol (Micro-particles, No large bubbles). "
        "6. Motion Scale: 2. 7. Occlusion Persistence (Enter from edges, No teleporting). "
        "8. Cinematic 8k resolution, Photorealistic."
    )
    
    if mode == "video":
        return f"Hyper-realistic ASMR VIDEO of {user_input}. {rules} Shot on 35mm lens, high temporal consistency."
    else:
        return f"Hyper-realistic ASMR MACRO PHOTO of {user_input}. {rules} Soft shadows, extreme detail, 8k render."

# --- 3. TAMPILAN ANTARMUKA ---
st.set_page_config(page_title="AIBisKit Pro v3.0", page_icon="🚀")

st.title("🚀 AIBisKit Pro v3.0")
st.subheader("Zero-API Professional Edition")

# Gerbang Password
pass_input = st.text_input("Masukkan Kunci Akses Pembeli:", type="password")

if pass_input == PASSWORD_AKSES:
    st.success("Akses Diterima! Mesin AIBisKit Siap.")
    
    # Input User
    user_query = st.text_input("Apa objek yang ingin dibuat?", placeholder="Contoh: Potong jeruk nipis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔥 Buat Prompt Video"):
            if user_query:
                hasil = generate_manual_prompt(user_query, "video")
                st.info("Copy teks di bawah ke Runway/Luma/Kling:")
                st.code(hasil, language="text")
            else:
                st.warning("Silakan isi objek dulu.")
                
    with col2:
        if st.button("📸 Buat Prompt Foto"):
            if user_query:
                hasil = generate_manual_prompt(user_query, "photo")
                st.info("Copy teks di bawah ke Midjourney/DALL-E:")
                st.code(hasil, language="text")
            else:
                st.warning("Silakan isi objek dulu.")

    st.markdown("---")
    st.caption("AIBisKit Logic Engine © 2026 - Stable Version")

else:
    if pass_input != "":
        st.error("Kunci Akses Salah!")
    st.info("Sistem Terkunci. Masukkan Kunci Akses untuk menggunakan Logika AIBisKit.")
