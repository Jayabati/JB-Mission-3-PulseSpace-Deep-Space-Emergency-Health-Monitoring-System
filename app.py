import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="JB-Mission 3: PulseSpace | Deep Space Health Monitor",
    layout="wide"
)

# Custom Styling for Deep Space UI
st.markdown("""
<style>
.main { background-color: #0b0f19; color: #e2e8f0; }
.stButton>button { background-color: #2563eb; color: white; border-radius: 8px; font-weight: bold; }
.alert-card { background-color: #1e1b4b; border-left: 5px solid #ef4444; padding: 15px; border-radius: 6px; }
.normal-card { background-color: #064e3b; border-left: 5px solid #10b981; padding: 15px; border-radius: 6px; }
</style>
""", unsafe_allow_html=True)

# Sidebar - Mission Control & Environment Selector
st.sidebar.title("PulseSpace OS")
st.sidebar.markdown("**Mission Control Setup**")
environment = st.sidebar.selectbox(
    "Select Operating Environment:",
    ["Transit Spacecraft (Artemis / Mars)", "Orbital Space Station", "Lunar Surface Base"]
)
mode = st.sidebar.radio("Navigation:", ["Emergency Triage", "Routine Vital Tracker", "NASA OSDR Grounding"])
st.sidebar.info(f"**Current Environment:** {environment}\n\n**Telemetry Status:** OFFLINE (Local Processing)")

# Header Section
st.title("JB-Mission 3: PulseSpace Emergency Diagnostic Platform")
st.caption(f"Optimized for Non-Physician Crew Members | {environment}")

# MODE 1: EMERGENCY TRIAGE (3-STEP WORKFLOW)
if mode == "Emergency Triage":
    st.subheader("Emergency Symptom Triage")
    symptom = st.selectbox(
        "Select Observed Acute Symptom:",
        ["Acute Chest Pain / Arrhythmia", "Severe Hypoxia / Shortness of Breath", "Hyperthermia / Heat Exhaustion"]
    )
    
    col1, col2, col3 = st.columns(3)
    
    if symptom == "Acute Chest Pain / Arrhythmia":
        with col1:
            st.markdown("### 1. HOW to Measure")
            st.write("• Attach 3-lead ECG electrode sensors to upper chest.\n• Secure pulse oximeter on index finger.\n• Initiate vital sign sweep.")
        with col2:
            st.markdown("### 2. WHY it Matters")
            st.write("• Microgravity causes cephalad fluid shifts and cardiac deconditioning.\n• Evaluates arrhythmia risk under solar flare radiation stress.")
        with col3:
            st.markdown("### 3. WHAT Action to Take")
            st.error("ACTION: Administer supplemental O2. Place crewmate in recumbent position. Prepare AED unit.")

    elif symptom == "Severe Hypoxia / Shortness of Breath":
        with col1:
            st.markdown("### 1. HOW to Measure")
            st.write("• Verify suit/cabin pressure sensor readings.\n• Check SpO2 sensor placement on fingertip.\n• Record respiration rate over 30s.")
        with col2:
            st.markdown("### 2. WHY it Matters")
            st.write("• Cabin pressure drops or suit scrub failure can trigger rapid hypoxia.\n• SpO2 below 90% risks cognitive impairment.")
        with col3:
            st.markdown("### 3. WHAT Action to Take")
            st.error("ACTION: Switch to secondary suit O2 loop. Check CO2 scrubber canister. Flush helmet line.")

    else:
        with col1:
            st.markdown("### 1. HOW to Measure")
            st.write("• Insert core body temperature ear sensor probe.\n• Measure skin surface temperature on torso.")
        with col2:
            st.markdown("### 2. WHY it Matters")
            st.write("• Lunar EVA suits face extreme thermal radiation spikes.\n• Core temp > 38.5°C risks heat stroke.")
        with col3:
            st.markdown("### 3. WHAT Action to Take")
            st.error("ACTION: Maximize liquid cooling garment flow. Abort EVA immediately. Initiate active rehydration.")

elif mode == "Routine Vital Tracker":
    st.subheader("Automated Routine Vital Tracking")
    st.success("All Baseline Crew Vitals Nominal (Last Sync: 02:00 UTC)")
    df = pd.DataFrame({
        "Metric": ["Heart Rate (BPM)", "SpO2 (%)", "Blood Pressure (mmHg)", "Core Temp (°C)"],
        "Value": [72, 98, "118/76", 36.8],
        "Status": ["Normal", "Normal", "Normal", "Normal"]
    })
    st.table(df)

else:
    st.subheader("NASA OSDR & HRP Scientific Grounding")
    st.markdown("""
    - **NASA Human Research Program (HRP):** Cardiovascular risk models and fluid shift thresholds.
    - **NASA Open Science Data Repository (OSDR):** Anomaly benchmarking using transcriptomic profile dataset **OSD-379**.
    - **Brazilian Space Agency (AEB):** Mandatory 3-step triage workflow integration (HOW, WHY, WHAT).
    """)
