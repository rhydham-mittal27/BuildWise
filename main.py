import json
import os

import streamlit as st

import agent

MEMORY_FILE = "memory/chat_history.json"

os.makedirs("memory", exist_ok=True)


def load_messages():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_messages(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=2,
        )


st.set_page_config(
    page_title="BuildWise",
    page_icon="🏗️",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────────────────────
#  VISUAL OVERHAUL  —  CSS + Animated Orbs + 3D Effects
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── RESET ────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

/* ── ROOT BACKGROUND ──────────────────────────────────────── */
.stApp {
    background: #030712 !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* subtle grid overlay */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(99,102,241,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,102,241,0.035) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
    z-index: 0;
}

/* ── FLOATING ORBS ────────────────────────────────────────── */
.bw-orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    will-change: transform;
}
.bw-orb-1 {
    width: 700px; height: 700px;
    background: radial-gradient(circle at 40% 40%,
        rgba(124,58,237,0.55) 0%, rgba(79,70,229,0.22) 45%, transparent 70%);
    top: -260px; left: -260px;
    filter: blur(65px);
    animation: orb1 18s ease-in-out infinite;
}
.bw-orb-2 {
    width: 560px; height: 560px;
    background: radial-gradient(circle at 60% 60%,
        rgba(14,165,233,0.5) 0%, rgba(6,182,212,0.18) 45%, transparent 70%);
    bottom: -150px; right: -150px;
    filter: blur(70px);
    animation: orb2 22s ease-in-out infinite;
}
.bw-orb-3 {
    width: 460px; height: 460px;
    background: radial-gradient(circle at 50% 50%,
        rgba(236,72,153,0.42) 0%, rgba(168,85,247,0.2) 45%, transparent 70%);
    top: 45%; left: 55%;
    filter: blur(80px);
    animation: orb3 26s ease-in-out infinite;
}
.bw-orb-4 {
    width: 360px; height: 360px;
    background: radial-gradient(circle at 50% 50%,
        rgba(34,211,238,0.38) 0%, rgba(99,102,241,0.16) 45%, transparent 70%);
    top: 20%; left: 4%;
    filter: blur(55px);
    animation: orb4 14s ease-in-out infinite;
}
.bw-orb-5 {
    width: 280px; height: 280px;
    background: radial-gradient(circle at 50% 50%,
        rgba(251,191,36,0.28) 0%, rgba(245,158,11,0.1) 45%, transparent 70%);
    top: 70%; left: 42%;
    filter: blur(50px);
    animation: orb5 19s ease-in-out infinite;
}

@keyframes orb1 {
    0%,100% { transform: translate(0,0) scale(1); }
    30%     { transform: translate(80px,60px) scale(1.07); }
    60%     { transform: translate(40px,-70px) scale(0.94); }
}
@keyframes orb2 {
    0%,100% { transform: translate(0,0) scale(1); }
    40%     { transform: translate(-70px,-50px) scale(1.09); }
    70%     { transform: translate(50px,70px) scale(0.93); }
}
@keyframes orb3 {
    0%,100% { transform: translate(-50%,-50%) scale(1); }
    35%     { transform: translate(calc(-50% + 90px),calc(-50% - 80px)) scale(1.12); }
    70%     { transform: translate(calc(-50% - 60px),calc(-50% + 50px)) scale(0.9); }
}
@keyframes orb4 {
    0%,100% { transform: translate(0,0) scale(1); }
    50%     { transform: translate(100px,-80px) scale(1.15); }
}
@keyframes orb5 {
    0%,100% { transform: translate(0,0) scale(1); }
    45%     { transform: translate(-80px,-60px) scale(1.1); }
}

/* shared sweep animation for glowing borders */
@keyframes sweep {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

/* ── LAYOUT ───────────────────────────────────────────────── */
.block-container {
    max-width: 1100px !important;
    padding-top: 2rem !important;
    position: relative;
    z-index: 1;
}

/* ── HEADER ───────────────────────────────────────────────── */
.bw-header {
    text-align: center;
    padding: 1rem 0 0.5rem;
}

/* 3-D floating logo box */
.bw-logo-box {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 84px; height: 84px;
    border-radius: 26px;
    background: linear-gradient(145deg, #4338ca 0%, #7c3aed 50%, #a855f7 100%);
    box-shadow:
        0 0 0 1px rgba(129,140,248,0.3),
        0 0 0 6px rgba(79,70,229,0.1),
        0 24px 48px rgba(79,70,229,0.45),
        0 48px 96px rgba(79,70,229,0.2),
        inset 0 1px 0 rgba(255,255,255,0.25),
        inset 0 -1px 0 rgba(0,0,0,0.3);
    font-size: 2.6rem;
    margin-bottom: 1.25rem;
    animation: logoFloat 6s ease-in-out infinite, logoPulse 6s ease-in-out infinite;
    transform-style: preserve-3d;
    user-select: none;
}
@keyframes logoFloat {
    0%,100% { transform: translateY(0) perspective(400px) rotateX(12deg) rotateY(-6deg); }
    50%     { transform: translateY(-8px) perspective(400px) rotateX(8deg) rotateY(6deg); }
}
@keyframes logoPulse {
    0%,100% {
        box-shadow:
            0 0 0 1px rgba(129,140,248,0.3),
            0 0 0 6px rgba(79,70,229,0.1),
            0 24px 48px rgba(79,70,229,0.45),
            0 48px 96px rgba(79,70,229,0.2),
            inset 0 1px 0 rgba(255,255,255,0.25);
    }
    50% {
        box-shadow:
            0 0 0 1px rgba(192,132,252,0.4),
            0 0 0 8px rgba(168,85,247,0.15),
            0 32px 64px rgba(168,85,247,0.55),
            0 64px 128px rgba(168,85,247,0.25),
            inset 0 1px 0 rgba(255,255,255,0.3);
    }
}

.bw-h1 {
    font-family: 'Syne', sans-serif;
    font-size: 3.4rem;
    font-weight: 800;
    background: linear-gradient(130deg, #60a5fa 0%, #818cf8 30%, #c084fc 60%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1.5px;
    line-height: 1;
    animation: glowPulse 5s ease-in-out infinite;
}
@keyframes glowPulse {
    0%,100% { filter: drop-shadow(0 0 22px rgba(129,140,248,0.35)); }
    50%     { filter: drop-shadow(0 0 44px rgba(192,132,252,0.62)); }
}

.bw-tag {
    display: inline-block;
    margin-top: 0.8rem;
    color: #334155;
    font-size: 0.72rem;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    font-weight: 400;
}

/* ── HERO CARD ────────────────────────────────────────────── */
.hero-card {
    position: relative;
    background: rgba(255,255,255,0.022);
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 28px;
    padding: 1.75rem 2.25rem;
    margin-bottom: 2rem;
    overflow: hidden;
    box-shadow:
        0 0 0 1px rgba(129,140,248,0.07),
        0 24px 64px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.06),
        inset 0 -1px 0 rgba(0,0,0,0.15);
    transition: transform 0.45s cubic-bezier(0.23,1,0.32,1),
                box-shadow 0.45s ease;
}
.hero-card:hover {
    box-shadow:
        0 0 0 1px rgba(129,140,248,0.13),
        0 32px 80px rgba(0,0,0,0.55),
        inset 0 1px 0 rgba(255,255,255,0.08),
        0 0 60px rgba(99,102,241,0.06);
}
/* animated gradient top border */
.hero-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg,
        transparent 0%, #6366f1 20%, #8b5cf6 40%,
        #ec4899 60%, #8b5cf6 80%, transparent 100%);
    background-size: 200% 100%;
    animation: sweep 4s linear infinite;
}
/* inner ambient glow */
.hero-card::after {
    content: '';
    position: absolute;
    inset: 0; border-radius: inherit;
    background: radial-gradient(
        ellipse at 15% 50%,
        rgba(99,102,241,0.07) 0%, transparent 60%);
    pointer-events: none;
}
.hero-card p {
    color: #94a3b8;
    font-size: 1rem;
    line-height: 1.85;
    position: relative;
    z-index: 1;
}

/* ── SIDEBAR ──────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: rgba(3,7,18,0.97) !important;
    border-right: 1px solid rgba(255,255,255,0.04) !important;
}
section[data-testid="stSidebar"] > div {
    position: relative;
}
section[data-testid="stSidebar"] > div::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #06b6d4, #6366f1);
    background-size: 300% 100%;
    animation: sweep 3s linear infinite;
    z-index: 10;
}
section[data-testid="stSidebar"] h2 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #818cf8, #c084fc) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}
section[data-testid="stSidebar"] h3 {
    color: #2d3748 !important;
    font-size: 0.68rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
}
section[data-testid="stSidebar"] li {
    color: #475569 !important;
    transition: all 0.2s ease !important;
    padding: 0.15rem 0 !important;
}
section[data-testid="stSidebar"] li:hover {
    color: #a5b4fc !important;
    padding-left: 6px !important;
}

/* ── METRIC ───────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.025) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 18px !important;
    padding: 1rem 1.25rem !important;
    box-shadow:
        0 0 0 1px rgba(99,102,241,0.07),
        0 8px 24px rgba(0,0,0,0.3) !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    background: linear-gradient(135deg, #818cf8, #c084fc) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    font-weight: 800 !important;
    font-size: 2.2rem !important;
}
[data-testid="stMetricLabel"] {
    color: #2d3748 !important;
    font-size: 0.7rem !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

/* ── CLEAR MEMORY BUTTON ──────────────────────────────────── */
.stButton > button {
    background: rgba(239,68,68,0.07) !important;
    border: 1px solid rgba(239,68,68,0.18) !important;
    color: #f87171 !important;
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.3s cubic-bezier(0.23,1,0.32,1) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
}
.stButton > button:hover {
    background: rgba(239,68,68,0.14) !important;
    border-color: rgba(239,68,68,0.38) !important;
    box-shadow:
        0 0 0 1px rgba(239,68,68,0.12),
        0 8px 28px rgba(239,68,68,0.18),
        0 0 40px rgba(239,68,68,0.08) !important;
    transform: translateY(-2px) !important;
}
.stButton > button:active {
    transform: translateY(0) scale(0.98) !important;
}

/* ── CHAT MESSAGES ────────────────────────────────────────── */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.045) !important;
    border-radius: 22px !important;
    margin-bottom: 0.85rem !important;
    backdrop-filter: blur(16px);
    box-shadow:
        0 4px 24px rgba(0,0,0,0.22),
        inset 0 1px 0 rgba(255,255,255,0.04) !important;
    transition: all 0.3s ease !important;
}
[data-testid="stChatMessage"]:hover {
    border-color: rgba(129,140,248,0.1) !important;
    box-shadow:
        0 8px 40px rgba(0,0,0,0.32),
        0 0 0 1px rgba(129,140,248,0.06),
        inset 0 1px 0 rgba(255,255,255,0.05) !important;
    transform: translateY(-1px) !important;
}

/* ── CHAT INPUT ───────────────────────────────────────────── */
.stChatInputContainer {
    background: rgba(3,7,18,0.88) !important;
    border-top: 1px solid rgba(255,255,255,0.05) !important;
    backdrop-filter: blur(24px) !important;
}
[data-testid="stChatInput"] textarea {
    background: rgba(255,255,255,0.025) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 18px !important;
    color: #e2e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: rgba(99,102,241,0.38) !important;
    box-shadow:
        0 0 0 4px rgba(99,102,241,0.08),
        0 0 30px rgba(99,102,241,0.1) !important;
}

/* ── SPINNER ──────────────────────────────────────────────── */
.stSpinner > div {
    border-color: rgba(129,140,248,0.15) !important;
    border-top-color: #818cf8 !important;
}

/* ── MISC ─────────────────────────────────────────────────── */
hr, [data-testid="stDivider"] hr {
    border-color: rgba(255,255,255,0.04) !important;
    margin: 1.25rem 0 !important;
}
[data-testid="stMarkdownContainer"] p {
    color: #94a3b8 !important;
    line-height: 1.8 !important;
}
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.22); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(99,102,241,0.42); }
::selection { background: rgba(99,102,241,0.28); color: #f8fafc; }
</style>

<!-- ── FLOATING ORBS ─────────────────────────────────────── -->
<div class="bw-orb bw-orb-1" aria-hidden="true"></div>
<div class="bw-orb bw-orb-2" aria-hidden="true"></div>
<div class="bw-orb bw-orb-3" aria-hidden="true"></div>
<div class="bw-orb bw-orb-4" aria-hidden="true"></div>
<div class="bw-orb bw-orb-5" aria-hidden="true"></div>

<!-- ── 3D TILT JS ─────────────────────────────────────────── -->
<script>
(function() {
    function initTilt() {
        var card = document.querySelector('.hero-card');
        if (!card) { setTimeout(initTilt, 300); return; }
        card.addEventListener('mousemove', function(e) {
            var r = card.getBoundingClientRect();
            var x = (e.clientX - r.left) / r.width  - 0.5;
            var y = (e.clientY - r.top)  / r.height - 0.5;
            card.style.transform =
                'perspective(1200px) rotateX(' + (-y * 7) + 'deg) rotateY(' + (x * 7) + 'deg)';
        });
        card.addEventListener('mouseleave', function() {
            card.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg)';
        });
    }
    document.addEventListener('DOMContentLoaded', initTilt);
    setTimeout(initTilt, 500);
})();
</script>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="bw-header">
    <div class="bw-logo-box" role="img" aria-label="BuildWise logo">🏗️</div>
    <div class="bw-h1">BuildWise</div>
    <span class="bw-tag">AI Software Architect &amp; Project Planner</span>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero-card">
    <p>
        Describe your <strong style="color:#a5b4fc;font-weight:500;">startup</strong>,
        <strong style="color:#c084fc;font-weight:500;">SaaS</strong>,
        <strong style="color:#f472b6;font-weight:500;">marketplace</strong>,
        AI application, mobile app, internal tool, or enterprise software.
        BuildWise will help generate <em>requirements, architecture,
        database&nbsp;schemas, APIs, roadmaps,</em> and <em>implementation&nbsp;plans</em>.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:

    st.markdown("## 🏗️ BuildWise")

    st.markdown("""
### Capabilities

- Product Requirements
- User Stories
- System Architecture
- Database Design
- API Planning
- Tech Stack Selection
- Development Roadmaps
- AI Integration Planning
""")

    st.divider()

    total_messages = len(load_messages())

    st.metric(
        label="Stored Messages",
        value=total_messages,
    )

    if st.button(
        "🗑️ Clear Memory",
        use_container_width=True,
    ):
        st.session_state.messages = []
        save_messages([])
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = load_messages()

# ─────────────────────────────────────────────────────────────────────────────
#  CHAT HISTORY
# ─────────────────────────────────────────────────────────────────────────────
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─────────────────────────────────────────────────────────────────────────────
#  USER INPUT
# ─────────────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Describe your project idea...")

if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("assistant"):

        with st.spinner("Designing architecture..."):

            result = agent.planner_agent.invoke({"messages": st.session_state.messages})

            assistant_message = result["messages"][-1].content

            st.markdown(assistant_message)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )

    save_messages(st.session_state.messages)
