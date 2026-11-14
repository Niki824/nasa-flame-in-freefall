# 🔥 NASA Flame in Freefall — Microgravity Fire Safety Dashboard

[![Live App](https://img.shields.io/badge/Streamlit%20Cloud-Live%20App-brightgreen?logo=streamlit)](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Niki824%2Fnasa--flame--in--freefall-blue?logo=github)](https://github.com/Niki824/nasa-flame-in-freefall)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple?logo=plotly)
![NASA Data](https://img.shields.io/badge/Data-NASA%20PSI%20Repository-blue?logo=nasa)
![License](https://img.shields.io/badge/License-MIT-green)

> **NASA Space Apps Challenge 2026** · *Flame in Freefall* Challenge Submission  
> **Team:** Solo Project by Nikini Edirisinghe  
> **Live Web Application:** [nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)

---

## 🧩 The Mission-Critical Challenge

In microgravity (such as aboard the International Space Station, or future Artemis lunar and Martian habitats), fire behaves completely differently than on Earth:
- **No Buoyant Convection:** Without gravity, warm air does not rise. Flames lack the natural upward draw of fresh oxygen and instead burn as eerie, silent, spherical diffusion domes.
- **Cool Flames Phenomenon:** Discovered during NASA's FLEX experiments, hydrocarbon droplet fuels can sustain sub-visible, low-temperature combustion long after the visible fire appears out, silently producing toxic carbon monoxide and formaldehyde.
- **Forced Ventilation Hazards:** Spacecraft life-support fans blowing gentle air (5–15 cm/s) actively sweep away extinguishing soot while replenishing oxygen to the flame front, accelerating flame spread far beyond standard 1-g Earth ground tests.
- **Data Accessibility:** Over 20+ years of microgravity combustion science is cataloged in the NASA Physical Sciences Informatics (PSI) repository. However, raw academic datasets are difficult for astronauts, flight controllers, and habitat designers to quickly interpret into actionable fire containment protocols.

---

## 💡 The Solution: Aerospace Fire Safety Command Center

**Flame in Freefall** is an interactive, browser-based flight safety dashboard that compiles, ranks, visualizes, and synthesizes empirical NASA combustion science into clear, actionable spacecraft fire safety intelligence for the ISS, the Lunar Gateway, Artemis Base Camp, and Mars transit vehicles.

---

## 🔬 Scientific Methodology & Data Provenance

### 1. Dataset Origin (`combustion_data.csv`)
The dataset contains **17 NASA spaceflight and ground combustion investigations**:
- **14 Spaceflight Experiments:** Compiled from published NASA Physical Sciences Informatics (PSI) investigations, peer-reviewed flight reports (Saffire I–VI, FLEX, FLEX-2, BRE, ACME, SoFIE, BASS, BASS-II, CFI, FLARE, Confined Combustion), and the *NASA ISS Researcher's Guide to Combustion Science* (NASA/TP-2015-218202).
- **3 Historical Spaceflight Fire Disasters:** Synthesized from official NASA accident review board reports (Apollo 204 Review Board, Apollo 13 Investigation Board, and NASA History Division Mir space station fire records).

| Column | Data Nature | Scientific Source |
|---|---|---|
| `Experiment_Name`, `Mission`, `Year` | Empirical Fact | Official NASA Mission flight manifests |
| `Gravity_Environment`, `Fuel_Type` | Empirical Fact | NASA PSI investigation specifications |
| `Flame_Spread_Rate` (mm/s) | Empirical Measurement | Published flight telemetry from NASA PSI & Saffire/BRE papers |
| `Min_Ignition_O2` (%) | Empirical Threshold | Published flammability limit data from NASA-STD-6001 / PSI |
| `Toxicity_Index` (1–10) | Qualitative Severity Index | Evaluated based on NASA-STD-6001B Test 7 ("Toxic Offgassing") and combustion product chemistry |
| `Key_Findings` | Empirical Synthesis | Primary conclusions from NASA Principal Investigator publications |
| `AI_Summary` & `Safety_Recommendations` | AI-Assisted Synthesis | Generated using Google Gemini 1.5 conditioned strictly on NASA technical reports |

### 2. Composite Fire Hazard Scoring Formula
In aerospace risk management, evaluating heterogeneous hazards (flame velocity, ignition limits, off-gas toxicity) requires a **Multi-Criteria Decision Analysis (MCDA)** model:

$$\text{Composite Hazard Score} = \left(\frac{\text{Spread Rate}}{20} \times 40\right) + \left[\left(1 - \frac{\text{Min } O_2}{30}\right) \times 35\right] + \left(\frac{\text{Toxicity Index}}{10} \times 25\right)$$

- **Flame Spread Weight (40%):** Spread speed dictates crew egress time and compartment flashover limits.
- **Ignition Oxygen Weight (35%):** Materials with lower minimum oxygen thresholds present higher accidental ignition risks in exploration atmospheres ($21\%\text{--}34\%\text{ } O_2$).
- **Toxicity Index Weight (25%):** In sealed spacecraft volumes, smoke and off-gases (CO, HCN, formaldehydes) represent fatal acute hazards before thermal barriers breach.
> *Scientific Disclosure: This composite weighting is an illustrative engineering multi-criteria utility function developed specifically for comparative dashboard visualization in this prototype. It is not an official NASA standard metric.*

### 3. Qualitative Flame Simulator Model
Tab 3 features an interactive **Morphing Flame Physics Chamber**. This is an **illustrative mathematical model** calibrated to empirical NASA observations:
- At $0.00g$ and low airflow, flames form spherical diffusion domes (demonstrating BASS-II quiescent self-extinction and FLEX cool flame behavior).
- As forced airflow increases ($5\text{--}18\text{ cm/s}$), the flame elongates and tilts according to empirical forced convective heat transfer relationships observed in NASA BRE and Saffire flight trials.
- At $0.16g$ (Moon) and $0.38g$ (Mars), weak buoyant convective currents are simulated to illustrate partial-gravity flame acceleration along structural materials.
> *Scientific Disclosure: The chamber renders an illustrative SVG model intended for intuitive conceptual training. For formal aerospace design, flight controllers rely on full 3D Computational Fluid Dynamics (CFD) codes such as NASA Glenn numerical combustion packages.*

---

## 🤖 Artificial Intelligence Disclosure

In compliance with NASA Space Apps Challenge 2026 rules:
- **Models Used:** Google Gemini 1.5 Pro & Gemini 1.5 Flash.
- **What AI Did:**
  1. **Executive Synthesis (`AI_Summary`):** Translating dense scientific terminology from published NASA reports into plain-English summaries accessible to astronauts and operational engineers.
  2. **Checklist Generation (`Safety_Recommendations`):** Structuring actionable flight deck procedures and sensor deployment guidelines directly from published NASA findings.
  3. **Visual Asset Concepting:** Generating prompt briefs for the 3D zero-g mission companions (NOVA AI, Commander Leo, Navigator Zog).
- **What AI Did NOT Do (Deterministic Code):**
  - All filtering, mathematical scoring, ranges, data normalization, radar chart geometry, and 3D scatter plots are computed using **100% deterministic Python standard libraries and Plotly**. No hallucinated data or black-box math is used in the telemetry pipelines.

---

## ✨ Dashboard Features & Architecture

```
NASA Flame in Freefall
├── 🛸 3D Mission Companions (Sidebar)
│   ├── 🤖 NOVA AI (Fire Safety Copilot)
│   ├── 🧑‍🚀 Commander Leo (Zero-G Crew Leader)
│   └── 🛸 Navigator Zog (Planetary Gravity Observer)
├── 🛰️ Tab 1: Telemetry Explorer (Dual View: Structured Matrix & Cards)
├── 🤖 Tab 2: AI Safety Interpreter & Emergency Checklist Generator
├── 🎛️ Tab 3: Morphing Flame Simulator (Live Interactive Physics Chamber)
├── 📊 Tab 4: 3D Multi-Dimensional Hazard Landscape & Risk Ranking
└── ⚖️ Tab 5: Head-to-Head Comparison & Historical Disaster Lessons
```

---

## 🚀 Local Installation & Setup

```bash
# 1. Clone repository
git clone https://github.com/Niki824/nasa-flame-in-freefall.git
cd nasa-flame-in-freefall

# 2. Install lightweight dependencies (zero C-compilation lockups)
pip install -r requirements.txt

# 3. Run dashboard locally
streamlit run app.py
```

The application opens locally at `http://localhost:8501`.

---

## 🛰️ NASA Official References

1. **NASA Physical Sciences Informatics (PSI) Repository:** [psi.nasa.gov](https://psi.nasa.gov/physci/repo/search?q=combustion)
2. **NASA Glenn Research Center Combustion Science:** [nasa.gov/glenn/combustion-science](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/)
3. **NASA ISS Researcher's Guide to Combustion Science (NASA/TP-2015-218202):** [Download PDF](https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/)
4. **NASA-STD-6001B:** *Flammability, Odor, Offgassing, and Compatibility Requirements and Test Procedures for Materials in Environments that Support Combustion.*
5. **NASA Apollo 1 Accident Investigation (AS-204):** [NASA SMA Archive](https://sma.nasa.gov/sma-disciplines/accllp/apollo-1)
6. **NASA Apollo 13 Review Board:** [NASA SMA Archive](https://sma.nasa.gov/sma-disciplines/accllp/apollo-13)
7. **NASA Mir Space Station Fire Analysis (1997):** [NASA History Record](https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/)

---

## 📄 License

This project is open-source and released under the [MIT License](LICENSE).
Built for the **NASA Space Apps Challenge 2026**.
