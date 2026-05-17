import os
import json
import urllib.request
import xml.etree.ElementTree as ET
import math
import subprocess
from datetime import datetime

class AutopilotProductionEngine:
    """
    Sovereign Predictive SEO Engine.
    1. Scrapes real-time trending indicators.
    2. Calculates B2B Commercial Feasibility scores.
    3. Auto-compiles responsive, light HTML landing portals.
    4. Auto-commits and pushes code directly to GitHub.
    """
    def __init__(self, output_dir: str = "production_sites", ledger_file: str = "predictive_ledger.json"):
        self.output_dir = output_dir
        self.ledger_file = ledger_file
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        self.ledger = self._load_ledger()

    def _load_ledger(self) -> dict:
        if os.path.exists(self.ledger_file):
            try:
                with open(self.ledger_file, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "active_portals": {},
            "cumulative_projected_value": 0.0,
            "last_prediction_cycle": None
        }

    def _save_ledger(self):
        with open(self.ledger_file, 'w') as f:
            json.dump(self.ledger, f, indent=4)

    def fetch_live_signals(self) -> list:
        print("[Predictive Engine] Ingesting search trend indicators...")
        raw_signals = []
        feed_url = "https://trends.google.com/trending/rss?geo=US"
        
        try:
            req = urllib.request.Request(
                feed_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read()
                
            root = ET.fromstring(xml_data)
            for item in root.findall('.//item'):
                title = item.find('title')
                approx_traffic = item.find('{ht}approx_traffic')
                
                title_text = title.text if title is not None else ""
                traffic_text = approx_traffic.text if approx_traffic is not None else "20,000+"
                
                if title_text:
                    raw_signals.append({
                        "keyword": title_text.strip(),
                        "volume_raw": traffic_text.strip()
                    })
        except Exception as e:
            print(f"[Notice] Direct trend feed offline/rate-limited. Deploying high-yield B2B nodes...")
            raw_signals = [
                {"keyword": "B2B AI Automation Agent", "volume_raw": "50,000+"},
                {"keyword": "Decentralized Database Hosting", "volume_raw": "100,000+"},
                {"keyword": "Local SEO No Code Pipeline", "volume_raw": "20,000+"},
                {"keyword": "Zero Latency Voice Synthesis", "volume_raw": "75,000+"}
            ]
        return raw_signals

    def calculate_predictive_score(self, keyword: str, raw_volume: str) -> dict:
        clean_vol = raw_volume.replace("+", "").replace(",", "")
        try:
            volume_scalar = float(clean_vol)
        except ValueError:
            volume_scalar = 20000.0

        base_volume_weight = math.log10(max(volume_scalar, 100))
        commercial_modifier = 1.0
        
        niche_keywords = {
            "ai": 2.5, "agent": 2.2, "automation": 2.0, "hosting": 1.9,
            "database": 1.8, "security": 2.1, "cloud": 1.7, "b2b": 2.4, "api": 2.3
        }
        
        for term, multiplier in niche_keywords.items():
            if term in keyword.lower():
                commercial_modifier += multiplier

        urgency_factor = 1.2 if len(keyword.split()) >= 3 else 1.0
        predictive_score = base_volume_weight * commercial_modifier * urgency_factor
        
        projected_payout = 45.00
        if commercial_modifier > 3.0:
            projected_payout = 150.00
        elif commercial_modifier > 2.0:
            projected_payout = 75.00

        return {
            "keyword": keyword,
            "score": round(predictive_score, 2),
            "estimated_payout": projected_payout,
            "niche_bracket": "B2B Infrastructure" if commercial_modifier > 2.0 else "General High-Yield"
        }

    def compile_production_html(self, evaluation: dict) -> str:
        kw = evaluation["keyword"]
        payout_tier = evaluation["estimated_payout"]
        
        border_color = "border-emerald-500/30" if payout_tier >= 100 else "border-indigo-500/30"
        bg_accent = "bg-emerald-950/20" if payout_tier >= 100 else "bg-indigo-950/20"
        text_accent = "text-emerald-400" if payout_tier >= 100 else "text-indigo-400"

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Index - {kw}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-black text-zinc-100 min-h-screen font-sans flex flex-col justify-between">
    <header class="border-b border-zinc-900 p-5 bg-zinc-950/50 backdrop-blur">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <h1 class="font-bold text-xs tracking-widest text-white uppercase">Sovereign Asset Node</h1>
            <span class="text-xs text-zinc-500">System Live</span>
        </div>
    </header>

    <main class="max-w-4xl mx-auto p-6 w-full flex-grow">
        <div class="my-14 text-center">
            <span class="text-xs font-bold {text_accent} tracking-widest uppercase">Autonomous Directory Portal</span>
            <h2 class="text-4xl font-extrabold mt-3 mb-4 text-white">Top Vetted {kw} Directory</h2>
            <p class="text-zinc-400 text-sm max-w-xl mx-auto">This portal ranks programmatically on Google search engines to route traffic into high-converting recurring software commissions.</p>
        </div>

        <div class="grid gap-6 md:grid-cols-3">
            <div class="bg-zinc-900 border {border_color} p-5 rounded-2xl flex flex-col justify-between hover:scale-[1.01] transition-all duration-300">
                <div>
                    <span class="text-xs {text_accent} {bg_accent} border {border_color} px-2.5 py-1 rounded-md font-semibold">Primary Platform</span>
                    <h3 class="text-lg font-bold mt-4 mb-2 text-white">{kw} Core</h3>
                    <p class="text-xs text-zinc-400 mb-6">Fully optimized runtime integration built for enterprise scale operations.</p>
                </div>
                <div class="border-t border-zinc-800 pt-4">
                    <div class="flex justify-between text-[11px] mb-3">
                        <span class="text-zinc-500">Affiliate Payout:</span>
                        <span class="{text_accent} font-bold">${payout_tier:,.2f} Recurring</span>
                    </div>
                    <a href="https://elevenlabs.io" target="_blank" class="block w-full text-center bg-zinc-850 hover:bg-white hover:text-black text-white font-bold py-2 rounded-xl text-xs transition duration-200">Get Integration Link ↗</a>
                </div>
            </div>

            <div class="bg-zinc-900 border border-zinc-800 p-5 rounded-2xl flex flex-col justify-between hover:scale-[1.01] transition-all duration-300">
                <div>
                    <span class="text-xs text-zinc-400 bg-zinc-800 border border-zinc-700 px-2.5 py-1 rounded-md font-semibold">Infrastructure</span>
                    <h3 class="text-lg font-bold mt-4 mb-2 text-white">Database Router</h3>
                    <p class="text-xs text-zinc-400 mb-6">Ultra-low latency database backplane optimized for scalable SaaS applications.</p>
                </div>
                <div class="border-t border-zinc-800 pt-4">
                    <div class="flex justify-between text-[11px] mb-3">
                        <span class="text-zinc-500">Affiliate Payout:</span>
                        <span class="text-zinc-300 font-bold">$150.00 Flat Fee</span>
                    </div>
                    <a href="https://kinsta.com" target="_blank" class="block w-full text-center bg-zinc-850 hover:bg-white hover:text-black text-white font-bold py-2 rounded-xl text-xs transition duration-200">Get Integration Link ↗</a>
                </div>
            </div>

            <div class="bg-zinc-900 border border-zinc-800 p-5 rounded-2xl flex flex-col justify-between hover:scale-[1.01] transition-all duration-300">
                <div>
                    <span class="text-xs text-zinc-400 bg-zinc-800 border border-zinc-700 px-2.5 py-1 rounded-md font-semibold">Automation</span>
                    <h3 class="text-lg font-bold mt-4 mb-2 text-white">Workflow Pipeline</h3>
                    <p class="text-xs text-zinc-400 mb-6">Autonomous webhooks and data syncs executing completely hands-free.</p>
                </div>
                <div class="border-t border-zinc-800 pt-4">
                    <div class="flex justify-between text-[11px] mb-3">
                        <span class="text-zinc-500">Affiliate Payout:</span>
                        <span class="text-zinc-300 font-bold">20% Monthly Rev-Share</span>
                    </div>
                    <a href="https://make.com" target="_blank" class="block w-full text-center bg-zinc-850 hover:bg-white hover:text-black text-white font-bold py-2 rounded-xl text-xs transition duration-200">Get Integration Link ↗</a>
                </div>
            </div>
        </div>
    </main>

    <footer class="border-t border-zinc-900 p-6 text-center text-xs text-zinc-600">
        <p>© Sovereign Arbitrage Hub. Hosted serverlessly, running indefinitely on autopilot.</p>
    </footer>
</body>
</html>"""

    def push_to_github(self):
        try:
            result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
            if result.returncode != 0:
                print("[Autopilot Notice] Remote 'origin' not linked yet. Bypassing GitHub push...")
                return
            
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto-update: Fresh SEO Trends added"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("[Autopilot Git] Push success! Live pages updated on GitHub.")
        except Exception as e:
            print(f"[Autopilot Notice] Git sync skipped: {e}")

    def run_cycle(self, limit: int = 5):
        print(f"\n--- Autopilot Run Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
        
        signals = self.fetch_live_signals()
        evaluations = []
        
        for sig in signals:
            eval_data = self.calculate_predictive_score(sig["keyword"], sig["volume_raw"])
            evaluations.append(eval_data)
            
        evaluations.sort(key=lambda x: x["score"], reverse=True)
        target_evals = evaluations[:limit]
        
        for idx, eval_item in enumerate(target_evals, 1):
            kw = eval_item["keyword"]
            slug = kw.lower().replace(" ", "-").replace("/", "-")
            
            page_html = self.compile_production_html(eval_item)
            file_name = f"{slug}.html"
            file_path = os.path.join(self.output_dir, file_name)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(page_html)
                
            if slug not in self.ledger["active_portals"]:
                self.ledger["active_portals"][slug] = {
                    "keyword": kw,
                    "file": file_path,
                    "payout_tier": eval_item["estimated_payout"],
                    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.ledger["cumulative_projected_value"] += eval_item["estimated_payout"]
                
        self.ledger["last_prediction_cycle"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_ledger()
        
        self.push_to_github()
        print(f"--- Autopilot Run Complete. Total Assets Listed: {len(self.ledger['active_portals'])} | Est. Monthly Value: ${self.ledger['cumulative_projected_value']:,.2f} ---")

if __name__ == "__main__":
    engine = AutopilotProductionEngine()
    engine.run_cycle(limit=5)
