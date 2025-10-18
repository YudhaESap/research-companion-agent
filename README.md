# Research Companion Agent
  
**Project Type:** OpenAI AgentKit / Research Automation Demo  
**Keywords:** Agentic AI · Scientific Automation · NLP · Research Workflow · GPT-5  

---

## Overview

**Research Companion Agent** is a lightweight demonstration of how the new [OpenAI Agent Builder](https://platform.openai.com/agent-builder) and `openai` Python SDK can automate structured research analysis.  

The prototype shows:
1. **Automated natural language reasoning** for extracting study designs and population features from abstracts.  
2. **Structured output generation** (JSON-like schema).  
3. **Creative writing test** via GPT-5-nano producing scientific or artistic micro-outputs such as haiku.

This project serves as an early step toward fully agentic, reproducible, and privacy-safe research pipelines for biomedical informatics and computational social science.

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YudhaESap/research-companion-agent.git
cd research-companion-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install openai
```

### 3. Set your OpenAI API key (do not hardcode it)

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 4. Run the demos
## Generate a Haiku

```bash
python3 haiku_test.py
```

## Example output:

```bash
Mist on quiet dawn
soft light in morning hush still
breath of a new day
```

## Research Information Extraction

```bash
python3 research_agent_test.py
```

## Example output:

```bash
{
  "study_design": "Prospective cohort study",
  "sample_size": 150,
  "population": {
    "age_range": "45-75",
    "sex_distribution": {
      "male_percent": 60,
      "female_percent": 40
    }
  },
  "key_outcomes": "Association between depression and cancer outcomes"
}
```

## Repository Structure

```bash
research-companion-agent/
├── haiku_test.py              # GPT-5-nano creative reasoning test
├── research_agent_test.py     # Research information extraction demo
├── .gitignore                 # Safe ignore rules for Python + OpenAI
└── README.md                  # Project documentation
```

## Scientific Motivation

This agent demonstrates how formalized natural language reasoning can support:
	•	Metadata extraction from real-world evidence (RWE) studies
	•	Study design classification
	•	Reproducible automation in biomedical literature reviews

It aligns with ongoing goals in AI safety and transparent scientific computation.

## Tech Stack

	•	Language Model: GPT-5-nano (via OpenAI Responses API)
	•	Language: Python 3.10+
	•	Environment: macOS / Linux / Windows (WSL)
	•	Core SDK: openai >= 2.0.0

## License
This repository is released under the MIT License.

## Citation

If you use this project or adapt its workflow for academic or open research, please cite as:

Saputra, Y. E. (2025). Research Companion Agent: A Lightweight Framework for Automated Study Extraction Using GPT-5.
GitHub repository: https://github.com/YudhaESap/research-companion-agent

## Future Work

Integration with OpenAI AgentKit for multi-tool reasoning
	•	Extension to structured systematic review parsing
	•	Addition of Gradio UI for demonstration
	•	Safe deployment on Myternet.com for federated academic agents


Maintainer: Author
