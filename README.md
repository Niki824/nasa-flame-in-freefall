# 🔥 NASA Flame in Freefall — AI-Powered Microgravity Fire Safety Command Center

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple?logo=plotly)
![NASA Data](https://img.shields.io/badge/Data-NASA%20PSI%20Repository-blue?logo=nasa)
![UI](https://img.shields.io/badge/Design-Aerospace%20Mission%20Control%20HUD-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> **NASA Space Apps Challenge 2026** · *Flame in Freefall* challenge submission

---

## 🧩 The Mission-Critical Problem

In microgravity (such as aboard the International Space Station, or future Artemis lunar and Martian habitats), fire behaves completely differently than on Earth:
- **No Buoyancy Plumes:** Without gravity, hot air doesn't rise. Flames burn as eerie, symmetrical spheres.
- **Cool Flames Phenomenon:** Discovered in NASA's FLEX experiments, liquid droplet fuels can sustain sub-visible, low-temperature combustion long after the visible fire looks extinguished, silently producing carbon monoxide and formaldehyde.
- **Ventilation Hazards:** Spacecraft life-support fans blowing gentle air (5–15 cm/s) actively replenish oxygen to the flame front, accelerating flame spread rates far beyond Earth ground tests.
- **Data Fragmentation:** NASA has over 20+ years of experimental data in the Physical Sciences Informatics (PSI) repository, but mission planners and engineers struggle to extract immediate, practical fire safety parameters.

---

## 💡 The Solution: Aerospace Fire Safety Command Center

An interactive, AI-synthesized command console designed to ingest, rank, simulate, and translate NASA combustion research into life-saving flight engineering protocols.

---

## ✨ Cutting-Edge Features

### 🛰️ Tab 1: Telemetry Explorer (Dual View: Matrix & Hologram Cards)
- Searchable filter console spanning **Fuel Chemistry**, **Gravity Regimes** (0g ISS, 0.16g Moon, 0.38g Mars), and **Hazard Severity**.
- Toggle between **Structured NASA Matrix** and **Holographic Investigation Flight Cards**.
- Donut & Sunburst hierarchical breakdowns of gravity vs. risk levels vs. fuel types.

### 🤖 Tab 2: AI Safety Interpreter & Executive Synthesis
- Plain-English executive summaries translating raw academic papers into astronaut-accessible directives.
- Specific engineering counter-measures (airflow dampers, multi-spectrum IR/UV sniffer placement, material bans).
- One-click **Emergency EVA / Flight Deck Checklist Generator**.
- Interactive composite hazard gauge.

### 🎛️ Tab 3: Morphing Flame Physics Chamber (Showstopper Interactive Visualizer)
- Real-time SVG-rendered **flame chamber** that visually morphs as you adjust sliders:
  - **In 0g Microgravity:** Renders a perfect spherical diffusion halo (NASA FLEX discovery).
  - **In Lunar Gravity (0.16g):** Morphs into a semi-buoyant teardrop flame dome.
  - **In Martian Gravity (0.38g):** Displays convective elongation and molten droplet risk.
  - **In Earth Gravity (1g):** Displays high-buoyancy convective plumes.
  - **Airflow Sliders:** Flame tilts and stretches aerodynamically with trailing wind vectors.
  - **Oxygen Sliders:** Cool flame violet mode (<16.5% O₂) vs. incandescent white-hot flashover mode (>24% O₂).
- Dynamic AI mission advisories calculating real-time ignition probability and nearest empirical NASA experiment.

### 📊 Tab 4: 3D Multi-Dimensional Hazard Landscape & Composite Ranking
- Fully interactive **3D Plotly Space Scatter**: Rotate and zoom through Minimum Ignition O₂ vs. Flame Spread Rate vs. Toxicity Index.
- Composite ranking formula:
  $$\text{Risk Score} = 40\% \times \text{Flame Spread} + 35\% \times \text{Ignition Threshold} + 25\% \times \text{Toxicity}$$
- Full sortable NASA Telemetry ranking sheet.

### ⚖️ Tab 5: Head-to-Head Comparison & Historical Disaster Lessons
- Side-by-side radar signature comparison between any two experiments across 4 normalized hazard dimensions.
- Deep dives into three spaceflight fire disasters:
  - **Apollo 1 (1967):** Pure oxygen flashover $\rightarrow$ Mixed N₂/O₂ atmospheres & NASA-STD-6001.
  - **Apollo 13 (1970):** Supercritical O₂ tank electrical explosion $\rightarrow$ Redundant cryo-tank architecture & ACME gas limit research.
  - **Mir Station Fire (1997):** Solid perchlorate candle 14-minute inferno $\rightarrow$ Electrolytic O₂ generation & Saffire-VI smoldering protocols.
- Historical disaster to modern ISS science timeline.

---

## 🛰️ NASA Data & Resources Directly Integrated

| Resource | Scope in Dashboard | Official URL |
|---|---|---|
| **NASA PSI Combustion Science** | Primary data repository for experiments | [Visit Repository](https://psi.nasa.gov/physci/repo/search?q=combustion) |
| **NASA Glenn Combustion Program** | Microgravity combustion science foundations | [Visit Program](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/) |
| **ISS Researcher's Guide (2015)** | Investigation parameters (FLEX, Saffire, BRE, ACME) | [Download Guide](https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/) |
| **Apollo 1 Accident Review** | Lessons learned on high-O₂ flammability | [View Archive](https://sma.nasa.gov/sma-disciplines/accllp/apollo-1) |
| **Apollo 13 Investigation** | Lessons learned on cryo-oxygen tanks | [View Archive](https://sma.nasa.gov/sma-disciplines/accllp/apollo-13) |
| **25 Years Ago: Mir Fire** | Lessons learned on chemical oxygen generation | [View Record](https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/) |

---

## 🚀 Quick Launch

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/nasa-flame-in-freefall.git
cd nasa-flame-in-freefall

# 2. Install dependencies (Clean & lightweight: zero numpy/pandas compilation locks)
pip install -r requirements.txt

# 3. Launch dashboard
streamlit run app.py
```

The Mission Control Console opens at `http://localhost:8501`.

---

## 👨‍🚀 Submission Credentials

- **Challenge:** NASA Space Apps Challenge 2026 — *Flame in Freefall*
- **Deadline:** Sunday, November 15, 2026 at 11:59 PM
- **Team Page:** [NASA Space Apps Challenge](https://www.spaceappschallenge.org/2026/find-a-team/flame-in-freefall-solo/)
