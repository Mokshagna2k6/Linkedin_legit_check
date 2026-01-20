# Linkedin_legit_check

# 🛡️ InternShield: The Anti-Scam Job Agent

> **"Stop paying to work. Start getting hired."**
> A DroidRun agent that scrapes LinkedIn and filters out "Pay-to-Intern" scams using AI.

## 🚨 The Problem
Finding an internship in India is broken.
- **70% of "Internships"** are actually training institutes asking for money.
- Students waste hours applying to scams that ask for **registration fees** or **security bonds**.
- Manual verification takes too long.

## 💡 The Solution
**InternShield** is an autonomous agent that:
1.  **Scrapes** live listings from the LinkedIn Android App.
2.  **Cross-references** companies against known scam patterns (Reddit/Glassdoor data).
3.  **Generates** a "Safe List" of legitimate opportunities.

## 🔄 How It Works
```mermaid
graph TD
    subgraph "Phase 1: Extraction (Android)"
        A[Start Agent] -->|ADB Connection| B[Phone: Open LinkedIn]
        B --> C[Search 'Data Science Intern']
        C --> D[Scroll & Capture Company Names]
        D --> E[Save to 'raw_jobs.txt']
    end

    subgraph "Phase 2: Forensic Analysis (Gemini AI)"
        E --> F[Read Company List]
        F --> G{Check Scam Indicators}
        G -->|Check 1| H[Registration Fees?]
        G -->|Check 2| I[Unpaid/Bond?]
        G -->|Check 3| J[Reddit Reviews]
        J --> K[Generate Safety Score]
    end

    subgraph "Phase 3: Result"
        K --> L[Output 'safe_leads.md']
    end
    
    style G fill:#ffcccc,stroke:#ff0000
    style L fill:#ccffcc,stroke:#00ff00

