import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI

def analyze_jobs():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    llm = GoogleGenAI(api_key=api_key, model="gemini-pro", temperature=0.1)

    # 1. Load Raw Data
    try:
        with open("data/raw_jobs.txt", "r", encoding="utf-8") as f:
            raw_companies = f.read()
    except FileNotFoundError:
        print("❌ Error: Run scraper.py first to generate data.")
        return

    print(f"🕵️ Analyzing Companies for Scam Indicators: {raw_companies} ...")

    # 2. The Forensic Prompt
    prompt = f"""
    I am a student looking for a legitimate Data Science internship.
    Here is a list of companies I scraped from LinkedIn: {raw_companies}

    TASK:
    Analyze each company based on your training data (Reddit, Glassdoor, News) for "Scam Indicators".
    
    SCAM INDICATORS (Red Flags):
    - "Pay to work" / Registration Fees
    - "Unpaid training" disguised as internship
    - "Security Bond" requirements
    - History of fake job postings
    
    OUTPUT FORMAT (Markdown Table):
    | Company | Legitimacy Score (1-10) | Verdict | Reason/Red Flags |
    | :--- | :---: | :--- | :--- |
    | [Name] | [Score] | [SAFE / RISKY / AVOID] | [Short Explanation] |

    After the table, provide a "Safe List" of companies I should actually apply to.
    """

    # 3. AI Analysis
    response = llm.complete(prompt)

    # 4. Save Final Report
    os.makedirs("data", exist_ok=True)
    with open("data/safe_leads.md", "w", encoding="utf-8") as f:
        f.write("# 🛡️ InternShield Safety Report\n")
        f.write(response.text)
        
    print("\n✅ ANALYSIS COMPLETE!")
    print("📄 Report saved to data/safe_leads.md")
    print("-" * 30)
    print(response.text)

if __name__ == "__main__":
    analyze_jobs()