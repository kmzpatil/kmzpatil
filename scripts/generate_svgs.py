import os

def create_svg(filename, content, height):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    svg_template = f"""<svg viewBox="0 0 1000 {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{ --bone: #444444; --rule: #C0C0C0; --muted: #888888; --dim: #AAAAAA; --accent: #555555; --bg: #ffffff; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --bone: #DDDDDD; --rule: #444444; --muted: #777777; --dim: #666666; --accent: #AAAAAA; --bg: #0d1117; }} }}
    .mono {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .draw {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.4s cubic-bezier(.6,0,.2,1) forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    .rise {{ opacity: 0; animation: rise .9s cubic-bezier(.2,.7,.2,1) forwards; }}
    @keyframes rise {{ from {{ opacity:0;transform:translateY(12px); }} to {{ opacity:1;transform:translateY(0); }} }}
    .fade {{ opacity: 0; animation: fade .7s ease forwards; }}
    @keyframes fade {{ to {{ opacity: 1; }} }}
    .a1{{animation-delay:.2s}} .a2{{animation-delay:.5s}} .a3{{animation-delay:.9s}} .a4{{animation-delay:1.2s}} .a5{{animation-delay:1.4s}} .a6{{animation-delay:1.7s}}
    @media (prefers-reduced-motion: reduce) {{
      .draw,.rise,.fade {{ animation: none; }}
      .draw{{stroke-dashoffset:0}} .rise,.fade{{opacity:1}}
    }}
  </style>
  <rect width="100%" height="100%" fill="var(--bg)" rx="10"/>
  {content}
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_template)

# 1. Header
header_content = """
  <line class="draw a1" x1="48" y1="58" x2="952" y2="58" stroke="var(--rule)" stroke-width="1"/>
  <g class="fade a1">
    <text class="mono" fill="var(--muted)" x="48" y="44" font-size="11" letter-spacing="3.5">PORTFOLIO — INDEX Nº 001</text>
    <text class="mono" fill="var(--muted)" x="952" y="44" font-size="11" letter-spacing="3.5" text-anchor="end">CHENNAI, IN — 13.08° N</text>
  </g>

  <g class="rise a2">
    <text class="mono" fill="var(--bone)" x="48" y="140" font-size="48" font-weight="bold">Kartik Patil</text>
    <text class="mono" fill="var(--bone)" x="48" y="180" font-size="18">Software Engineer — Chennai, India.</text>
  </g>

  <g class="fade a3 mono" font-size="12" fill="var(--bone)">
    <text x="48" y="240">focus ▸    Full-Stack Systems · AI-Integrated Products · Low-Latency C++</text>
    <text x="48" y="265">status     open to opportunities · collaboration</text>
  </g>

  <line class="draw a4" x1="48" y1="320" x2="952" y2="320" stroke="var(--rule)" stroke-width="1"/>
"""
create_svg('assets/header.svg', header_content, 380)

# 2. Whoami
whoami_content = """
  <g class="fade a1 mono" font-size="14" font-weight="bold" fill="var(--bone)" letter-spacing="2">
    <text x="48" y="60" font-size="32">01</text>
    <text x="96" y="55">W H O A M I</text>
    <line class="draw a1" x1="220" y1="50" x2="780" y2="50" stroke="var(--rule)" stroke-width="1"/>
    <text x="800" y="55" font-size="10" fill="var(--muted)">~/01-whoami</text>
  </g>

  <g class="rise a2 mono" font-size="13" fill="var(--bone)">
    <text x="48" y="120">Student at Vellore Institute of Technology, Chennai.</text>
    <text x="48" y="145">Building robust full-stack applications and high-performance algorithms.</text>
    <text x="48" y="170">Passionate about elegant architecture, AI integration, and systems programming.</text>
  </g>
"""
create_svg('assets/01-whoami.svg', whoami_content, 220)

# 3. System Map (Expertise)
sysmap_content = """
  <g class="fade a1 mono" font-size="14" font-weight="bold" fill="var(--bone)" letter-spacing="2">
    <text x="48" y="60" font-size="32">02</text>
    <text x="96" y="55">S Y S T E M   M A P</text>
    <line class="draw a1" x1="280" y1="50" x2="780" y2="50" stroke="var(--rule)" stroke-width="1"/>
    <text x="800" y="55" font-size="10" fill="var(--muted)">~/02-system-map</text>
  </g>

  <g class="rise a2 mono" font-size="13" fill="var(--bone)">
    <text x="48" y="120" fill="var(--muted)">LANGUAGES</text>
    <text x="200" y="120">C++, Python, TypeScript, JavaScript</text>
    
    <text x="48" y="150" fill="var(--muted)">FRAMEWORKS</text>
    <text x="200" y="150">React, Next.js, Node.js, FastAPI, Flask, TailwindCSS, Vite</text>
    
    <text x="48" y="180" fill="var(--muted)">AI / DATA</text>
    <text x="200" y="180">PyTorch, TensorFlow, Pandas</text>
    
    <text x="48" y="210" fill="var(--muted)">INFRA</text>
    <text x="200" y="210">PostgreSQL, MongoDB, Docker, Git, CMake</text>
  </g>
"""
create_svg('assets/02-sysmap.svg', sysmap_content, 260)

# 4. Projects
projects_content = """
  <g class="fade a1 mono" font-size="14" font-weight="bold" fill="var(--bone)" letter-spacing="2">
    <text x="48" y="60" font-size="32">03</text>
    <text x="96" y="55">P R O J E C T S</text>
    <line class="draw a1" x1="240" y1="50" x2="780" y2="50" stroke="var(--rule)" stroke-width="1"/>
    <text x="800" y="55" font-size="10" fill="var(--muted)">~/03-projects</text>
  </g>

  <g class="rise a2 mono" fill="var(--bone)">
    <text x="48" y="110" font-size="16" font-weight="bold">Frammer - Unified AI Analytics Platform</text>
    <text x="48" y="130" font-size="11" fill="var(--muted)">General Championship | Rank 1 Gold Medal</text>
    <text x="48" y="160" font-size="12">Full-stack platform with ATLAS AI engine. Developed DSL parser tracking 19+ KPIs.</text>
    <text x="48" y="180" font-size="12">PostgreSQL multi-tenant RBAC. Cut delays by 35% using B-tree indexes.</text>
    <text x="48" y="200" font-size="12" fill="var(--muted)">FastAPI · React · Vite · PostgreSQL · Docker · Gemini</text>
    
    <text x="48" y="250" font-size="16" font-weight="bold">Mini-Compiler</text>
    <text x="48" y="280" font-size="12">Developed a recursive descent parser generating Abstract Syntax Trees (AST).</text>
    <text x="48" y="300" font-size="12">Implemented support for 18+ operators (arithmetic, bitwise, comparison).</text>
    <text x="48" y="320" font-size="12" fill="var(--muted)">C++ · Compiler Design · AST · Flex/Bison</text>

    <text x="48" y="370" font-size="16" font-weight="bold">DeFi Arbitrage Bot</text>
    <text x="48" y="400" font-size="12">Python DeFi arbitrage engine using Web3.py monitoring 50+ Uniswap V3 pools.</text>
    <text x="48" y="420" font-size="12">Bellman-Ford negative cycle detection on 100+ node token graphs.</text>
    <text x="48" y="440" font-size="12" fill="var(--muted)">Python · Web3.py · Defi · Graph Algorithms</text>
  </g>
"""
create_svg('assets/03-projects.svg', projects_content, 480)

# 5. Telemetry
telemetry_content = """
  <g class="fade a1 mono" font-size="14" font-weight="bold" fill="var(--bone)" letter-spacing="2">
    <text x="48" y="60" font-size="32">04</text>
    <text x="96" y="55">T E L E M E T R Y</text>
    <line class="draw a1" x1="260" y1="50" x2="780" y2="50" stroke="var(--rule)" stroke-width="1"/>
    <text x="800" y="55" font-size="10" fill="var(--muted)">~/04-telemetry</text>
  </g>
"""
create_svg('assets/04-telemetry.svg', telemetry_content, 100)

# 6. Open Source
oss_content = """
  <g class="fade a1 mono" font-size="14" font-weight="bold" fill="var(--bone)" letter-spacing="2">
    <text x="48" y="60" font-size="32">05</text>
    <text x="96" y="55">O P E N   S O U R C E</text>
    <line class="draw a1" x1="300" y1="50" x2="780" y2="50" stroke="var(--rule)" stroke-width="1"/>
    <text x="800" y="55" font-size="10" fill="var(--muted)">~/05-open-source</text>
  </g>
  <g class="rise a2 mono" font-size="12" fill="var(--bone)">
    <text x="48" y="110">▸ Cdc-Companion     (TypeScript)   Google Chrome Extension for placement portal.</text>
    <text x="48" y="140">▸ 2026-PortFolio    (TypeScript)   Personal portfolio website using Next.js.</text>
    <text x="48" y="170">▸ Image-Colorizer   (Python)       DL model to colorize greyscale images.</text>
    <text x="48" y="200">▸ Object-Detection  (Python)       Real-time object detection using YOLO.</text>
  </g>
"""
create_svg('assets/05-oss.svg', oss_content, 240)

print("Generated SVGs in assets/")
