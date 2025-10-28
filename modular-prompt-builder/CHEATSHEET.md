# Modular Prompt Builder - Cheat Sheet

## 🚀 Quick Commands

```bash
# Build prompts
python prompt_builder.py

# Run interactive demo
python interactive_demo.py

# Test with API
python test_with_api.py

# View generated prompt
cat output/complete_prompt.txt
```

## 📂 File Structure

```
prompt_modules/         ← Edit these
  01_identity.md       ← Who is the agent?
  02_capabilities.md   ← What can it do?
  03_safety.md         ← Safety rules
  04_tone.md           ← How it talks
  05_examples.md       ← Example scenarios

output/                ← Generated here
  complete_prompt.txt  ← All modules
  minimal_prompt.txt   ← Selected modules
```

## 🛠️ Common Tasks

### Edit a Module
```bash
nano prompt_modules/01_identity.md
python prompt_builder.py  # Rebuild
```

### Add New Module
```bash
nano prompt_modules/06_newmodule.md
python prompt_builder.py  # Auto-includes it
```

### Custom Build (Python)
```python
from prompt_builder import PromptBuilder

builder = PromptBuilder()

# All modules
full = builder.build_prompt()

# Selected modules
minimal = builder.build_prompt(
    include_modules=["01_identity", "04_tone"]
)

# Save to file
builder.save_prompt("output/custom.txt", 
    include_modules=["01_identity"])
```

## 🔌 API Usage

```python
import anthropic
from prompt_builder import PromptBuilder

# Build prompt
builder = PromptBuilder()
system_prompt = builder.build_prompt()

# Use with Claude
client = anthropic.Anthropic(api_key="key")
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": "Hi!"}]
)
```

## 📋 Module Template

Create `prompt_modules/XX_name.md`:

```markdown
# Module Title

## Section 1
Content here

## Section 2  
More content

## Section 3
Examples and rules
```

## 🎯 Workflow

1. **Edit** modules in `prompt_modules/`
2. **Run** `python prompt_builder.py`
3. **Check** `output/complete_prompt.txt`
4. **Test** with `python test_with_api.py`
5. **Use** in production

## 💡 Tips

- Keep modules focused (100-500 words)
- Use `01_`, `02_` prefixes for ordering
- Test individual modules before combining
- Version control each module separately
- Reuse modules across different agents

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | Check you're in the right directory |
| Python not found | Use `python3` instead of `python` |
| API key error | Set `ANTHROPIC_API_KEY` env variable |
| Import error | Run from project root directory |

## 📚 Documentation

- **QUICKSTART.md** - 5-minute guide
- **TUTORIAL.md** - Step-by-step walkthrough  
- **VISUAL_GUIDE.md** - Screenshots and examples
- **README.md** - Complete documentation

## 🎓 Key Concepts

**Modular** = Each module is independent  
**Reusable** = Share modules across agents  
**Composable** = Mix and match as needed  
**Maintainable** = Update one without breaking others

---

Need more detail? Read **TUTORIAL.md** or run `python interactive_demo.py`
