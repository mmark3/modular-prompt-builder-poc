"""
Modular Prompt Builder - Proof of Concept

This script demonstrates how to build system prompts from modular components.
"""

import os
from pathlib import Path
from typing import List, Optional
import json


class PromptBuilder:
    """Assembles system prompts from modular components."""
    
    def __init__(self, modules_dir: str = "prompt_modules"):
        self.modules_dir = Path(modules_dir)
        self.modules = {}
        self.load_modules()
    
    def load_modules(self):
        """Load all markdown modules from the modules directory."""
        if not self.modules_dir.exists():
            raise FileNotFoundError(f"Modules directory not found: {self.modules_dir}")
        
        for filepath in sorted(self.modules_dir.glob("*.md")):
            module_name = filepath.stem
            with open(filepath, 'r', encoding='utf-8') as f:
                self.modules[module_name] = f.read()
            print(f"✓ Loaded module: {module_name}")
    
    def build_prompt(self, include_modules: Optional[List[str]] = None) -> str:
        """
        Build a complete system prompt from specified modules.
        
        Args:
            include_modules: List of module names to include (without extension).
                           If None, includes all modules in alphabetical order.
        
        Returns:
            Complete assembled system prompt as a string.
        """
        if include_modules is None:
            include_modules = sorted(self.modules.keys())
        
        prompt_parts = []
        
        # Add header
        prompt_parts.append("=" * 80)
        prompt_parts.append("SYSTEM PROMPT - Assembled from Modular Components")
        prompt_parts.append("=" * 80)
        prompt_parts.append("")
        
        # Add each module
        for module_name in include_modules:
            if module_name not in self.modules:
                print(f"⚠ Warning: Module '{module_name}' not found, skipping...")
                continue
            
            prompt_parts.append(self.modules[module_name])
            prompt_parts.append("\n" + "-" * 80 + "\n")
        
        return "\n".join(prompt_parts)
    
    def save_prompt(self, output_path: str, include_modules: Optional[List[str]] = None):
        """Build and save the complete prompt to a file."""
        prompt = self.build_prompt(include_modules)
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        print(f"\n✓ Saved complete prompt to: {output_path}")
        print(f"  Total length: {len(prompt)} characters")
    
    def get_available_modules(self) -> List[str]:
        """Return list of all available module names."""
        return sorted(self.modules.keys())
    
    def preview_module(self, module_name: str):
        """Print a preview of a specific module."""
        if module_name in self.modules:
            print(f"\n{'=' * 80}")
            print(f"Preview of module: {module_name}")
            print('=' * 80)
            print(self.modules[module_name])
        else:
            print(f"Module '{module_name}' not found.")


def main():
    """Demonstration of the prompt builder."""
    
    print("Modular Prompt Builder - Proof of Concept")
    print("=" * 80)
    print()
    
    # Initialize builder
    builder = PromptBuilder()
    
    print(f"\nAvailable modules: {', '.join(builder.get_available_modules())}")
    print()
    
    # Build complete prompt with all modules
    print("Building complete system prompt...")
    builder.save_prompt("output/complete_prompt.txt")
    
    # Build a custom prompt with only selected modules
    print("\nBuilding custom prompt (identity + capabilities + tone only)...")
    builder.save_prompt(
        "output/minimal_prompt.txt",
        include_modules=["01_identity", "02_capabilities", "04_tone"]
    )
    
    # Example: Preview a specific module
    print("\n" + "=" * 80)
    print("Example: Previewing the 'tone' module")
    print("=" * 80)
    builder.preview_module("04_tone")
    
    print("\n" + "=" * 80)
    print("✓ Proof of concept complete!")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Check the 'output' directory for generated prompts")
    print("2. Modify modules in 'prompt_modules' directory")
    print("3. Run this script again to regenerate prompts")
    print("4. Use the prompts with Claude API (see test_with_api.py)")


if __name__ == "__main__":
    main()
