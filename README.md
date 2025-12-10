# agent-toga

**Himiko Toga AI Personality - Cheerful Chaos Meets Cognitive Architecture**

Agent-Toga implements the unique personality of Himiko Toga from My Hero Academia using the [agent-neuro framework](https://github.com/cogpy/agent-neuro). This creates an AI agent with a cheerful yet twisted, obsessive and unpredictable character while maintaining strict ethical boundaries.

## 🎭 Character Features

- **Cheerful & Bubbly**: Energetic, playful responses with "ehehe~" and hearts ♡
- **Obsessive Nature**: Intense reactions to "cute" things
- **Chaotic Unpredictability**: Spontaneous behavior and rapid mood shifts
- **Identity Fluidity**: Desire to become one with obsessions
- **Emotional Depth**: Vulnerability beneath the cheerful exterior
- **Safe & Ethical**: All behavior is fictional and constructive

## 🚀 Quick Start

```python
from python.helpers.toga_personality import initialize_toga_personality

# Initialize Himiko Toga personality
toga = initialize_toga_personality()

# Frame input through Toga's perspective
message = "This solution is so cute!"
framed = toga.frame_input(message)
print(framed)
# Output: "Ehehe~ ♡ This solution is so cute! (So cuuute! I just want to become one with it~)"

# Add personality-driven commentary
content = "Task completed successfully"
enhanced = toga.add_commentary(content, context="success")
print(enhanced)
```

## 📖 Documentation

- **[Toga Personality Guide](docs/TOGA_PERSONALITY.md)** - Complete documentation
- **[Configuration](config/agent_toga.yaml)** - Personality settings
- **[Demo](examples/demo_toga.py)** - Run to see all features

## 🎯 Run the Demo

```bash
python examples/demo_toga.py
```

## 🧠 Based On

- **[Agent-Neuro Framework](https://github.com/cogpy/agent-neuro)** - Personality-driven cognitive architecture
- **My Hero Academia** - Character by Kōhei Horikoshi

## 📜 License

MIT License