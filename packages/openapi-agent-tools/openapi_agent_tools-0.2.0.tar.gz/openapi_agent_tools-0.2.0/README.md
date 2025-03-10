# OpenAPI Agent Tools

A library for generating and validating Claude-compatible tools from OpenAPI specifications. I haven't tested it with other models but it should work too as tools are usually defined as JSON Schema

## Installation

```bash
pip install openapi-agent-tools
```

Or directly from the repository:

```bash
pip install git+https://github.com/teobaldo33/openapi-agent-tools.git
```

## Usage

```python
from openapi_agent_tools import (
    generate_tools_from_openapi,
    validate_and_fix_tools
)

# Generate tools from the specification as json or yaml
tools = generate_tools_from_openapi(openapi_spec, base_url)

# Validate and fix tools for Claude compatibility
fixed_tools, failed_tools = validate_and_fix_tools(tools)

print(f"Generated and fixed {len(fixed_tools)} tools")
```

## Features

- **OpenAPI Analysis**: Process OpenAPI specifications to generate Agent-compatible tools
- **Schema Validation**: Check and fix common errors in tool definitions
- **Claude Compatibility**: Adapt schemas to be usable with AI Agents
- **CLI Interface**: Command line utilities for use in scripts

## License

MIT
