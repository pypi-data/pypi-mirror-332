# AgentWeave 🧵

AgentWeave is a powerful CLI tool for initializing and managing AI agent projects based on LangGraph, making it easier to build, customize, and deploy sophisticated AI agents.

Think of AgentWeave as a "create-react-app" but for AI agents - it helps you bootstrap a complete project with all the necessary components, configurations, and integrations.

## Features ✨

- **Quick Project Setup**: Initialize complete AI agent projects with a single command
- **Component Management**: Easily add, remove, and update agent components
- **Tool Integration**: Add and configure agent tools from a growing library of predefined tools
- **LangGraph Integration**: Built on top of LangGraph for powerful agent orchestration
- **Monitoring & Visualization**: Built-in components for monitoring, debugging, and visualizing agent behavior
- **Memory Management**: Easy integration of different memory solutions
- **Service Integrations**: Connect to various external services and APIs
- **Extensible Architecture**: Design focused on extensibility and customization
- **FastAPI Backend**: Well-structured FastAPI backend for serving your agents

## Installation 🚀

```bash
pip install agentweave
```

## Quick Start 🏁

```bash
# Initialize a new agent project
agentweave init my-agent-project

# Change to the project directory
cd my-agent-project

# Setup environment variables in .env.local or .env

# Install the environment (sets up dependencies)
agentweave install_env

# Run your agent in development mode
agentweave run
```

## Environment Setup 🔐

After initializing your project, make sure to:

1. Find the `.env.example` file in your project
2. Copy it to `.env.local`
3. Update the values in `.env.local` with your API keys and configuration

This step is essential for your agent to function properly with external services.

## Project Commands 📝

### Core Commands

```bash
# Initialize a new agent project
agentweave init [project-name]

# Run your agent in development mode
agentweave run

# Run the agent in development mode with hot reloading
agentweave dev

# Install environment dependencies
agentweave install_env
```

### Component Management

```bash
# Add a new tool to your agent
agentweave add tool [tool-name]

# Add a memory component
agentweave add memory [memory-type]

# Add monitoring or visualization
agentweave add monitor [monitor-name]
```

### Templates and Deployment

```bash
# List available components, templates, or tools
agentweave list [components|templates|tools]

# Create a new template
agentweave template create [template-name]

# Use a specific template
agentweave template use [template-name]

# List available templates
agentweave template list

# Convert existing project to a template
agentweave convert-to-template [template-name]

# Deploy your agent (various options)
agentweave deploy [target]
```

### Utility Commands

```bash
# Display version information
agentweave version

# Display general information about AgentWeave
agentweave info
```

## Project Structure 📂

```
my-agent-project/
├── agents/              # Agent definitions
├── tools/               # Custom tools
├── templates/           # Templates for agents and tools
├── memory/              # Memory configurations
├── monitoring/          # Monitoring and visualization
├── frontend/            # UI for interacting with agents
├── config/              # Configuration files
├── README.md            # Project documentation
└── agentweave.yaml      # AgentWeave configuration
```

## Extensibility 🔌

AgentWeave is designed to be highly extensible:

- Create custom templates for new project types
- Develop and share custom tools
- Create plugins for new functionalities
- Integrate with various AI services and platforms

## Dependencies

AgentWeave is built using:

- LangGraph v0.0.30+ for agent orchestration
- FastAPI for the backend API
- Typer and Click for the CLI interface
- Rich for beautiful terminal output
- Jinja2 for template rendering
- And more!

## Troubleshooting 🔧

### Common Issues

#### ModuleNotFoundError: No module named 'agentweave.cli.commands'

If you encounter this error after installation, you may need to:

1. Ensure you have the latest version installed:
   ```bash
   pip install agentweave --upgrade
   ```

2. Try installing the package in development mode:
   ```bash
   git clone https://github.com/yourusername/agentweave.git
   cd agentweave
   pip install -e .
   ```

3. Check if the package structure was correctly installed:
   ```bash
   python -c "import pkgutil; print([p for p in pkgutil.iter_modules(path=['agentweave'])])"
   ```

#### Environment Issues

If you're having trouble with environment variable loading:

1. Make sure you've copied `.env.example` to `.env.local` in your project directory
2. Verify that your API keys are correctly formatted (no extra spaces, quotes, etc.)
3. Run `agentweave install_env` to ensure all dependencies are installed

For more help, please open an issue on our GitHub repository with details about your problem.

## Contributing 🤝

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License 📄

AgentWeave is open source software [licensed as MIT](LICENSE).
