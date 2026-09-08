# AutoCodeGPT

> A multi-agent coding system that generates, executes, validates, and iteratively improves Python solutions using Microsoft AutoGen and Docker-based code execution.

AutoCodeGPT is an experimental Generative AI project built to explore how specialized AI agents can collaborate on programming problems rather than relying on a single LLM response.

The system separates **problem solving** from **code execution**, allowing one agent to reason about the solution while another executes the generated Python code inside an isolated Docker environment.

---

## Overview

Traditional LLM coding workflows usually follow:

```text
Question
   ↓
LLM
   ↓
Generated Code
```

AutoCodeGPT extends this into an agent-based workflow:

```text
User Problem
     ↓
Problem Solver Agent
     ↓
Python Solution
     ↓
Code Executor Agent
     ↓
Docker Execution
     ↓
Result / Error
     ↓
Problem Solver Agent
     ↓
Correction or Explanation
```

This creates a basic feedback loop where generated code can be tested and corrected before the workflow terminates.

---

## Key Features

* Multi-agent architecture using Microsoft AutoGen
* Dedicated problem-solving agent
* Dedicated code-execution agent
* Docker-isolated Python execution
* Iterative error correction
* Automatic test-case generation
* Streaming agent messages
* Controlled termination condition
* Streamlit-based user interface
* Asynchronous agent execution

---

## Agent Architecture

### ProblemSolverAgent

The Problem Solver Agent is responsible for:

* Understanding the programming problem
* Explaining the solution approach
* Generating Python code
* Creating test cases
* Reviewing execution results
* Correcting failed code
* Producing the final explanation

The agent is instructed to generate a single executable Python block and include multiple test cases before handing the solution to the executor.

---

### CodeExecutorAgent

The Code Executor Agent is responsible for running generated code inside an isolated Docker environment.

This separates language-model reasoning from actual program execution.

```text
Generated Python
      ↓
CodeExecutorAgent
      ↓
Docker Container
      ↓
stdout / stderr
      ↓
Agent Workflow
```

---

## Team Orchestration

The agents are coordinated using AutoGen's `RoundRobinGroupChat`.

```text
ProblemSolverAgent
        ↓
CodeExecutorAgent
        ↓
ProblemSolverAgent
        ↓
...
```

A text-based termination condition ends the workflow when the problem-solving agent produces:

```text
STOP
```

The current workflow also limits the conversation to a maximum number of turns to prevent uncontrolled execution loops.

---

## Code Execution Isolation

Generated code is executed using AutoGen's Docker command-line executor.

```text
LLM Generated Code
        ↓
DockerCommandLineCodeExecutor
        ↓
Temporary Docker Environment
        ↓
Execution Result
```

Using Docker provides separation between generated code and the host Python environment.

> Docker must be installed and running before starting the application.

---

## User Interface

The project includes a Streamlit interface where a user can enter a DSA or Python programming problem and observe the interaction between the agents.

Example:

```text
Input:
"Write a function to determine whether a number is prime."

ProblemSolverAgent:
- explains the approach
- generates Python code
- creates test cases

CodeExecutorAgent:
- executes the code
- returns the result

ProblemSolverAgent:
- evaluates execution
- corrects the code if required
- explains the final solution
```

---

## Project Structure

```text
AutoCodeGPT/
│
├── agents/
│   ├── problem_solver_agent.py
│   └── code_executor_agent.py
│
├── teams/
│   └── dsa_solver_team.py
│
├── config/
│   ├── constants.py
│   ├── docker_utils.py
│   └── model_client.py
│
├── app.py
├── main.py
├── requirements.txt
└── .gitignore
```

### `agents/`

Contains the specialized AutoGen agents.

### `teams/`

Defines how the agents collaborate and when the workflow terminates.

### `config/`

Contains LLM client configuration, Docker executor configuration, and application constants.

### `main.py`

Provides the core asynchronous orchestration workflow.

### `app.py`

Provides the Streamlit interface.

---

## Requirements

* Python 3.10+
* Docker
* OpenAI API access
* Microsoft AutoGen
* Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/piyush8227/AutoCodeGPT.git
cd AutoCodeGPT
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Do not commit API keys to GitHub.

---

## Running the Application

Make sure Docker is running.

Then start the Streamlit application:

```bash
streamlit run app.py
```

For the CLI version:

```bash
python main.py
```

---

## Workflow

```text
1. User submits programming problem
               ↓
2. ProblemSolverAgent analyzes problem
               ↓
3. Agent generates Python implementation
               ↓
4. CodeExecutorAgent executes code in Docker
               ↓
5. Execution result is returned
               ↓
6. ProblemSolverAgent evaluates result
               ↓
       ┌───────┴────────┐
       │                │
    Success           Error
       │                │
       │           Correct code
       │                │
       └───────┬────────┘
               ↓
7. Final solution and explanation
               ↓
             STOP
```

---

## Technology Stack

* Python
* Microsoft AutoGen
* OpenAI API
* Docker
* Streamlit
* AsyncIO

---

## What This Project Demonstrates

This project explores several important Agentic AI concepts:

### Specialized Agents

Different responsibilities are assigned to different agents instead of asking one model to perform every step.

### Agent Collaboration

Agents exchange messages and results through an orchestrated group-chat workflow.

### Tool / Environment Interaction

The code-execution agent interacts with an external execution environment rather than only generating text.

### Feedback Loops

Execution results are returned to the reasoning agent so failed solutions can be corrected.

### Controlled Termination

The workflow combines explicit termination instructions with a maximum number of turns.

### Safe Code Execution

Generated Python is executed inside Docker instead of directly inside the application process.

---

## Project Purpose

AutoCodeGPT was built as a hands-on exploration of **multi-agent software engineering workflows**.

The project focuses on understanding how an AI system can move beyond:

```text
Prompt → Response
```

toward:

```text
Reason → Act → Observe → Correct → Complete
```

That interaction loop is one of the core ideas behind Agentic AI systems.

---

## Author

**Piyush More**
Machine Learning Engineer

[LinkedIn](https://www.linkedin.com/in/piyushm9034/) • [GitHub](https://github.com/piyush8227)
