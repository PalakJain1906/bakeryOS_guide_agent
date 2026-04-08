# BakeryOS Guide Agent 🧁

An AI-powered technical assistant for home-based organic bakers, built for the Gen AI Academy APAC Edition.

## How it Works
BakeryOS uses a **Sequential Agent Workflow** to bridge the gap between food science and the kitchen:
- **The Researcher:** Uses Wikipedia to find the scientific "why" behind ingredients.
- **The Formatter:** Translates technical data into a professional "Head Baker" persona.

## Tech Stack
- **Google ADK:** Multi-agent orchestration.
- **Gemini 2.5 Flash:** High-speed reasoning engine.
- **LangChain:** Tool integration for real-time research.

## Setup
1. Clone the repo.
2. Create a `.env` file with your `PROJECT_ID`.
3. Run `python agent.py`.
   
## 🏗️ System Architecture
The system uses a **Sequential Logic** flow:
1. **Root Agent:** Analyzes the user's intent.
2. **Researcher Agent:** Performs real-time research using technical databases to verify ingredient properties.
3. **Formatter Agent:** Packages the scientific data into a warm, professional response tailored for a business owner.

<img width="1827" height="842" alt="image" src="https://github.com/user-attachments/assets/7f9f1b99-109f-48bd-b5e6-b58d3ce51ad3" />

## 🏃‍♂️ How to Run
1. Clone the repository.
2. Activate your virtual environment: `source .venv/bin/activate`
3. Set up your `.env` file with `PROJECT_ID` and `LOCATION`.
4. Run the web interface:
   ```bash
   adk web --allow_origins "*" ..
