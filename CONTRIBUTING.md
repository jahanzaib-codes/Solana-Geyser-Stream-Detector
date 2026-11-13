# Contributing to Solana-Geyser-Stream-Detector

Thank you for your interest in contributing to **Solana-Geyser-Stream-Detector**. This project provides sub-millisecond Yellowstone gRPC streaming, Raydium/Pump.fun genesis pair decoding, and automated honeypot auditing for Solana.

## Guidelines

1. **Code Standards**:
   - Write clean, type-annotated Python 3.10+ compliant code.
   - Use `pydantic` schemas for data models.
   - Maintain static analysis compliance: zero warnings under `flake8`.
2. **Commit Conventions**:
   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat(...)`: New features
   - `fix(...)`: Bug fixes
   - `docs(...)`: Documentation updates
   - `infra(...)`: CI/CD or Docker configurations
3. **Pull Request Workflow**:
   - Run `python cli.py demo` locally before submitting PRs.
   - Ensure zero warnings under `flake8`.
