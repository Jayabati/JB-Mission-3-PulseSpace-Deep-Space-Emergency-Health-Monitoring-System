JB-Mission 3: PulseSpace: Deep Space Emergency Health Monitoring System
> **2026 NASA Space Apps Challenge Submission**
> **Challenge:** Create Health Monitoring Software for Astronauts on Space Missions
> **Lead Agency Partner:** Brazilian Space Agency (AEB) & NASA

---

## Executive Summary
As human spaceflight extends to Artemis lunar operations and future deep-space Mars transits, crew members face physical isolation, communication delays of up to 20+ light-minutes, and the complete absence of onboard physicians.

**PulseSpace** is an offline-first, autonomous emergency health monitoring and medical diagnostic software engineered specifically for non-doctor astronauts operating under high stress. The system bridges space medicine with rapid emergency triage through an intuitive 3-step decision flow:
1. **HOW to Measure:** Step-by-step visual guidance for placing sensors and collecting vital signs.
2. **WHY it Matters:** Plain-language medical rationale explaining physiological significance without complex clinical jargon.
3. **WHAT Action to Take:** Immediate, actionable emergency triage steps when vital values deviate from baseline norms.

---

## Key Features
* **3-Step Emergency Triage Workflow:** Standardized emergency response guidance designed for high-stress, non-physician operations.
* **Multi-Environment UI Adaptation:** Dynamically toggles interface layouts for **Transit Spacecraft**, **Orbital Space Station**, and **Lunar Surface Base** settings.
* **Proactive Routine Vital Tracking:** Automated scheduling reminders to capture baseline vitals and detect silent health degradation before crisis events occur.
* **Offline-First Architecture:** Operates completely independent of Earth telemetry or cloud access, ensuring continuous availability during solar flares or blackout windows.
* **Terrestrial Dual-Use Care:** Built with an adaptable architecture for deployment in Earth-based remote clinics, polar research stations, and rural emergency response units.

---

## NASA Scientific Grounding & Data Attribution
**PulseSpace** integrates parameters derived from official space biology research and risk frameworks:
* **NASA Human Research Program (HRP):** Baseline physiological risk definitions, vital sign baseline metrics (cardiovascular deconditioning, microgravity fluid shifts, hypoxia/SpO2 limits, and thermal core temp).
* **NASA Open Science Data Repository (OSDR):** Anomaly detection benchmarks using spaceflight transcriptomic and biomarker profiles (e.g., OSD-379).
* **Brazilian Space Agency (AEB):** Direct implementation of the 3-step emergency triage mandate (HOW, WHY, WHAT).

---

## Repository Structure
- `app.py`: Interactive Streamlit application prototype.
- `requirements.txt`: Python package dependencies.
- `README.md`: System documentation and project summary.
