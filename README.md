# PAPER-RUN
An automated AI agent that reads machine learning research papers, finds the corresponding GitHub implementation, and attempts to run the code automatically.

## ML Research Agent

An AI-powered research assistant that reads machine learning papers, identifies their implementation, and helps reproduce the method.

The agent analyzes research papers and:

- Finds the official GitHub implementation if available  
- Explains how to run the repository  
- Generates a custom implementation if no code exists  

This makes it easier to understand and reproduce machine learning research without manually digging through papers.

## Workflow
                ┌─────────────────────┐
                │  Research Paper PDF │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Text Extraction   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Document Chunking  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Vector Database   │
                │  (Semantic Search)  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     LLM Analysis    │
                └──────────┬──────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼

     ┌─────────────────────┐        ┌─────────────────────┐
     │ GitHub Repo Detected│        │  No Repo Detected   │
     └──────────┬──────────┘        └──────────┬──────────┘
                │                              │
                ▼                              ▼
     ┌─────────────────────┐        ┌─────────────────────┐
     │  Repository Analysis│        │ Method Understanding│
     └──────────┬──────────┘        └──────────┬──────────┘
                │                              │
                ▼                              ▼
     ┌─────────────────────┐        ┌─────────────────────┐
     │   Run Instructions  │        │  Script Generation  │
     └─────────────────────┘        └──────────┬──────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                                    │ Implementation Guide│
                                    └─────────────────────┘
