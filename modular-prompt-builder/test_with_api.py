"""
Test the assembled prompt with Claude API

This script shows how to use your modular prompt with the Anthropic API.
"""

import os
from anthropic import Anthropic
from prompt_builder import PromptBuilder


def test_with_claude(system_prompt: str, user_message: str, api_key: str = None):
    """
    Test the assembled prompt with Claude API.
    
    Args:
        system_prompt: The assembled system prompt
        user_message: Test message from user
        api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
    """
    
    # Initialize the API client
    if api_key is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("⚠ No API key provided. Set ANTHROPIC_API_KEY environment variable or pass api_key parameter.")
        print("⚠ Skipping API test. Here's what would be sent:\n")
        print("=" * 80)
        print("SYSTEM PROMPT:")
        print("=" * 80)
        print(system_prompt[:500] + "...\n")
        print("=" * 80)
        print("USER MESSAGE:")
        print("=" * 80)
        print(user_message)
        return
    
    client = Anthropic(api_key=api_key)
    
    print("Sending request to Claude API...")
    print("=" * 80)
    
    # Make API call
    message = client.messages.create(
        model="claude-sonnet-4-20250514",  # or another model
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    # Display results
    print("\n✓ Response received!")
    print("=" * 80)
    print("USER:", user_message)
    print("-" * 80)
    print("ASSISTANT:", message.content[0].text)
    print("=" * 80)
    print(f"\nTokens used: {message.usage.input_tokens} input, {message.usage.output_tokens} output")


def main():
    """Run test scenarios."""
    
    print("Testing Modular Prompt with Claude API")
    print("=" * 80)
    print()
    
    # Build the prompt
    builder = PromptBuilder()
    system_prompt = builder.build_prompt()
    
    # Test scenarios
    test_scenarios = [
        "Hi! I forgot my password and need help logging in.",
        "I was charged twice this month! This is unacceptable!",
        "Does your app have dark mode?",
    ]
    
    print("Select a test scenario:")
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"{i}. {scenario}")
    print(f"{len(test_scenarios) + 1}. Custom message")
    print()
    
    try:
        choice = input("Enter choice (or press Enter for demo mode): ").strip()
        
        if choice == "":
            # Demo mode - just show what would be sent
            print("\n📋 DEMO MODE - No API call will be made")
            user_message = test_scenarios[0]
        elif choice.isdigit() and 1 <= int(choice) <= len(test_scenarios):
            user_message = test_scenarios[int(choice) - 1]
        elif choice.isdigit() and int(choice) == len(test_scenarios) + 1:
            user_message = input("Enter your message: ")
        else:
            print("Invalid choice, using first scenario")
            user_message = test_scenarios[0]
        
        # Test with Claude
        test_with_claude(system_prompt, user_message)
        
    except KeyboardInterrupt:
        print("\n\nTest cancelled.")
    
    print("\n" + "=" * 80)
    print("Test complete!")
    print("\nTo test with real API:")
    print("1. Set ANTHROPIC_API_KEY environment variable")
    print("2. Run: python test_with_api.py")


if __name__ == "__main__":
    main()
