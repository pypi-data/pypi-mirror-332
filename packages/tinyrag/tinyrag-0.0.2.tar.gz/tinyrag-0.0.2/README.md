<div align="center">
  <h1>tinyrag</h1>
  <p>Lightweight RAG implementation for all your LLM endpoints</p>
 <img src="https://raw.githubusercontent.com/divine-architect/tinyrag/refs/heads/main/tinyrag.png" width="300" alt="tinyrag logo">
  
</div>

## About
tinyrag is a "tiny" RAG implementation that aims to give developers a plug and play experience while writing RAG applications.
It aims to be compatible with major LLM providers and be as tiny (as the name suggests) as possible while doing so.

## Usage
Before you run tinyrag make sure you have pulled the following models from the ollama repo:
- [Nomic Text Embeddings](https://ollama.com/library/nomic-embed-text)
- Any large language model of your choice from the ollama library

Install using pip: 
```sh
pip install tinyrag
```

Example usage:
```python
from tinyrag.tinyrag import TinyRAG_Ollama

rag = TinyRAG_Ollama(llm_model='llama3.2:1b')

sample_docs = [ # made up info, pass any text here
    "Zephyr Quantum was founded in 2023 by Dr. Voss in Maple Ridge, BC.",
    "QuantumShield 3.0 launched January 2025 with 512-bit encryption.",
    "Board: Dr. Voss (CEO), Chen (CTO), Karim (CFO), plus 3 non-execs.",
    "Series B: $42M in October 2024 from Horizon, Quantum Capital, TechFusion.",
    "78 employees across Maple Ridge, Singapore, Zurich. 120 planned by end of 2025.",
    "Competitors: QuantumWall (US), SecureFuture (Germany), NexGen (Israel).",
    "Q4 2024: $8.7M revenue, up 34%. 2025 projection: $45-50M.",
    "Project Aurora: quantum-resistant IoT protocol in development.",
    "Clients: 2 Fortune 500 banks, 3 govt agencies, healthcare providers. Largest: GlobalBank.",
    "17 patents filed, 9 granted as of January 2025."
]

rag.add_documents(sample_docs) # add custom instructions to the LLM here if required
result = rag.query("What's Zephyr Quantums largest client? and give me more info about who their other clients are, be super verbose about it (do not makeup info and stick to the context)")
print(result)
```

## Current features:
- Uses [nomic text embeddings](https://ollama.com/library/nomic-embed-text) as the embedding model via ollama
- Is currently compatible with any model available on [Ollama](https://ollama.com/search)

## Planned features/Roadmap
- Add support to more embedding models
- Currently only plaintext documents are supported, so support for database files, spreadsheets, documents, ppts, etc
- Support more endpoints such as Open AI, Claude, Deepseek, etc
- Multimodal embedding support
- Chroma DB/Custom Vector DBs support
- Implement FAISS from scratch

## Contribution | Issues/Bug reports
Contributions are always welcome! Make sure to test your forks before making a PR. \
Open an issue for Bug reports or to report other issues

## License
This project is licensed under the [MIT license](https://opensource.org/license/MIT)
