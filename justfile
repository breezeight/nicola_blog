# Justfile for Nicola's Blog Zensical project with uv
# Main justfile that includes modular command files

# Default recipe - show available commands
default:
    @just --list

# Import modular justfile components
import "justfile.zensical"
