# LLM-Agent-work

A centralized repository for projects, experiments, research, tooling, prompts, agents, and workflows built with or around Large Language Models (LLMs).

This repository serves as my working environment for experimenting with AI systems including ChatGPT, Claude, Hermes, local LLMs, coding agents, automation frameworks, and related tools.

The goal is to maintain a structured and version-controlled collection of LLM-assisted work that can be reused, improved, and referenced over time.

## Purpose

`LLM-Agent-work` contains work involving:

- ChatGPT and OpenAI models
- Claude and Anthropic models
- Hermes and Hermes Agent
- Local LLMs
- AI agents and agentic workflows
- Prompt engineering
- Model testing and evaluation
- AI-assisted software development
- Automation
- Retrieval-Augmented Generation (RAG)
- Tool and API integrations
- Privacy-preserving AI workflows
- Cybersecurity-focused AI projects
- Research and experimentation

Projects in this repository may range from small proof-of-concept experiments to complete applications and production-oriented tooling.

## Repository Structure

The repository may evolve over time, but projects should generally follow a structure similar to:

```text
LLM-Agent-work/
├── agents/
│   ├── hermes/
│   ├── chatgpt/
│   ├── claude/
│   └── local/
│
├── projects/
│   ├── project-name/
│   └── another-project/
│
├── prompts/
│   ├── system-prompts/
│   ├── coding/
│   ├── cybersecurity/
│   ├── research/
│   └── templates/
│
├── experiments/
│   ├── model-comparisons/
│   ├── agent-tests/
│   └── prototypes/
│
├── tools/
│   ├── scripts/
│   ├── utilities/
│   └── integrations/
│
├── docs/
│   ├── architecture/
│   ├── research/
│   └── notes/
│
├── examples/
│
├── archive/
│
└── README.md
```

Not every directory must be used immediately. The structure is intended to provide logical separation as the repository grows.

## Project Organization

Individual projects should normally live under:

```text
projects/<project-name>/
```

A project can contain its own documentation and dependencies:

```text
projects/example-project/
├── README.md
├── docs/
├── src/
├── tests/
├── prompts/
├── config/
├── scripts/
├── examples/
└── requirements.txt
```

Each substantial project should include a project-level `README.md` explaining:

1. What the project does
2. Why it exists
3. Which LLMs or agents it uses
4. Installation requirements
5. Configuration
6. Usage
7. Security considerations
8. Current project status

## Agents

The `agents/` directory contains configuration, instructions, workflows, tools, and experimentation related specifically to AI agents.

Examples include:

- Hermes Agent configurations
- ChatGPT workflows
- Claude workflows
- Local agent implementations
- Tool-calling agents
- Multi-agent systems
- Delegation workflows
- Specialized cybersecurity agents

Agent-specific secrets, credentials, authentication tokens, or sensitive configuration must not be committed to the repository.

## Prompts

Reusable prompts should be stored under `prompts/`.

Prompts may include:

- System prompts
- Agent instructions
- Research prompts
- Coding prompts
- Cybersecurity analysis prompts
- SOC workflows
- Data analysis prompts
- Prompt templates
- Model-specific variants

Where useful, prompts should contain documentation describing their intended model, purpose, inputs, outputs, and known limitations.

## Experiments

The `experiments/` directory is intended for temporary or exploratory work such as:

- Model comparisons
- Prompt testing
- Benchmarking
- Context-window experiments
- RAG testing
- Agent behavior testing
- Tool-use experiments
- Quantization testing
- Local inference experiments

Experiments that mature into standalone tools or applications should eventually be moved into `projects/`.

## Documentation

Long-form documentation should be placed under `docs/`.

Examples include:

- Architecture diagrams
- Design decisions
- Research notes
- Deployment procedures
- Model evaluations
- Security assessments
- Integration documentation
- Lessons learned

Important architectural decisions should be documented rather than existing only in AI chat history.

## AI-Assisted Development

A significant portion of the code and documentation in this repository may be created or modified with assistance from LLMs.

Possible contributors include:

- OpenAI ChatGPT
- Anthropic Claude
- Hermes
- Local LLMs
- AI coding agents
- Other AI-assisted development tools

AI-generated code should be treated the same as code from any other source: it should be reviewed, tested, and validated before being trusted.

LLM output should not be assumed to be correct simply because it compiles or appears technically plausible.

## Security

Because this repository contains AI and cybersecurity-related experimentation, security is a primary consideration.

Do not commit:

- API keys
- Authentication tokens
- Passwords
- Private keys
- Certificates containing private material
- Production credentials
- Sensitive customer information
- Personally identifiable information
- Confidential SOC data
- Proprietary incident data
- Unredacted security logs
- Sensitive infrastructure details

Secrets should instead be stored using environment variables, secret-management systems, or files excluded through `.gitignore`.

Example:

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
HERMES_API_KEY=
```

A local `.env` file may be used where appropriate:

```text
.env
```

The `.env` file should never be committed.

## Privacy

Projects involving external or cloud-hosted LLMs should consider what information is being transmitted outside the local environment.

Sensitive data should be:

1. Removed when unnecessary
2. Sanitized when possible
3. Tokenized or pseudonymized where appropriate
4. Processed locally when confidentiality requirements demand it

Projects involving privacy gateways, data sanitization, or local LLM processing should document their trust boundaries and data flows.

## Local LLMs

Projects involving locally hosted models may include:

- llama.cpp
- Ollama
- vLLM
- Transformers
- GGUF models
- CUDA acceleration
- Vulkan acceleration
- CPU inference
- Hybrid local/cloud inference

Model files should generally not be committed to this repository because of their size.

Instead, project documentation should specify:

- Model name
- Model version
- Quantization
- Source
- Expected filename
- Hardware requirements
- Runtime configuration

## Configuration

Environment-specific configuration should be kept separate from source code whenever practical.

Example:

```text
config/
├── config.example.yaml
└── README.md
```

Sensitive configuration should remain outside version control.

## Testing

Projects should include automated tests whenever practical.

Depending on the project, testing may include:

- Unit tests
- Integration tests
- Prompt regression tests
- Agent behavior tests
- Security tests
- Input validation tests
- Privacy/sanitization tests
- Model output evaluations

LLM-based applications should account for nondeterministic behavior when designing test criteria.

## Git Practices

Commits should be focused and descriptive.

Example:

```text
feat: add local model delegation support
fix: prevent sensitive fields from being sent to cloud models
test: add privacy gateway redaction tests
docs: document Hermes agent configuration
refactor: separate model providers from agent logic
```

Recommended commit prefixes include:

```text
feat:
fix:
docs:
test:
refactor:
chore:
security:
experiment:
```

Large experiments should be isolated from stable projects whenever possible.

## Branching

For significant work:

```text
main
├── feature/<name>
├── fix/<name>
├── experiment/<name>
└── refactor/<name>
```

The `main` branch should ideally remain in a usable state.

## Project Status

This repository is an active working environment.

Projects may exist in different stages:

```text
Concept
Prototype
Experimental
Active Development
Stable
Maintenance
Archived
```

Individual project READMEs should identify their current status where useful.

## Philosophy

LLMs are tools, not authorities.

Outputs should be verified against:

- Source code
- Documentation
- Logs
- Primary sources
- Test results
- Vendor documentation
- Security controls
- Human review

The objective is not simply to generate more AI output, but to build reliable workflows where LLM capabilities can be used safely, efficiently, and reproducibly.

## License

Unless otherwise specified within an individual project, licensing information for this repository will be documented here once a repository-wide license is selected.

Third-party software, models, prompts, and datasets remain subject to their respective licenses and terms.

## Disclaimer

Projects in this repository may include experimental software, security tooling, AI-generated code, and research prototypes.

Code should be reviewed and tested before being deployed in production or trusted with sensitive information.
