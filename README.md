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

## 🌍 Real-Life Applications

InternShield is designed for immediate, practical use in real-world job hunting scenarios:

- **Students & Fresh Graduates**  
  Quickly filter out fake internships before wasting time on applications or interviews.

- **College Placement Cells**  
  Pre-screen internship opportunities shared with students to ensure only legitimate roles are circulated.

- **Career Counselors & NGOs**  
  Assist first-time job seekers and underrepresented groups in avoiding exploitative hiring practices.

- **High-Volume Job Hunters**  
  Reduce manual verification effort when applying to dozens of roles across different companies.

- **Parental & Guardian Oversight**  
  Provide an additional layer of trust for families evaluating internship offers received by students.

## 🚀 Future Extensions

InternShield is built to scale beyond its initial use case:

- **Multi-Role Support**  
  Extend searches to any role (software, design, marketing, finance, operations) by changing the query.

- **Multi-Platform Scraping**  
  Support additional job platforms such as Internshala, Indeed, company career pages, and startup portals.

- **Continuous Monitoring**  
  Schedule daily or weekly scans to detect new postings and flag risky companies early.

- **Shared Scam Intelligence**  
  Build a community-maintained blacklist or safety score database for companies.

- **Resume-Safe Automation**  
  Integrate a verification-first workflow where applications are submitted only after legitimacy checks.

- **Regional Scam Pattern Detection**  
  Identify location-specific scam behaviors and adapt rules dynamically.

- **Browser or Mobile Companion App**  
  Provide real-time warnings while users browse job listings manually.

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

