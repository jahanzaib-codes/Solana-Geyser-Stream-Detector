# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-13

### Added
- **Yellowstone gRPC Streaming Ingestion**:
  - Direct Geyser transaction log decoding at sub-5ms latency.
  - Multi-DEX genesis support: Raydium CPMM, Raydium AMMv4, and Pump.fun bonding curves.
- **Sub-Millisecond Anti-Rug Pre-Auditing**:
  - Freeze authority and mint authority revocation detection.
  - LP burn percentage threshold monitoring.
  - Developer wallet concentration and cabal supply alerts.
- **Jito MEV Routing Bridge**:
  - Automated dynamic tip ladder calculation for front-of-block bundle inclusion.
  - Interactive Click CLI and dual-matrix CI/CD via GitHub Actions.
