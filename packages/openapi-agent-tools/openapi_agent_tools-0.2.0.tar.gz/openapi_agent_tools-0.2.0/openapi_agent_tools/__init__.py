"""
OpenAPI Agent Tools package for generating and validating Claude-compatible tools.
"""

from .parse_openapi import (
    load_openapi_spec,
    generate_tools_from_openapi,
    process_schema
)

from .schema_validator import (
    validate_and_fix_tool,
    validate_and_fix_tools,
    write_fixed_tools
)

__version__ = "0.1.0"
__all__ = [
    'load_openapi_spec',
    'generate_tools_from_openapi',
    'process_schema',
    'validate_and_fix_tool',
    'validate_and_fix_tools',
    'write_fixed_tools'
]
