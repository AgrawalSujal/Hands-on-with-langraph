\# LangGraph Hands-On Playground

A compact, practical workspace to explore LangGraph building blocks through
notebooks and small scripts. Use this to learn core patterns like graph
construction, conditional edges, tool calls, and agent-style flows.

\#\# What is inside

- **Notebooks** for interactive experiments and visualizations.
- **Python scripts** for minimal, repeatable examples.
- **pyproject.toml** to capture dependencies and project metadata.

\#\# Workspace map

- `chatbot.ipynb` - Basic conversational flow in a graph.
- `graph_view.ipynb` - Visualize a graph structure.
- `graph_with_condition.ipynb` - Conditional routing with edges.
- `tools_agent.ipynb` - Tool-augmented agent flow.
- `tools_call.ipynb` - Isolated tool calling examples.
- `simple_graph.py` - Minimal graph example in a script.
- `main.py` - Entry point for running a scripted flow.

\#\# Prerequisites

- Windows, macOS, or Linux
- Python 3.10+ (3.11 recommended)

\#\# Setup

1. Create and activate a virtual environment.

	 ```powershell
	 python -m venv .venv
	 .\.venv\Scripts\Activate.ps1
	 ```

2. Install dependencies (choose one).

	 ```powershell
	 pip install -U pip
	 pip install -e .
	 ```

	 Or, if you manage deps via another tool (poetry, uv, etc.), use the
	 workflow already defined in `pyproject.toml`.

\#\# Run the examples

- **Notebooks:** open any `.ipynb` and run cells top-to-bottom.
- **Scripts:** run the minimal example.

	```powershell
	python simple_graph.py
	```

	Or run the main entry point:

	```powershell
	python main.py
	```

\#\# Notes

- Keep notebooks small and focused. Add a new notebook when exploring a new
	LangGraph concept.
- Prefer scripts when you want repeatable, quick runs.

\#\# Troubleshooting

- If the kernel cannot be found, verify the virtual environment is selected
	in the notebook UI.
- If imports fail, reinstall dependencies and restart the kernel.

\#\# Next ideas

- Add memory and persistence to a graph.
- Integrate a retrieval step.
- Create a multi-agent coordinator graph.

