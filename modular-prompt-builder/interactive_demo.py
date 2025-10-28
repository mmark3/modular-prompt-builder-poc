#!/usr/bin/env python3
"""
Interactive Demo - Modular Prompt Builder
This script walks you through the features step by step.
"""

import os
import time
from pathlib import Path
from prompt_builder import PromptBuilder


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80 + "\n")


def print_step(number, title):
    """Print a step header."""
    print(f"\n{'─' * 80}")
    print(f"STEP {number}: {title}")
    print('─' * 80)


def pause(message="Press Enter to continue..."):
    """Pause for user input."""
    input(f"\n💡 {message}")


def demo_load_modules():
    """Demonstrate loading modules."""
    print_step(1, "Loading Modules")
    
    print("Let's see what modules are available...")
    pause()
    
    builder = PromptBuilder()
    
    print("\n📦 Available modules:")
    for i, module in enumerate(builder.get_available_modules(), 1):
        print(f"  {i}. {module}")
    
    pause()
    return builder


def demo_preview_module(builder):
    """Demonstrate previewing a module."""
    print_step(2, "Preview a Module")
    
    print("Let's look at what's inside the 'identity' module...")
    pause()
    
    builder.preview_module("01_identity")
    
    print("\n✨ This module defines WHO the agent is.")
    pause()


def demo_build_complete(builder):
    """Demonstrate building complete prompt."""
    print_step(3, "Build Complete Prompt")
    
    print("Now let's combine ALL modules into one system prompt...")
    pause()
    
    builder.save_prompt("output/demo_complete.txt")
    
    print("\n📄 Let's see a preview of what was created:")
    pause()
    
    with open("output/demo_complete.txt") as f:
        lines = f.readlines()
        # Show first 20 lines
        for line in lines[:20]:
            print(line.rstrip())
        print("\n... (truncated, see output/demo_complete.txt for full prompt) ...")
    
    print(f"\n✅ Complete prompt saved with {len(''.join(lines))} characters")
    pause()


def demo_custom_combination(builder):
    """Demonstrate custom module selection."""
    print_step(4, "Custom Module Combinations")
    
    print("You don't always need ALL modules.")
    print("Let's build a minimal prompt with just:")
    print("  - Identity (who the agent is)")
    print("  - Tone (how they should talk)")
    pause()
    
    builder.save_prompt(
        "output/demo_minimal.txt",
        include_modules=["01_identity", "04_tone"]
    )
    
    print("\n✨ Created a much shorter, focused prompt!")
    print("This is perfect when you don't need all the safety rules and examples.")
    pause()


def demo_modify_module():
    """Demonstrate modifying a module."""
    print_step(5, "Modifying Modules")
    
    print("The real power is in customization!")
    print("\nLet's say you want to change the agent's company...")
    print("\n📝 You would edit: prompt_modules/01_identity.md")
    print("\nChange this:")
    print('  "You are a helpful customer support agent for TechCo..."')
    print("\nTo this:")
    print('  "You are a helpful customer support agent for MyCorp..."')
    
    print("\nThen just run the builder again, and your prompt is updated!")
    pause()


def demo_use_cases():
    """Show different use cases."""
    print_step(6, "Different Use Cases")
    
    print("This modular approach works for ANY type of agent:")
    print()
    print("🤖 Customer Support (current example)")
    print("   └─ Identity, Capabilities, Safety, Tone, Examples")
    print()
    print("💻 Code Assistant")
    print("   └─ Identity, Languages, Best Practices, Code Style, Examples")
    print()
    print("📊 Data Analyst")
    print("   └─ Identity, Tools (Python/SQL), Analysis Methods, Visualization")
    print()
    print("✍️  Content Writer")
    print("   └─ Identity, Writing Style, SEO Guidelines, Brand Voice")
    print()
    print("Just swap out the modules to match your needs!")
    pause()


def demo_next_steps():
    """Show next steps."""
    print_step(7, "Next Steps")
    
    print("Here's what you can do now:")
    print()
    print("1️⃣  Customize the modules:")
    print("    Edit files in prompt_modules/ to match your use case")
    print()
    print("2️⃣  Test with Claude:")
    print("    Run: python test_with_api.py")
    print("    (Need API key: export ANTHROPIC_API_KEY='your-key')")
    print()
    print("3️⃣  Create new modules:")
    print("    Add 06_yourmodule.md to prompt_modules/")
    print()
    print("4️⃣  Build custom combinations:")
    print("    Use the Python API to select specific modules")
    print()
    print("5️⃣  Use in production:")
    print("    Copy the generated prompt to your application")
    pause()


def demo_code_examples():
    """Show code examples."""
    print_step(8, "Code Examples")
    
    print("Here's how to use the builder in your own code:")
    print()
    print("─" * 80)
    print("""
# Basic usage
from prompt_builder import PromptBuilder

builder = PromptBuilder()
prompt = builder.build_prompt()

# Custom modules
custom_prompt = builder.build_prompt(
    include_modules=["01_identity", "04_tone"]
)

# Save to file
builder.save_prompt("my_prompt.txt", 
                    include_modules=["01_identity", "02_capabilities"])

# Get list of modules
modules = builder.get_available_modules()
print(modules)
""")
    print("─" * 80)
    pause()


def demo_api_example():
    """Show API usage example."""
    print_step(9, "Using with Claude API")
    
    print("Once you've built your prompt, use it with Claude:")
    print()
    print("─" * 80)
    print("""
import anthropic
from prompt_builder import PromptBuilder

# Build your prompt
builder = PromptBuilder()
system_prompt = builder.build_prompt()

# Use with Claude API
client = anthropic.Anthropic(api_key="your-key")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=system_prompt,  # Your modular prompt here!
    messages=[
        {"role": "user", "content": "I need help with my account"}
    ]
)

print(message.content[0].text)
""")
    print("─" * 80)
    pause()


def main():
    """Run the interactive demo."""
    print_header("🚀 Interactive Demo: Modular AI Agent Prompts")
    
    print("Welcome! This demo will walk you through building AI agent prompts")
    print("using modular, reusable components.")
    print()
    print("You'll learn:")
    print("  ✓ How to load and preview modules")
    print("  ✓ How to build complete prompts")
    print("  ✓ How to create custom combinations")
    print("  ✓ How to use it in your own projects")
    
    pause("Ready to begin?")
    
    try:
        # Run through each demo
        builder = demo_load_modules()
        demo_preview_module(builder)
        demo_build_complete(builder)
        demo_custom_combination(builder)
        demo_modify_module()
        demo_use_cases()
        demo_next_steps()
        demo_code_examples()
        demo_api_example()
        
        # Completion
        print_header("🎉 Demo Complete!")
        print("You now know how to:")
        print("  ✅ Load modules")
        print("  ✅ Build prompts")
        print("  ✅ Customize for your needs")
        print("  ✅ Use with Claude API")
        print()
        print("Check the output/ directory to see what was generated!")
        print()
        print("📚 More resources:")
        print("  - QUICKSTART.md - 5-minute guide")
        print("  - TUTORIAL.md - Detailed walkthrough")
        print("  - README.md - Full documentation")
        print()
        print("Happy building! 🚀")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted. You can run it again anytime!")
        print("Run: python interactive_demo.py")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("Make sure you're in the correct directory with all files present.")


if __name__ == "__main__":
    main()
