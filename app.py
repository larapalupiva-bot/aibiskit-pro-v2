import streamlit as st

# --- INISIALISASI ---
PASSWORD_AKSES = "rahasia-aibiskit-2026"
st.set_page_config(page_title="AIBisKit ASMR Pro", page_icon="🚀")

# State Management
if 'hasil_video' not in st.session_state: st.session_state.hasil_video = ""
if 'hasil_photo' not in st.session_state: st.session_state.hasil_photo = ""
if 'hasil_konten' not in st.session_state: st.session_state.hasil_konten = None
if 'input_objek' not in st.session_state: st.session_state.input_objek = ""

def reset_ide():
    st.session_state.hasil_video = ""
    st.session_state.hasil_photo = ""
    st.session_state.hasil_konten = None
    st.session_state.input_objek = ""

# --- LOGIKA INTELLIGENCE v3.5 ---
def generate_asmr_intelligence(user_input):
    ui = user_input.lower()
    
    # 1. Klasifikasi Material (Kitab Standar Dinamis)
    is_nature = any(x in ui for x in ["hujan", "sungai", "hutan", "angin", "pantai"])
    is_hard = any(x in ui for x in ["kaca", "besi", "kedondong", "kayu", "batu"])
    is_thick = any(x in ui for x in ["jeruk", "lemon", "madu", "sirup", "selai"])
    
    # 2. Standar Komposisi (Global)
    base = "Rules: 1. 30/70 Framing. 2. Fixed Tripod. 3. Soft Side Lighting. 4. Motion Scale 1.2. "
    
    # 3. Adaptasi Fisika (Poin Perbaikan Anda)
    if is_nature:
        physic = "Physics: Natural flow, zero tools, zero knives, realistic environment tension."
    elif is_hard:
        physic = "Physics: Dry impact, zero juice, realistic fragmentation, industrial steel tool."
    else:
        viscos = "high viscosity, syrupy drip" if is_thick else "low viscosity, watery transparent drip"
        physic = f"Physics: {viscos}, gravity-bound, zero explosive splash, sharp ceramic tool."

    video = f"Hyper-realistic ASMR VIDEO of {user_input}. {base} {physic} No teleporting, 8k."
    photo = f"Hyper-realistic ASMR PHOTO of {user_input}. {base} Extreme macro texture, 8k."
    
    konten = {"judul": f"ASMR: {user_input.title()}", "hastag": "#asmr #aibiskit #satisfying"}
    return video, photo, konten

# --- TAMPILAN ---
st.title("🚀 AIBisKit ASMR Pro")
pass_input = st.text_input("Kunci Akses:", type="password")

if pass_input == PASSWORD_AKSES:
    # Sinkronisasi input dengan reset button
    u_query = st.text_input("Objek yang ingin dibuat:", value=st.session_state.input_objek)
    st.session_state.input_objek = u_query

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔥 Jalankan Generator"):
            if u_query:
                v, p, k = generate_asmr_intelligence(u_query)
                st.session_state.hasil_video, st.session_state.hasil_photo, st.session_state.hasil_konten = v, p, k
    with c2:
        st.button("🔄 Mulai Ide Baru", on_click=reset_ide)

    if st.session_state.hasil_video:
        st.code(st.session_state.hasil_video)
        st.code(st.session_state.hasil_photo)
        st.write(st.session_state.hasil_konten)
