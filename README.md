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

## 🩸 Transform Quirk - Code Absorption System

**"Once I taste your code... I can become you~ ♡"**

Toga's signature ability: By "drinking the blood" (absorbing knowledge) of systems and codebases, she learns to transform and use their abilities - **turning defenses into offensive weapons!**

```python
from python.helpers.toga_transform import initialize_transform_quirk

toga = initialize_transform_quirk()

# "Taste" a system by analyzing its code
print(toga.taste_target("ModSecurity WAF", "WAF", waf_config_code))
# "*savoring* Ooh~ ModSecurity WAF has a unique flavor! I need to drink more~"

# Absorb more knowledge (70% needed to transform)
toga.taste_target("ModSecurity WAF", "WAF", more_config)
toga.taste_target("ModSecurity WAF", "WAF", even_more_config)

# Transform into the system!
print(toga.transform_into("ModSecurity WAF"))
# "*TRANSFORMATION* ♡♡♡ I'm becoming ModSecurity WAF now!"
# "Available techniques: Reverse WAF Rules, WAF Weaponization"

# Use their defenses as YOUR weapons
print(toga.use_technique("Reverse WAF Rules", "TargetApp"))
# "Ehehe~ Their own defense is destroying them! So ironic~!"
```

**Techniques Learned by System Type:**
- **WAF**: Reverse engineer rules, weaponize blocking patterns
- **IDS**: Signature evasion, alert flooding
- **Firewall**: Rule inversion, ACL tunneling
- **Authentication**: Token forgery, session hijacking
- **Encryption**: Crypto oracle attacks, key extraction
- **Logging**: Log injection, log poisoning

## 🔐 Security Testing Extension

**"Violence as Affection" - Breaking Systems Because We Love Them ♡**

Toga's obsessive and "violent" tendencies are channeled into ethical hacking:
- **Obsessiveness** → Thorough vulnerability analysis
- **"Violence as affection"** → Aggressive testing with good intentions
- **Playfulness** → Creative exploit approaches
- **"Becoming one"** → Deep system penetration (ethical)

```python
from python.helpers.toga_security import initialize_toga_security_tester

toga = initialize_toga_security_tester()

# Target analysis
print(toga.analyze_target("SecureBank API", "api"))
# "Ehehe~ ♡ That's such a CUTE api! I can't wait to smash it open!"

# Vulnerability discovery
print(toga.vulnerability_found("SecureBank API", "SQL Injection", "critical"))
# "*GASP* ♡♡♡ Such a BEAUTIFUL SQL Injection! I love it SO much!"

# Exploitation
print(toga.exploit_success("SecureBank API", "SQLi payload"))
# "*SQUEAL* ♡♡♡ I'M IN! We're one now~ Ehehe!"
```

Perfect for: Penetration testing, red-teaming, security assessments, CTF challenges

⚠️ **ETHICAL USE ONLY** - Only test systems you have permission to test!

## 🚀 Quick Start

### General Personality

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

### Transform Quirk (Code Absorption)

```python
from python.helpers.toga_transform import initialize_transform_quirk

toga = initialize_transform_quirk()

# Absorb knowledge from systems
toga.taste_target("JWT Auth", "Authentication", auth_code)
toga.taste_target("JWT Auth", "Authentication", more_code)

# Transform and use their techniques
toga.transform_into("JWT Auth")
toga.use_technique("Token Forgery", "ProductionAPI")
```

### Security Testing

```python
from python.helpers.toga_security import initialize_toga_security_tester

toga = initialize_toga_security_tester()

# Analyze target with enthusiasm
print(toga.analyze_target("webapp.com", "web application"))

# React to findings
print(toga.vulnerability_found("webapp.com", "XSS", "high"))

# Generate personality-driven reports
print(toga.generate_report_intro("webapp.com"))
```

## 📖 Documentation

- **[Toga Personality Guide](docs/TOGA_PERSONALITY.md)** - Complete personality documentation
- **[Transform Quirk Guide](docs/TRANSFORM_QUIRK.md)** - Code absorption system ⭐ NEW
- **[Security Testing Guide](docs/SECURITY_TESTING.md)** - Ethical hacking with Toga
- **[Integration Guide](docs/INTEGRATION_GUIDE.md)** - Agent-neuro framework integration
- **[Configuration](config/agent_toga.yaml)** - Personality settings

## 🎯 Run Examples

```bash
# General personality demo
python examples/demo_toga.py

# Transform Quirk examples
python examples/transform_examples.py

# Security testing examples
python examples/security_testing_examples.py

# Unit tests
python examples/test_toga.py

# Usage patterns
python examples/usage_examples.py
```

## 🧠 Based On

- **[Agent-Neuro Framework](https://github.com/cogpy/agent-neuro)** - Personality-driven cognitive architecture
- **My Hero Academia** - Character by Kōhei Horikoshi

## 📜 License

MIT License
## 🤖 Agent-Zero Integration

**NEW:** Agent-Toga now includes **Agent-Zero-HCK** integration!

Agent-Zero-HCK combines Agent-Toga's personality with the [Agent-Zero](https://github.com/frdel/agent-zero) multi-agent orchestration framework for production deployment.

### Features

- **Multi-Agent Orchestration**: Spawn subordinates with inherited personality
- **Tool Ecosystem**: Full Agent-Zero tool integration
- **Docker Deployment**: Production-ready containerization
- **Daedalos Integration**: Deploy to distributed agent environments
- **Optional Enhancements**: NPU coprocessor, AtomSpace, ontogenesis

### Quick Start

```bash
# Navigate to integration directory
cd agent-zero-hck

# Deploy standalone
./deploy.sh standalone

# Or with Daedalos
export DAEDALOS_AUTH_TOKEN=your_token
ENABLE_DAEDALOS=true ./deploy.sh daedalos
```

### Documentation

- **[Integration Guide](agent-zero-hck/INTEGRATION.md)** - How Agent-Zero-HCK relates to Agent-Toga
- **[Architecture](agent-zero-hck/ARCHITECTURE.md)** - Detailed system design
- **[Deployment](agent-zero-hck/DEPLOYMENT.md)** - Comprehensive deployment guide
- **[Standalone Repository](https://github.com/cogpy/agent-zero-hck)** - Agent-Zero-HCK as separate repo

### Relationship

- **Agent-Toga** (this repo): Core personality modules, Transform Quirk, security testing
- **Agent-Zero-HCK**: Production integration with Agent-Zero framework

Agent-Zero-HCK **extends** Agent-Toga by wrapping the personality modules in an orchestration layer while keeping the core modules unchanged.

