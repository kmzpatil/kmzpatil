import os
import textwrap

def generate_svg(filename, content, height):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    svg = f"""<svg viewBox="0 0 1000 {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{ 
      --bg: #0d1117; 
      --text-main: #c9d1d9;
      --text-muted: #8b949e;
      --accent: #1F8ACB; 
      --accent-glow: #00f0ff;
      --line: #30363d;
    }}
    .mono {{ font-family: "Cascadia Code", "Fira Code", Consolas, "SF Mono", monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    
    /* Animations */
    .draw {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.2s ease-out forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    
    .rise {{ opacity: 0; animation: rise 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
    @keyframes rise {{ 
      from {{ opacity: 0; transform: translateY(10px); }} 
      to {{ opacity: 1; transform: translateY(0); }} 
    }}
    
    .fade {{ opacity: 0; animation: fade 1s ease forwards; }}
    @keyframes fade {{ to {{ opacity: 1; }} }}

    /* Delays */
    .d1 {{ animation-delay: 0.1s; }}
    .d2 {{ animation-delay: 0.3s; }}
    .d3 {{ animation-delay: 0.5s; }}
    .d4 {{ animation-delay: 0.7s; }}
    .d5 {{ animation-delay: 0.9s; }}
  </style>
  
  <rect width="100%" height="100%" fill="var(--bg)" rx="8"/>
  {content}
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

def render_text(x, y, text, font_size, fill="var(--text-main)", weight="normal", delay_class="d2", font_class="mono"):
    text = str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<text class="{font_class} rise {delay_class}" fill="{fill}" x="{x}" y="{y}" font-size="{font_size}" font-weight="{weight}">{text}</text>'

def section_header(number, title):
    visual_length = len(title)
    title_escaped = str(title).replace("&", "&amp;").replace("   ", "&#160;&#160;&#160;&#160;")
    return f"""
  <g class="fade d1 mono">
    <text x="40" y="60" font-size="36" font-weight="bold" fill="var(--accent-glow)">{number}</text>
    <text x="96" y="52" font-size="16" letter-spacing="4" fill="var(--text-main)" font-weight="bold">{title_escaped}</text>
    <line class="draw d1" x1="{105 + visual_length*16}" y1="46" x2="960" y2="46" stroke="var(--line)" stroke-width="1"/>
  </g>
"""

def wrap_text(text, width=105):
    return textwrap.wrap(text, width=width)

# ================= 1. Header & About Me =================
header = f"""
  <line class="draw d1" x1="40" y1="60" x2="960" y2="60" stroke="var(--accent-glow)" stroke-width="2"/>
  <g class="fade d1 mono" font-size="12" letter-spacing="2" fill="var(--text-muted)">
    <text x="40" y="44">INIT SEQUENCE // ROOT</text>
    <text x="960" y="44" text-anchor="end">SYS.VER: 1.0.0</text>
  </g>
  
  {render_text(40, 140, "Kartik Mahendra Patil", 48, "var(--text-main)", "bold", "d2")}
  
  {render_text(40, 180, "ECE Undergrad @ IIT Kharagpur", 16, "var(--accent)", "bold", "d2")}
  {render_text(340, 180, "◆", 10, "var(--accent-glow)", "normal", "d2")}
  {render_text(360, 180, "LINKEDIN : kartik-patil-957834201", 12, "var(--text-muted)", "normal", "d2")}
  {render_text(630, 180, "◆", 10, "var(--accent-glow)", "normal", "d2")}
  {render_text(650, 180, "EMAIL : kmzpatil@gmail.com", 12, "var(--text-muted)", "normal", "d2")}
  {render_text(850, 180, "◆", 10, "var(--accent-glow)", "normal", "d2")}
  {render_text(870, 180, "CF : kresol", 12, "var(--text-muted)", "normal", "d2")}
  
  {render_text(40, 230, "A passionate systems engineer and competitive programmer driven to build the next generation", 14, "var(--text-muted)", "normal", "d3", "sans")}
  {render_text(40, 255, "of high-performance scalable architectures. Specializing in C++ sub-microsecond matching engines,", 14, "var(--text-muted)", "normal", "d3", "sans")}
  {render_text(40, 280, "robust full-stack multi-agent AI platforms, low-level kernel optimizations, and DeFi infrastructure.", 14, "var(--text-muted)", "normal", "d3", "sans")}
  
  <line class="draw d4" x1="40" y1="320" x2="960" y2="320" stroke="var(--line)" stroke-width="1"/>
"""
generate_svg('assets/00_header.svg', header, 360)

# ================= 2. Tech Stack =================
sysmap = section_header("01", "S Y S T E M   A R C H I T E C T U R E")
sysmap += render_text(40, 120, "LANGUAGES", 12, "var(--accent-glow)", "bold", "d2")
sysmap += render_text(220, 120, "C++, Python, TypeScript, JavaScript", 14, "var(--text-main)", "normal", "d2")
sysmap += render_text(40, 160, "FRAMEWORKS", 12, "var(--accent-glow)", "bold", "d3")
sysmap += render_text(220, 160, "React, Next.js, Node.js, FastAPI, Flask, TailwindCSS, Vite", 14, "var(--text-main)", "normal", "d3")
sysmap += render_text(40, 200, "DATA & AI", 12, "var(--accent-glow)", "bold", "d4")
sysmap += render_text(220, 200, "PyTorch, TensorFlow, Pandas, PostgreSQL, MongoDB", 14, "var(--text-main)", "normal", "d4")
sysmap += render_text(40, 240, "TOOLCHAIN", 12, "var(--accent-glow)", "bold", "d5")
sysmap += render_text(220, 240, "Docker, Git, CMake, Flex/Bison", 14, "var(--text-main)", "normal", "d5")
generate_svg('assets/01_sysmap.svg', sysmap, 290)

# ================= 3. Projects (Categorized) =================
def build_project_svg(number, title, projects):
    y_cursor = 120
    content = section_header(number, title)
    for p in projects:
        content += render_text(40, y_cursor, p["title"], 18, "var(--text-main)", "bold", "d2")
        y_cursor += 25
        content += render_text(40, y_cursor, p["subtitle"], 13, "var(--accent)", "normal", "d2")
        y_cursor += 30
        for bullet in p["bullets"]:
            lines = wrap_text(bullet, width=105)
            for i, line in enumerate(lines):
                prefix = "▸ " if i == 0 else "  "
                content += render_text(40, y_cursor, prefix + line, 13, "var(--text-muted)", "normal", "d3", "sans")
                y_cursor += 22
            y_cursor += 5
        
        y_cursor += 15
        content += render_text(40, y_cursor, f"[{p['stack']}]", 12, "var(--line)", "normal", "d4")
        y_cursor += 50
    return content, y_cursor

proj_cpp = [
    {
        "title": "Multithreaded Order Book Matching Engine",
        "subtitle": "Low-Latency C++ Systems",
        "bullets": [
            "Matching engine processing concurrent orders via thread-safe mutex-protected single-consumer queue handling 10,000+ msgs/sec.",
            "Concurrent state management using condition variable for blocking pops and an atomic engine flag for zero-leak teardowns.",
            "Price-time priority order matching using std::map with std::greater. Optimized critical paths for sub-microsecond processing, reducing p99 latency by 40%."
        ],
        "stack": "C++ · Multithreading · CMake · Google Benchmarks"
    },
    {
        "title": "Mini-Compiler",
        "subtitle": "Compiler Design from Scratch",
        "bullets": [
            "Assembled C++ compiler pipeline translating source code into bytecode for a stack-based virtual machine, compiling 10K+ lines/sec.",
            "Constructed recursive descent Lexer and Parser from scratch to tokenize 5 core keywords and execute syntax checking.",
            "Implemented comprehensive support for 18+ operators in AST visitors. Built stack-based VM optimizing memory management for 50%+ quicker runs."
        ],
        "stack": "C++ · CMake"
    },
    {
        "title": "Real-Time Autocomplete Engine",
        "subtitle": "High-Performance Data Structures",
        "bullets": [
            "C++ top-k suggestion system providing predictive completions for 1.2M+ entries.",
            "Memory-efficient Radix Tries with per-node top-K caching indexing 500,000+ word vocabularies.",
            "Interactive terminal interface capturing dynamic keystrokes to benchmark latency. Optimized string matching for 10K+ QPS throughput, achieving sub-millisecond lookup for 10M+ queries."
        ],
        "stack": "C++ · CMake"
    }
]
c_svg, h_cpp = build_project_svg("02", "C O R E   S Y S T E M S", proj_cpp)
generate_svg('assets/02_core_systems.svg', c_svg, h_cpp)

proj_ai = [
    {
        "title": "Frammer - Unified AI Analytics Platform",
        "subtitle": "General Championship | Rank 1 Gold Medal",
        "bullets": [
            "Full-stack analytics platform with an autonomous ATLAS AI engine using a custom ReAct loop for data analysis.",
            "Developed a custom DSL parser to track 19+ complex KPIs, implementing a secure PostgreSQL multi-tenant RBAC architecture supporting strict tenant isolation.",
            "Integrated Docker, Google Gemini, and Chronos forecasting. Cut data retrieval delays by 35% on 1M+ row operations using partial and covering B-tree indexes."
        ],
        "stack": "FastAPI · React · Vite · PostgreSQL · Docker · Gemini"
    },
    {
        "title": "DeFi Arbitrage Bot",
        "subtitle": "Decentralized Finance",
        "bullets": [
            "Python DeFi arbitrage engine using Web3.py and Infura monitoring 50+ Uniswap V3 pools for price discrepancies.",
            "Implemented Bellman-Ford negative cycle detection on 100+ node token graphs to identify triangular arbitrage paths.",
            "Formulated profit calculations with real-time gas oracles for 95%+ accurate net PnL. Deployed FastAPI dashboard with WebSocket feeds."
        ],
        "stack": "Python · Web3.py · FastAPI · WebSocket"
    },
    {
        "title": "Gloser AI - Pharma Intelligence",
        "subtitle": "Multi-Agent LLM System",
        "bullets": [
            "AI-powered intelligence systems using LangGraph multi-agent architectures to profile 5,000+ clinical and trade queries.",
            "Specialized Python agents integrated with Groq API to process 30,000+ pharmaceutical records.",
            "Designed Next.js chat interfaces and Flask APIs enabling backend communication with live LLMs under 500ms latency. Strict TypeScript definitions reducing runtime errors by 40%."
        ],
        "stack": "Next.js · LangGraph · Groq · Flask · Python"
    },
    {
        "title": "Chernobyl Prevention System",
        "subtitle": "Deep Learning for Risk Classification",
        "bullets": [
            "Deep sequence classification model utilizing LSTM to predict 4 risk levels from 27-dimensional continuous sensor data.",
            "Engineered rolling volatility and interquartile ranges, applying cubic transforms to amplify extreme datasets. Dynamic training strategy using decreasing batch sizes.",
            "Optimized hyperparameters using Optuna, boosting F1-score to 0.94 and reducing training epochs by 30%."
        ],
        "stack": "Python · PyTorch · Optuna · LSTM"
    },
    {
        "title": "Cancer Detection System",
        "subtitle": "1st Runner-up at KDAG ML Hackathon",
        "bullets": [
            "Engineered pipeline resolving circular dependencies via HDBSCAN outlier detection and KNN imputation, achieving 92%+ precision.",
            "Architected ensemble of 10 EfficientNet and ResNet using majority-class batching. Optimized Gradient Boosting hyperparameters utilizing Optuna, maximizing F1-scores by 15%.",
            "Accelerated processing pipeline speed by 35% utilizing multi-threaded data loading and vectorized pandas operations."
        ],
        "stack": "Python · PyTorch · Optuna · Scikit-Learn"
    },
    {
        "title": "Summer Analytics Hackathon",
        "subtitle": "Data Science Competition",
        "bullets": [
            "Developed advanced machine learning models for predictive analytics on large datasets.",
            "Utilized exploratory data analysis (EDA) to uncover actionable business insights."
        ],
        "stack": "Python · Scikit-Learn · Pandas · Jupyter Notebook"
    }
]
ai_svg, h_ai = build_project_svg("03", "A I   D A T A   &   Q U A N T", proj_ai)
generate_svg('assets/03_ai_quant.svg', ai_svg, h_ai)


proj_web = [
    {
        "title": "CDC Companion - CV Review Platform",
        "subtitle": "Full-Stack SaaS",
        "bullets": [
            "High-performance REST API matching 500+ candidates with reviewers.",
            "AI review agent extracting text from 1,000+ PDFs to generate domain-specific CV feedback via LLMs.",
            "JWT auth, dependency-free rate limiter, and automated Nodemailer with <2s delivery latency."
        ],
        "stack": "Node.js · TypeScript · Prisma · LLMs"
    },
    {
        "title": "GMUN 2026 - Event Platform",
        "subtitle": "Official IIT KGP MUN Platform",
        "bullets": [
            "Digital interface for the Global Model United Nations at IIT KGP handling 300+ delegate registrations.",
            "Mobile-first responsive design with seamless registration workflows."
        ],
        "stack": "React.js · Node.js · CSS3"
    },
    {
        "title": "Todo Full-Stack App",
        "subtitle": "Productivity Tool",
        "bullets": [
            "Built a robust full-stack task management application featuring user authentication and real-time state synchronization.",
            "Implemented RESTful API endpoints for complete CRUD functionality with persistent database storage."
        ],
        "stack": "TypeScript · JavaScript · React · Node.js"
    }
]
web_svg, h_web = build_project_svg("04", "W E B   &   F U L L   S T A C K", proj_web)
generate_svg('assets/04_web_fullstack.svg', web_svg, h_web)

# ================= 4. Competitions =================
comps = section_header("05", "A C H I E V E M E N T S")
y_cursor = 120
for c_title, c_res in [
    ("Codeforces Expert", "Max Rating 1616"),
    ("IICPC CodeFest 2026 Global", "Rank 1254 / 13,000+ coders"),
    ("IMC Prosperity 4", "Global Rank 529, Country Rank 81"),
    ("Goldman Sachs India Hackathon 2026", "Quant: Rank 447, CS: Rank 584"),
    ("AMS Derive 2026 (Jane Street, QRT)", "Rank 198 / 2,500")
]:
    comps += render_text(40, y_cursor, c_title, 15, "var(--text-main)", "bold", "d2")
    comps += render_text(450, y_cursor, c_res, 14, "var(--text-muted)", "normal", "d3")
    comps += f'<line class="draw d4" x1="40" y1="{y_cursor+15}" x2="960" y2="{y_cursor+15}" stroke="var(--line)" stroke-width="1" stroke-dasharray="4 4"/>'
    y_cursor += 40
generate_svg('assets/05_achievements.svg', comps, y_cursor + 20)

# ================= 5. OSS =================
oss = section_header("06", "F E A T U R E D   P R O J E C T S")
y_cursor = 120
oss += render_text(40, y_cursor, "19+ active repositories across C++, Python, and Web architectures.", 14, "var(--text-main)", "normal", "d2", "sans")
y_cursor += 25
oss += render_text(40, y_cursor, "View them all below or at github.com/kmzpatil", 14, "var(--text-muted)", "normal", "d3", "sans")
generate_svg('assets/06_oss.svg', oss, y_cursor + 40)

# ================= 6. Telemetry =================
telemetry = section_header("07", "T E L E M E T R Y")
generate_svg('assets/07_telemetry.svg', telemetry, 90)

print("All precision SVGs generated successfully.")
