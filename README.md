# AI-Powered SDLC Automation using LangGraph

An AI-powered Software Development Life Cycle (SDLC) automation platform built using **LangGraph**, **FastAPI**, **OpenRouter**, and **Mem0**.

This project simulates a complete software development lifecycle where multiple AI agents collaborate to transform software requirements into deployable project artifacts while performing iterative reviews, security analysis, testing, and deployment recommendations.

---

# Features

- AI Requirement Analysis
- Agile User Story Generation
- Product Owner Review & Revision
- Software Design Document Generation
- AI Design Review
- Project Skeleton Code Generation
- AI Code Review
- Security Review
- Automated Security Fix Suggestions
- Test Case Generation
- AI Test Case Review
- QA Testing
- Deployment Recommendation
- Long-Term Memory using Mem0
- LangGraph State Machine Workflow
- REST API using FastAPI
- OpenRouter LLM Integration

---

# Workflow

```text
Requirements
      │
      ▼
User Story Generation
      │
      ▼
Product Owner Review
      │
      ├──────────────┐
      ▼              │
Revise Stories ◄─────┘
      │
      ▼
Design Generation
      │
      ▼
Design Review
      │
      ├──────────────┐
      ▼              │
Revise Design ◄──────┘
      │
      ▼
Code Generation
      │
      ▼
AI Code Review
      │
      ├──────────────┐
      ▼              │
Revise Code ◄────────┘
      │
      ▼
Security Review
      │
      ├──────────────┐
      ▼              │
Fix Security ◄───────┘
      │
      ▼
Generate Test Cases
      │
      ▼
Test Case Review
      │
      ├──────────────┐
      ▼              │
Revise Test Cases ◄──┘
      │
      ▼
QA Testing
      │
      ▼
Deployment Recommendation
```

---

# AI Agents

- Requirement Analyst
- Product Owner
- Software Architect
- Design Reviewer
- Backend Developer
- Code Reviewer
- Security Engineer
- Security Fix Agent
- Test Case Generator
- QA Engineer
- Deployment Advisor

---

# Tech Stack

## Backend

- Python
- FastAPI

## AI Framework

- LangGraph
- LangChain
- OpenRouter
- Mem0

## LLM

- OpenRouter Models

## Validation

- Pydantic

## Environment Management

- python-dotenv

---

# Long-Term Memory (Mem0)

The project integrates **Mem0** to provide persistent memory across workflow executions.

Current implementation includes:

- Storing project requirements
- Retrieving relevant memories before User Story Generation
- Retrieving relevant memories before Design Generation

This enables the AI agents to maintain contextual awareness across multiple software development sessions.

---

# API

### Run Workflow

**POST**

```
/run
```

Example Request

```json
{
    "requirements": "Build a Bank Management System"
}
```

---

# Example Output

The workflow generates:

- Agile User Stories
- Software Design Document
- Project Skeleton
- Code Review Feedback
- Security Review Report
- Generated Test Cases
- QA Testing Report
- Deployment Recommendation

---

# Deployment Recommendation

The workflow recommends deployment platforms such as:

- Vercel
- Render
- Railway
- AWS
- Azure

---

# Future Improvements

- LangGraph Checkpointer
- Thread-based Conversations
- Resume Workflow
- Human-in-the-loop Interrupts
- Multi-user Support
- Docker Support
- CI/CD Integration
- Code Execution Sandbox
- Automated Documentation Generation

---

# Why This Project?

This project demonstrates how multiple AI agents can collaboratively automate different phases of the Software Development Life Cycle using a state-driven workflow.

It showcases:

- Agentic AI
- Multi-Agent Systems
- LangGraph State Machines
- Prompt Engineering
- Long-Term Memory with Mem0
- AI-Powered Code Review
- Security Analysis
- Automated Testing
- End-to-End SDLC Automation

---

# Author

**Rishu Raj**
