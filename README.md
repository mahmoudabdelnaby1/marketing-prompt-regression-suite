# Marketing Prompt Regression Testing Suite across LLM Version Upgrades

> Stop prompt drift after LLM API updates. Automate regression testing, JSON schema validation, and tone checks for marketing prompts.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source prompt regression testing framework for marketing teams (`prompt_eval_runner.py`): 1) Evaluates prompt outputs against strict assertions (Valid JSON schema, Max word count, Presence of required CTA, Absence of forbidden AI clichés like 'delve' or 'game-changer'), 2) Calculates semantic tone similarity against golden reference answers, 3) Terminal pass/fail test reports suitable for CI/CD.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `eval_suites/ad_copy_json_suite.json`
- `eval_suites/seo_meta_suite.json`
- `LICENSE`
- `README.md`
- `reports/sample_eval_report.html`
- `src/prompt_eval_runner.py`
- `tests/test_runner.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/prompt_eval_runner.py --help
```

### Interactive Browser Tool
Open `reports/sample_eval_report.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "career",
  "repository": "marketing-prompt-regression-suite",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Deterministic Evaluation Fixtures:** Runs assertions against LLM outputs across version upgrades to detect regression in tone, dialect, or factual accuracy.
- **Multi-Model Parity:** Evaluates prompt performance across GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro to identify breaking prompt behaviors.
- **Hallucination Score Bounds:** Quantifies factual consistency and flags forbidden promotional superlative claims.

---

## 📚 Primary Documentation & Verifiable References

- [OpenAI API Documentation: Model Evaluation & Prompt Governance](https://platform.openai.com/docs/guides/prompt-engineering) - Best practices for evaluating prompt repeatability and regression testing.
- [Anthropic Claude Documentation: Prompt Evaluation Strategies](https://docs.anthropic.com/) - Methodology for testing prompt robustness and measuring output drift.
- [ISO/IEC 25010: Software Quality Requirements and Evaluation](https://www.iso.org/standard/35733.html) - International standard for systems and software quality models and regression evaluation.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
