# Step-by-Step Tutorial: Modular AI Agent Prompts

## Prerequisites

- Python 3.7 or higher installed
- Basic command line knowledge
- (Optional) Anthropic API key for testing with Claude

## Step 1: Set Up Your Environment

### Option A: Download from Claude
If you're reading this in Claude, all files are in the outputs folder. Download them to your computer.

### Option B: Create manually
Create a new directory and save all the files from the outputs folder.

### Verify your setup:
```bash
# Navigate to your project directory
cd path/to/modular-agent-prompt

# Check that you have these files:
ls -la
```

You should see:
```
prompt_modules/
  ├── 01_identity.md
  ├── 02_capabilities.md
  ├── 03_safety.md
  ├── 04_tone.md
  └── 05_examples.md
prompt_builder.py
test_with_api.py
README.md
```

## Step 2: Run the Basic Prompt Builder

```bash
python prompt_builder.py
```

### What this does:
1. ✅ Loads all 5 modules from `prompt_modules/`
2. ✅ Combines them into a complete system prompt
3. ✅ Saves two versions:
   - `output/complete_prompt.txt` - All modules
   - `output/minimal_prompt.txt` - Just identity, capabilities, and tone

### Expected output:
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
```

## Step 3: Examine the Generated Prompts

Open the generated files to see what was created:

```bash
# View the complete prompt
cat output/complete_prompt.txt

# Or open in your favorite editor
open output/complete_prompt.txt
# On Windows: notepad output/complete_prompt.txt
# On Linux: nano output/complete_prompt.txt
```

You'll see all 5 modules combined with clear separators between each section.

## Step 4: Modify a Module

Let's customize the agent! Open one of the modules and make changes:

```bash
# Edit the identity module
nano prompt_modules/01_identity.md
# Or use your preferred editor
```

### Example modification:
Change the company name and role:

**Before:**
```markdown
You are a helpful customer support agent for TechCo, a software 
company that provides project management tools.
```

**After:**
```markdown
You are a friendly virtual assistant for MyCorp, an e-commerce 
platform that sells eco-friendly products.
```

Save the file, then rebuild:

```bash
python prompt_builder.py
```

The new prompt will reflect your changes!

## Step 5: Create a Custom Module Combination

You can build prompts with only the modules you need.

### Option A: Use the Python API

Create a new file called `my_custom_build.py`:

```python
from prompt_builder import PromptBuilder

# Initialize builder
builder = PromptBuilder()

# Build with only specific modules
custom_prompt = builder.build_prompt(
    include_modules=[
        "01_identity",
        "02_capabilities",
        "04_tone"
    ]
)

# Save it
builder.save_prompt(
    "output/my_custom_prompt.txt",
    include_modules=["01_identity", "02_capabilities", "04_tone"]
)

print("✓ Custom prompt created!")
```

Run it:
```bash
python my_custom_build.py
```

### Option B: Modify prompt_builder.py

At the bottom of `prompt_builder.py`, in the `main()` function, add:

```python
# Build your own combination
builder.save_prompt(
    "output/marketing_agent.txt",
    include_modules=["01_identity", "04_tone", "05_examples"]
)
```

## Step 6: Test with Claude API (Optional)

If you have an Anthropic API key, you can test your prompt with real Claude API calls.

### Install the Anthropic SDK:
```bash
pip install anthropic
```

### Set your API key:

**On Mac/Linux:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**On Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**On Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY='your-api-key-here'
```

### Run the test:
```bash
python test_with_api.py
```

You'll see a menu:
```
Select a test scenario:
1. Hi! I forgot my password and need help logging in.
2. I was charged twice this month! This is unacceptable!
3. Does your app have dark mode?
4. Custom message

Enter choice (or press Enter for demo mode):
```

**Try it:**
- Press `1` and Enter to test password reset scenario
- Press `4` to enter your own test message
- Press just Enter to run in demo mode (no API call)

### What happens:
1. Your modular prompt is assembled
2. Sent to Claude as the system prompt
3. Your test message is sent as the user message
4. Claude responds according to your prompt modules
5. You see the response and token usage

## Step 7: Create Your Own Module

Let's add a new module for handling refunds:

```bash
# Create new module
nano prompt_modules/06_refunds.md
```

Add this content:
```markdown
# Refund Policy

## Refund Eligibility
Customers are eligible for refunds within 30 days of purchase if:
- Product was defective
- Service was not delivered as promised
- Customer cancels subscription within trial period

## Refund Process
1. Verify purchase date and order details
2. Confirm reason for refund request
3. Check refund eligibility based on policy
4. Process refund if approved (3-5 business days)
5. Send confirmation email

## Approval Requirements
- Under $100: You can approve
- $100-$500: Requires supervisor approval
- Over $500: Requires manager approval

Always express empathy and understanding when handling refund requests.
```

Save and rebuild:
```bash
python prompt_builder.py
```

Now your complete prompt includes the refund module!

## Step 8: Use in Production

### Copy the assembled prompt:
```bash
cat output/complete_prompt.txt | pbcopy  # Mac
cat output/complete_prompt.txt | clip    # Windows
```

### Use it anywhere:
- Paste into Claude.ai as a project custom instruction
- Use as the system prompt in API calls
- Include in your application code
- Share with your team

### Example API usage:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

# Load your assembled prompt
with open("output/complete_prompt.txt") as f:
    system_prompt = f.read()

# Use it
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "I need help with my account"}
    ]
)

print(message.content[0].text)
```

## Troubleshooting

### "Module not found" error
- Make sure you're in the correct directory
- Check that `prompt_modules/` folder exists
- Verify .md files are in the folder

### Python import errors
```bash
# Make sure Python can find the modules
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### API key not recognized
```bash
# Verify it's set
echo $ANTHROPIC_API_KEY

# If empty, set it again
export ANTHROPIC_API_KEY='your-key'
```

## Next Steps

Now that you know the basics, try:

1. ✅ **Customize for your use case** - Change modules to match your needs
2. ✅ **Add versioning** - Track changes to modules over time
3. ✅ **Create module variants** - Have different tone options you can swap
4. ✅ **Add metadata** - Include version numbers, authors, descriptions
5. ✅ **Build conditional logic** - Load different modules based on context
6. ✅ **Share modules** - Create a library of reusable components

## Quick Reference Commands

```bash
# Rebuild prompts
python prompt_builder.py

# Test with API
python test_with_api.py

# View a specific module
cat prompt_modules/01_identity.md

# See what was generated
cat output/complete_prompt.txt

# List all modules
ls prompt_modules/
```

## Questions?

Common questions:

**Q: Can I use YAML instead of Markdown?**
A: Yes! Just modify `prompt_builder.py` to load `.yaml` files instead.

**Q: How do I add conditional logic?**
A: Modify the `build_prompt()` method to check conditions before including modules.

**Q: Can I have nested modules?**
A: Yes! You could have subfolders and recursively load them.

**Q: What's the best module size?**
A: Keep modules focused on one concept (100-500 words each).

Happy building! 🚀
