import asyncio
import os
from dotenv import load_dotenv
from droidrun import AdbTools, DroidAgent
from llama_index.llms.google_genai import GoogleGenAI

# CONFIG
MODEL_NAME = "gemini-pro"  # Stable model
JOB_QUERY = "Data Science Intern"
MAX_JOBS = 5  # Increased slightly for better demo data

async def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Connect to Phone
    print("📱 Connecting to Android Device...")
    try:
        tools = AdbTools()
    except Exception as e:
        print(f"❌ Connection Failed: {e}. Did you run 'droidrun setup'?")
        return

    llm = GoogleGenAI(api_key=api_key, model=MODEL_NAME, temperature=0.0)

    # The Prompt
    mission_goal = f"""
    You are a Job Collector.
    1. Open "LinkedIn".
    2. Tap "Jobs".
    3. Search for "{JOB_QUERY}".
    4. Filter: Location "India", Date "Past Week".
    5. Scroll and identify {MAX_JOBS} distinct Company Names.
    6. OUTPUT FORMAT: Return ONLY a python list of strings. Example: ["Google", "TCS", "StartupX"]
    """

    agent = DroidAgent(goal=mission_goal, llm=llm, tools=tools, verbose=True)

    print(f"🤖 Scraping {MAX_JOBS} jobs from LinkedIn...")
    result = await agent.run()
    
    # Save Data
    output_text = str(result.get("output"))
    os.makedirs("data", exist_ok=True)
    
    with open("data/raw_jobs.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
        
    print("\n✅ SCRAPING COMPLETE!")
    print(f"📄 Data saved to data/raw_jobs.txt: {output_text}")

if __name__ == "__main__":
    asyncio.run(main())