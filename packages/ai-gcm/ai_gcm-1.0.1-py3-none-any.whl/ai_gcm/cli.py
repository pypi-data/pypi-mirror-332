#!/usr/bin/env python3
"""Command-line interface for AI Commit."""

import click

from ai_gcm.commands import version, generate

@click.group()
def cli():
    """AI-powered Git commit message generator."""
    pass

# Register commands
cli.add_command(version)
cli.add_command(generate)

if __name__ == '__main__':
    cli() 
