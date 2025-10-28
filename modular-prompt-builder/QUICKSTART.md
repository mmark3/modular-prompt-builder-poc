# Quick Start Guide - 5 Minutes

## Fastest Way to Get Started

### 1. Download & Extract (30 seconds)
Download all files from Claude's outputs folder to your computer.

### 2. Run the Builder (30 seconds)
```bash
cd path/to/modular-agent-prompt
python prompt_builder.py
```

### 3. See the Results (30 seconds)
```bash
cat output/complete_prompt.txt
```

That's it! You now have a complete, assembled AI agent prompt.

---

## What You Just Did

✅ Loaded 5 modular prompt components  
✅ Combined them into a complete system prompt  
✅ Saved it to `output/complete_prompt.txt`

---

## Try It With Claude (2 minutes)

### Option 1: Claude.ai Web Interface
1. Copy the prompt: `cat output/complete_prompt.txt | pbcopy`
2. Go to claude.ai
3. Start a new chat
4. Paste the prompt
5. Ask: "Hi! I forgot my password"

### Option 2: API (if you have a key)
```bash
pip install anthropic
export ANTHROPIC_API_KEY='your-key'
python test_with_api.py
```

Choose option 1, 2, or 3 to test different scenarios.

---

## Customize It (2 minutes)

### Edit a Module:
```bash
nano prompt_modules/01_identity.md
```

Change the company name from "TechCo" to your company.

### Rebuild:
```bash
python prompt_builder.py
```

Done! Your prompt now reflects your changes.

---

## Common Commands

```bash
# Rebuild everything
python prompt_builder.py

# Test with API
python test_with_api.py

# View a module
cat prompt_modules/01_identity.md

# View generated prompt
cat output/complete_prompt.txt

# List all modules
ls -la prompt_modules/
```

---

## Module Overview

| Module | Purpose | When to Edit |
|--------|---------|--------------|
| `01_identity.md` | Who is the agent? | Change company/role |
| `02_capabilities.md` | What can it do? | Add/remove features |
| `03_safety.md` | Safety guardrails | Adjust policies |
| `04_tone.md` | How it talks | Change personality |
| `05_examples.md` | Example conversations | Add use cases |

---

## File Structure

```
modular-agent-prompt/
├── prompt_modules/          ← Edit these
│   ├── 01_identity.md
│   ├── 02_capabilities.md
│   ├── 03_safety.md
│   ├── 04_tone.md
│   └── 05_examples.md
├── output/                  ← Generated prompts go here
│   ├── complete_prompt.txt
│   └── minimal_prompt.txt
├── prompt_builder.py        ← Runs the assembly
├── test_with_api.py        ← Tests with Claude
└── README.md               ← Full documentation
```

---

## Next Steps

1. ✅ Read `TUTORIAL.md` for detailed walkthrough
2. ✅ Customize modules for your use case
3. ✅ Test with `test_with_api.py`
4. ✅ Use in production!

---

## Get Help

- **Detailed guide**: Read `TUTORIAL.md`
- **Full docs**: Read `README.md`
- **Issues**: Check file permissions, Python version (needs 3.7+)

---

## Copy-Paste Examples

### Use in Python:
```python
from prompt_builder import PromptBuilder

builder = PromptBuilder()
prompt = builder.build_prompt()
print(prompt)
```

### Use with Anthropic API:
```python
import anthropic
from prompt_builder import PromptBuilder

client = anthropic.Anthropic(api_key="your-key")
builder = PromptBuilder()
system_prompt = builder.build_prompt()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Custom Module Selection:
```python
builder = PromptBuilder()
prompt = builder.build_prompt(
    include_modules=["01_identity", "04_tone"]
)
```

---

That's all you need to get started! 🎉
