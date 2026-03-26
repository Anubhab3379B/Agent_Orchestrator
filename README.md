# Unified Passive Income Operating System (UPIS)

This directory serves as the technical backbone for the multi-agent passive income network.

## System Architecture

The network consists of three specialized agents coordinated by a central orchestrator:

1.  **Content-Commerce Arbitrage Agent**: Viral distribution.
2.  **Digital Asset Factory Agent**: High-volume creation.
3.  **Ecom Scale Automation Agent**: Arbitrage Scaling.

## Getting Started

1.  **Environment Setup**:
    - Install Python 3.9+.
    - Run `pip install pyyaml requests`.
2.  **Configuration**:
    - Update `config.yaml` with your preferred niches and targets.
    - Set environment variables for your API keys (`OPENAI_API_KEY`, `PINTEREST_ACCESS_TOKEN`, etc.).
3.  **Launch**:
    - Run `python core_orchestrator.py` to start the central sync loop.

## Inter-Agent Synergies
- **Factory -> Content**: The Digital Asset Factory pushes new design templates to the Content Agent for marketing.
- **Ecom -> Content**: The Ecom Agent reports trending products to the Content Agent for rapid video creation.
- **Performance Feedback**: The Orchestrator collects click/conversion data to pivot agents toward more profitable niches.
