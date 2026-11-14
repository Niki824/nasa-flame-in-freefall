# 🔥 NASA Flame in Freefall — Microgravity Fire Safety Dashboard

[![Live App](https://img.shields.io/badge/Streamlit%20Cloud-Live%20App-brightgreen?logo=streamlit)](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Niki824%2Fnasa--flame--in--freefall-blue?logo=github)](https://github.com/Niki824/nasa-flame-in-freefall)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple?logo=plotly)
![NASA Data](https://img.shields.io/badge/Data-NASA%20PSI%20Derived-blue?logo=nasa)
![License](https://img.shields.io/badge/License-MIT-green)

> **NASA Space Apps Challenge 2026** · *Flame in Freefall* Challenge Submission  
> **Team:** Solo Project by Nikini Edirisinghe  
> **Live Web Application:** [nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)

---

> ### ⚠️ Notice of Limitation
> **This application is an educational demonstration and prototype developed for the NASA Space Apps Challenge 2026; it is not certified for operational flight planning or real-world spacecraft fire safety decisions.**

---

## 🧩 The Mission-Critical Challenge

In microgravity (such as aboard the International Space Station, or future Artemis lunar and Martian habitats), fire behaves completely differently than on Earth:
- **No Buoyant Convection:** Without gravity, warm air does not rise. Flames lack the natural upward draw of fresh oxygen and instead burn as eerie, silent, spherical diffusion domes.
- **Cool Flames Phenomenon:** Discovered during NASA's FLEX experiments, hydrocarbon droplet fuels can sustain sub-visible, low-temperature combustion long after the visible fire appears out, silently producing toxic carbon monoxide and formaldehyde.
- **Forced Ventilation Hazards:** Spacecraft life-support fans blowing gentle air (5–15 cm/s) actively sweep away extinguishing soot while replenishing oxygen to the flame front, accelerating flame spread far beyond standard 1-g Earth ground tests.
- **Data Accessibility:** Over 20+ years of microgravity combustion science is cataloged in NASA archives. However, raw academic reports are difficult for astronauts, flight controllers, and habitat designers to quickly interpret into actionable fire containment protocols.

---

## 💡 The Solution: Aerospace Fire Safety Command Center

**Flame in Freefall** is an interactive, browser-based flight safety dashboard that compiles, ranks, visualizes, and synthesizes empirical NASA combustion science into clear, accessible spacecraft fire safety intelligence for the ISS, the Lunar Gateway, Artemis Base Camp, and Mars transit vehicles.

---

## 📊 Data Source & Dataset Provenance

The file `combustion_data.csv` was **manually compiled and curated from published NASA technical literature**, not exported as an automated bulk file from the Physical Sciences Informatics (PSI) repository. 

### Source Documents Used:
1. **NASA ISS Researcher's Guide to Combustion Science (NASA/TP-2015-218202):** Provided flight overviews, fuel chemistries, hardware constraints, and primary findings for FLEX, FLEX-2, BASS, BASS-II, BRE, and ACME investigations.
2. **NASA Glenn Research Center Saffire Flight Reports (Urban, Ferkul, Olson et al., 2016–2022):** Provided large-scale cotton-fiberglass and Nomex flame spread rates, airflow sensitivity data, and exploration atmosphere findings for Saffire-I, II, III, and VI.
3. **NASA Kibo & CIR Technical Summaries:** Provided reduced-gravity flammability parameters for SoFIE (0.16g Moon simulation) and FLARE (0.38g Mars simulation).
4. **Official NASA Accident Review Board Records:**
   - *Report of Apollo 204 Review Board (NASA SP-138, 1967)*: 100% O₂ flashover dynamics and material flammability tests.
   - *Report of Apollo 13 Review Board (1970)*: Supercritical cryogenic oxygen tank wiring failure and explosion.
   - *NASA History Division: Mir Space Station Fire Analysis (1997)*: Solid-fuel perchlorate oxygen candle combustion and toxic smoke generation.

### Field-by-Field Origin Breakdown:
- **`Experiment_Name`, `Fuel_Type`, `Gravity_Environment`, `Oxygen_Concentration`, `Year`, `Mission`, `Historical_Incident`:** Typed directly from the NASA source documents above.
- **`Flame_Spread_Rate` (mm/s) & `Min_Ignition_O2` (%):** Sourced directly from empirical measurements reported in published NASA mission summaries and flight papers.
- **`Key_Findings`:** Hand-curated technical summaries of primary findings published by the NASA Principal Investigator teams.
- **`Toxicity_Index` (1–10, Illustrative Index):** **Raw NASA PSI records do not measure or report a numerical toxicity index.** To bridge combustion physics with life-support safety, we assigned an illustrative 1–10 qualitative severity score based on the material off-gas hazard classifications defined in **NASA-STD-6001B Test 7** (*"Toxic Offgassing Determination and Carbon Monoxide / Hydrogen Cyanide Analysis"*). For example, liquid fuels generating sub-visible formaldehyde receive 7/10, thick PMMA acrylic receives 5–6/10, and burning perchlorate candles producing acrid smoke receive 9/10.
- **`AI_Summary` & `Safety_Recommendations`:** AI-generated plain-language translations produced by Google Gemini 1.5, conditioned strictly on the factual text of the NASA documents.

---

## ⚖️ Risk Score Methodology & Scaling

The Composite Hazard Score (0–100) is **our own engineering choice developed for this demonstration and is NOT an official NASA metric or standard.** NASA safety engineering evaluates materials on independent pass/fail criteria per NASA-STD-6001.

### Rationale for the 40 / 35 / 25 Weights:
- **Flame Spread Rate (40% Weight):** Flame velocity directly determines available crew evacuation time and compartment flashover margins.
- **Minimum Ignition O₂ (35% Weight):** Materials that ignite at lower oxygen concentrations present a higher likelihood of accidental ignition in elevated-O₂ exploration atmospheres ($21\%\text{--}34\%\text{ }O_2$).
- **Toxicity Index (25% Weight):** In sealed spacecraft volumes, toxic combustion gases (CO, HCN, formaldehydes) cause incapacitation long before thermal structural failure.

### Mathematical Scaling to a Common 0–100 Range:
Each input is normalized and scaled in Python as follows:

$$\text{Spread Component} = \frac{\min(\text{Flame Spread Rate}, 20)}{20} \times 40$$
*(Spread rate is capped at 20 mm/s and normalized to contribute 0 to 40 points).*

$$\text{Ignition Component} = \left(1 - \frac{\text{clamp}(\text{Min Ignition } O_2, 10, 30)}{30}\right) \times 35$$
*(Inverted so that a lower ignition threshold yields a higher risk score, contributing 0 to 35 points).*

$$\text{Toxicity Component} = \frac{\text{Toxicity Index}}{10} \times 25$$
*(The 1–10 qualitative toxicity index is normalized to contribute 0 to 25 points).*

$$\text{Composite Hazard Score} = \text{Spread Component} + \text{Ignition Component} + \text{Toxicity Component}$$

---

## 🤖 Use of Artificial Intelligence (AI Disclosure)

In compliance with NASA Space Apps Challenge submission standards:

- **Model & Service Used:** Google Gemini 1.5 Pro and Gemini 1.5 Flash accessed via Google AI Studio.
- **What the Model Received (Input):** Verbatim technical findings, mission logs, and experimental parameters extracted from the NASA source documents listed above.
- **What the Model Returned (Output):**
  1. Plain-English executive summaries (`AI_Summary` in `combustion_data.csv`) that translate academic jargon into accessible explanations.
  2. Operational crew directives (`Safety_Recommendations` in `combustion_data.csv`) outlining emergency sensor placements and ventilation protocols.
  3. Character concept briefs for the cute 3D zero-gravity companion mascots (NOVA AI, Commander Leo, Navigator Zog).
- **What is Fixed Text or Ordinary Code:**
  - All web interface code (`app.py`), Streamlit widgets, CSS zero-gravity keyframe animations, filtering logic, mathematical scoring formulas, normalizations, and Plotly charts are **fixed text and ordinary Python code**.
  - **No AI is invoked at runtime** when users view or interact with the dashboard, ensuring 100% deterministic, repeatable behavior with zero hallucination risk.

---

## 🎛️ Interactive Visualizations vs. Empirical Data

- **Empirical Visualizations (Tabs 1, 2, 4, 5):** The telemetry matrix, donut charts, sunburst hierarchies, 3D scatter plot, and radar profiles directly display the empirical values compiled in `combustion_data.csv`.
- **Illustrative Model (Tab 3: Morphing Flame Chamber):** The SVG flame chamber is an **illustrative mathematical model** calibrated to qualitative NASA observations:
  - At $0.00g$, flames form spherical diffusion domes (BASS-II quiescent extinction and FLEX cool flame behavior).
  - At higher airflow velocities ($5\text{--}18\text{ cm/s}$), the flame elongates and tilts based on empirical forced convection relationships observed in NASA BRE and Saffire flight trials.
  - At $0.16g$ (Moon) and $0.38g$ (Mars), weak buoyant convective currents illustrate partial-gravity flame propagation along structural materials.
  - *This chamber is an intuitive conceptual model; certified spacecraft engineering relies on full 3D Computational Fluid Dynamics (CFD) codes.*

---

## 🚀 Quick Launch (Local Setup)

```bash
# 1. Clone repository
git clone https://github.com/Niki824/nasa-flame-in-freefall.git
cd nasa-flame-in-freefall

# 2. Install dependencies (lightweight: zero numpy/pandas compilation locks)
pip install -r requirements.txt

# 3. Launch dashboard
streamlit run app.py
```

The application opens locally at `http://localhost:8501`.

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).  
Copyright (c) 2026 Nikini Edirisinghe.
