import streamlit as st
import streamlit.components.v1 as components
import csv
import os
import math
import textwrap
import html
import base64
import plotly.graph_objects as go

def render_html(html_str):
    """Render raw HTML safely by stripping indentation so Markdown never converts it to code."""
    st.markdown(textwrap.dedent(html_str).strip(), unsafe_allow_html=True)

@st.cache_data
def get_base64_image(filename):
    """Return base64 data URI of a local image file."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"
    return ""

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_title="🔥 FLAME IN FREEFALL // NASA Space Safety HUD",
    page_icon="🔥",
    initial_sidebar_state="expanded",
)

# ── Master Aerospace HUD & Deep Space CSS ─────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

.stApp {
    background-color: #050813;
    background-image: 
        radial-gradient(circle at 50% 10%, rgba(255, 69, 0, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(0, 210, 255, 0.06) 0%, transparent 45%),
        linear-gradient(rgba(14, 23, 42, 0.45) 1px, transparent 1px),
        linear-gradient(90deg, rgba(14, 23, 42, 0.45) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
    font-family: 'Inter', sans-serif;
    color: #e2e8f8;
}

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #070b16; }
::-webkit-scrollbar-thumb { background: #1e2c4f; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #ff6b35; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #090e1d 0%, #060914 100%);
    border-right: 1px solid rgba(0, 210, 255, 0.2);
    box-shadow: 10px 0 30px rgba(0, 0, 0, 0.6);
}

.stApp::before {
    content: " ";
    display: block;
    position: fixed;
    top: 0; left: 0; bottom: 0; right: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.22) 50%);
    background-size: 100% 4px;
    z-index: 9999;
    pointer-events: none;
    opacity: 0.35;
}

.telemetry-ticker {
    background: rgba(10, 16, 32, 0.9);
    border: 1px solid rgba(0, 210, 255, 0.3);
    border-radius: 8px;
    padding: 8px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: #a6b9dc;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4);
}
.ticker-left { display: flex; align-items: center; gap: 10px; }
.ticker-badge {
    background: rgba(0, 210, 255, 0.15);
    border: 1px solid #00d2ff;
    color: #00d2ff;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 700;
}
.pulse-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    background: #00d2ff;
    border-radius: 50%;
    margin-right: 4px;
}

.hero-box {
    background: linear-gradient(135deg, rgba(14, 22, 45, 0.85) 0%, rgba(7, 11, 24, 0.95) 100%);
    border: 1px solid rgba(0, 210, 255, 0.35);
    border-radius: 18px;
    padding: 24px 28px;
    margin-bottom: 20px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.55), inset 0 0 30px rgba(0, 210, 255, 0.05);
}
.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.1rem;
    font-weight: 900;
    letter-spacing: 0.06em;
    background: linear-gradient(90deg, #ffffff 0%, #ff6b35 50%, #00d2ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    font-size: 0.94rem;
    color: #a6b9dc;
    margin-top: 8px;
    line-height: 1.5;
}

.hero-3d-box {
    background: linear-gradient(135deg, rgba(20, 28, 52, 0.85), rgba(10, 14, 28, 0.95));
    border: 1.5px solid rgba(0, 210, 255, 0.45);
    border-radius: 18px;
    padding: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 210, 255, 0.2);
    text-align: center;
}
.hero-3d-img { width: 100%; border-radius: 12px; display: block; }
.hero-3d-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.76rem;
    font-weight: 800;
    color: #00d2ff;
    margin-top: 6px;
    display: block;
}
.hero-3d-sub { font-size: 0.68rem; color: #a6b9dc; display: block; }

.hud-card {
    background: rgba(12, 19, 38, 0.75);
    border: 1px solid rgba(0, 210, 255, 0.25);
    border-top: 3px solid #00d2ff;
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
}
.hud-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #ffffff;
}
.hud-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #8da4d0;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}

.table-wrap {
    overflow-y: auto;
    border: 1px solid #1e2c4f;
    border-radius: 10px;
    background: #080d1c;
}
.nasa-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.81rem;
    color: #d1dbf4;
}
.nasa-table th {
    background: #0f1830;
    color: #00d2ff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    padding: 10px 14px;
    text-align: left;
    position: sticky;
    top: 0;
    z-index: 10;
    border-bottom: 2px solid #1e2c4f;
}
.nasa-table td {
    padding: 9px 14px;
    border-bottom: 1px solid #141f38;
    vertical-align: top;
}
.nasa-table tr:hover { background: rgba(0, 210, 255, 0.06); }

.exp-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
    margin-top: 14px;
}
.exp-card {
    background: linear-gradient(135deg, rgba(14, 23, 44, 0.85) 0%, rgba(8, 13, 26, 0.95) 100%);
    border: 1px solid rgba(0, 210, 255, 0.22);
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    transition: transform 0.2s ease, border-color 0.2s ease;
}
.exp-card:hover {
    transform: translateY(-2px);
    border-color: rgba(0, 210, 255, 0.6);
}

.cute-speech-bubble {
    background: rgba(14, 24, 48, 0.9);
    border: 1.5px solid rgba(0, 229, 255, 0.5);
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 0.78rem;
    color: #d6e8ff;
    line-height: 1.45;
    margin-top: 10px;
    position: relative;
    box-shadow: 0 4px 14px rgba(0,0,0,0.5);
}
.cute-badge {
    background: linear-gradient(90deg, #00d2ff, #0077ff);
    color: #ffffff;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    letter-spacing: 0.05em;
}

.ai-panel {
    background: linear-gradient(135deg, rgba(10, 22, 45, 0.85) 0%, rgba(5, 12, 28, 0.95) 100%);
    border: 1px solid rgba(0, 210, 255, 0.35);
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 14px;
    box-shadow: 0 8px 26px rgba(0, 0, 0, 0.5);
}
.safety-panel {
    background: linear-gradient(135deg, rgba(32, 18, 20, 0.85) 0%, rgba(18, 8, 10, 0.95) 100%);
    border: 1px solid rgba(255, 107, 53, 0.45);
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 14px;
    box-shadow: 0 8px 26px rgba(0, 0, 0, 0.5);
}
.incident-box {
    background: rgba(16, 20, 36, 0.85);
    border-radius: 12px;
    padding: 18px;
    border: 1px solid rgba(255, 107, 53, 0.3);
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ── Color Palette & Plotly Layout ─────────────────────────────────────────────
PHASE_COLOR = {
    "Solid": "#00d2ff",
    "Liquid": "#ffa500",
    "Gaseous": "#00f5a0",
    "Historical": "#ff4d4d",
}

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#e2e8f8",
    font_family="Inter",
)

def html_table(row_dicts, max_height=420):
    """Render an HTML table safely with escaped values."""
    if not row_dicts:
        return "<p style='color:#8da4d0;padding:20px'>No matching records in current filter envelope.</p>"
    headers = list(row_dicts[0].keys())
    head = "".join(f"<th>{html.escape(str(h))}</th>" for h in headers)
    rows_html = []
    for r in row_dicts:
        cells = []
        for h in headers:
            raw_v = r.get(h, "")
            # Allow safely formatted link or span HTML
            if isinstance(raw_v, str) and (raw_v.startswith("<a ") or raw_v.startswith("<span ")):
                v = raw_v
            else:
                v = html.escape(str(raw_v))
            cells.append(f"<td>{v}</td>")
        rows_html.append(f"<tr>{''.join(cells)}</tr>")
    return (f'<div class="table-wrap" style="max-height:{max_height}px">'
            f'<table class="nasa-table"><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(rows_html)}</tbody></table></div>')

# ── Data Loading (Strict NASA PSI Traceability / Zero pandas / Zero numpy) ─────
@st.cache_data
def load_data():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "combustion_data.csv")
    if not os.path.exists(path):
        return None
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:    row["Year_Num"] = int(float(row.get("Year", 0)))
            except: row["Year_Num"] = None

            row["Is_Historical"] = row.get("Historical_Incident", "No").strip().lower() == "yes"

            raw_o2 = row.get("Test_Atmosphere_O2", "").strip()
            try:
                if " to " in raw_o2:
                    parts = raw_o2.split(" to ")
                    row["O2_Min"] = float(parts[0])
                    row["O2_Max"] = float(parts[1])
                    row["O2_Mid"] = (row["O2_Min"] + row["O2_Max"]) / 2.0
                    row["O2_Is_Range"] = True
                    row["O2_Numeric"] = row["O2_Mid"]
                else:
                    val = float(raw_o2)
                    row["O2_Min"] = val
                    row["O2_Max"] = val
                    row["O2_Mid"] = val
                    row["O2_Is_Range"] = False
                    row["O2_Numeric"] = val
            except:
                row["O2_Min"] = None
                row["O2_Max"] = None
                row["O2_Mid"] = None
                row["O2_Is_Range"] = False
                row["O2_Numeric"] = None

            # Fuel phase categorization
            fuel = row.get("Fuel_Type", "")
            if row["Is_Historical"]:
                row["Phase"] = "Historical"
            elif "Liquid" in fuel:
                row["Phase"] = "Liquid"
            elif "Gaseous" in fuel:
                row["Phase"] = "Gaseous"
            else:
                row["Phase"] = "Solid"

            rows.append(row)
    return rows

all_rows = load_data()

# ── Pre-load Asset Base64 Data URIs ───────────────────────────────────────────
robot_b64  = get_base64_image("cute_3d_robot.jpg")
astro_b64  = get_base64_image("cute_astronaut_3d.jpg")
ufo_b64    = get_base64_image("cute_ufo_3d.jpg")
saturn_b64 = get_base64_image("cute_saturn_3d.jpg")
iss_b64    = get_base64_image("3d_iss.jpg")
rocket_b64 = get_base64_image("3d_rocket.jpg")

# ── Sidebar Command Console ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;margin-bottom:8px;">
        <span style="font-family:'Orbitron',sans-serif;font-size:0.82rem;font-weight:900;letter-spacing:0.1em;color:#00d2ff;text-transform:uppercase;">
            🛸 Mission Companion
        </span>
    </div>
    """, unsafe_allow_html=True)

    companion = st.selectbox(
        "Choose Companion",
        ["🤖 NOVA (Research Assistant)", "🧑‍🚀 Commander Leo (Space Explorer)", "🛸 Navigator Zog (Gravity Observer)"],
        label_visibility="collapsed"
    )

    if "NOVA" in companion:
        if robot_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <img src="{robot_b64}" style="width:150px;height:auto;border-radius:20px;border:2px solid #00e5ff;box-shadow:0 0 24px rgba(0,229,255,0.6);background:#050a18;">
                <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                    <span class="cute-badge">✨ NOVA RESEARCH NOTE</span>
                </div>
                <div class="cute-speech-bubble">
                    Beep boop! 🤖 In microgravity, fire burns as calm, silent blue spheres without rising hot air! ✨
                </div>
            </div>
            """)
    elif "Leo" in companion:
        if astro_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <img src="{astro_b64}" style="width:150px;height:auto;border-radius:20px;border:2px solid #ffaa00;box-shadow:0 0 24px rgba(255,170,0,0.6);background:#050a18;">
                <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                    <span class="cute-badge" style="background:linear-gradient(90deg, #ff8c00, #ffd000);">🧑‍🚀 CREW DISPATCH</span>
                </div>
                <div class="cute-speech-bubble" style="border-color:rgba(255,170,0,0.65);">
                    Greetings! 🧑‍🚀 Spacecraft cabin ventilation fans feed fresh oxygen to fires. Airflow management is everything! 🚀
                </div>
            </div>
            """)
    else:
        if ufo_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <img src="{ufo_b64}" style="width:150px;height:auto;border-radius:20px;border:2px solid #00f5a0;box-shadow:0 0 24px rgba(0,245,160,0.6);background:#050a18;">
                <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                    <span class="cute-badge" style="background:linear-gradient(90deg, #00f5a0, #00d2ff);">🛸 GRAVITY SCAN</span>
                </div>
                <div class="cute-speech-bubble" style="border-color:rgba(0,245,160,0.65);">
                    Zorp! 🛸 NASA PSI currently has microgravity data; Moon (0.16g) and Mars (0.38g) in Tab 3 are hypothetical conceptual models! 🪐
                </div>
            </div>
            """)

    st.markdown("#### 🎛️ Investigation Filters")
    keyword = st.text_input("🔎 Search Investigations", placeholder="FLEX, Saffire, PMMA, O2, cool flame...")

    if all_rows:
        all_fuels = sorted({r["Fuel_Type"] for r in all_rows if r.get("Fuel_Type")})
        all_gravs = sorted({r["Gravity_Environment"] for r in all_rows if r.get("Gravity_Environment")})
        sel_fuel  = st.multiselect("🧪 Fuel Chemistry & Phase", all_fuels, default=all_fuels)
        sel_grav  = st.multiselect("🌌 Gravity Regime", all_gravs, default=all_gravs)
        sel_types = st.multiselect("📂 Record Category", ["Flight Investigation", "Historical Benchmark Incident"], default=["Flight Investigation", "Historical Benchmark Incident"])
        sel_o2 = st.selectbox("🫧 Oxygen Concentration", ["All oxygen levels", "Below 18%", "18%–21%", "Above 21%"])
    else:
        sel_fuel = sel_grav = sel_types = []
        sel_o2 = "All oxygen levels"

    st.markdown("---")

    # Deep Space Educational Card
    if saturn_b64:
        render_html(f"""
        <div style="text-align:center;margin-top:2px;">
            <div style="background:linear-gradient(135deg, rgba(20,28,52,0.85), rgba(10,14,28,0.95));border:1.5px solid rgba(255,208,0,0.4);border-radius:14px;padding:8px;box-shadow:0 8px 24px rgba(0,0,0,0.5);">
                <img src="{saturn_b64}" style="width:100%;border-radius:10px;display:block;">
                <div style="font-family:'Orbitron',sans-serif;font-size:0.72rem;font-weight:800;color:#ffd000;margin-top:6px;">
                    🪐 FUTURE EXPLORATION
                </div>
                <div style="font-size:0.67rem;color:#a6b9dc;margin-top:2px;">
                    Exploring Future Lunar &amp; Mars Fire Safety
                </div>
            </div>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 📡 NASA Archival Portals")
    st.markdown("• [🛰️ NASA PSI Database](https://psi.nasa.gov/physci/repo/search?q=combustion)")
    st.markdown("• [🔬 Glenn Fire Science](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/)")
    st.markdown("• [📖 ISS Research Guide](https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/)")

    st.markdown("---")
    st.caption("⚡ NASA Space Apps Challenge 2026 // Team Solo: Nikini Edirisinghe")
    st.caption("🎨 Mascot assets synthesized via Google Imagen / Gemini. Conceptual illustrations; depicts no real individuals or minors.")

if all_rows is None:
    st.error("❌ `combustion_data.csv` is missing from the working directory.")
    st.stop()

# ── Dynamic Counts & Filter Execution ─────────────────────────────────────────
n_experiments = sum(1 for r in all_rows if not r["Is_Historical"])
n_historical  = sum(1 for r in all_rows if r["Is_Historical"])

def apply_filters(rows):
    out = []
    kw = keyword.strip().lower()
    for r in rows:
        cat = "Historical Benchmark Incident" if r["Is_Historical"] else "Flight Investigation"
        if cat not in sel_types: continue
        if r["Fuel_Type"] not in sel_fuel: continue
        if r["Gravity_Environment"] not in sel_grav: continue
        o2_mid = r.get("O2_Mid")
        if sel_o2 == "Below 18%" and (o2_mid is None or o2_mid >= 18):
            continue
        elif sel_o2 == "18%–21%" and (
            o2_mid is None or not 18 <= o2_mid <= 21
        ):
            continue
        elif sel_o2 == "Above 21%" and (o2_mid is None or o2_mid <= 21):
            continue
        if kw:
            haystack = (r["Experiment_Name"] + r["Key_Findings"] + r["Fuel_Type"] + r["Mission"] + r["Sensors_And_Diagnostics"]).lower()
            if kw not in haystack: continue
        out.append(r)
    return out

rows = apply_filters(all_rows)

# ── Status Ticker (Archive Notice) ────────────────────────────────────────────
st.markdown("""
<div class="telemetry-ticker">
    <div class="ticker-left">
        <span class="ticker-badge"><span class="pulse-dot"></span> ARCHIVE DATA</span>
        <span>NASA PSI COMBUSTION ARCHIVE // CURATED FROM PUBLISHED TECHNICAL REPORTS</span>
    </div>
    <div style="font-size:0.75rem;color:#00d2ff;">
        STANDARD ISS CABIN REFERENCE: 21.0% O₂ | 101.3 kPa | 0.00g µG
    </div>
</div>
""", unsafe_allow_html=True)

# ── Hero Mission Command Header ───────────────────────────────────────────────
col_hero_text, col_hero_3d = st.columns([3.1, 1.3])
with col_hero_text:
    render_html(f"""
    <div class="hero-box" style="margin-bottom:0px;height:100%;">
        <div class="hero-title">🔥 FLAME IN FREEFALL</div>
        <div class="hero-sub">
            NASA Microgravity Combustion &amp; Spacecraft Fire Safety Research Hub for ISS, Moon &amp; Mars Habitats.
        </div>
        <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;">
            <span class="ticker-badge"><span class="pulse-dot"></span> ARCHIVE DATA</span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#00d2ff;background:rgba(0,210,255,0.08);border:1px solid rgba(0,210,255,0.25);padding:3px 10px;border-radius:6px;">
                🛰️ {n_experiments} EXPERIMENT RECORDS + {n_historical} HISTORICAL INCIDENTS
            </span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#ffd000;background:rgba(255,208,0,0.08);border:1px solid rgba(255,208,0,0.25);padding:3px 10px;border-radius:6px;">
                🌙 Exploring Future Lunar &amp; Mars Fire Safety
            </span>
        </div>
    </div>
    """)
with col_hero_3d:
    if iss_b64:
        render_html(f"""
        <div class="hero-3d-box">
            <img src="{iss_b64}" class="hero-3d-img" alt="ISS Orbital Fire Lab">
            <span class="hero-3d-title">🛸 ISS CIR FIRE LAB</span>
            <span class="hero-3d-sub">Combustion Integrated Rack &amp; MSG Experiments</span>
        </div>
        """)
    else:
        st.caption("🛸 ISS Orbital Module")

st.markdown("<br>", unsafe_allow_html=True)

# ── Main Tab Navigation ───────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛰️ NASA Experiment Explorer",
    "🤖 AI Research Briefing & Synthesis",
    "🎛️ Morphing Flame Physics Chamber",
    "📊 Evidence-Based Experiment Comparison",
    "⚖️ Head-to-Head & Historical Lessons",
])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 — ARCHIVAL TELEMETRY EXPLORER
# ═══════════════════════════════════════════════════════════════════════════════
with tab1:
    if astro_b64:
        render_html(f"""
        <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(135deg, rgba(14,24,50,0.75), rgba(8,14,30,0.9));border:1px solid rgba(0,210,255,0.3);border-radius:14px;padding:10px 18px;margin-bottom:18px;">
            <div style="flex-shrink:0;">
                <img src="{astro_b64}" style="width:48px;height:48px;border-radius:50%;border:2px solid #ffaa00;object-fit:cover;">
            </div>
            <div style="flex-grow:1;">
                <div style="font-family:'Orbitron',sans-serif;font-size:0.78rem;font-weight:800;color:#ffd000;">🧑‍🚀 COMMANDER LEO's FLIGHT LOG</div>
                <div style="font-size:0.84rem;color:#d1dbf4;margin-top:2px;">
                    "Without buoyant convection, flames in space form diffusion-limited domes. Use the filters to inspect verified NASA flight investigations and hardware setups!"
                </div>
            </div>
        </div>
        """)

    # Dynamic KPI Cards
    cur_exp  = sum(1 for r in rows if not r["Is_Historical"])
    cur_hist = sum(1 for r in rows if r["Is_Historical"])
    elev_o2  = sum(1 for r in rows if r.get("O2_Numeric") and r["O2_Numeric"] > 21.0)

    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="hud-card"><div class="hud-val">{len(rows)}</div><div class="hud-lbl">Filtered Records</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="hud-card" style="border-top-color:#00d2ff;"><div class="hud-val" style="color:#5ce1ff;">{cur_exp}</div><div class="hud-lbl">Flight Investigations</div></div>', unsafe_allow_html=True)
    k3.markdown(f'<div class="hud-card" style="border-top-color:#ff4d4d;"><div class="hud-val" style="color:#ff6b6b;">{cur_hist}</div><div class="hud-lbl">Historical Incidents</div></div>', unsafe_allow_html=True)
    k4.markdown(f'<div class="hud-card" style="border-top-color:#ffd000;"><div class="hud-val" style="color:#ffd000;">{elev_o2}</div><div class="hud-lbl">Elevated-O₂ Studies (>21%)</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("🛰️ **Data Provenance:** Hand-compiled from published NASA Technical Reports, the ISS Researcher's Guide to Combustion Science (NP-2015-10-034-JSC), and official NASA accident investigation board records. All links trace directly to official NASA repositories.")

    view_mode = st.radio("Display Mode:", ["📊 Comprehensive Archival Matrix", "🃏 Investigation Briefing Cards"], horizontal=True)

    if view_mode == "📊 Comprehensive Archival Matrix":
        tbl = []
        for r in rows:
            url = r.get("NASA_Source_URL", "")
            url_link = f'<a href="{html.escape(url)}" target="_blank" style="color:#00d2ff;font-weight:600;text-decoration:none;">🔗 NASA Record ↗</a>' if url else "—"
            tbl.append({
                "Investigation": r["Experiment_Name"],
                "Mission / Carrier": r["Mission"],
                "Fuel & Phase": r["Fuel_Type"],
                "Gravity Regime": r["Gravity_Environment"],
                "Test Atmosphere (O₂ %)": r["Test_Atmosphere_O2"],
                "Airflow Conditions": r["Airflow_Conditions"],
                "Spread / Burning Kinetics": r["Flame_Spread_Measurement"],
                "Extinction Limit Observation": r["Extinction_Limit_Observation"],
                "Diagnostics / Sensors": r["Sensors_And_Diagnostics"],
                "Quality": r["Data_Quality"],
                "Source Link": url_link,
            })
        st.markdown(html_table(tbl, max_height=460), unsafe_allow_html=True)
    else:
        cards_html = []
        for r in rows:
            col_bar = "#ff4d4d" if r["Is_Historical"] else ("#00d2ff" if "Solid" in r["Fuel_Type"] else ("#ffa500" if "Liquid" in r["Fuel_Type"] else "#00f5a0"))
            badge_text = "HISTORICAL BENCHMARK" if r["Is_Historical"] else "FLIGHT EXPERIMENT"
            url = r.get("NASA_Source_URL", "")
            link_html = f'<a href="{html.escape(url)}" target="_blank" style="color:#00d2ff;text-decoration:none;font-weight:600;">NASA Investigation Record ↗</a>' if url else ""
            
            cards_html.append(textwrap.dedent(f"""
            <div class="exp-card" style="border-left: 4px solid {col_bar};">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;">
                    <div style="font-family:'Orbitron',sans-serif;font-size:0.92rem;font-weight:700;color:#ffffff;">{html.escape(r['Experiment_Name'])}</div>
                    <span class="ticker-badge" style="border-color:{col_bar};color:{col_bar};font-size:0.65rem;">{badge_text}</span>
                </div>
                <div style="font-size:0.78rem;color:#8da4d0;margin-bottom:8px;">
                    🛰️ <b>{html.escape(r['Mission'])}</b> | 🌌 {html.escape(r['Gravity_Environment'])}
                </div>
                <div style="font-size:0.83rem;color:#c9d7f5;line-height:1.45;margin-bottom:10px;">
                    {html.escape(r['AI_Research_Summary'])}
                </div>
                <div style="font-size:0.75rem;color:#a6b9dc;margin-bottom:6px;">
                    <b>Airflow:</b> {html.escape(r['Airflow_Conditions'])}
                </div>
                <div style="font-size:0.75rem;color:#a6b9dc;margin-bottom:8px;">
                    <b>Diagnostics:</b> {html.escape(r['Sensors_And_Diagnostics'])}
                </div>
                <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #1a2744;padding-top:6px;font-size:0.75rem;">
                    <span style="color:#ffd000;">{html.escape(r['Measurement_Type'])}</span>
                    {link_html}
                </div>
            </div>
            """).strip())
        render_html(f'<div class="exp-grid">{"".join(cards_html)}</div>')

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 — AI RESEARCH BRIEFING & SYNTHESIS
# ═══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.info(
        "🤖 **AI Disclosure & Architecture:** The research summaries and operational takeaways below were "
        "**synthesized during project development using Google Gemini 1.5 Pro**, conditioned directly on the "
        "underlying NASA technical reports (NP-2015-10-034-JSC, Saffire reports, and NASA accident review boards). "
        "The model's outputs were verified and stored as static archival text in `combustion_data.csv`. "
        "**No generative AI is invoked at runtime.** AI-assisted summaries were prepared during development and reviewed against the cited research sources. "
        "This dashboard operates deterministically in Python. NOVA is an illustrated UI mascot, not a live conversational agent."
    )

    if not rows:
        st.warning("No investigations match the current filter selection.")
    else:
        names = [r["Experiment_Name"] for r in rows]
        sel_exp = st.selectbox("Select NASA Investigation to Inspect:", names)
        row = next(r for r in rows if r["Experiment_Name"] == sel_exp)

        st.markdown(f"### {html.escape(row['Experiment_Name'])}")
        st.caption(f"🛰️ **Carrier / Mission:** {row['Mission']} | 📅 **Year:** {row.get('Year_Num', '—')} | 🌌 **Regime:** {row['Gravity_Environment']} | 🧪 **Fuel:** {row['Fuel_Type']}")

        if row["Is_Historical"]:
            st.error("⚠️ HISTORICAL BENCHMARK: In-flight or pre-launch catastrophic accident investigation.")

        col_left, col_right = st.columns([2.5, 1.5])

        with col_left:
            render_html(f"""
            <div class="ai-panel">
                <div style="font-family:'JetBrains Mono',monospace;color:#00d2ff;font-size:0.82rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
                    <span>🤖</span> AI RESEARCH BRIEFING // EXECUTIVE SYNTHESIS
                </div>
                <div style="font-size:0.98rem;line-height:1.6;color:#f0f4ff;">
                    {html.escape(row['AI_Research_Summary'])}
                </div>
            </div>
            """)

            render_html(f"""
            <div class="safety-panel">
                <div style="font-family:'JetBrains Mono',monospace;color:#ff8c42;font-size:0.82rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
                    <span>🛰️</span> POTENTIAL SPACECRAFT RELEVANCE
                </div>
                <div style="font-size:0.96rem;line-height:1.6;color:#ffe8e0;">
                    {html.escape(row.get('Potential_Spacecraft_Relevance', row.get('Operational_Relevance', '')))}
                </div>
            </div>
            """)

            with st.expander("🔬 View Primary Investigator Findings & Telemetry Details"):
                st.markdown(f"**Primary Findings:** {row['Key_Findings']}")
                st.markdown(f"**Airflow Conditions:** `{row['Airflow_Conditions']}`")
                st.markdown(f"**Diagnostics & Sensors:** `{row['Sensors_And_Diagnostics']}`")
                st.markdown(f"**Measurement Classification:** `{row['Measurement_Type']}`")
                st.markdown(f"**Source Notes:** {row['Source_Notes']}")

        with col_right:
            st.markdown("#### 📑 Archival Citation & Metadata")
            st.markdown(f"**Test Atmosphere:** `{row['Test_Atmosphere_O2']}% O₂`")
            st.markdown(f"**Measurement Type:** `{row['Measurement_Type']}`")
            st.markdown(f"**Data Quality Status:** `{row['Data_Quality']}`")
            
            ref = row.get("DOI_Or_Reference", "")
            if ref:
                st.markdown(f"**Publication / DOI:** `{ref}`")

            url = row.get("NASA_Source_URL", "")
            if url:
                st.markdown(f"[🔗 View Official NASA Investigation Record]({url})")

            st.markdown("---")
            st.markdown("#### 🔍 Research Scope & Limitations")
            if "Droplet" in row["Fuel_Type"]:
                st.info("ℹ️ **Droplet Experiment:** Measures single-droplet burning rates and extinction diameters. Surface flame spread is not applicable.")
            elif "Gaseous" in row["Fuel_Type"]:
                st.info("ℹ️ **Gaseous Diffusion Experiment:** Measures gas flame structure, soot radiation, and extinction limits. Surface spread does not apply.")
            elif row["Is_Historical"]:
                st.warning("⚠️ **Historical Accident Record:** Included for baseline safety architecture context; excluded from quantitative microgravity comparisons.")
            else:
                st.success("✅ **Solid Combustion Test:** Evaluated material surface flammability under controlled low-speed forced ventilation.")

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 — MORPHING FLAME PHYSICS CHAMBER (CONCEPTUAL VISUALIZER)
# ═══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("### 🎛️ Conceptual Visualizer of Low-Gravity Flame Physics")
    
    st.warning(
        "⚠️ **Conceptual Educational Visualizer:** This interactive chamber illustrates **qualitative flame behavior** "
        "observed during NASA microgravity flight investigations (such as spherical diffusion flames in quiescent air, "
        "flame elongation and tilt under forced ventilation, and altered soot luminosity). "
        "**This is an educational visualization and NOT a validated numerical CFD or combustion physics simulation.** "
        "It does NOT compute ignition probabilities or fire risk scores, and no real-world spacecraft safety decisions should be based on it."
    )

    s1, s2, s3 = st.columns(3)
    sim_o2   = s1.slider("Cabin Oxygen Concentration (%)", 14.0, 36.0, 21.0, 0.5)
    sim_flow = s2.slider("Ventilation Airflow Velocity (cm/s)", 0.0, 30.0, 10.0, 1.0)
    sim_grav = s3.selectbox("Gravity Environment Regime", [
        "0.00g — ISS Microgravity (Freefall)",
        "0.16g — Lunar Surface (Hypothetical Illustration; PSI holds no partial-g data)",
        "0.38g — Martian Surface (Hypothetical Illustration; PSI holds no partial-g data)",
        "1.00g — Earth Reference",
    ])

    is_microg = "0.00g" in sim_grav
    is_lunar  = "0.16g" in sim_grav
    is_mars   = "0.38g" in sim_grav

    tilt_deg = min(sim_flow * 1.8, 38)

    # Physical regime identification
    if sim_flow < 2 and is_microg:
        regime_title = "QUIESCENT DIFFUSION REGIME (Spherical Dome; Oxygen Transport Limited)"
        regime_desc = "Without buoyancy or ventilation, oxygen transport relies strictly on molecular diffusion. As demonstrated in BASS, thin fuels starve and extinguish unless external heat flux is sustained."
    elif 4 <= sim_flow <= 18 and is_microg:
        regime_title = "VENTILATION-FED CONVECTIVE REGIME (Airflow-Assisted Flame Spread)"
        regime_desc = "Forced airflow (5–18 cm/s) sweeps away extinguishing soot and replenishes oxygen to the flame front. Saffire-I and Saffire-III demonstrated that flame spread rate increases with ventilation speed."
    elif sim_o2 > 24.0:
        regime_title = "ELEVATED-OXYGEN EXPLORATION REGIME (Intense Oxidation & Radical Release)"
        regime_desc = "Elevated oxygen atmospheres (26.5% to 34% planned for lunar airlocks) lower material ignition energy thresholds and accelerate combustion reaction rates, as observed in Saffire-VI."
    elif is_lunar or is_mars:
        regime_title = "WEAK BUOYANCY REGIME (Hypothetical Conceptual Exploration)"
        regime_desc = "Note: NASA PSI currently holds no tabulated partial-gravity combustion datasets. In theory, weak fractional gravity generates slight buoyancy, producing a transition between spherical 0-g domes and elongated 1-g plumes."
    else:
        regime_title = "STANDARD BUOYANT CONVECTIVE PLUME (Earth Reference)"
        regime_desc = "At 1.00g, buoyancy drives hot gases upward at ~1–2 m/s, creating the familiar teardrop flame shape."

    # Visual coloring
    if sim_o2 < 16.5:
        core_c1, core_c2, halo_c = "#00d2ff", "#1e3cff", "rgba(0, 210, 255, 0.35)"
    elif sim_o2 > 24.0:
        core_c1, core_c2, halo_c = "#ffffff", "#ffb700", "rgba(255, 65, 0, 0.6)"
    else:
        core_c1 = "#ffe875" if not is_microg else "#7be0ff"
        core_c2 = "#ff5500" if not is_microg else "#0077ff"
        halo_c  = "rgba(255, 107, 53, 0.45)"

    if is_microg and sim_flow < 3:
        flame_svg_shape = f"""
        <circle cx="200" cy="140" r="48" fill="url(#flameGrad)" filter="url(#glowFilter)" />
        <circle cx="200" cy="140" r="24" fill="{core_c1}" opacity="0.85" filter="url(#glowFilter)" />
        <circle cx="200" cy="140" r="10" fill="#ffffff" opacity="0.9" />
        """
    elif is_microg and sim_flow >= 3:
        flame_svg_shape = f"""
        <g transform="rotate({tilt_deg}, 200, 150)">
            <ellipse cx="200" cy="140" rx="42" ry="62" fill="url(#flameGrad)" filter="url(#glowFilter)" />
            <ellipse cx="200" cy="145" rx="20" ry="36" fill="{core_c1}" opacity="0.85" />
            <circle cx="200" cy="155" r="9" fill="#ffffff" />
        </g>
        """
    else:
        flame_h = 105 if is_lunar else (125 if is_mars else 150)
        flame_svg_shape = f"""
        <g transform="rotate({tilt_deg * 0.7}, 200, 180)">
            <path d="M 200, {190 - flame_h} C 160, 130 165, 185 200, 190 C 235, 185 240, 130 200, {190 - flame_h} Z" 
                  fill="url(#flameGrad)" filter="url(#glowFilter)" />
            <path d="M 200, {190 - (flame_h * 0.65)} C 178, 145 182, 182 200, 186 C 218, 182 222, 145 200, {190 - (flame_h * 0.65)} Z" 
                  fill="{core_c1}" opacity="0.9" />
            <circle cx="200" cy="178" r="8" fill="#ffffff" />
        </g>
        """

    flame_chamber_html = f"""
    <div style="background: radial-gradient(circle at 50% 50%, #0d152b 0%, #060914 85%);
                border: 2px solid rgba(0, 210, 255, 0.4); border-radius: 16px;
                padding: 16px; box-shadow: 0 0 35px rgba(0,0,0,0.8);
                text-align: center; position: relative;">
        <div style="display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#00d2ff;margin-bottom:8px;border-bottom:1px solid #1a2a4c;padding-bottom:6px;">
            <span>CHAMBER: CONCEPTUAL FLUID MODEL</span>
            <span>REGIME: {regime_title}</span>
        </div>
        
        <svg width="100%" height="240" viewBox="0 0 400 240" style="overflow:visible;">
            <defs>
                <filter id="glowFilter" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur1" />
                    <feGaussianBlur in="SourceGraphic" stdDeviation="18" result="blur2" />
                    <feMerge>
                        <feMergeNode in="blur2" />
                        <feMergeNode in="blur1" />
                        <feMergeNode in="SourceGraphic" />
                    </feMerge>
                </filter>
                <radialGradient id="flameGrad" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="{core_c1}" stop-opacity="0.95" />
                    <stop offset="50%" stop-color="{core_c2}" stop-opacity="0.8" />
                    <stop offset="100%" stop-color="{halo_c}" stop-opacity="0.0" />
                </radialGradient>
            </defs>

            <line x1="20" y1="120" x2="380" y2="120" stroke="rgba(0, 210, 255, 0.15)" stroke-dasharray="4,4" />
            <line x1="200" y1="20" x2="200" y2="220" stroke="rgba(0, 210, 255, 0.15)" stroke-dasharray="4,4" />
            <circle cx="200" cy="140" r="95" stroke="rgba(0, 210, 255, 0.1)" fill="none" stroke-width="1" />
            <rect x="196" y="188" width="8" height="24" fill="#586c8f" rx="2" />
            <circle cx="200" cy="188" r="4" fill="#ff6b35" />
            {flame_svg_shape}
        </svg>

        <div style="display:flex;justify-content:space-around;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#8da4d0;margin-top:6px;border-top:1px solid #1a2a4c;padding-top:6px;">
            <span>BUOYANCY VECTOR: {"0.00 m/s² (QUIESCENT)" if is_microg else ("1.62 m/s² (WEAK)" if is_lunar else ("3.72 m/s² (FRACTIONAL)" if is_mars else "9.81 m/s² (FULL)"))}</span>
            <span>AIRFLOW DEFLECTION TILT: {tilt_deg:.1f}°</span>
            <span>CHAMBER O₂: {sim_o2}%</span>
        </div>
    </div>
    """
    components.html(f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>body{{margin:0;padding:0;background:transparent;overflow:hidden;}}</style></head><body>{flame_chamber_html}</body></html>""", height=280)
    st.markdown("<br>", unsafe_allow_html=True)

    col_desc, col_advisory = st.columns([1.8, 1.2])
    with col_desc:
        st.markdown(f"#### 🔬 Conceptual Interpretation")
        st.info(f"**{regime_title}**\n\n{regime_desc}")
    with col_advisory:
        st.markdown("#### 📖 NASA Flight Observations")
        if is_microg and sim_flow < 2:
            st.markdown("• **BASS & BASS-II:** Thin materials self-extinguished in still air when ventilation dropped below ~2 cm/s.")
        elif is_microg and sim_flow >= 10:
            st.markdown("• **Saffire-I & III:** Large-scale fabrics burned vigorously when airflow reached 20 cm/s.")
        elif sim_o2 > 24.0:
            st.markdown("• **Saffire-VI:** Smoldering in 26.5% O₂ exploration atmospheres produced elevated CO/HCN gas concentrations.")
        else:
            st.markdown("• **Standard Microgravity Physics:** Diffusion limits dominate; flame behavior is controlled by forced airflow currents.")

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 — EVIDENCE-BASED EXPERIMENT COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
with tab4:
    flight_rows = [r for r in rows if not r["Is_Historical"]]
    st.markdown("### 📊 Evidence-Based Experiment Comparison & Synthesis")
    st.caption("Systematic multi-parameter comparison across NASA microgravity combustion investigations.")

    c_left, c_right = st.columns([1.2, 1])

    with c_left:
        st.markdown("#### 🧪 Research Timeline & Tested Oxygen Concentrations")
        fig_scatter = go.Figure()

        phases = ["Solid", "Liquid", "Gaseous", "Historical"]
        for p in phases:
            sub = [r for r in flight_rows if r["Phase"] == p and r.get("Year_Num") is not None and r.get("O2_Mid") is not None]
            if not sub: continue
            
            y_mid = [r["O2_Mid"] for r in sub]
            y_err_plus = [r["O2_Max"] - r["O2_Mid"] for r in sub]
            y_err_minus = [r["O2_Mid"] - r["O2_Min"] for r in sub]
            has_error = any(e > 0.01 for e in y_err_plus)
            
            error_dict = dict(
                type="data",
                symmetric=False,
                array=y_err_plus,
                arrayminus=y_err_minus,
                color=PHASE_COLOR.get(p, "#00d2ff"),
                thickness=2,
                width=6
            ) if has_error else None

            fig_scatter.add_trace(go.Scatter(
                x=[r["Year_Num"] for r in sub],
                y=y_mid,
                error_y=error_dict,
                mode="markers+text",
                name=f"{p} Investigation",
                marker=dict(
                    size=16,
                    color=PHASE_COLOR.get(p, "#00d2ff"),
                    opacity=0.88,
                    line=dict(color="#ffffff", width=1.5)
                ),
                text=[r["Experiment_Name"].split()[0] for r in sub],
                textposition="top center",
                hovertemplate="<b>%{customdata[0]}</b><br>Year: %{x}<br>Tested O₂: %{customdata[2]}%<br>Carrier: %{customdata[1]}<extra></extra>",
                customdata=[[r["Experiment_Name"], r["Mission"], r["Test_Atmosphere_O2"]] for r in sub],
            ))

        fig_scatter.update_layout(
            title=dict(text="NASA Flight Experiments: Atmosphere O₂ Range (%) vs. Calendar Year", font=dict(family="Orbitron", size=13)),
            xaxis_title="Mission Year",
            yaxis_title="Tested Oxygen Concentration Range (%)",
            height=420,
            margin=dict(l=10, r=20, t=40, b=30),
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
            **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.caption("Vertical range bars represent the full parametric oxygen concentration range tested (e.g. BASS: 17.0%–21.0% O₂). Discrete markers represent single-atmosphere test conditions.")

    with c_right:
        st.markdown("#### 🧬 Fuel Physical Phase Distribution")
        phase_counts = {}
        for r in flight_rows:
            phase_counts[r["Phase"]] = phase_counts.get(r["Phase"], 0) + 1

        fig_donut = go.Figure(go.Pie(
            labels=list(phase_counts.keys()),
            values=list(phase_counts.values()),
            hole=0.6,
            marker=dict(colors=[PHASE_COLOR.get(k, "#888") for k in phase_counts], line=dict(color="#090e1d", width=2)),
            textinfo="label+value",
            hoverinfo="label+value+percent",
        ))
        fig_donut.update_layout(
            title=dict(text="Investigation Distribution by Fuel Phase", font=dict(family="Orbitron", size=13)),
            height=420,
            margin=dict(l=10, r=10, t=40, b=30),
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    st.markdown("---")
    st.markdown("#### 🔬 Detailed Experimental Parameters & Instrumentation Comparison")
    comp_tbl = []
    for r in flight_rows:
        url = r.get("NASA_Source_URL", "")
        link = f'<a href="{html.escape(url)}" target="_blank" style="color:#00d2ff;text-decoration:none;">Record ↗</a>' if url else "—"
        comp_tbl.append({
            "Experiment": r["Experiment_Name"],
            "Fuel Chemistry": r["Fuel_Type"],
            "Regime": r["Gravity_Environment"],
            "O₂ Level": r["Test_Atmosphere_O2"],
            "Airflow": r["Airflow_Conditions"],
            "Key Measurement": r["Flame_Spread_Measurement"],
            "Sensors / Instrumentation": r["Sensors_And_Diagnostics"],
            "Verified Findings": r["Key_Findings"][:110] + "…",
            "NASA Link": link
        })
    st.markdown(html_table(comp_tbl, max_height=420), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🔭 Critical Research Gaps & Frontiers")
    g1, g2, g3 = st.columns(3)
    with g1:
        st.info(
            "🌑 **Partial-Gravity Data Gap:**\n\n"
            "NASA PSI currently tabulates microgravity (0g) data. Quantitative combustion flammability on the Lunar surface (0.16g) "
            "and Martian surface (0.38g) remains an active research frontier (SoFIE project). Certified partial-g data is not yet in PSI."
        )
    with g2:
        st.info(
            "💨 **Long-Duration Smoldering in Exploration Atmospheres:**\n\n"
            "Smoldering combustion under 26.5% to 34% O₂ exploration atmospheres produces elevated carbon monoxide and hydrogen cyanide. "
            "Long-duration smoldering kinetics inside packed avionics racks remain under active investigation."
        )
    with g3:
        st.info(
            "🧯 **Suppression Agent Efficacy in Zero-G:**\n\n"
            "FLEX-2 demonstrated that gaseous suppression agents (CO₂) behave differently in space without gravity-driven convective mixing. "
            "Optimal discharge durations and nozzle designs require tailored microgravity qualification."
        )

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 — HEAD-TO-HEAD & HISTORICAL LESSONS
# ═══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("### ⚖️ Side-by-Side Investigation Comparison")
    st.caption("Select two NASA investigations to inspect comparative objectives, environments, and findings.")

    exp_list = [r["Experiment_Name"] for r in flight_rows]
    if len(exp_list) >= 2:
        c1, c2 = st.columns(2)
        exp_a = c1.selectbox("🔴 Investigation A", exp_list, index=0)
        exp_b = c2.selectbox("🔵 Investigation B", exp_list, index=min(1, len(exp_list)-1))

        if exp_a != exp_b:
            ra = next(r for r in rows if r["Experiment_Name"] == exp_a)
            rb = next(r for r in rows if r["Experiment_Name"] == exp_b)

            ca, cb = st.columns(2)
            with ca:
                st.markdown(f"#### 🔴 {html.escape(exp_a)}")
                st.markdown(f"**Carrier / Mission:** {ra['Mission']}")
                st.markdown(f"**Fuel Type:** {ra['Fuel_Type']}")
                st.markdown(f"**Gravity Environment:** {ra['Gravity_Environment']}")
                st.markdown(f"**Test Atmosphere:** {ra['Test_Atmosphere_O2']}% O₂")
                st.markdown(f"**Airflow Conditions:** {ra['Airflow_Conditions']}")
                st.markdown(f"**Primary Measurement:** {ra['Flame_Spread_Measurement']}")
                st.markdown(f"**Diagnostics:** {ra['Sensors_And_Diagnostics']}")
                st.markdown(f"**Key Findings:** {ra['Key_Findings']}")
                if ra.get("NASA_Source_URL"):
                    st.markdown(f"[🔗 Official NASA Investigation Record]({ra['NASA_Source_URL']})")

            with cb:
                st.markdown(f"#### 🔵 {html.escape(exp_b)}")
                st.markdown(f"**Carrier / Mission:** {rb['Mission']}")
                st.markdown(f"**Fuel Type:** {rb['Fuel_Type']}")
                st.markdown(f"**Gravity Environment:** {rb['Gravity_Environment']}")
                st.markdown(f"**Test Atmosphere:** {rb['Test_Atmosphere_O2']}% O₂")
                st.markdown(f"**Airflow Conditions:** {rb['Airflow_Conditions']}")
                st.markdown(f"**Primary Measurement:** {rb['Flame_Spread_Measurement']}")
                st.markdown(f"**Diagnostics:** {rb['Sensors_And_Diagnostics']}")
                st.markdown(f"**Key Findings:** {rb['Key_Findings']}")
                if rb.get("NASA_Source_URL"):
                    st.markdown(f"[🔗 Official NASA Investigation Record]({rb['NASA_Source_URL']})")
    else:
        st.warning("Please maintain at least two investigations in your filter selection for side-by-side comparison.")

    st.markdown("---")
    st.markdown("### 🏛️ Historical Space Fires & Lessons Learned")
    st.caption("How real flight emergencies established modern spacecraft life-support and flammability architectures.")

    h1, h2, h3 = st.columns(3)
    incidents = [
        (h1, "#ff6b6b", "🚀 Apollo 1 (1967)",
         "A 100% pure oxygen cabin atmosphere at 16.7 psi caused an instantaneous electrical flashover within 17 seconds during a pre-launch pad test.",
         "NASA eliminated pure oxygen ground operations, mandated mixed nitrogen-oxygen cabin atmospheres, and standardized material flammability screening under NASA-STD-6001.",
         "https://sma.nasa.gov/sma-disciplines/accllp/apollo-1"),
        (h2, "#ffa500", "🌙 Apollo 13 (1970)",
         "Damaged Teflon wire insulation sparked inside cryogenic oxygen tank 2, causing an electrical arc and tank rupture en route to the Moon.",
         "Redesigned spacecraft oxygen tanks with zero internal wiring or immersed electrical components, added isolated backup batteries, and established lifeboat emergency procedures.",
         "https://sma.nasa.gov/sma-disciplines/accllp/apollo-13"),
        (h3, "#ffd166", "🛸 Mir Station Fire (1997)",
         "A solid-fuel perchlorate oxygen candle ignited unexpectedly, burning for 14 minutes and filling the Mir station with dense, toxic smoke.",
         "The ISS adopted water-electrolysis oxygen generation rather than chemical candles as the primary system, and mandates multiple unobstructed egress routes at all times.",
         "https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/"),
    ]
    for col, color, title, what, fix, link in incidents:
        col.markdown(textwrap.dedent(f"""
        <div class="incident-box" style="border-left: 4px solid {color};">
            <h4 style="color:{color};margin-top:0;">{title}</h4>
            <p style="color:#c9d7f5;font-size:0.88rem;line-height:1.5;">{what}</p>
            <p style="color:#00f5a0;font-size:0.84rem;line-height:1.45;"><b>✅ Modern Architecture Fix:</b> {fix}</p>
            <a href="{link}" target="_blank" style="color:{color};font-size:0.78rem;text-decoration:none;">NASA Official Incident Archive ↗</a>
        </div>
        """).strip(), unsafe_allow_html=True)

# ── Footer & Asset Attribution ────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;color:#475d84;font-size:0.76rem;padding:22px;border-top:1px solid #141f38;margin-top:30px;line-height:1.6;">
    🔥 <b>NASA Flame in Freefall</b> · NASA Space Apps Challenge 2026 · Built by Nikini Edirisinghe<br>
    🛰️ <i>Data Sources: NASA Physical Sciences Informatics (PSI), ISS Researcher's Guide to Combustion Science (NP-2015-10-034-JSC), Saffire Project flight reports, and NASA Accident Review Boards.</i><br>
    🎨 <i>Asset Attribution: Companion mascot illustrations (NOVA, Commander Leo, Navigator Zog) and 3D spacecraft modules were generated using Google Imagen / Gemini. They depict fictional conceptual avatars and contain no depictions of real individuals or minors.</i><br>
    ⚠️ <i>Notice of Limitation: This educational demonstration is an interactive prototype; it is not certified for operational flight planning or certified spacecraft life-support engineering.</i>
</div>
""", unsafe_allow_html=True)
