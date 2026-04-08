---
title: Email Triage V1
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Email AI — OpenEnv Submission

An AI agent that classifies and replies to emails across three difficulty tiers using a Qwen 72B model via Hugging Face Inference Router.

## Project Structure

email_ai_project/
├── app.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── validate.sh
├── env/
│   ├── __init__.py
│   ├── models.py
│   ├── email_env.py
│   ├── reward.py
│   └── tasks.py
└── dashboard/
    └── index.html

## Quick Start

export HF_TOKEN=your_huggingface_token
export MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
python app.py
