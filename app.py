import streamlit as st

# --- 1. PENGATURAN KEAMANAN & JUDUL ---
PASSWORD_AKSES = "aibis2026"

st.set_page_config(page_title="AIBisKit ASMR Pro", page_icon="🚀")

# --- 2. LOGIKA GENERATOR (STANDAR AIBISKIT) ---
def generate_asmr_logic(user_input):
    # Logika Anti-Anomali Air & Viscosity Lock
    rules = (
        "Rules: 1. 30/70 Framing. 2. Fixed Tripod. 3. Organic Texture. 4. Soft Lighting. "
        "5. Fluid Physics: High viscosity droplets, gravity-bound juice, strictly zero explosive splashes, "
        "only slow drips on knife. 6. Motion Scale: 1.5. 7. No teleporting."
    )
    
    video = f"Hyper-realistic ASMR VIDEO of {user_input}. {rules} Shot on 35mm, high temporal consistency."
    photo = f"Hyper-realistic ASMR MACRO PHOTO of {user_input}. {rules} 8k resolution, extreme citrus pores detail."
    
    # Logika Isi Konten (Social Media Kit)
    konten = {
        "judul": f"ASMR Memuaskan: {user_input.title()} 🍋✨",
        "deskripsi": f"Rasakan detail mikro dan suara memuaskan saat {user_input}. Dibuat dengan presisi visual AIBisKit Standar. #ASMR #Satisfying #Relaxing",
        "hastag": "#asmrindonesia #satisfyingvideo #visualasmr #aibiskit #relaxing #microdetails"
    }
    
    return video, photo, konten

# --- 3. STATE MANAGEMENT (Agar hasil tidak hilang) ---
if 'hasil_video' not in st.session_state:
    st.session_state.hasil_video = ""
if 'hasil_photo' not in st.session_state:
    st.session_state.hasil_photo = ""
if 'hasil_konten' not in st.session_state:
    st.session_state.hasil_konten = None

def reset_ide():
    st.session_state.hasil_video = ""
    st.session_state.hasil_photo = ""
    st.session_state.hasil_konten = None
    st.rerun()

# --- 4. TAMPILAN ANTARMUKA ---
st.title("🚀 AIBisKit ASMR Pro") # Perubahan Nama Sesuai Permintaan

pass_input = st.text_input("Masukkan Kunci Akses Pembeli:", type="password")

if pass_input == PASSWORD_AKSES:
    st.success("Akses Diterima! Mesin AIBisKit Siap.")
    
    user_query = st.text_input("Apa objek yang ingin dibuat?", placeholder="Contoh: Potong jeruk nipis")
    
    # Tombol Utama
    if st.button("🔥 Jalankan Generator AIBisKit"):
        if user_query:
            v, p, k = generate_asmr_logic(user_query)
            st.session_state.hasil_video = v
            st.session_state.hasil_photo = p
            st.session_state.hasil_konten = k
        else:
            st.warning("Silakan isi ide objek terlebih dahulu.")

    # Tombol Reset
    if st.button("🔄 Mulai Ide Baru"):
        reset_ide()

    st.markdown("---")

    # --- TAMPILAN HASIL BERSAMAAN ---
    if st.session_state.hasil_video:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎬 Prompt Video (Anti-Anomali)")
            st.code(st.session_state.hasil_video, language="text")
            
        with col2:
            st.subheader("📸 Prompt Foto (Macro Detail)")
            st.code(st.session_state.hasil_photo, language="text")
            
        st.markdown("---")
        
        # Generator Isi Konten
        st.subheader("📱 Isi Konten Sosial Media")
        k = st.session_state.hasil_konten
        st.write(f"**Judul:** {k['judul']}")
        st.write(f"**Deskripsi:** {k['deskripsi']}")
        st.write(f"**Hashtags:** {k['hastag']}")
        
        st.info("Tips: Gunakan 'High Viscosity' pada setting generator video Anda untuk hasil tetesan air yang sempurna.")

else:
    if pass_input != "":
        st.error("Kunci Akses Salah!")
