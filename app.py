import streamlit as st
import streamlit.components.v1 as components
import csv
import os
import math
import textwrap
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

# ── Master Aerospace HUD & Cyber-Space CSS ────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

/* Deep Space Canvas with Holographic Grid & Vignette */
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

/* Custom Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #070b16; }
::-webkit-scrollbar-thumb { background: #1e2c4f; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #ff6b35; }

/* Sidebar Command Deck */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #090e1d 0%, #060914 100%);
    border-right: 1px solid rgba(0, 210, 255, 0.2);
    box-shadow: 10px 0 30px rgba(0, 0, 0, 0.6);
}

/* 3D Aerospace Holographic Image Cards */
[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid rgba(0, 210, 255, 0.45);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.75), 0 0 20px rgba(0, 210, 255, 0.25);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
[data-testid="stImage"] img:hover {
    transform: translateY(-3px) scale(1.02);
    border-color: rgba(255, 107, 53, 0.8);
    box-shadow: 0 14px 38px rgba(255, 107, 53, 0.4);
}

/* Scanline Overlay Effect */
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

/* Animations */
@keyframes pulse-glow {
    0%   { box-shadow: 0 0 0 0 rgba(0, 245, 160, 0.8); }
    70%  { box-shadow: 0 0 0 9px rgba(0, 245, 160, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 245, 160, 0); }
}

@keyframes flame-shimmer {
    0%   { filter: drop-shadow(0 0 16px rgba(255, 77, 0, 0.7)); }
    50%  { filter: drop-shadow(0 0 28px rgba(255, 170, 0, 0.95)); }
    100% { filter: drop-shadow(0 0 16px rgba(255, 77, 0, 0.7)); }
}

@keyframes scan-horizontal {
    0%   { left: -100%; }
    100% { left: 200%; }
}

/* Zero-G Floating Microgravity Animations */
@keyframes zero-g-float {
    0%   { transform: translateY(0px) rotate(0deg); }
    33%  { transform: translateY(-11px) rotate(2deg); }
    66%  { transform: translateY(-4px) rotate(-1.5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes zero-g-bob {
    0%   { transform: translateY(0px) rotate(0deg); }
    50%  { transform: translateY(-12px) rotate(3deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes ufo-hover {
    0%   { transform: translateY(0px) scale(1); filter: drop-shadow(0 0 15px rgba(0, 245, 160, 0.4)); }
    50%  { transform: translateY(-9px) scale(1.03); filter: drop-shadow(0 0 25px rgba(0, 245, 160, 0.75)); }
    100% { transform: translateY(0px) scale(1); filter: drop-shadow(0 0 15px rgba(0, 245, 160, 0.4)); }
}

@keyframes saturn-wobble {
    0%   { transform: translateY(0px) rotate(0deg); }
    50%  { transform: translateY(-8px) rotate(-2.5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes robot-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 229, 255, 0.45); }
    50%      { box-shadow: 0 0 35px rgba(0, 229, 255, 0.85), 0 0 50px rgba(0, 229, 255, 0.3); }
}

.floating-robot {
    animation: zero-g-float 4.2s ease-in-out infinite;
    display: inline-block;
}

.floating-astronaut {
    animation: zero-g-bob 4.8s ease-in-out infinite;
    display: inline-block;
}

.floating-ufo {
    animation: ufo-hover 3.6s ease-in-out infinite;
    display: inline-block;
}

.floating-saturn {
    animation: saturn-wobble 6s ease-in-out infinite;
    display: inline-block;
}

.floating-hero-card {
    animation: zero-g-float 5.5s ease-in-out infinite;
}

.hero-3d-box {
    background: linear-gradient(135deg, rgba(14,24,48,0.85), rgba(8,14,30,0.95));
    border: 1.5px solid rgba(0,210,255,0.45);
    border-radius: 18px;
    padding: 10px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.7), 0 0 22px rgba(0,210,255,0.22);
    text-align: center;
    position: relative;
    overflow: hidden;
}

.hero-3d-img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    border: 1px solid rgba(0,210,255,0.3);
    display: block;
}

.hero-3d-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.78rem;
    font-weight: 800;
    color: #00d2ff;
    letter-spacing: 0.06em;
    display: block;
    margin-top: 8px;
}

.hero-3d-sub {
    font-size: 0.68rem;
    color: #8da4d0;
    display: block;
    margin-top: 2px;
}

.cute-speech-bubble {
    position: relative;
    background: linear-gradient(135deg, rgba(13, 26, 52, 0.95), rgba(8, 16, 36, 0.98));
    border: 1.5px solid rgba(0, 229, 255, 0.55);
    border-radius: 16px;
    padding: 12px 16px;
    color: #e2f1ff;
    font-size: 0.84rem;
    line-height: 1.5;
    box-shadow: 0 8px 24px rgba(0, 229, 255, 0.2);
    margin-top: 10px;
    margin-bottom: 14px;
}
.cute-speech-bubble::before {
    content: "";
    position: absolute;
    top: -8px;
    left: 45%;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 8px solid rgba(0, 229, 255, 0.65);
}

.cute-badge {
    background: linear-gradient(90deg, #ff5e7e 0%, #ff8da4 100%);
    color: white;
    font-weight: 800;
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 99px;
    letter-spacing: 0.06em;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    box-shadow: 0 0 12px rgba(255, 94, 126, 0.4);
}

/* Live Telemetry Bar */
.telemetry-ticker {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(10, 16, 32, 0.85);
    border: 1px solid rgba(0, 210, 255, 0.3);
    border-radius: 8px;
    padding: 7px 16px;
    margin-bottom: 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #8da4d0;
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}
.ticker-left { display: flex; align-items: center; gap: 12px; }
.ticker-badge {
    background: rgba(0, 245, 160, 0.12);
    border: 1px solid #00f5a0;
    color: #00f5a0;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 700;
}
.pulse-dot {
    width: 8px; height: 8px; background: #00f5a0;
    border-radius: 50%; display: inline-block;
    animation: pulse-glow 1.8s infinite;
}

/* Hero Command Box */
.hero-box {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, rgba(255, 69, 0, 0.16) 0%, rgba(13, 21, 44, 0.88) 50%, rgba(0, 210, 255, 0.12) 100%);
    border: 1px solid rgba(255, 107, 53, 0.45);
    border-radius: 18px;
    padding: 28px 34px;
    margin-bottom: 22px;
    backdrop-filter: blur(14px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255,255,255,0.1);
}
.hero-box::after {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 45%; height: 2px;
    background: linear-gradient(90deg, transparent, #ff9e00, transparent);
    animation: scan-horizontal 4s linear infinite;
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.7rem;
    font-weight: 900;
    letter-spacing: 0.05em;
    background: linear-gradient(90deg, #ff4100 0%, #ff8c00 40%, #ffd000 80%, #ffffff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.15;
    animation: flame-shimmer 3.5s ease-in-out infinite;
}
.hero-sub {
    color: #a7bbdf;
    font-size: 1.05rem;
    margin-top: 10px;
    max-width: 860px;
    line-height: 1.55;
}

/* Sci-Fi Corner-Cut Cards (KPI HUD) */
.hud-card {
    background: linear-gradient(145deg, rgba(16, 24, 46, 0.8) 0%, rgba(9, 14, 28, 0.9) 100%);
    border: 1px solid rgba(0, 210, 255, 0.22);
    border-top: 3px solid #ff6b35;
    border-radius: 14px;
    padding: 22px 18px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    position: relative;
}
.hud-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 107, 53, 0.7);
    box-shadow: 0 14px 34px rgba(255, 107, 53, 0.25);
}
.hud-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.25rem;
    font-weight: 900;
    color: #ffffff;
    text-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
}
.hud-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: #8da4d0;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-top: 7px;
}

/* Risk Badges */
.badge-high {
    background: rgba(255, 59, 59, 0.18);
    border: 1px solid #ff4d4d;
    color: #ff7b7b;
    box-shadow: 0 0 14px rgba(255, 59, 59, 0.35);
    padding: 4px 12px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.8rem;
    display: inline-block;
}
.badge-medium {
    background: rgba(255, 165, 0, 0.18);
    border: 1px solid #ffa500;
    color: #ffc266;
    box-shadow: 0 0 14px rgba(255, 165, 0, 0.3);
    padding: 4px 12px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.8rem;
    display: inline-block;
}
.badge-low {
    background: rgba(0, 245, 160, 0.14);
    border: 1px solid #00f5a0;
    color: #5cffc3;
    box-shadow: 0 0 14px rgba(0, 245, 160, 0.28);
    padding: 4px 12px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.8rem;
    display: inline-block;
}

/* Mission Panels */
.ai-panel {
    background: linear-gradient(145deg, rgba(16, 28, 54, 0.85), rgba(8, 14, 30, 0.95));
    border: 1px solid rgba(0, 210, 255, 0.35);
    border-left: 5px solid #00d2ff;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
}
.safety-panel {
    background: linear-gradient(145deg, rgba(46, 18, 14, 0.85), rgba(22, 9, 8, 0.95));
    border: 1px solid rgba(255, 107, 53, 0.45);
    border-left: 5px solid #ff6b35;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
}

/* Tabs Styling */
[data-baseweb="tab-list"] {
    background: rgba(9, 14, 28, 0.85);
    padding: 7px;
    border-radius: 14px;
    border: 1px solid rgba(0, 210, 255, 0.25);
    gap: 8px;
}
[data-baseweb="tab"] {
    background-color: transparent !important;
    border-radius: 10px !important;
    color: #92a7ce !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    padding: 11px 20px !important;
    transition: all 0.2s ease !important;
}
[aria-selected="true"] {
    background: linear-gradient(90deg, rgba(255, 65, 0, 0.3), rgba(255, 140, 0, 0.2)) !important;
    border: 1px solid rgba(255, 107, 53, 0.7) !important;
    color: #ffb852 !important;
    box-shadow: 0 4px 14px rgba(255, 107, 53, 0.25) !important;
}

/* Interactive Experiment Grid Hologram Cards */
.exp-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
    margin-top: 14px;
}
.exp-card {
    background: linear-gradient(145deg, rgba(14, 22, 42, 0.75) 0%, rgba(8, 13, 26, 0.85) 100%);
    border: 1px solid rgba(110, 145, 225, 0.22);
    border-radius: 12px;
    padding: 16px 20px;
    transition: all 0.2s ease;
    cursor: default;
}
.exp-card:hover {
    border-color: rgba(0, 210, 255, 0.6);
    box-shadow: 0 8px 24px rgba(0, 210, 255, 0.15);
    transform: translateY(-2px);
}

/* Pure HTML table styles */
.nasa-table { width:100%; border-collapse:collapse; min-width:640px; }
.nasa-table th {
    padding: 11px 14px; text-align: left; border-bottom: 2px solid #233458;
    color: #8da4d0; font-family: 'JetBrains Mono', monospace; font-size: 0.76rem;
    text-transform: uppercase; letter-spacing: .08em; white-space: nowrap;
    background: #090e1d; position: sticky; top: 0; z-index: 2;
}
.nasa-table td {
    padding: 9px 14px; border-bottom: 1px solid #141f36;
    color: #d1dbf4; font-size: 0.87rem; white-space: nowrap;
}
.nasa-table tr:nth-child(even) td { background: #0c1326; }
.nasa-table tr:nth-child(odd)  td { background: #080d1a; }
.nasa-table tr:hover td { background: #131d38; }
.table-wrap {
    overflow: auto; border: 1px solid #1f2f54; border-radius: 14px;
    background: #080d1a; box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

/* Incident Cards */
.incident-box {
    background: linear-gradient(135deg, rgba(38, 14, 18, 0.88), rgba(16, 9, 20, 0.94));
    border: 1px solid rgba(255, 77, 77, 0.4);
    border-radius: 14px;
    padding: 22px 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 26px rgba(0, 0, 0, 0.5);
}
</style>
""", unsafe_allow_html=True)

# ── Color Palette & Helpers ───────────────────────────────────────────────────
RISK_COLOR = {"High": "#ff4d4d", "Medium": "#ffa500", "Low": "#00f5a0"}

def risk_badge(level):
    cls = {"High": "badge-high", "Medium": "badge-medium", "Low": "badge-low"}.get(level, "badge-low")
    return f'<span class="{cls}">● {level.upper()} RISK</span>'

def safe_mean(vals):
    return round(sum(vals)/len(vals), 1) if vals else 0.0

def html_table(row_dicts, max_height=420):
    if not row_dicts:
        return "<p style='color:#8da4d0;padding:20px'>No matching records in filter envelope.</p>"
    headers = list(row_dicts[0].keys())
    head = "".join(f"<th>{h}</th>" for h in headers)
    rows_html = []
    for r in row_dicts:
        cells = []
        for h in headers:
            v = str(r.get(h, ""))
            if v in RISK_COLOR:
                col = RISK_COLOR[v]
                v = f"<span style='color:{col};font-weight:700'>{v}</span>"
            cells.append(f"<td>{v}</td>")
        rows_html.append(f"<tr>{''.join(cells)}</tr>")
    return (f'<div class="table-wrap" style="max-height:{max_height}px">'
            f'<table class="nasa-table"><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(rows_html)}</tbody></table></div>')

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#e2e8f8",
    font_family="Inter",
)

# ── Data Loading (Zero pandas / Zero numpy) ───────────────────────────────────
@st.cache_data
def load_data():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "combustion_data.csv")
    if not os.path.exists(path):
        return None
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for col in ["Oxygen_Concentration", "Flame_Spread_Rate", "Min_Ignition_O2",
                        "Toxicity_Index", "Year"]:
                try:    row[col] = float(row[col])
                except: row[col] = 0.0
            spread = min(row["Flame_Spread_Rate"], 20)
            o2     = min(max(row["Min_Ignition_O2"], 10), 30)
            row["Risk_Score"] = round(spread/20*40 + (1-o2/30)*35 + row["Toxicity_Index"]/10*25, 1)
            rows.append(row)
    return rows

all_rows = load_data()

# ── Sidebar Command Console ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;margin-bottom:8px;">
        <span style="font-family:'Orbitron',sans-serif;font-size:0.82rem;font-weight:900;letter-spacing:0.1em;color:#00d2ff;text-transform:uppercase;">
            🛸 3D Mission Companion
        </span>
    </div>
    """, unsafe_allow_html=True)

    companion = st.selectbox(
        "Choose Copilot",
        ["🤖 NOVA Bot (Safety AI)", "🧑‍🚀 Commander Leo (Astronaut)", "🛸 Navigator Zog (Alien Observer)"],
        label_visibility="collapsed"
    )

    if "NOVA" in companion:
        robot_b64 = get_base64_image("cute_3d_robot.jpg")
        if robot_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <div class="floating-robot">
                    <img src="{robot_b64}" style="width:160px;height:auto;border-radius:24px;border:2.5px solid #00e5ff;box-shadow:0 0 28px rgba(0,229,255,0.7), 0 8px 30px rgba(0,0,0,0.8);background:#050a18;">
                    <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                        <span class="cute-badge">✨ NOVA AI</span>
                        <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#00f5a0;font-weight:700;">● PATROL 0-G</span>
                    </div>
                </div>
                <div class="cute-speech-bubble">
                    Beep boop! 🤖 I'm <b>NOVA</b>! In microgravity, fire burns as calm, silent blue spheres! ✨
                </div>
            </div>
            """)
    elif "Leo" in companion:
        astro_b64 = get_base64_image("cute_astronaut_3d.jpg")
        if astro_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <div class="floating-astronaut">
                    <img src="{astro_b64}" style="width:160px;height:auto;border-radius:24px;border:2.5px solid #ffaa00;box-shadow:0 0 28px rgba(255,170,0,0.6), 0 8px 30px rgba(0,0,0,0.8);background:#050a18;">
                    <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                        <span class="cute-badge" style="background:linear-gradient(90deg, #ff8c00, #ffd000);">🧑‍🚀 CREW LEADER</span>
                        <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#ffd000;font-weight:700;">● ZERO-G EVA</span>
                    </div>
                </div>
                <div class="cute-speech-bubble" style="border-color:rgba(255,170,0,0.65);">
                    Greetings! 🧑‍🚀 Without gravity, hot air doesn't rise—flames need ventilation airflow to spread! 🚀✨
                </div>
            </div>
            """)
    else:
        ufo_b64 = get_base64_image("cute_ufo_3d.jpg")
        if ufo_b64:
            render_html(f"""
            <div style="text-align:center;padding:4px 0 2px 0;">
                <div class="floating-ufo">
                    <img src="{ufo_b64}" style="width:160px;height:auto;border-radius:24px;border:2.5px solid #00f5a0;box-shadow:0 0 28px rgba(0,245,160,0.6), 0 8px 30px rgba(0,0,0,0.8);background:#050a18;">
                    <div style="margin-top:8px;display:flex;justify-content:center;align-items:center;gap:6px;">
                        <span class="cute-badge" style="background:linear-gradient(90deg, #00f5a0, #00d2ff);">🛸 ALIEN OBSERVER</span>
                        <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#00f5a0;font-weight:700;">● GRAVITY SCAN</span>
                    </div>
                </div>
                <div class="cute-speech-bubble" style="border-color:rgba(0,245,160,0.65);">
                    Zorp! 🛸 Moon (0.16g) and Mars (0.38g) gravity change how fire spreads! Test it in Tab 3! 🪐
                </div>
            </div>
            """)

    st.markdown("#### 🎛️ Mission Telemetry Filters")
    keyword = st.text_input("🔎 Search Investigations", placeholder="FLEX, Saffire, cool flame, O2...")

    if all_rows:
        all_fuels = sorted({r["Fuel_Type"] for r in all_rows if r.get("Fuel_Type")})
        all_gravs = sorted({r["Gravity_Environment"] for r in all_rows if r.get("Gravity_Environment")})
        sel_fuel  = st.multiselect("🧪 Fuel Chemistry", all_fuels, default=all_fuels)
        sel_grav  = st.multiselect("🌌 Gravity Regime", all_gravs, default=all_gravs)
        sel_risk  = st.multiselect("🚨 Hazard Severity", ["High", "Medium", "Low"], default=["High", "Medium", "Low"])
    else:
        sel_fuel = sel_grav = sel_risk = []

    st.markdown("---")

    # 3D Saturn Planetary Habitat Card in Sidebar
    saturn_b64 = get_base64_image("cute_saturn_3d.jpg")
    if saturn_b64:
        render_html(f"""
        <div style="text-align:center;margin-top:2px;" class="floating-saturn">
            <div style="background:linear-gradient(135deg, rgba(20,28,52,0.85), rgba(10,14,28,0.95));border:1.5px solid rgba(255,208,0,0.4);border-radius:14px;padding:8px;box-shadow:0 8px 24px rgba(0,0,0,0.5), 0 0 16px rgba(255,208,0,0.18);">
                <img src="{saturn_b64}" style="width:100%;border-radius:10px;display:block;">
                <div style="font-family:'Orbitron',sans-serif;font-size:0.72rem;font-weight:800;color:#ffd000;margin-top:6px;">
                    🪐 DEEP SPACE MISSIONS
                </div>
                <div style="font-size:0.67rem;color:#a6b9dc;margin-top:2px;">
                    Moon • Mars • Deep Exploration
                </div>
            </div>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 📡 NASA Archives")
    st.markdown("• [🛰️ NASA PSI Database](https://psi.nasa.gov/physci/repo/search?q=combustion)")
    st.markdown("• [🔬 Glenn Fire Science](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/)")
    st.markdown("• [📖 ISS Research Guide](https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/)")

    st.markdown("---")
    st.caption("⚡ NASA Space Apps Challenge 2026 // Team Solo")

if all_rows is None:
    st.error("❌ `combustion_data.csv` is missing. Please make sure it is in your project directory.")
    st.stop()

# ── Filter Execution ─────────────────────────────────────────────────────────
def apply_filters(rows):
    out = []
    kw = keyword.strip().lower()
    for r in rows:
        if r["Fuel_Type"] not in sel_fuel: continue
        if r["Gravity_Environment"] not in sel_grav: continue
        if r["Fire_Risk_Level"] not in sel_risk: continue
        if kw:
            haystack = (r["Experiment_Name"] + r["Key_Findings"] + r["Fuel_Type"] + r["Mission"]).lower()
            if kw not in haystack: continue
        out.append(r)
    return out

rows = apply_filters(all_rows)

# ── Live Telemetry Status Ticker ─────────────────────────────────────────────
st.markdown("""
<div class="telemetry-ticker">
    <div class="ticker-left">
        <span class="ticker-badge"><span class="pulse-dot"></span> LIVE TELEMETRY</span>
        <span>NASA PSI COMBUSTION ARCHIVE // EXPEDITION 71 ECLSS SYNCED</span>
    </div>
    <div style="font-size:0.75rem;color:#00d2ff;">
        CABIN: 21.0% O₂ | 101.3 kPa | 0.00g µG | PROTOCOL: NASA-STD-6001
    </div>
</div>
""", unsafe_allow_html=True)

# ── Hero Mission Command Header with 3D ISS Station Render ────────────────────
col_hero_text, col_hero_3d = st.columns([3.1, 1.3])
with col_hero_text:
    render_html("""
    <div class="hero-box" style="margin-bottom:0px;height:100%;">
        <div class="hero-title">🔥 FLAME IN FREEFALL</div>
        <div class="hero-sub">
            NASA Microgravity Combustion &amp; Spacecraft Fire Safety Dashboard for ISS, Moon &amp; Mars.
        </div>
        <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;">
            <span class="ticker-badge"><span class="pulse-dot"></span> ACTIVE</span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#00d2ff;background:rgba(0,210,255,0.08);border:1px solid rgba(0,210,255,0.25);padding:3px 10px;border-radius:6px;">
                🛰️ 25 EXPERIMENTS
            </span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#ffd000;background:rgba(255,208,0,0.08);border:1px solid rgba(255,208,0,0.25);padding:3px 10px;border-radius:6px;">
                🌙 ARTEMIS &amp; MARS READY
            </span>
        </div>
    </div>
    """)
with col_hero_3d:
    iss_b64 = get_base64_image("3d_iss.jpg")
    if iss_b64:
        render_html(f"""
        <div class="floating-hero-card">
            <div class="hero-3d-box">
                <img src="{iss_b64}" class="hero-3d-img" alt="ISS Orbital Fire Lab">
                <span class="hero-3d-title">🛸 ISS CIR FIRE LAB</span>
                <span class="hero-3d-sub">Expedition 71 • Combustion Integrated Rack</span>
            </div>
        </div>
        """)
    else:
        st.caption("🛸 ISS Orbital Module")

st.markdown("<br>", unsafe_allow_html=True)

# ── Main Tab Navigation ───────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛰️ Telemetry Explorer",
    "🤖 AI Safety Interpreter",
    "🎛️ Morphing Flame Simulator",
    "📊 3D Hazard Landscape & Ranking",
    "⚖️ Head-to-Head & Historical Lessons",
])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 — TELEMETRY EXPLORER
# ═══════════════════════════════════════════════════════════════════════════════
with tab1:
    astro_b64 = get_base64_image("cute_astronaut_3d.jpg")
    if astro_b64:
        render_html(f"""
        <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(135deg, rgba(14,24,50,0.75), rgba(8,14,30,0.9));border:1px solid rgba(0,210,255,0.3);border-radius:14px;padding:10px 18px;margin-bottom:18px;box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div class="floating-astronaut" style="flex-shrink:0;">
                <img src="{astro_b64}" style="width:52px;height:52px;border-radius:50%;border:2px solid #ffaa00;box-shadow:0 0 14px rgba(255,170,0,0.6);object-fit:cover;">
            </div>
            <div style="flex-grow:1;">
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="font-family:'Orbitron',sans-serif;font-size:0.78rem;font-weight:800;color:#ffd000;letter-spacing:0.05em;">🧑‍🚀 COMMANDER LEO's FLIGHT LOG</span>
                    <span class="cute-badge" style="background:linear-gradient(90deg, #ff8c00, #ffd000);font-size:0.65rem;padding:2px 8px;">ORBITAL DISPATCH</span>
                </div>
                <div style="font-size:0.86rem;color:#d1dbf4;margin-top:2px;line-height:1.4;">
                    "Without gravity, hot air never rises—flames burn as calm, spherical blue domes! Use the filters to explore." ✨
                </div>
            </div>
        </div>
        """)

    high_n  = sum(1 for r in rows if r["Fire_Risk_Level"] == "High")
    spreads = [min(r["Flame_Spread_Rate"], 20) for r in rows]
    avg_sp  = safe_mean(spreads)
    avg_o2  = safe_mean([r["Min_Ignition_O2"] for r in rows])

    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="hud-card"><div class="hud-val">{len(rows)}</div><div class="hud-lbl">Total Experiments</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="hud-card" style="border-top-color:#ff4d4d;"><div class="hud-val" style="color:#ff6b6b;">{high_n}</div><div class="hud-lbl">High Fire Risk</div></div>', unsafe_allow_html=True)
    k3.markdown(f'<div class="hud-card" style="border-top-color:#ffa500;"><div class="hud-val" style="color:#ffc266;">{avg_sp}</div><div class="hud-lbl">Avg Spread (mm/s)</div></div>', unsafe_allow_html=True)
    k4.markdown(f'<div class="hud-card" style="border-top-color:#00d2ff;"><div class="hud-val" style="color:#5ce1ff;">{avg_o2}%</div><div class="hud-lbl">Min Ignition O₂</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # View Toggle: Matrix vs Interactive Holographic Cards
    view_mode = st.radio("Display Mode:", ["📊 Structured Matrix", "🃏 Holographic Investigation Cards"], horizontal=True)

    if view_mode == "📊 Structured Matrix":
        tbl = [{
            "Experiment": r["Experiment_Name"],
            "Fuel": r["Fuel_Type"],
            "Regime": r["Gravity_Environment"],
            "Severity": r["Fire_Risk_Level"],
            "Risk Score": r["Risk_Score"],
            "Spread mm/s": r["Flame_Spread_Rate"],
            "Min O₂ %": r["Min_Ignition_O2"],
            "Tox": r["Toxicity_Index"],
            "Mission / Year": f"{r['Mission']} ({int(r['Year'])})",
        } for r in rows]
        st.markdown(html_table(tbl, max_height=420), unsafe_allow_html=True)
    else:
        # Card Grid
        cards_html = []
        for r in rows:
            col_bar = RISK_COLOR.get(r["Fire_Risk_Level"], "#888")
            badge = risk_badge(r["Fire_Risk_Level"])
            cards_html.append(textwrap.dedent(f"""
            <div class="exp-card" style="border-left: 4px solid {col_bar};">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
                    <div style="font-family:'Orbitron',sans-serif;font-size:0.95rem;font-weight:700;color:#ffffff;">{r['Experiment_Name']}</div>
                    <div>{badge}</div>
                </div>
                <div style="font-size:0.8rem;color:#8da4d0;margin-bottom:8px;">
                    🛰️ <b>{r['Mission']}</b> | 🌌 {r['Gravity_Environment']}
                </div>
                <div style="font-size:0.84rem;color:#c9d7f5;line-height:1.45;margin-bottom:10px;">
                    {r['AI_Summary'][:140]}…
                </div>
                <div style="display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#00d2ff;border-top:1px solid #1a2744;padding-top:6px;">
                    <span>SPREAD: {r['Flame_Spread_Rate']} mm/s</span>
                    <span>MIN O₂: {r['Min_Ignition_O2']}%</span>
                    <span>SCORE: {r['Risk_Score']}</span>
                </div>
            </div>
            """).strip())
        render_html(f'<div class="exp-grid">{"".join(cards_html)}</div>')

    st.markdown("<br>", unsafe_allow_html=True)
    c_left, c_right = st.columns(2)

    # Donut Chart
    with c_left:
        risk_counts = {}
        for r in rows:
            risk_counts[r["Fire_Risk_Level"]] = risk_counts.get(r["Fire_Risk_Level"], 0) + 1
        fig_donut = go.Figure(go.Pie(
            labels=list(risk_counts.keys()),
            values=list(risk_counts.values()),
            hole=0.6,
            marker=dict(colors=[RISK_COLOR.get(k, "#888") for k in risk_counts], line=dict(color="#090e1d", width=2)),
            textinfo="label+percent",
            hoverinfo="label+value+percent",
        ))
        fig_donut.update_layout(
            title=dict(text="Hazard Severity Breakdown", font=dict(family="Orbitron", size=14)),
            height=340,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    # Sunburst Hierarchy
    with c_right:
        sb_labels, sb_parents, sb_values, sb_colors = [], [], [], []
        grav_risk: dict = {}
        for r in rows:
            g, rl, fu = r["Gravity_Environment"], r["Fire_Risk_Level"], r["Fuel_Type"]
            grav_risk.setdefault(g, {}).setdefault(rl, {}).setdefault(fu, 0)
            grav_risk[g][rl][fu] += 1

        for g, risks in grav_risk.items():
            if g not in sb_labels:
                sb_labels.append(g); sb_parents.append(""); sb_values.append(sum(sum(f.values()) for f in risks.values())); sb_colors.append("#19325c")
            for rl, fuels in risks.items():
                key = f"{g} — {rl}"
                if key not in sb_labels:
                    sb_labels.append(key); sb_parents.append(g); sb_values.append(sum(fuels.values())); sb_colors.append(RISK_COLOR.get(rl, "#888"))
                for fu, cnt in fuels.items():
                    leaf = f"{fu} ({rl})"
                    rgba_dim = {"High": "rgba(255, 77, 77, 0.45)", "Medium": "rgba(255, 165, 0, 0.45)", "Low": "rgba(0, 245, 160, 0.45)"}
                    sb_labels.append(leaf); sb_parents.append(key); sb_values.append(cnt); sb_colors.append(rgba_dim.get(rl, "rgba(136, 136, 136, 0.45)"))

        fig_sun = go.Figure(go.Sunburst(
            labels=sb_labels, parents=sb_parents, values=sb_values,
            marker=dict(colors=sb_colors),
            hovertemplate="<b>%{label}</b><br>Count: %{value}<extra></extra>",
            maxdepth=3,
        ))
        fig_sun.update_layout(
            title=dict(text="Gravity Regime → Hazard → Fuel Hierarchy", font=dict(family="Orbitron", size=14)),
            height=340, **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_sun, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 — AI SAFETY INTERPRETER
# ═══════════════════════════════════════════════════════════════════════════════
with tab2:
    if not rows:
        st.warning("No investigations match the current filter envelope.")
    else:
        names = [r["Experiment_Name"] for r in rows]
        sel_exp = st.selectbox("Select NASA Investigation:", names)
        row = next(r for r in rows if r["Experiment_Name"] == sel_exp)

        # Header Info Row
        tl, tr = st.columns([3, 1])
        tl.markdown(f"### {row['Experiment_Name']}")
        tl.caption(f"🛰️ **{row['Mission']}** | 📅 {int(row['Year'])} | 🌌 {row['Gravity_Environment']} | 🧪 {row['Fuel_Type']}")
        tr.markdown(f"<div style='text-align:right;padding-top:10px'>{risk_badge(row['Fire_Risk_Level'])}</div>", unsafe_allow_html=True)

        if row.get("Historical_Incident", "").strip().lower() == "yes":
            st.error("⚠️ HISTORICAL EMERGENCY: Investigation of an in-flight catastrophic accident.")

        st.markdown("<br>", unsafe_allow_html=True)
        col_brief, col_gauge = st.columns([2, 1])

        with col_brief:
            c_nova, c_ai_text = st.columns([0.7, 3.3])
            with c_nova:
                if robot_b64:
                    render_html(f"""
                    <div style="text-align:center;padding-top:6px;" class="floating-robot">
                        <img src="{robot_b64}" style="width:100%;max-width:110px;border-radius:18px;border:2px solid #00e5ff;box-shadow:0 0 22px rgba(0,229,255,0.6);background:#050a18;">
                        <div style="font-family:'Orbitron',sans-serif;font-size:0.75rem;color:#00e5ff;font-weight:900;margin-top:6px;">NOVA</div>
                        <span class="cute-badge" style="font-size:0.62rem;padding:2px 6px;">AI COPILOT</span>
                    </div>
                    """)
            with c_ai_text:
                render_html(f"""
                <div class="ai-panel">
                    <div style="font-family:'JetBrains Mono',monospace;color:#00d2ff;font-size:0.8rem;margin-bottom:6px;display:flex;align-items:center;gap:6px;">
                        <span>🤖</span> NOVA's EXECUTIVE SUMMARY
                    </div>
                    <div style="font-size:1.02rem;line-height:1.6;color:#f0f4ff;">
                        {row['AI_Summary']}
                    </div>
                </div>
                """)

            render_html(f"""
            <div class="safety-panel">
                <div style="font-family:'JetBrains Mono',monospace;color:#ff8c42;font-size:0.8rem;margin-bottom:6px;display:flex;align-items:center;gap:6px;">
                    <span>🚨</span> CREW SAFETY PROTOCOL
                </div>
                <div style="font-size:1.01rem;line-height:1.6;color:#ffe8e0;">
                    {row['Safety_Recommendations']}
                </div>
            </div>
            """)

            with st.expander("🔬 View Primary Empirical Telemetry"):
                st.markdown(f"**Findings:** {row['Key_Findings']}")
                st.markdown(f"**Environment:** `{row['Gravity_Environment']}` | **Fuel:** `{row['Fuel_Type']}`")

            # Quick Metric Chips
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("O₂ Level", f"{row['Oxygen_Concentration']}%")
            m2.metric("Spread Rate", f"{row['Flame_Spread_Rate']} mm/s")
            m3.metric("Min O₂ Limit", f"{row['Min_Ignition_O2']}%")
            m4.metric("Toxicity", f"{row['Toxicity_Index']} / 10")

        with col_gauge:
            score = row["Risk_Score"]
            fig_g = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                number={"font": {"family": "Orbitron", "color": "#ffffff", "size": 38}},
                title={"text": "FIRE RISK SCORE", "font": {"family": "JetBrains Mono", "size": 13, "color": "#8da4d0"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#8da4d0", "tickwidth": 1},
                    "bar": {"color": RISK_COLOR.get(row["Fire_Risk_Level"], "#ff6b35"), "thickness": 0.28},
                    "bgcolor": "rgba(16, 24, 46, 0.7)",
                    "borderwidth": 1,
                    "bordercolor": "#233458",
                    "steps": [
                        {"range": [0, 35], "color": "rgba(0, 245, 160, 0.12)"},
                        {"range": [35, 65], "color": "rgba(255, 165, 0, 0.12)"},
                        {"range": [65, 100], "color": "rgba(255, 77, 77, 0.15)"},
                    ],
                }
            ))
            fig_g.update_layout(**PLOTLY_LAYOUT, height=300, margin=dict(t=40, b=10, l=20, r=20))
            st.plotly_chart(fig_g, use_container_width=True)

            # Astronaut Quick Checklist Generator
            if st.button("📋 Generate Emergency Flight Checklist", use_container_width=True):
                st.success(f"""
                **EMERGENCY CHECKLIST // {row['Experiment_Name'].split()[0].upper()} PROTOCOL**
                1. 🛑 Throttle cabin airflow fans (< 2 cm/s).
                2. 🤿 Don emergency breathing masks immediately.
                3. 🔍 Scan for invisible cool flames using UV/IR sensors.
                4. 🧯 Trigger automated CO₂/N₂ inert gas rack purge.
                """)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 — MORPHING FLAME SIMULATOR (SHOWSTOPPER VISUAL FEATURE)
# ═══════════════════════════════════════════════════════════════════════════════
with tab3:
    ufo_b64 = get_base64_image("cute_ufo_3d.jpg")
    if ufo_b64:
        render_html(f"""
        <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(135deg, rgba(12,26,44,0.75), rgba(6,16,28,0.9));border:1px solid rgba(0,245,160,0.3);border-radius:14px;padding:10px 18px;margin-bottom:18px;box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div class="floating-ufo" style="flex-shrink:0;">
                <img src="{ufo_b64}" style="width:52px;height:52px;border-radius:50%;border:2px solid #00f5a0;box-shadow:0 0 14px rgba(0,245,160,0.6);object-fit:cover;">
            </div>
            <div style="flex-grow:1;">
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="font-family:'Orbitron',sans-serif;font-size:0.78rem;font-weight:800;color:#00f5a0;letter-spacing:0.05em;">🛸 NAVIGATOR ZOG's GRAVITY SCAN</span>
                    <span class="cute-badge" style="background:linear-gradient(90deg, #00f5a0, #00d2ff);font-size:0.65rem;padding:2px 8px;">PHYSICS LAB</span>
                </div>
                <div style="font-size:0.86rem;color:#d1dbf4;margin-top:2px;line-height:1.4;">
                    "Adjust the sliders below to watch the flame change shape, color, and danger level in real time!" 🌌
                </div>
            </div>
        </div>
        """)

    st.markdown("### 🎛️ Interactive Spacecraft Flame Physics Chamber")

    s1, s2, s3 = st.columns(3)
    sim_o2   = s1.slider("Cabin Oxygen Concentration (%)", 14.0, 36.0, 21.0, 0.5)
    sim_flow = s2.slider("Ventilation Airflow Velocity (cm/s)", 0.0, 30.0, 10.0, 1.0)
    sim_grav = s3.selectbox("Gravity Environment Regime", [
        "0.00g — ISS Microgravity (Freefall)",
        "0.16g — Lunar Habitat Surface",
        "0.38g — Martian Habitat Surface",
        "1.00g — Earth Sea Level Reference",
    ])

    # Empirical Physics Calculations
    grav_mult = {
        "0.00g — ISS Microgravity (Freefall)": 1.15,
        "0.16g — Lunar Habitat Surface": 1.25,
        "0.38g — Martian Habitat Surface": 1.10,
        "1.00g — Earth Sea Level Reference": 1.00
    }[sim_grav]

    if sim_flow < 2:
        flow_mult = 0.72   # Quiescent starves flames (BASS-II finding)
        airflow_note = "QUIESCENT (Self-Extinction Window)"
    elif 4 <= sim_flow <= 18:
        flow_mult = 1.28   # Ideal oxygen replenishment (BRE & Saffire-I finding)
        airflow_note = "CRITICAL (Optimal Flame Convection Flow)"
    else:
        flow_mult = 1.08   # Flame stretching & partial liftoff
        airflow_note = "HIGH FLOW (Flame Stretch & Blowout Risk)"

    sim_score = min(100.0, round(((sim_o2 - 12) / 24 * 65 * grav_mult * flow_mult) + 15, 1))
    sim_status = "CRITICAL HAZARD" if sim_score >= 65 else ("ELEVATED RISK" if sim_score >= 38 else "NOMINAL ENVELOPE")
    sim_color = "#ff4d4d" if sim_score >= 65 else ("#ffa500" if sim_score >= 38 else "#00f5a0")

    is_microg = "0.00g" in sim_grav
    is_lunar  = "0.16g" in sim_grav
    is_mars   = "0.38g" in sim_grav

    # Tilt angle from airflow
    tilt_deg = min(sim_flow * 1.8, 38)
    
    # Flame colors based on O2 and gravity
    if sim_o2 < 16.5:
        core_c1 = "#00d2ff"
        core_c2 = "#1e3cff"
        halo_c  = "rgba(0, 210, 255, 0.35)"
        regime_title = "BLUE-VIOLET COOL FLAME (Sub-Visible, Low-Temp Oxidation)"
    elif sim_o2 > 24.0:
        core_c1 = "#ffffff"
        core_c2 = "#ffb700"
        halo_c  = "rgba(255, 65, 0, 0.6)"
        regime_title = "INCANDESCENT WHITE-HOT FLAME (Severe Soot & Toxic Radical Output)"
    else:
        core_c1 = "#ffe875" if not is_microg else "#7be0ff"
        core_c2 = "#ff5500" if not is_microg else "#0077ff"
        halo_c  = "rgba(255, 107, 53, 0.45)"
        regime_title = "SPHERICAL DIFFUSION DOME" if is_microg else "BUOYANCY-DRIVEN CONVECTIVE PLUME"

    # SVG Flame Shape definition
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
                padding: 16px; box-shadow: 0 0 35px rgba(0,0,0,0.8), inset 0 0 40px rgba(0,210,255,0.06);
                text-align: center; position: relative;">
        <div style="display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#00d2ff;margin-bottom:8px;border-bottom:1px solid #1a2a4c;padding-bottom:6px;">
            <span>CHAMBER ID: NASA-PSI-SIM-01</span>
            <span>REGIME: {regime_title}</span>
            <span>AIRFLOW: {airflow_note}</span>
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
            <span>BUOYANCY VECTOR: {"0.00 m/s² (QUIESCENT)" if is_microg else ("1.62 m/s²" if is_lunar else ("3.72 m/s²" if is_mars else "9.81 m/s²"))}</span>
            <span>TILT ANGLE: {tilt_deg:.1f}°</span>
            <span>IGNITION PROBABILITY: {sim_score}%</span>
        </div>
    </div>
    """
    chamber_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
body {{ margin: 0; padding: 0; background: transparent; overflow: hidden; }}
</style>
</head>
<body>
{flame_chamber_html}
</body>
</html>"""
    components.html(chamber_doc, height=280)
    st.markdown("<br>", unsafe_allow_html=True)

    # Telemetry Output & AI Advisories
    r_card, r_adv = st.columns([1, 2])
    with r_card:
        render_html(f"""
        <div class="hud-card" style="border-top-color:{sim_color};padding:24px;">
            <div class="hud-lbl">PREDICTED FIRE RISK SCORE</div>
            <div class="hud-val" style="color:{sim_color};font-size:3.1rem;margin:8px 0;">{sim_score}</div>
            <div style="font-family:'JetBrains Mono',monospace;color:{sim_color};font-weight:700;letter-spacing:0.08em;">
                ● {sim_status}
            </div>
        </div>
        """)

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sim_score,
            number={"font": {"family": "Orbitron", "color": sim_color}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#8da4d0"},
                "bar": {"color": sim_color},
                "bgcolor": "rgba(16, 24, 46, 0.7)",
                "steps": [
                    {"range": [0, 38], "color": "rgba(0, 245, 160, 0.12)"},
                    {"range": [38, 65], "color": "rgba(255, 165, 0, 0.12)"},
                    {"range": [65, 100], "color": "rgba(255, 77, 77, 0.15)"},
                ],
            }
        ))
        fig_gauge.update_layout(**PLOTLY_LAYOUT, height=220, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

        # NOVA Cute Reactive Mood
        cute_reaction = (
            "🚨 'Eeeek! High fire danger! Throttle ventilation fans & prepare CO₂ extinguishers!'"
            if sim_score >= 65 else (
                "🧐 'Caution, astronaut! Convective airflow is feeding the flame front!'"
                if sim_score >= 38 else
                "🥳 'Yay! Nominal cabin atmosphere! Flame stays small and self-extinguishes!'"
            )
        )
        if robot_b64:
            render_html(f"""
            <div style="display:flex;align-items:center;gap:12px;background:rgba(0,229,255,0.08);border:1px solid rgba(0,229,255,0.35);border-radius:14px;padding:10px 14px;margin-top:8px;">
                <div class="floating-robot">
                    <img src="{robot_b64}" style="width:52px;height:auto;border-radius:50%;border:1.5px solid #00e5ff;box-shadow:0 0 14px rgba(0,229,255,0.5);">
                </div>
                <div style="font-size:0.8rem;color:#e2f1ff;line-height:1.4;">
                    <div style="font-family:'JetBrains Mono',monospace;color:#00e5ff;font-size:0.7rem;font-weight:700;">✨ NOVA'S LIVE REACTION:</div>
                    {cute_reaction}
                </div>
            </div>
            """)

    with r_adv:
        st.markdown("#### 🧠 Real-Time Safety Advisories")
        advisories = []
        if sim_o2 > 24.0:
            advisories.append(("🚨", "High Oxygen Hazard (>24%)",
                "Per Saffire-VI: Ignition energy drops >60%. Materials release dangerous toxic CO and cyanide gases."))
        if sim_o2 < 17.0:
            advisories.append(("ℹ️", "Hypoxic Low-Oxygen (<17%)",
                "Flames self-extinguish easily, but crew cognitive alertness drops."))
        if 4 <= sim_flow <= 18 and "0.00g" in sim_grav:
            advisories.append(("⚠️", "Forced Airflow Hazard (5–18 cm/s)",
                "Per Saffire-I & BRE: Cabin airflow feeds fresh oxygen—flame spread rate doubles!"))
        if sim_flow < 2 and "0.00g" in sim_grav:
            advisories.append(("✅", "Still Air Zone (<2 cm/s)",
                "Per BASS-II: Without airflow, trapped smoke chokes the flame into self-extinguishment."))
        if "Lunar" in sim_grav:
            advisories.append(("🌑", "Lunar Gravity (0.16g)",
                "Per SoFIE: Weak buoyancy spreads flame along structural plastics faster than in 0-g."))
        if "Martian" in sim_grav:
            advisories.append(("🔴", "Martian Gravity (0.38g)",
                "Per FLARE: Melting polymer droplets drip down wire bundles and spread fire across walls."))
        if not advisories:
            advisories.append(("✅", "Nominal Atmosphere",
                "Standard ISS fire safety envelope. Keep automated smoke and gas sensors active."))

        for icon, title, body in advisories:
            lvl = "error" if icon == "🚨" else ("warning" if icon in ("⚠️", "🔴") else "info")
            getattr(st, lvl)(f"**{icon} {title}** — {body}")

        if rows:
            nearest = min(rows, key=lambda r: abs(r["Risk_Score"] - sim_score))
            st.caption(f"🔍 **Closest NASA Study:** `{nearest['Experiment_Name']}` (Score: {nearest['Risk_Score']})")

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 — 3D HAZARD LANDSCAPE & RANKING
# ═══════════════════════════════════════════════════════════════════════════════
with tab4:
    saturn_b64 = get_base64_image("cute_saturn_3d.jpg")
    if saturn_b64:
        render_html(f"""
        <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(135deg, rgba(22,26,48,0.75), rgba(10,14,28,0.9));border:1px solid rgba(255,208,0,0.3);border-radius:14px;padding:10px 18px;margin-bottom:18px;box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div class="floating-saturn" style="flex-shrink:0;">
                <img src="{saturn_b64}" style="width:52px;height:52px;border-radius:50%;border:2px solid #ffd000;box-shadow:0 0 14px rgba(255,208,0,0.5);object-fit:cover;">
            </div>
            <div style="flex-grow:1;">
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="font-family:'Orbitron',sans-serif;font-size:0.78rem;font-weight:800;color:#ffd000;letter-spacing:0.05em;">🪐 DEEP SPACE HAZARD TOPOLOGY</span>
                    <span class="cute-badge" style="background:linear-gradient(90deg, #ff8c00, #ffd000);font-size:0.65rem;padding:2px 8px;">3D MULTIVARIATE</span>
                </div>
                <div style="font-size:0.86rem;color:#d1dbf4;margin-top:2px;line-height:1.4;">
                    "Rotate the 3D scatter plot to see how Oxygen, Spread Rate, and Toxicity interact across NASA studies!" ✨
                </div>
            </div>
        </div>
        """)

    ranked = sorted(rows, key=lambda r: r["Risk_Score"], reverse=True)

    r_l, r_r = st.columns([1.1, 1])
    with r_l:
        st.markdown("#### 🏆 Spacecraft Fire Risk Ranking")
        st.caption("Score = 40% Flame Spread + 35% Ignition O₂ + 25% Toxicity")

        fig_bar = go.Figure(go.Bar(
            x=[r["Risk_Score"] for r in ranked],
            y=[r["Experiment_Name"] for r in ranked],
            orientation="h",
            marker=dict(
                color=[RISK_COLOR.get(r["Fire_Risk_Level"], "#888") for r in ranked],
                line=dict(color="rgba(255,255,255,0.2)", width=1)
            ),
            text=[f"{r['Risk_Score']}" for r in ranked],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Hazard Score: %{x}<br>Fuel: %{customdata[0]}<extra></extra>",
            customdata=[[r["Fuel_Type"]] for r in ranked],
        ))
        fig_bar.update_layout(
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Composite Hazard Score (0–100)",
            height=540,
            showlegend=False,
            margin=dict(l=10, r=30, t=10, b=30),
            **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with r_r:
        st.markdown("#### 🌌 3D Multi-Dimensional Fire Hazard Landscape")
        st.caption("Drag to rotate in 3D: Min O₂ (%) vs. Flame Spread (mm/s) vs. Toxicity Index")

        fig_3d = go.Figure()
        for rl in ["High", "Medium", "Low"]:
            sub = [r for r in rows if r["Fire_Risk_Level"] == rl]
            if not sub: continue
            fig_3d.add_trace(go.Scatter3d(
                x=[r["Min_Ignition_O2"] for r in sub],
                y=[min(r["Flame_Spread_Rate"], 20) for r in sub],
                z=[r["Toxicity_Index"] for r in sub],
                mode="markers+text",
                name=f"{rl} Risk",
                marker=dict(
                    size=[r["Risk_Score"]/5 + 4 for r in sub],
                    color=RISK_COLOR[rl],
                    opacity=0.88,
                    line=dict(width=1, color="rgba(255, 255, 255, 0.45)"),
                ),
                text=[r["Experiment_Name"].split()[0] for r in sub],
                textposition="top center",
                hovertemplate="<b>%{customdata[0]}</b><br>Min O₂: %{x}%<br>Spread: %{y} mm/s<br>Toxicity: %{z}/10<br>Score: %{customdata[1]}<extra></extra>",
                customdata=[[r["Experiment_Name"], r["Risk_Score"]] for r in sub],
            ))

        fig_3d.update_layout(
            scene=dict(
                xaxis=dict(title="Min O₂ (%)", backgroundcolor="rgba(10, 16, 32, 0.8)", gridcolor="#1e2c4f", zerolinecolor="#1e2c4f"),
                yaxis=dict(title="Spread (mm/s)", backgroundcolor="rgba(10, 16, 32, 0.8)", gridcolor="#1e2c4f", zerolinecolor="#1e2c4f"),
                zaxis=dict(title="Toxicity (0-10)", backgroundcolor="rgba(10, 16, 32, 0.8)", gridcolor="#1e2c4f", zerolinecolor="#1e2c4f"),
                bgcolor="rgba(6, 9, 20, 0.95)",
            ),
            height=540,
            margin=dict(l=0, r=0, b=0, t=10),
            legend=dict(orientation="h", yanchor="bottom", y=0.02, xanchor="center", x=0.5),
            **PLOTLY_LAYOUT
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    st.markdown("---")
    st.markdown("#### 📋 Full NASA Hazard Ranking Telemetry Sheet")
    rank_tbl = [{
        "Rank": f"#{i+1}",
        "Experiment": r["Experiment_Name"],
        "Severity": r["Fire_Risk_Level"],
        "Composite Hazard Score": r["Risk_Score"],
        "Spread mm/s": r["Flame_Spread_Rate"],
        "Min O₂ %": r["Min_Ignition_O2"],
        "Tox Index": r["Toxicity_Index"],
        "Gravity Environment": r["Gravity_Environment"],
        "Mission": r["Mission"],
    } for i, r in enumerate(ranked)]
    st.markdown(html_table(rank_tbl, max_height=380), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 — HEAD-TO-HEAD & HISTORICAL DISASTERS
# ═══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("### ⚖️ Side-by-Side Investigation Comparison")
    st.caption("Select two NASA experiments to analyze head-to-head flammability differences.")

    exp_list = [r["Experiment_Name"] for r in rows]
    if len(exp_list) >= 2:
        c1, c2 = st.columns(2)
        exp_a = c1.selectbox("🔴 Target Investigation A", exp_list, index=0)
        exp_b = c2.selectbox("🔵 Target Investigation B", exp_list, index=min(1, len(exp_list)-1))

        if exp_a != exp_b:
            ra = next(r for r in rows if r["Experiment_Name"] == exp_a)
            rb = next(r for r in rows if r["Experiment_Name"] == exp_b)

            mc1, mc2, mc3 = st.columns([2, 1, 2])
            metrics = [
                ("Flame Spread Rate (mm/s)", "Flame_Spread_Rate", True, "{:.1f}"),
                ("Min Ignition O₂ (%)", "Min_Ignition_O2", False, "{:.1f}"),
                ("Toxicity Index (0-10)", "Toxicity_Index", True, "{:.0f}"),
                ("Composite Hazard Score", "Risk_Score", True, "{:.1f}"),
            ]
            with mc1:
                st.markdown(f"**{exp_a}**")
                st.markdown(risk_badge(ra["Fire_Risk_Level"]), unsafe_allow_html=True)
                st.caption(f"Mission: {ra['Mission']} ({int(ra['Year'])})")
                for lbl, fld, low_safe, fmt in metrics:
                    va, vb = ra[fld], rb[fld]
                    better = va < vb if low_safe else va > vb
                    st.markdown(f"• **{lbl}:** {'🟢' if better else '🔴'} {fmt.format(va)}")
            with mc2:
                st.markdown("<br><br>", unsafe_allow_html=True)
                for _ in metrics:
                    st.markdown("<div style='text-align:center;'>⚡ VS ⚡</div>", unsafe_allow_html=True)
            with mc3:
                st.markdown(f"**{exp_b}**")
                st.markdown(risk_badge(rb["Fire_Risk_Level"]), unsafe_allow_html=True)
                st.caption(f"Mission: {rb['Mission']} ({int(rb['Year'])})")
                for lbl, fld, low_safe, fmt in metrics:
                    va, vb = ra[fld], rb[fld]
                    better = vb < va if low_safe else vb > va
                    st.markdown(f"• **{lbl}:** {'🟢' if better else '🔴'} {fmt.format(vb)}")

            st.markdown("---")
            st.markdown("#### 🕸️ Radar Hazard Signature Profile")

            cats = ["Flame Spread", "Low-O₂ Ignition Propensity", "Toxicity", "Overall Composite Score"]
            def nv(val, lo, hi): return (val - lo) / (hi - lo) if hi != lo else 0.5
            va_v = [nv(min(ra["Flame_Spread_Rate"], 20), 0, 20),
                    1 - nv(min(max(ra["Min_Ignition_O2"], 10), 30), 10, 30),
                    nv(ra["Toxicity_Index"], 0, 10),
                    nv(ra["Risk_Score"], 0, 100)]
            vb_v = [nv(min(rb["Flame_Spread_Rate"], 20), 0, 20),
                    1 - nv(min(max(rb["Min_Ignition_O2"], 10), 30), 10, 30),
                    nv(rb["Toxicity_Index"], 0, 10),
                    nv(rb["Risk_Score"], 0, 100)]

            fig_rad = go.Figure()
            for label, vals, color in [(exp_a[:35], va_v, "#ff4d4d"), (exp_b[:35], vb_v, "#00d2ff")]:
                fig_rad.add_trace(go.Scatterpolar(
                    r=vals + [vals[0]],
                    theta=cats + [cats[0]],
                    name=label,
                    line=dict(color=color, width=2),
                    fill="toself",
                    fillcolor="rgba(255, 77, 77, 0.22)" if color == "#ff4d4d" else "rgba(0, 210, 255, 0.22)",
                ))
            fig_rad.update_layout(
                polar=dict(
                    bgcolor="rgba(14, 22, 42, 0.7)",
                    radialaxis=dict(visible=True, range=[0, 1], gridcolor="#233458", tickcolor="#8da4d0"),
                    angularaxis=dict(gridcolor="#233458", tickcolor="#8da4d0"),
                ),
                height=420,
                legend=dict(bgcolor="rgba(0,0,0,0)", orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
                title="Normalised Hazard Vector Comparison (1.0 = Maximum Hazard)",
                **PLOTLY_LAYOUT
            )
            st.plotly_chart(fig_rad, use_container_width=True)

            riskier, safer = (exp_a, exp_b) if ra["Risk_Score"] > rb["Risk_Score"] else (exp_b, exp_a)
            diff = abs(ra["Risk_Score"] - rb["Risk_Score"])
            st.info(f"⚠️ **Comparison:** **{riskier}** has a **{diff:.1f}-point higher fire risk** than **{safer}** due to faster flame spread and higher combustion toxicity.")
    else:
        st.warning("Please maintain at least two experiments in your filter selection for head-to-head comparison.")

    # ── Historical Space Disasters Section ───────────────────────────────────
    st.markdown("---")
    c_hist_title, c_hist_img = st.columns([3, 1.2])
    with c_hist_title:
        st.markdown("### 🏛️ Historical Space Fires & Modern NASA Solutions")
        st.caption("How real-life flight emergencies directly shaped modern microgravity fire research.")
    with c_hist_img:
        rocket_b64 = get_base64_image("3d_rocket.jpg")
        if rocket_b64:
            render_html(f"""
            <div style="background:linear-gradient(135deg, rgba(26,18,36,0.85), rgba(12,8,20,0.95));border:1.5px solid rgba(255,107,53,0.5);border-radius:14px;padding:8px;box-shadow:0 8px 24px rgba(0,0,0,0.6), 0 0 18px rgba(255,107,53,0.25);text-align:center;">
                <img src="{rocket_b64}" style="width:100%;border-radius:10px;display:block;">
                <div style="font-family:'Orbitron',sans-serif;font-size:0.72rem;font-weight:800;color:#ff8c42;margin-top:6px;">
                    🚀 APOLLO PROPULSION ARCHIVE
                </div>
                <div style="font-size:0.67rem;color:#a6b9dc;margin-top:2px;">
                    Supercritical O₂ &amp; Cryo Safety
                </div>
            </div>
            """)
        else:
            st.caption("🚀 Cryo Propulsion Archive")

    h1, h2, h3 = st.columns(3)
    incidents = [
        (h1, "#ff6b6b", "🚀 Apollo 1 (1967)",
         "100% pure O₂ cabin atmosphere caused an instantaneous electrical flashover within 17 seconds during a pre-launch test.",
         "Mandated mixed N₂/O₂ atmospheres and standardized materials flammability testing (NASA-STD-6001).",
         "https://sma.nasa.gov/sma-disciplines/accllp/apollo-1"),
        (h2, "#ffa500", "🌙 Apollo 13 (1970)",
         "Damaged Teflon wire insulation sparked inside supercritical oxygen tank #2, causing a catastrophic tank rupture.",
         "Redesigned oxygen tanks with zero internal wiring and added isolated backup life-support systems.",
         "https://sma.nasa.gov/sma-disciplines/accllp/apollo-13"),
        (h3, "#ffd166", "🛸 Mir Station Fire (1997)",
         "Solid perchlorate oxygen candle ignited unexpectedly, burning for 14 minutes and filling Mir with blinding toxic smoke.",
         "Replaced solid chemical candles with water-electrolysis oxygen generation on the ISS.",
         "https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/"),
    ]
    for col, color, title, what, fix, link in incidents:
        col.markdown(textwrap.dedent(f"""
        <div class="incident-box" style="border-left: 4px solid {color};">
            <h4 style="color:{color};margin-top:0;">{title}</h4>
            <p style="color:#c9d7f5;font-size:0.92rem;line-height:1.5;">{what}</p>
            <p style="color:#00f5a0;font-size:0.87rem;line-height:1.45;"><b>✅ Modern NASA Fix:</b> {fix}</p>
            <a href="{link}" target="_blank" style="color:{color};font-size:0.8rem;text-decoration:none;">NASA Official Mission Archive ↗</a>
        </div>
        """).strip(), unsafe_allow_html=True)

    # Historical → Modern Research Timeline
    st.markdown("#### 📅 Space Disasters → Modern ISS Combustion Timeline")
    tl_events = [
        ("Apollo 1 Fire", 1967, "Incident", "Pure O₂ flashover kills 3 astronauts"),
        ("Apollo 13 Explosion", 1970, "Incident", "Cryo O₂ tank explosion, LM lifeboat recovery"),
        ("Mir Station Fire", 1997, "Incident", "Solid chemical candle fire fills station with smoke"),
        ("BASS / BRE Inception", 2012, "Research", "ISS solid fuel microgravity tests initiate"),
        ("Saffire-I Flight", 2016, "Research", "First large-scale spacecraft fire test (Cygnus)"),
        ("FLEX Cool Flames", 2017, "Research", "Discovery of invisible low-temp combustion"),
        ("SoFIE & Saffire-VI", 2022, "Research", "Lunar gravity flammability & exploration atmospheres"),
    ]
    fig_tl = go.Figure()
    for ev, yr, typ, desc in tl_events:
        col = "#ff4d4d" if typ == "Incident" else "#00d2ff"
        fig_tl.add_trace(go.Scatter(
            x=[yr], y=[typ],
            mode="markers+text",
            marker=dict(size=22, color=col, opacity=0.9, line=dict(color="#ffffff", width=1.5)),
            text=[ev.split()[0]],
            textposition="top center",
            name=ev,
            showlegend=False,
            hovertemplate=f"<b>{ev} ({yr})</b><br>{desc}<extra></extra>",
        ))
    fig_tl.update_layout(
        title=dict(text="Timeline: Space Disasters Driving Modern Microgravity Science", font=dict(family="Orbitron", size=14)),
        xaxis_title="Calendar Year",
        height=320,
        margin=dict(t=40, b=30, l=20, r=20),
        **PLOTLY_LAYOUT
    )
    st.plotly_chart(fig_tl, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;color:#475d84;font-size:0.78rem;padding:18px;border-top:1px solid #141f38;margin-top:30px;">
    🔥 <b>NASA Flame in Freefall</b> · Space Apps Challenge 2026 · Data from <a href="https://psi.nasa.gov/physci/repo/search?q=combustion" target="_blank" style="color:#00d2ff;text-decoration:none;">NASA PSI</a> &amp; <a href="https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/" target="_blank" style="color:#00d2ff;text-decoration:none;">ISS Combustion Guide</a>
</div>
""", unsafe_allow_html=True)
