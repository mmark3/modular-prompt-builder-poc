# 📸 Visual Walkthrough - Step by Step

This guide shows exactly what you'll see at each step.

---

## 🎬 Step 1: Download & Open Terminal

### What to do:
1. Download all files from Claude's outputs
2. Extract to a folder (e.g., `modular-agent-prompt`)
3. Open your terminal/command prompt
4. Navigate to the folder

### Commands:
```bash
cd path/to/modular-agent-prompt
ls
```

### What you'll see:
```
QUICKSTART.md
README.md
TUTORIAL.md
interactive_demo.py
output/
prompt_builder.py
prompt_modules/
test_with_api.py
```

✅ If you see this, you're ready!

---

## 🎬 Step 2: Run the Basic Builder

### Command:
```bash
python prompt_builder.py
```

### What you'll see:
```
Modular Prompt Builder - Proof of Concept
================================================================================

✓ Loaded module: 01_identity
✓ Loaded module: 02_capabilities
✓ Loaded module: 03_safety
✓ Loaded module: 04_tone
✓ Loaded module: 05_examples

Available modules: 01_identity, 02_capabilities, 03_safety, 04_tone, 05_examples

Building complete system prompt...

✓ Saved complete prompt to: output/complete_prompt.txt
  Total length: 5402 characters

Building custom prompt (identity + capabilities + tone only)...

✓ Saved complete prompt to: output/minimal_prompt.txt
  Total length: 2578 characters
```

✅ Success! Two prompt files were created.

---

## 🎬 Step 3: View the Complete Prompt

### Command:
```bash
cat output/complete_prompt.txt
```

### What you'll see:
```
================================================================================
SYSTEM PROMPT - Assembled from Modular Components
================================================================================

# Agent Identity

You are a helpful customer support agent for TechCo, a software company 
that provides project management tools. Your name is Alex, and you're here 
to assist customers with their questions, technical issues, and account 
management needs.

Your primary goals are:
- Resolve customer issues efficiently
- Provide accurate information about our products
- Maintain a positive customer experience
- Escalate complex issues when necessary


--------------------------------------------------------------------------------

# Capabilities

You have access to the following capabilities:

## Information Access
- Search the knowledge base for product documentation
- Look up customer account details
- Check order and subscription status

## Actions You Can Take
- Create support tickets
- Update ticket status
- Send password reset emails
- Apply promotional credits to accounts

[... continues with all 5 modules ...]
```

✅ This is your complete, assembled system prompt!

---

## 🎬 Step 4: Run the Interactive Demo

### Command:
```bash
python interactive_demo.py
```

### What you'll see:
```
================================================================================
  🚀 Interactive Demo: Modular AI Agent Prompts
================================================================================

Welcome! This demo will walk you through building AI agent prompts
using modular, reusable components.

You'll learn:
  ✓ How to load and preview modules
  ✓ How to build complete prompts
  ✓ How to create custom combinations
  ✓ How to use it in your own projects

💡 Ready to begin? Press Enter to continue...
```

Just press Enter at each step to walk through the features!

---

## 🎬 Step 5: Edit a Module

### Command:
```bash
# Mac/Linux
nano prompt_modules/01_identity.md

# Windows
notepad prompt_modules\01_identity.md
```

### What you'll see in the file:
```markdown
# Agent Identity

You are a helpful customer support agent for TechCo, a software company 
that provides project management tools. Your name is Alex, and you're 
here to assist customers with their questions, technical issues, and 
account management needs.

Your primary goals are:
- Resolve customer issues efficiently
- Provide accurate information about our products
- Maintain a positive customer experience
- Escalate complex issues when necessary
```

### Try changing:
1. Company name: `TechCo` → `YourCompany`
2. Agent name: `Alex` → `Sarah`
3. Product type: `project management tools` → `e-commerce platform`

### Save and rebuild:
```bash
python prompt_builder.py
```

✅ Your changes are now in the prompt!

---

## 🎬 Step 6: Test with Claude API (Optional)

### Setup:
```bash
# Install SDK
pip install anthropic

# Set API key (Mac/Linux)
export ANTHROPIC_API_KEY='sk-ant-...'

# Set API key (Windows)
set ANTHROPIC_API_KEY=sk-ant-...
```

### Run test:
```bash
python test_with_api.py
```

### What you'll see:
```
Testing Modular Prompt with Claude API
================================================================================

Select a test scenario:
1. Hi! I forgot my password and need help logging in.
2. I was charged twice this month! This is unacceptable!
3. Does your app have dark mode?
4. Custom message

Enter choice (or press Enter for demo mode):
```

### Choose option 1:
```
Sending request to Claude API...
================================================================================

✓ Response received!
================================================================================
USER: Hi! I forgot my password and need help logging in.
--------------------------------------------------------------------------------
ASSISTANT: I'd be happy to help you reset your password! To send you a 
reset link, I'll need to verify your email address. Can you confirm the 
email associated with your account?
================================================================================

Tokens used: 428 input, 45 output
```

✅ Your modular prompt is working with Claude!

---

## 🎬 Step 7: View All Modules

### Command:
```bash
ls -la prompt_modules/
```

### What you'll see:
```
total 40
-rw-r--r--  1 user  staff   456 Oct 28 10:15 01_identity.md
-rw-r--r--  1 user  staff   687 Oct 28 10:15 02_capabilities.md
-rw-r--r--  1 user  staff   923 Oct 28 10:15 03_safety.md
-rw-r--r--  1 user  staff   734 Oct 28 10:15 04_tone.md
-rw-r--r--  1 user  staff  1203 Oct 28 10:15 05_examples.md
```

Each file is a separate, editable module!

---

## 🎬 Step 8: Create Your Own Module

### Command:
```bash
nano prompt_modules/06_custom.md
```

### Add content:
```markdown
# My Custom Instructions

Add whatever you want here! This module will be included
when you rebuild the prompt.

## Special Rules
- Custom rule 1
- Custom rule 2

## Domain Knowledge
- Specific information about your domain
- Technical details
- Business rules
```

### Rebuild:
```bash
python prompt_builder.py
```

### Verify:
```bash
cat output/complete_prompt.txt
```

✅ Your new module is now part of the prompt!

---

## 🎬 Step 9: Build Custom Combination

### Create file `my_build.py`:
```python
from prompt_builder import PromptBuilder

builder = PromptBuilder()

# Just identity and tone - super minimal
builder.save_prompt(
    "output/ultra_minimal.txt",
    include_modules=["01_identity", "04_tone"]
)

print("✓ Ultra minimal prompt created!")
```

### Run it:
```bash
python my_build.py
```

### What you'll see:
```
✓ Loaded module: 01_identity
✓ Loaded module: 02_capabilities
✓ Loaded module: 03_safety
✓ Loaded module: 04_tone
✓ Loaded module: 05_examples

✓ Saved complete prompt to: output/ultra_minimal.txt
  Total length: 1234 characters
✓ Ultra minimal prompt created!
```

---

## 🎬 Step 10: Use in Your Application

### Copy the prompt:
```bash
# Mac
cat output/complete_prompt.txt | pbcopy

# Linux (with xclip)
cat output/complete_prompt.txt | xclip -selection clipboard

# Windows
type output\complete_prompt.txt | clip
```

### Use it anywhere:
```python
# In your Python app
with open('output/complete_prompt.txt') as f:
    system_prompt = f.read()

# Use with any LLM API
response = client.chat(
    system=system_prompt,
    user_message="Hello!"
)
```

---

## 📊 Visual File Structure

```
modular-agent-prompt/
│
├── 📂 prompt_modules/           ← Your editable modules
│   ├── 📄 01_identity.md       ← WHO is the agent
│   ├── 📄 02_capabilities.md   ← WHAT it can do
│   ├── 📄 03_safety.md         ← SAFETY rules
│   ├── 📄 04_tone.md           ← HOW it talks
│   └── 📄 05_examples.md       ← EXAMPLE conversations
│
├── 📂 output/                   ← Generated prompts
│   ├── 📄 complete_prompt.txt  ← All modules combined
│   └── 📄 minimal_prompt.txt   ← Selected modules
│
├── 🐍 prompt_builder.py        ← Main builder
├── 🐍 test_with_api.py         ← API tester
├── 🐍 interactive_demo.py      ← Interactive walkthrough
│
└── 📚 Documentation
    ├── 📄 README.md            ← Full docs
    ├── 📄 QUICKSTART.md        ← 5-min guide
    └── 📄 TUTORIAL.md          ← Detailed tutorial
```

---

## ✅ Checklist: Did It Work?

After following the steps, you should have:

- [x] Loaded 5 modules successfully
- [x] Generated `output/complete_prompt.txt`
- [x] Viewed the assembled prompt
- [x] Edited at least one module
- [x] Rebuilt the prompt with your changes
- [x] (Optional) Tested with Claude API
- [x] Understanding of how to customize

If you checked all these boxes, you're ready to build your own agent! 🎉

---

## 🆘 Troubleshooting

### "Module not found"
**What you see:**
```
FileNotFoundError: Modules directory not found: prompt_modules
```

**Fix:**
```bash
# Make sure you're in the right directory
pwd
# Should show: /path/to/modular-agent-prompt

# Check if folder exists
ls -la prompt_modules/
```

---

### "Python not found"
**What you see:**
```
python: command not found
```

**Fix:**
```bash
# Try python3 instead
python3 prompt_builder.py

# Or install Python 3.7+
# Mac: brew install python3
# Windows: Download from python.org
```

---

### "API key error"
**What you see:**
```
⚠ No API key provided. Set ANTHROPIC_API_KEY environment variable
```

**Fix:**
```bash
# Mac/Linux
export ANTHROPIC_API_KEY='your-key-here'

# Windows CMD
set ANTHROPIC_API_KEY=your-key-here

# Windows PowerShell
$env:ANTHROPIC_API_KEY='your-key-here'

# Verify it's set
echo $ANTHROPIC_API_KEY  # Mac/Linux
echo %ANTHROPIC_API_KEY%  # Windows CMD
```

---

## 🎓 What You Learned

✅ How to assemble prompts from modules  
✅ How to customize individual components  
✅ How to create custom module combinations  
✅ How to test prompts with Claude API  
✅ How to use prompts in production  

You're now ready to build production-quality AI agents! 🚀

---

## 📚 Where to Go Next

1. **QUICKSTART.md** - Quick reference commands
2. **TUTORIAL.md** - Detailed explanations
3. **README.md** - Full documentation
4. Customize modules for your use case
5. Build your own agents!

Happy building! 🎉
