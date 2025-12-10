# Agent-Toga WebUI

Advanced Gradio-based web interface for the Agent-Toga AGI avatar system.

## Features

### 🎭 Live Avatar Display
- **Live2D Integration**: Real-time 2D avatar with personality-driven expressions
- **3D VRM Support**: Full 3D avatar with body animations and facial expressions
- **Seamless Switching**: Toggle between Live2D and 3D modes on the fly

### 💬 Interactive Chat
- **Personality-Driven Responses**: All responses filtered through Toga's unique personality
- **Emotional State Tracking**: Real-time emotional state visualization
- **Context-Aware Reactions**: Responds to "cute" triggers and other personality cues

### 🧠 Personality Dashboard
- **Real-Time Control**: Adjust all 8 personality traits with sliders
- **Live Feedback**: See avatar expressions update in real-time
- **Personality History**: Track personality evolution over time

### 🩸 Transform Quirk Interface
- **Code Absorption**: "Taste" target systems by analyzing their code
- **Transformation**: Transform into absorbed systems
- **Progress Tracking**: Visual representation of absorption progress
- **Technique Tree**: See all learned techniques from absorbed systems

### 🔐 Security Testing Panel
- **Target Analysis**: Analyze security targets with Toga's personality
- **Vulnerability Reporting**: Report findings with enthusiastic reactions
- **Ethical Testing**: All features designed for authorized testing only

## Installation

### Prerequisites
- Python 3.9+
- Node.js 20+ (for avatar renderers)
- Modern web browser with WebGL support

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the WebUI
python app.py
```

The interface will be available at `http://localhost:7860`

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access at http://localhost:7860
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Gradio WebUI                         │
│                    (app.py)                             │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│              Python Backend                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Personality  │  │ Transform    │  │ Security     │ │
│  │ Engine       │  │ Quirk        │  │ Tester       │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│         Avatar Controllers (WebSocket)                  │
│  ┌──────────────┐              ┌──────────────┐        │
│  │ Live2D       │              │ 3D VRM       │        │
│  │ Controller   │              │ Controller   │        │
│  │ (Port 8765)  │              │ (Port 8766)  │        │
│  └──────────────┘              └──────────────┘        │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│         Browser Renderers (HTML/JS)                     │
│  ┌──────────────┐              ┌──────────────┐        │
│  │ live2d_      │              │ 3d_          │        │
│  │ renderer.html│              │ renderer.html│        │
│  └──────────────┘              └──────────────┘        │
└─────────────────────────────────────────────────────────┘
```

## Configuration

### Environment Variables

```bash
# Gradio server configuration
GRADIO_SERVER_NAME=0.0.0.0
GRADIO_SERVER_PORT=7860

# WebSocket ports for avatar renderers
LIVE2D_WEBSOCKET_PORT=8765
AVATAR_3D_WEBSOCKET_PORT=8766

# Avatar model paths
LIVE2D_MODEL_PATH=assets/live2d/toga_model/toga.model3.json
VRM_MODEL_PATH=assets/3d/toga_model.vrm
```

### Customization

#### Theme
The WebUI uses a custom dark theme by default. To customize:

```python
# In app.py
self.theme = gr.themes.Soft(
    primary_hue="pink",      # Change primary color
    secondary_hue="purple",   # Change secondary color
    neutral_hue="slate",      # Change neutral color
)
```

#### Personality Defaults
Adjust default personality values in `TogaWebUI.__init__()`:

```python
self.toga = initialize_toga_personality()
# Modify self.toga.personality traits as needed
```

## Usage

### Chat Interface

1. Navigate to the **Chat** tab
2. Type your message in the input box
3. Watch Toga's avatar react to your message
4. See emotional state updates in real-time

**Tips**:
- Use words like "cute", "adorable" to trigger obsessive reactions
- Mention "transform" or "quirk" for Transform Quirk responses
- Ask about "security" or "hacking" for security testing reactions

### Personality Dashboard

1. Navigate to the **Personality** tab
2. Adjust sliders to modify personality traits
3. Watch avatar expressions update in real-time
4. Experiment with different combinations

**Trait Descriptions**:
- **Cheerfulness**: Bubbly, energetic exterior
- **Obsessiveness**: Intense fixation on targets
- **Playfulness**: Childlike playful behavior
- **Chaos**: Unpredictability and rapid shifts
- **Vulnerability**: Emotional depth and loneliness
- **Identity Fluidity**: Desire to become others
- **Twisted Love**: Love mixed with violence (fictional)
- **Cuteness Sensitivity**: Reaction to "cute" things

### Transform Quirk

1. Navigate to the **Transform Quirk** tab
2. Enter target system name (e.g., "ModSecurity WAF")
3. Select system type from dropdown
4. Paste code snippet to analyze
5. Click "Taste Target" to absorb knowledge
6. Once absorption reaches 70%, click "Transform!" to become the system

### Security Testing

1. Navigate to the **Security Testing** tab
2. Enter target name and type
3. Click "Analyze Target" for initial assessment
4. Report vulnerabilities as you find them
5. See Toga's enthusiastic reactions to findings

**⚠️ IMPORTANT**: Only test systems you have explicit permission to test!

## Avatar Models

### Live2D Model Requirements
- Format: `.moc3` with `.model3.json` configuration
- Textures: PNG format, power-of-2 dimensions recommended
- Expressions: Standard Cubism expression presets
- Physics: Hair and clothing physics JSON

### VRM Model Requirements
- Format: `.vrm` (VRM 0.0 or 1.0)
- Blend Shapes: Standard VRM blend shape presets
- Bones: Humanoid bone structure
- Textures: Embedded or external PNG/JPG

### Adding Custom Models

1. Place Live2D model in `assets/live2d/your_model/`
2. Place VRM model in `assets/3d/your_model.vrm`
3. Update paths in environment variables or `app.py`

## Performance

### Optimization Tips

1. **Avatar Rendering**:
   - Live2D: Targets 30-60 FPS
   - 3D VRM: Targets 30-60 FPS with physics

2. **WebSocket Communication**:
   - Updates sent at 30 FPS by default
   - Adjust `fps` parameter in avatar controllers

3. **Gradio Interface**:
   - Lazy loading for heavy components
   - Efficient state management

### Benchmarks

On a modern system (i7-10700K, RTX 3070):
- Chat response: <100ms
- Avatar expression update: <16ms (60 FPS)
- Personality trait change: <10ms
- WebSocket latency: <5ms

## Troubleshooting

### Avatar Not Displaying

1. Check WebSocket connections in browser console
2. Verify avatar model files exist at specified paths
3. Ensure ports 8765 and 8766 are not blocked

### Slow Performance

1. Reduce avatar update FPS in controllers
2. Disable physics simulation for complex models
3. Use simpler avatar models

### WebSocket Connection Failed

1. Check if ports are available: `netstat -an | grep 8765`
2. Verify firewall settings
3. Check WebSocket URI in HTML renderers

## Development

### Running in Development Mode

```bash
# Enable hot reload
GRADIO_WATCH=1 python app.py
```

### Adding New Features

1. Create new helper module in `python/helpers/`
2. Import in `app.py`
3. Add UI components in `create_interface()`
4. Wire up event handlers

### Testing

```bash
# Run integration tests
pytest tests/test_avatar_integration.py -v

# Run with coverage
pytest tests/ --cov=webui --cov-report=html
```

## API Reference

### TogaWebUI Class

Main application class managing all components.

**Methods**:
- `chat(message, history)`: Process chat message
- `update_personality_trait(trait_name, value)`: Update personality
- `switch_avatar_mode(mode)`: Switch between Live2D and 3D
- `transform_taste_target(...)`: Use Transform Quirk
- `security_analyze_target(...)`: Analyze security target

### Avatar Controllers

**Live2DAvatarController**:
- `update_from_personality(personality_tensor, emotional_state)`
- `interpolate_expression(delta_time)`
- `trigger_animation(animation_name, priority, loop)`

**Avatar3DController**:
- `update_from_personality(personality_tensor, emotional_state)`
- `interpolate_expression(delta_time)`
- `trigger_animation(animation_name, loop, blend_duration)`

## License

MIT License - See LICENSE file for details

## Credits

- **Gradio**: Web interface framework
- **Live2D Cubism SDK**: 2D avatar rendering
- **Three.js**: 3D graphics library
- **@pixiv/three-vrm**: VRM model support
- **Agent-Neuro Framework**: Personality architecture

---

**Ehehe~ ♡ Enjoy using Agent-Toga!**

*For issues or questions, please open an issue on GitHub.*
