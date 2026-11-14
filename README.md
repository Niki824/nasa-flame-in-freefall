# 🔥 NASA Flame in Freefall — Microgravity Fire Safety Research Hub

[![Live App](https://img.shields.io/badge/Streamlit%20Cloud-Live%20App-brightgreen?logo=streamlit)](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Niki824%2Fnasa--flame--in--freefall-blue?logo=github)](https://github.com/Niki824/nasa-flame-in-freefall)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple?logo=plotly)
![NASA Data](https://img.shields.io/badge/Data-NASA%20PSI%20Archival-blue?logo=nasa)
![License](https://img.shields.io/badge/License-MIT-green)

> **NASA Space Apps Challenge 2026** · *Flame in Freefall* Challenge Submission  
> **Team:** Solo Project by Nikini Edirisinghe  
> **Live Web Application:** [nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app](https://nasa-flame-in-freefall-fbnzgdeusdbbluisygxsqe.streamlit.app/)

---

> ### ⚠️ Notice of Limitation
> **This application is an educational demonstration and research synthesis prototype developed for the NASA Space Apps Challenge 2026; it is not certified for operational flight planning or real-world spacecraft fire safety decisions.**

---

## 🧩 The Mission-Critical Challenge

In microgravity (such as aboard the International Space Station, or future Artemis lunar and Martian habitats), fire behaves completely differently than on Earth:
- **Absence of Buoyant Convection:** Without gravity, warm combustion gases do not rise. Flames lack the natural convective draw of fresh oxygen and instead burn as eerie, silent, spherical diffusion domes.
- **Cool Flames Phenomenon:** Discovered during NASA's FLEX experiments, hydrocarbon droplet fuels can sustain sub-visible, low-temperature combustion (below 1000 K) long after the visible fire appears out, continuing to consume fuel without emitting visible soot luminosity.
- **Forced Ventilation Hazards:** Spacecraft life-support fans blowing gentle air (5–20 cm/s) actively sweep away extinguishing soot while replenishing fresh oxygen to the flame front, accelerating flame spread rates far beyond standard 1-g Earth ground tests.
- **Data Traceability & Accessibility:** Over 20+ years of microgravity combustion science is cataloged across NASA Physical Sciences Informatics (PSI) archives and technical publications. However, raw academic reports are difficult for astronauts, flight controllers, students, and habitat designers to quickly cross-compare into actionable fire safety insights.

---

## 💡 The Solution: Aerospace Fire Safety Research Hub

**Flame in Freefall** is an interactive, browser-based aerospace research platform that systematically organizes, synthesizes, and visualizes peer-reviewed NASA microgravity combustion investigations alongside historical incident benchmarks:

1. **🛰️ Archival Telemetry Explorer:** Filter and inspect 12 verified NASA flight investigations and 3 historical accident benchmarks across fuel chemistry (solid, liquid droplet, gaseous), carrier platforms (ISS CIR, MSG, Cygnus), and diagnostics.
2. **🤖 AI Research Briefing & Synthesis:** Plain-English research translations outlining what NASA investigated, fuels tested, experimental conditions, verified discoveries, operational spacecraft relevance, and critical knowledge gaps.
3. **🎛️ Morphing Flame Physics Chamber:** An interactive educational SVG visualizer illustrating qualitative flame geometry, tilt deflection, and physical burning regimes (quiescent spherical diffusion dome vs ventilation-fed flame spread).
4. **📊 Evidence-Based Experiment Comparison:** Rigorous cross-investigation comparison analyzing tested oxygen concentrations over mission timelines, fuel physical phase distributions, and critical exploration research gaps.
5. **⚖️ Head-to-Head & Historical Lessons:** Side-by-side technical parameters comparison paired with deep historical case studies (Apollo 1, Apollo 13, Mir) and the safety redesigns they established.

---

## 📊 Data Source & Scientific Traceability

The curated dataset `combustion_data.csv` was **hand-compiled from published NASA technical literature and official investigation reports**, with full provenance traceability:

### Source Documents Used:
1. **NASA ISS Researcher's Guide to Combustion Science (NASA NP-2015-10-034-JSC):** Flight overviews, hardware constraints, and primary findings for FLEX, FLEX-2, BASS, BASS-II, ACME, and the BRE (Burning Rate Emulator) sub-investigation.
2. **NASA Glenn Research Center Saffire Flight Reports (Urban, Ferkul, Olson et al., 2016–2022):** Large-scale fabric combustion, airflow sensitivity, and exploration atmospheres (Cygnus OA-6, OA-5, OA-7, NG-18).
3. **NASA Physical Sciences Informatics (PSI) Database:** Primary flight investigation repositories:
   - FLEX: [PSI-69](https://psi.nasa.gov/physci/repo/data/investigations/PSI-69) (DOI: `10.1016/j.combustflame.2014.07.032`)
   - BASS: [PSI-24](https://psi.nasa.gov/physci/repo/data/investigations/PSI-24) (DOI: `10.2514/6.2013-3806`)
   - BASS-II: [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) (DOI: `10.1016/j.proci.2014.05.074`)
   - Saffire-I: [PSI-98](https://psi.nasa.gov/physci/repo/data/investigations/PSI-98) (AIAA 2017-3746)
   - ACME: [PSI-15](https://psi.nasa.gov/physci/repo/data/investigations/PSI-15)
   - FLEX-2: [PSI-70](https://psi.nasa.gov/physci/repo/data/investigations/PSI-70)
4. **Official NASA Accident Review Board Records:**
   - *Report of Apollo 204 Review Board (NASA SP-138, 1967)*: 100% O₂ flashover dynamics and material flammability.
   - *Report of Apollo 13 Review Board (1970)*: Supercritical cryogenic oxygen tank wiring arc and explosion.
   - *NASA History Division: Mir Space Station Fire Analysis (1997)*: Solid-fuel perchlorate oxygen candle combustion.

### Dataset Schema & Provenance Columns:
- **`Experiment_Name`, `Fuel_Type`, `Gravity_Environment`, `Test_Atmosphere_O2`, `Airflow_Conditions`, `Year`, `Mission`, `Historical_Incident`:** Direct archival parameters.
- **`Flame_Spread_Measurement`:** Sourced from published papers for solid surface tests (Saffire, BASS, Confined Combustion); explicitly marked **N/A** for droplet kinetics and gaseous burner experiments where surface spread is not a physical measurement.
- **`Extinction_Limit_Observation`:** Empirical flammability and extinction limits documented in NASA reports.
- **`Sensors_And_Diagnostics`:** Specific instrumentation arrays (e.g. UV/visible radiometers, high-speed CIR cameras, tunable diode laser spectrometers).
- **`Measurement_Type` & `Data_Quality`:** Categorized as *Verified Archival*, *Reported Observation*, or *Historical Incident Record*.
- **`NASA_Source_URL` & `DOI_Or_Reference`:** Direct hyperlinks and persistent identifiers for third-party auditing.

---

## ⚖️ Scientific Integrity: Evidence-Based Comparison vs. Composite Scores

In strict accordance with scientific validity principles:
- **No Fabricated Scores or Indices:** This platform does **NOT** compute artificial composite fire-risk scores or numerical toxicity indices. Raw NASA flight archives evaluate materials under specific test conditions (e.g., airflow velocity, ambient oxygen, sample thickness) rather than arbitrary numerical formulas.
- **Evidence-Based Comparison:** The dashboard replaces subjective rankings with **systematic evidence-based comparisons**: contrasting experimental goals, fuel phases, ambient conditions, diagnostic suites, verified findings, and documented knowledge gaps.
- **Partial-Gravity Disclaimer:** NASA PSI **does not currently hold tabulated partial-gravity combustion data**. Lunar (0.16g) and Martian (0.38g) settings in the simulator are **hypothetical educational illustrations** exploring theoretical buoyancy transitions; they are not empirical datasets.

---

## 🤖 Use of Artificial Intelligence (AI Disclosure)

In compliance with NASA Space Apps Challenge submission standards:

- **Model Used:** Google Gemini 1.5 Pro accessed via Google AI Studio.
- **What the Model Received (Input):** Verbatim technical findings, flight summaries, and mission logs extracted directly from the NASA publications listed above.
- **What the Model Returned (Output):**
  1. Plain-English research summaries (`AI_Research_Summary` in `combustion_data.csv`).
  2. Potential spacecraft relevance interpretations (`Potential_Spacecraft_Relevance` in `combustion_data.csv`).
  3. Character concept briefs for the cute 3D zero-gravity companion mascots (NOVA, Commander Leo, Navigator Zog).
- **Deterministic Runtime Architecture:**
  - All web interface code (`app.py`), Streamlit components, SVG flame rendering, data filtering, and Plotly visualizations are **fixed text and ordinary Python code**.
  - **No generative AI is invoked at runtime.** AI-assisted summaries were prepared during development and reviewed against the cited research sources. This dashboard operates deterministically in Python with zero latency.
  - NOVA is a static illustrated mascot, not a live conversational chatbot.

---

## 🎛️ Conceptual Visualization vs. Empirical Data

- **Empirical Archival Visualizations (Tabs 1, 2, 4, 5):** The telemetry matrix, timeline scatter plot, fuel distribution donut, and head-to-head comparison directly render verified values from `combustion_data.csv`.
- **Conceptual Visualizer (Tab 3: Morphing Flame Physics Chamber):** The interactive SVG chamber is an **educational qualitative visualizer** illustrating low-gravity flame phenomena:
  - At $0.00g$, flames form spherical diffusion envelopes.
  - At higher airflow velocities ($5\text{--}20\text{ cm/s}$), the flame elongates and tilts based on forced convection relationships observed in NASA BASS and Saffire flight trials.
  - *This visualizer is an educational illustration; certified spacecraft fire safety engineering relies on high-fidelity Computational Fluid Dynamics (CFD) codes.*

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

## 🎨 Asset Provenance & Ethics Disclosure

All visual mascot and spacecraft imagery stored in the `assets/` directory (`cute_3d_robot.jpg`, `cute_astronaut_3d.jpg`, `cute_ufo_3d.jpg`, `cute_saturn_3d.jpg`, `3d_iss.jpg`, `3d_rocket.jpg`):
- Were **synthesized using Google Imagen / Gemini** as conceptual 3D character illustrations.
- Depict **fictional, stylized sci-fi avatars** (NOVA research assistant, Commander Leo space explorer, Navigator Zog alien observer) and 3D spacecraft modules.
- **Do NOT depict any real persons**, living or deceased.
- **Do NOT depict anyone under 18 years of age.**

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).  
Copyright (c) 2026 Nikini Edirisinghe.
