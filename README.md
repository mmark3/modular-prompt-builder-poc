# Modular AI Agent Prompt - Proof of Concept

This project demonstrates how to build AI agent system prompts using modular, reusable components.

## 🎯 Overview

Instead of maintaining one giant system prompt, this approach breaks it into logical modules:

- **01_identity.md** - Who is the agent? What's their role?
- **02_capabilities.md** - What can the agent do? What tools are available?
- **03_safety.md** - Safety guardrails and constraints
- **04_tone.md** - Communication style and guidelines
- **05_examples.md** - Few-shot examples for common scenarios

## 📁 Project Structure

```
.
├── prompt_modules/          # Individual prompt modules
│   ├── 01_identity.md
│   ├── 02_capabilities.md
│   ├── 03_safety.md
│   ├── 04_tone.md
│   └── 05_examples.md
├── prompt_builder.py        # Main builder class
├── test_with_api.py        # Test with Claude API
├── output/                 # Generated prompts (created on first run)
└── README.md
```

## 🚀 Quick Start

### 1. Run the Prompt Builder

```bash
python prompt_builder.py
```

This will:
- Load all modules from `prompt_modules/`
- Generate a complete system prompt
- Save it to `output/complete_prompt.txt`
- Create a minimal version with selected modules

### 2. Test with Claude API (Optional)

```bash
# Set your API key
export ANTHROPIC_API_KEY='your-api-key-here'

# Run the test
python test_with_api.py
```

Or run in demo mode (no API key needed):
```bash
python test_with_api.py
```

## 🔧 Customization

### Adding New Modules

1. Create a new `.md` file in `prompt_modules/`
2. Use numeric prefix for ordering (e.g., `06_new_module.md`)
3. Run `prompt_builder.py` to regenerate

### Building Custom Prompts

```python
from prompt_builder import PromptBuilder

builder = PromptBuilder()

# Build with specific modules only
custom_prompt = builder.build_prompt(
    include_modules=["01_identity", "02_capabilities", "04_tone"]
)

# Save to file
builder.save_prompt("output/my_custom_prompt.txt", 
                    include_modules=["01_identity", "04_tone"])
```

### Module Format

Each module is a markdown file with clear sections:

```markdown
# Module Title

## Section 1
Content here...

## Section 2
More content...
```

## 💡 Benefits of This Approach

✅ **Easy to Maintain** - Update one module without touching others
✅ **Reusable** - Share modules across different agents
✅ **Testable** - Test individual modules or combinations
✅ **Version Control** - Track changes to specific components
✅ **Flexible** - Mix and match modules for different use cases
✅ **Collaborative** - Different team members can own different modules

## 🎨 Use Cases

- **Customer Support Agent** (current example)
- Code Assistant
- Research Agent
- Content Writer
- Data Analyst
- Sales Assistant

Just swap out the modules to match your use case!

## 📊 Example Output

The builder creates prompts like:

```
================================================================================
SYSTEM PROMPT - Assembled from Modular Components
================================================================================

# Agent Identity

You are a helpful customer support agent...

--------------------------------------------------------------------------------

# Capabilities

You have access to the following capabilities...

--------------------------------------------------------------------------------
...
```

## 🔐 Security Note

The safety module (`03_safety.md`) includes important constraints:
- Data privacy requirements
- Access verification
- Escalation triggers
- Authorization limits

Always review and customize the safety module for your specific use case!

## 🚦 Next Steps

1. ✅ Run `prompt_builder.py` to see it in action
2. ✅ Modify modules in `prompt_modules/` for your use case
3. ✅ Test with `test_with_api.py`
4. ✅ Build custom module combinations
5. ✅ Add versioning/metadata for production use
6. ✅ Implement conditional logic for dynamic prompts

## 📝 License

This is a proof of concept for demonstration purposes.

---

**Questions?** Open an issue or modify the code to fit your needs!
# modular-prompt-builder
