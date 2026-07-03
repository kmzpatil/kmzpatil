"""
Daily dev log generator for GitHub profile repo.
Appends a meaningful rotating entry to dev_log.md each day.
"""

import datetime
import random
import os

# Topics cycling through your actual domain areas
TOPICS = [
    # C++ / Systems
    ("Low-Latency C++", [
        "Reviewed lock-free queue patterns using `std::atomic` and memory ordering semantics.",
        "Studied cache-oblivious algorithms and their impact on branch predictor performance.",
        "Analyzed false sharing in multithreaded order books — padding structs to 64-byte alignment.",
        "Explored `std::memory_order_acquire/release` for building wait-free data structures.",
        "Benchmarked `std::map` vs flat sorted arrays for price-time priority order matching.",
        "Read about DPDK (Data Plane Development Kit) for kernel-bypass networking in HFT.",
        "Studied CPU prefetching strategies to optimize hot paths in the matching engine.",
        "Profiled memory allocator overhead — switched inner loop to arena allocation pattern.",
    ]),
    # Algorithms / CP
    ("Competitive Programming", [
        "Practiced Bellman-Ford on negative-cycle detection for triangular arbitrage graphs.",
        "Solved a segment tree with lazy propagation problem — range assign and range sum.",
        "Reviewed Knuth-Yao DP optimization for convex cost functions.",
        "Analyzed amortized complexity of DSU with path compression and union by rank.",
        "Worked through a flow network problem using Dinic's algorithm with BFS layering.",
        "Studied Li Chao tree for dynamic convex hull trick on online queries.",
        "Practiced 2-SAT formulation for scheduling constraint satisfaction problems.",
        "Revisited offline LCA using Euler tour + sparse table for range minimum queries.",
    ]),
    # AI / LLM / Agents
    ("AI & Multi-Agent Systems", [
        "Studied ReAct loop internals — how thought/action/observation cycles handle tool calls.",
        "Reviewed LangGraph state machine patterns for orchestrating parallel agent branches.",
        "Explored multi-head attention complexity trade-offs in transformer inference.",
        "Read about retrieval-augmented generation (RAG) chunking strategies for long documents.",
        "Analyzed Groq's LPU architecture and why it achieves lower token latency than GPUs.",
        "Studied function-calling schemas in OpenAI and Gemini APIs for structured agent output.",
        "Reviewed KV-cache eviction policies in vLLM for high-throughput LLM serving.",
        "Explored RLHF vs DPO trade-offs for fine-tuning instruction-following behavior.",
    ]),
    # Quant / DeFi
    ("Quant & DeFi", [
        "Reviewed Uniswap V3 concentrated liquidity math and tick-based price range encoding.",
        "Studied Black-Scholes Greeks — delta hedging and gamma scalping intuition.",
        "Analyzed IMC Prosperity market-making strategy — bid-ask spread optimization.",
        "Read about cross-venue statistical arbitrage using cointegrated asset pairs.",
        "Explored Bellman-Ford on exchange rate graphs for detecting arbitrage cycles.",
        "Reviewed EIP-1559 fee mechanism and miner-extractable value (MEV) implications.",
        "Studied pairs trading using Ornstein-Uhlenbeck mean-reversion process.",
        "Analyzed flash loan mechanics and atomic transaction composability in DeFi.",
    ]),
    # Web / Full Stack
    ("Full Stack Engineering", [
        "Reviewed PostgreSQL EXPLAIN ANALYZE output — identified sequential scan vs index scan.",
        "Studied multi-tenant RBAC patterns with row-level security in PostgreSQL.",
        "Explored React Server Components vs Client Components trade-offs in Next.js 14.",
        "Read about HTTP/2 multiplexing and how it reduces latency for API-heavy apps.",
        "Analyzed JWT vs session token security — refresh token rotation best practices.",
        "Reviewed WebSocket connection pooling strategies for real-time dashboard updates.",
        "Studied Prisma query optimization — N+1 problem and relation loading strategies.",
        "Explored FastAPI dependency injection patterns for modular API route organization.",
    ]),
    # ML / Deep Learning
    ("Machine Learning", [
        "Reviewed LSTM vanishing gradient problem — why gating mechanisms solve it.",
        "Studied Optuna TPE sampler — how it models hyperparameter distributions.",
        "Analyzed class imbalance handling: SMOTE vs majority batching vs focal loss.",
        "Explored HDBSCAN clustering — density reachability and minimum cluster size.",
        "Read about EfficientNet compound scaling — depth, width, and resolution coefficients.",
        "Studied ensemble diversity — why combining EfficientNet and ResNet improves recall.",
        "Reviewed t-SNE vs UMAP for high-dimensional embedding visualization.",
        "Analyzed feature engineering for time-series: rolling volatility and IQR transforms.",
    ]),
]

def get_entry_for_day(day_of_year: int) -> tuple[str, str]:
    """Pick a topic and note based on the day, cycling deterministically."""
    topic_idx = day_of_year % len(TOPICS)
    topic_name, notes = TOPICS[topic_idx]
    note_idx = (day_of_year // len(TOPICS)) % len(notes)
    return topic_name, notes[note_idx]

def main():
    today = datetime.date.today()
    day_of_year = today.timetuple().tm_yday
    year = today.year

    topic, note = get_entry_for_day(day_of_year + year)  # vary by year too

    entry = f"""
## {today.strftime('%B %d, %Y')} — {topic}

{note}

---
"""

    log_path = "dev_log.md"

    # Create file with header if it doesn't exist
    if not os.path.exists(log_path):
        header = """# Daily Dev Log

A running record of daily learning, exploration, and engineering notes.
Topics rotate across: Low-Latency Systems, Competitive Programming, AI/Agents, Quant/DeFi, Full Stack, and ML.

---
"""
        with open(log_path, "w") as f:
            f.write(header)

    # Append the new entry
    with open(log_path, "a") as f:
        f.write(entry)

    print(f"Logged entry for {today}: [{topic}] {note[:60]}...")

if __name__ == "__main__":
    main()
