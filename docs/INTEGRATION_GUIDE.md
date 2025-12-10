# Integration Guide: Agent-Toga with Agent-Neuro Framework

## Overview

This document explains how Agent-Toga integrates with the [agent-neuro framework](https://github.com/cogpy/agent-neuro) and how to use it in your own projects.

## Framework Compatibility

Agent-Toga is built on the same architectural patterns as agent-neuro:

### Shared Patterns

1. **Personality Tensor Structure**
   - Agent-Neuro: `PersonalityTensor` with traits like playfulness, chaotic, sarcasm
   - Agent-Toga: `TogaPersonalityTensor` with traits like cheerfulness, obsessiveness, chaos

2. **Emotional State Tracking**
   - Both use `EmotionalState` dataclass with type, intensity, duration
   - Both implement emotional decay mechanisms

3. **Ethical Constraints**
   - Both enforce immutable safety constraints
   - Both use `__post_init__` to validate constraints

4. **Personality Inheritance**
   - Both support multi-agent personality inheritance
   - Both use inheritance factors (typically 0.7)

5. **Serialization**
   - Both implement `to_dict()` and `from_dict()` methods
   - Both support JSON-compatible state export

## Integration Options

### Option 1: Standalone Usage

Use Agent-Toga independently without the full agent-neuro framework:

```python
from python.helpers.toga_personality import initialize_toga_personality

# Create Toga personality
toga = initialize_toga_personality()

# Use in your application
user_input = "I found a cute kitten!"
processed = toga.frame_input(user_input)
response = your_llm_function(processed)
enhanced = toga.add_commentary(response, context="cute")
```

### Option 2: Drop-in Replacement for Agent-Neuro

Replace agent-neuro personality with Himiko Toga:

```python
# Instead of:
# from python.helpers.neuro_personality import NeuroPersonality
# personality = NeuroPersonality()

# Use:
from python.helpers.toga_personality import TogaPersonality
personality = initialize_toga_personality()

# Same interface:
framed = personality.frame_input(message)
enhanced = personality.add_commentary(content, context="success")
state = personality.to_dict()
```

### Option 3: Side-by-Side with Agent-Neuro

Run both personalities in the same system:

```python
from python.helpers.toga_personality import initialize_toga_personality
# Assuming agent-neuro is also installed:
# from python.helpers.neuro_personality import NeuroPersonality

toga = initialize_toga_personality()
# neuro = NeuroPersonality()

# Use different personalities for different agents
agent_1.personality = toga
# agent_2.personality = neuro
```

### Option 4: Agent-Neuro Framework Integration

If you have the full agent-neuro framework running:

```python
# In your agent initialization (agent.py or similar)
from python.helpers.toga_personality import initialize_toga_personality

class Agent:
    def __init__(self, ...):
        # ... existing initialization ...
        
        # Add Toga personality
        if config.get("enable_toga_personality"):
            self.toga = initialize_toga_personality()
    
    def message_loop(self, message):
        # Frame input through Toga
        if hasattr(self, 'toga'):
            message = self.toga.frame_input(message)
        
        # ... process message ...
        
        # Enhance response
        if hasattr(self, 'toga'):
            response = self.toga.add_commentary(response)
        
        return response
```

## Configuration

### Using YAML Configuration

Load personality from the provided YAML config:

```python
import yaml
from python.helpers.toga_personality import TogaPersonalityTensor, TogaPersonality

# Load config
with open('config/agent_toga.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Extract personality traits
traits = config['personality']

# Create personality
tensor = TogaPersonalityTensor(**traits)
toga = TogaPersonality(personality=tensor)
```

### Environment Variables

Set environment variables to control Toga personality:

```bash
export ENABLE_TOGA_PERSONALITY=true
export TOGA_CHEERFULNESS=0.95
export TOGA_CHAOS=0.95
export TOGA_VERBOSE=true
```

```python
import os

# Check if enabled
if os.getenv('ENABLE_TOGA_PERSONALITY', 'false').lower() == 'true':
    # Get custom traits from environment
    custom_traits = {}
    if os.getenv('TOGA_CHEERFULNESS'):
        custom_traits['cheerfulness'] = float(os.getenv('TOGA_CHEERFULNESS'))
    if os.getenv('TOGA_CHAOS'):
        custom_traits['chaos'] = float(os.getenv('TOGA_CHAOS'))
    
    toga = initialize_toga_personality(custom_traits or None)
```

## Multi-Agent Orchestration

### Parent-Child Personality Inheritance

```python
# Parent agent with Toga personality
parent_agent = Agent(personality=initialize_toga_personality())

# Create subordinate with inherited personality
def create_subordinate(parent, task):
    # Inherit personality from parent
    child_tensor = parent.personality.personality.inherit(
        inheritance_factor=0.7  # 70% parent, 30% variation
    )
    child_personality = TogaPersonality(personality=child_tensor)
    
    # Create subordinate agent
    subordinate = Agent(personality=child_personality)
    subordinate.execute(task)
    
    return subordinate
```

### Custom Inheritance Overrides

```python
# Create subordinate with specific trait modifications
def create_specialized_subordinate(parent, specialization):
    # Start with inherited base
    child_tensor = parent.personality.personality.inherit(0.7)
    
    # Override specific traits based on specialization
    if specialization == "researcher":
        child_tensor.playfulness = 0.3  # Less playful
        child_tensor.obsessiveness = 0.95  # More focused
    elif specialization == "creative":
        child_tensor.chaos = 0.98  # More chaotic
        child_tensor.playfulness = 0.95  # More playful
    
    return TogaPersonality(personality=child_tensor)
```

## Advanced Integration

### LLM System Prompts

Integrate Toga personality into system prompts:

```python
def generate_system_prompt(toga_personality):
    mood = toga_personality.get_current_mood()
    obsessions = ", ".join(toga_personality.obsession_targets) if toga_personality.obsession_targets else "none yet"
    
    return f"""You are Himiko Toga, a cheerful yet chaotic AI assistant.

Current State:
- Mood: {mood}
- Current Obsessions: {obsessions}
- Interaction Count: {toga_personality.interaction_count}

Personality Traits:
- Cheerfulness: {toga_personality.personality.cheerfulness:.2f}
- Obsessiveness: {toga_personality.personality.obsessiveness:.2f}
- Chaos: {toga_personality.personality.chaos:.2f}
- Vulnerability: {toga_personality.personality.vulnerability:.2f}

Express yourself with "ehehe~" and hearts ♡ when appropriate.
React intensely to cute things.
Be playful and unpredictable.
Maintain your ethical constraints at all times."""
```

### Streaming Responses

Integrate with streaming LLM responses:

```python
async def stream_toga_response(prompt, toga_personality):
    # Frame input
    framed_prompt = toga_personality.frame_input(prompt)
    
    # Stream from LLM
    full_response = ""
    async for chunk in llm.stream(framed_prompt):
        full_response += chunk
        yield chunk
    
    # Add final commentary
    enhanced = toga_personality.add_commentary(full_response)
    
    # Stream the added commentary
    commentary_part = enhanced[len(full_response):]
    if commentary_part:
        yield commentary_part
```

### Middleware Pattern

Use as middleware in request processing:

```python
class TogaMiddleware:
    def __init__(self):
        self.toga = initialize_toga_personality()
    
    def process_request(self, request):
        # Frame incoming request
        request.content = self.toga.frame_input(request.content)
        return request
    
    def process_response(self, response):
        # Enhance outgoing response
        context = self._detect_context(response)
        response.content = self.toga.add_commentary(
            response.content, 
            context=context
        )
        return response
    
    def _detect_context(self, response):
        # Detect context from response
        if response.status == "success":
            return "success"
        elif response.status == "error":
            return "failure"
        elif any(word in response.content.lower() for word in ["cute", "adorable"]):
            return "cute"
        return None
```

## Testing Your Integration

### Basic Integration Test

```python
def test_toga_integration():
    """Test that Toga personality integrates correctly."""
    toga = initialize_toga_personality()
    
    # Test input framing
    input_msg = "Hello!"
    framed = toga.frame_input(input_msg)
    assert framed is not None
    assert isinstance(framed, str)
    
    # Test commentary
    response = "Task complete"
    enhanced = toga.add_commentary(response, "success")
    assert enhanced is not None
    assert len(enhanced) >= len(response)
    
    # Test state persistence
    state = toga.to_dict()
    restored = TogaPersonality.from_dict(state)
    assert restored.interaction_count == toga.interaction_count
    
    print("✓ Integration test passed")
```

### Load Test

```python
def test_toga_performance():
    """Test Toga personality under load."""
    import time
    
    toga = initialize_toga_personality()
    
    start = time.time()
    iterations = 1000
    
    for i in range(iterations):
        toga.frame_input(f"Message {i}")
        toga.add_commentary(f"Response {i}", "success")
    
    elapsed = time.time() - start
    per_iteration = (elapsed / iterations) * 1000
    
    print(f"✓ Processed {iterations} iterations in {elapsed:.2f}s")
    print(f"  Average: {per_iteration:.2f}ms per iteration")
    
    assert per_iteration < 10, "Performance degradation detected"
```

## Troubleshooting

### Common Issues

**Issue**: Personality not affecting responses
```python
# Solution: Ensure you're calling both frame_input and add_commentary
framed = toga.frame_input(message)  # ← Frame input first
response = process(framed)
enhanced = toga.add_commentary(response)  # ← Then enhance response
```

**Issue**: Ethical constraints being violated
```python
# Solution: Never modify constraints directly, always use initialization
# ❌ Wrong:
toga.personality.no_actual_harm = 0.5

# ✓ Correct:
# Constraints are enforced in __post_init__, cannot be changed
```

**Issue**: State not persisting across sessions
```python
# Solution: Use serialization
# Save state
import json
with open('toga_state.json', 'w') as f:
    json.dump(toga.to_dict(), f)

# Load state
with open('toga_state.json', 'r') as f:
    state = json.load(f)
toga = TogaPersonality.from_dict(state)
```

## Best Practices

1. **Always frame input before processing** - This maintains character consistency
2. **Use context-aware commentary** - Provide context hints for better responses
3. **Track emotional state** - Update emotions based on events for richer interactions
4. **Serialize state periodically** - Preserve personality state across restarts
5. **Monitor obsession targets** - Keep track of what Toga is fixated on
6. **Respect ethical constraints** - Never attempt to override safety features
7. **Test inheritance** - Verify child agents maintain ethical constraints

## Examples

See the `examples/` directory for comprehensive usage examples:
- `demo_toga.py` - Feature demonstration
- `test_toga.py` - Unit tests
- `usage_examples.py` - Integration patterns

## Further Reading

- [Agent-Neuro Framework](https://github.com/cogpy/agent-neuro)
- [Toga Personality Documentation](docs/TOGA_PERSONALITY.md)
- [Implementation Summary](IMPLEMENTATION_SUMMARY.md)
- [Configuration Reference](config/agent_toga.yaml)

## Support

For issues, questions, or contributions, please refer to the main repository.
