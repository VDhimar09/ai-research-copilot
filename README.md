<!-- @format -->

# Mini Co-Analyst

A small interview-practice project inspired by the architecture described for ExTrac's Co-Analyst.

## Current Features

- FastAPI backend
- Health check endpoint
- Research API endpoint
- Simple document retrieval
- Keyword-based document matching
- Basic research service
- Simple retrieval testing

## Current Architecture

```text
POST /research
      |
      v
Research Service
      |
      v
Document Retriever
      |
      v
Research Documents
```
