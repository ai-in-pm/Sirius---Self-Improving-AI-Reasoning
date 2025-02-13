# Self-improving Multi-agent System

A collaborative AI system inspired by Stanford's SiriuS framework, featuring six specialized AI agents working together to solve complex problems across various domains.

The development of this repository was inspired by the "SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning" paper. To read the entire paper, visit https://arxiv.org/pdf/2502.04780?.

## System Architecture

The system consists of six PhD-level expert agents:
1. Lead Problem Solver - Generates initial solutions
2. Critic Agent - Provides constructive criticism
3. Judgment Agent - Verifies facts and logic
4. Strategist Agent - Considers long-term implications
5. Data Augmentor - Learns from mistakes and refines solutions
6. Consensus Builder - Synthesizes final recommendations

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env` file with your API keys:
- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- GROQ_API_KEY
- GOOGLE_API_KEY
- COHERE_API_KEY
- EMERGENCEAI_API_KEY

## Usage

Run the system:
```bash
python main.py
```

## Features

- Real-time agent interaction and collaborative reasoning
- Multi-domain adaptability
- Iterative self-improvement
- Strategic decision-making
- Interactive user engagement

## Project Structure

```
.
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── lead_solver.py
│   └── [other agent implementations]
├── main.py
├── requirements.txt
└── .env
```

## Security Note

API keys are stored in the `.env` file and should never be committed to version control. Make sure to keep your `.env` file secure and private.
