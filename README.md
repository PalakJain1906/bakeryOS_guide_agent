<img width="1877" height="852" alt="image" src="https://github.com/user-attachments/assets/2581eb14-cad3-4a98-a969-b5ca5f32a394" /># BakeryOS Guide Agent 🥐🔬

**BakeryOS** is an AI-powered technical consultant designed for home-based bakers and micro-entrepreneurs. It bridges the gap between complex food science and daily production, helping bakers understand the "why" behind their ingredients to create consistent, high-quality organic products.

## 🚀 Key Features
- **Scientific Deep-Dives:** Explains the chemistry of baking (e.g., hygroscopy, Maillard reaction).
- **Multi-Agent Orchestration:** Uses a specialized "Researcher" for facts and a "Head Baker" persona for professional advice.
- **Healthy Substitutions:** Provides data-driven guidance on organic and alternative ingredients.

## 🛠️ Tech Stack
- **Orchestration:** [Google ADK](https://github.com/google/adk) (Agent Development Kit)
- **Model:** Gemini 2.5 Flash via Vertex AI
- **Reasoning:** Sequential Agent Workflow (Root -> Researcher -> Formatter)
- **Tools:** Wikipedia API, Python, LangChain

## 🏗️ System Architecture
The system uses a **Sequential Logic** flow:
1. **Root Agent:** Analyzes the user's intent.
2. **Researcher Agent:** Performs real-time research using technical databases to verify ingredient properties.
3. **Formatter Agent:** Packages the scientific data into a warm, professional response tailored for a business owner.


## 🏃‍♂️ How to Run
1. Clone the repository.
2. Activate your virtual environment: `source .venv/bin/activate`
3. Set up your `.env` file with `PROJECT_ID` and `LOCATION`.
4. Run the web interface:
   ```bash
   adk web --allow_origins "*" ..
