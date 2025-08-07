# GenAI Projects [![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/release/python-310/) 

This repository contains a collection of generative AI experiments and implementations using modern LLM frameworks and APIs. The focus is on building practical applications and experimenting with language model chaining, prompt engineering, and serving models via APIs and web interfaces.

## Table of Contents
- [Projects](#projects)
  - [1. ChatBot](#1-chatbot)
  - [2. LCEL (Lightweight Language Chain Experiment)](#2-lcel-lightweight-language-chain-experiment)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
- [Models Used](#models-used)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Projects

### 1. ChatBot
#### Description
A conversational chatbot built with [Streamlit](https://streamlit.io/) and [LangChain](https://python.langchain.com/), designed to answer user questions interactively.

#### Features
- Environment variable configuration for secure API key management
- Message history tracking for conversational context
- API response handling and error management
- Multiple chat format compatibility
- Simple and interactive web UI via Streamlit

#### Requirements
- Python 3.9+
- Streamlit
- LangChain
- Ollama integration

#### Usage
1. Install dependencies:
   ```bash
   pip install -r ChatBot/requirements.txt
   ```
2. Configure environment variables:
   ```bash
   export OLLAMA_API_KEY=your_api_key_here
   ```
3. Run the application:
   ```bash
   streamlit run ChatBot/app.py
   ```

### 2. LCEL (Lightweight Language Chain Experiment)
#### Description
Experiments with language model chaining and prompt templates using [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/).

#### Features
- Translation functionality using prompt templates and chained components
- Language model chaining with output parsing
- Prompt engineering and message chain implementation
- REST API serving with [LangServe](https://github.com/langchain-ai/langserve) and FastAPI

#### Requirements
- Python 3.9+
- FastAPI
- LangChain
- Groq API integration

#### Usage
1. Install dependencies:
   ```bash
   pip install -r LCEL/requirements.txt
   ```
2. Configure environment variables:
   ```bash
   export GROQ_API_KEY=your_api_key_here
   ```
3. Run the API server:
   ```bash
   uvicorn LCEL.serve:app --reload
   ```

## Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package installer
- Git for version control
- (Optional) Docker for containerization

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GenAI-Projects.git
   cd GenAI-Projects
   ```

2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Set up environment variables:
   - For ChatBot:
     ```bash
     export OPENAI_API_KEY=your_openai_key_here
     ```
   - For LCEL:
     ```bash
     export GROQ_API_KEY=your_groq_key_here
     ```

2. (Optional) Create a `.env` file in the root directory:
   ```bash
   echo "OPENAI_API_KEY=your_openai_key_here" > .env
   echo "GROQ_API_KEY=your_groq_key_here" >> .env
   ```

### Usage
- **ChatBot:**
  ```bash
  streamlit run ChatBot/app.py
  ```
- **LCEL:**
  ```bash
  uvicorn LCEL.serve:app --reload
  ```

## Models Used
- **ChatBot:**
  - Gemma-2b (via Ollama)
    - Used for conversational interactions
    - Local inference for privacy and speed
- **LCEL:**
  - Gemma-2-9b-It (via Groq)
    - Used for language translation and processing
    - High-performance implementation

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you have a suggestion, improvement, or bug fix, please:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure all contributions adhere to the [Contributor Code of Conduct](CODE_OF_CONDUCT.md).

## Contact
For questions, suggestions, or feedback, please reach out to:
- Email: your.email@example.com
- Twitter: [@yourhandle](https://twitter.com/yourhandle)
- GitHub: [yourusername](https://github.com/yourusername)

## Acknowledgments
- Inspired by the [LangChain](https://python.langchain.com/) community and their innovative approaches to language model applications.
- Special thanks to the developers of [Streamlit](https://streamlit.io/) and [FastAPI](https://fastapi.tiangolo.com/) for their excellent frameworks.

