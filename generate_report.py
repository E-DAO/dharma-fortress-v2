import json
from fpdf import FPDF
from datetime import datetime

SUMMARY_PATH = "simulation_summary.json"
LOG_PATH = "attack_log.json"
OUTPUT_PDF = "YinYang_Simulation_Report.pdf"

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Yin Yang Deception Simulation Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_report():
    try:
        with open(SUMMARY_PATH, "r") as f:
            summary = json.load(f)
    except FileNotFoundError:
        print("❌ No simulation_summary.json found.")
        return

    try:
        with open(LOG_PATH, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        print("❌ No attack_log.json found.")
        return

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    mode = summary.get("mode", "SIMULATION").upper()
    label = "🧪 SIMULATION MODE" if mode == "SIMULATION" else "⚠️ LIVE SYSTEM MODE"
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(0, 0, 255) if mode == "SIMULATION" else pdf.set_text_color(220, 50, 50)
    pdf.cell(0, 10, f"Mode: {label}", ln=True)
    pdf.set_text_color(0, 0, 0)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Generated: {datetime.utcnow().isoformat()}", ln=True)
    pdf.cell(0, 10, f"Total Attacks: {summary['total_attacks']}", ln=True)
    pdf.cell(0, 10, f"Blocked: {summary['blocked']}", ln=True)
    pdf.cell(0, 10, f"Bypassed: {summary['bypassed']}", ln=True)
    pdf.cell(0, 10, f"Trap Triggered: {summary['trap_triggered']}", ln=True)
    pdf.cell(0, 10, f"Escalated: {summary['escalated']}", ln=True)
    pdf.cell(0, 10, f"Mean Detection Time: {summary['mean_detection_time_ms']} ms", ln=True)
    pdf.cell(0, 10, f"DAO Recommendation: {summary['dao_recommendation']}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sample Attack Logs:", ln=True)
    pdf.set_font("Arial", "", 11)

    for entry in logs[:5]:
        line = f"{entry['timestamp']} | {entry['attacker']} | {entry['attack_type']} -> {entry['result']}"
        pdf.cell(0, 10, line, ln=True)

    pdf.output(OUTPUT_PDF)
    print(f"✅ Report generated: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_report()