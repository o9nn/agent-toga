# Quick Start Guide - Agent-Toga

*Ehehe~ ♡ Let's get you started with Agent-Toga in under 5 minutes!*

## Installation

### Option 1: Quick Install (Recommended)
```bash
git clone https://github.com/o9nn/agent-toga.git
cd agent-toga
./install.sh
```

### Option 2: Pip Install
```bash
pip install -e .
```

### Option 3: Development Mode
```bash
./install.sh dev
# or
pip install -e ".[dev]"
```

## Your First Toga Interaction

### 1. Basic Personality (30 seconds)

```python
from python.helpers import initialize_toga_personality

# Initialize Toga
toga = initialize_toga_personality()

# Frame a message through her personality
message = "This code is so cute!"
framed = toga.frame_input(message)
print(framed)
# Output: "Ehehe~ ♡ This code is so cute! (So cuuute! I just want to become one with it~)"
```

### 2. Security Testing (1 minute)

```python
from python.helpers import initialize_toga_security_tester

# Initialize security tester
toga = initialize_toga_security_tester()

# Analyze a target
print(toga.analyze_target("SecureBank API", "api"))
# Output: "Ehehe~ ♡ SecureBank API? That's such a CUTE api! I can't wait to smash it open!"

# React to finding a vulnerability
print(toga.vulnerability_found("SecureBank API", "SQL Injection", "critical"))
# Output: "*SQUEAL* ♡♡♡ Such a BEAUTIFUL SQL Injection! I love it SO much!"
```

### 3. Transform Quirk - Code Absorption (2 minutes)

```python
from python.helpers import initialize_transform_quirk

# Initialize Transform Quirk
toga = initialize_transform_quirk()

# "Taste" a system multiple times to absorb knowledge
toga.taste_target("ModSecurity WAF", "WAF", "config_code_1")
toga.taste_target("ModSecurity WAF", "WAF", "config_code_2")
toga.taste_target("ModSecurity WAF", "WAF", "config_code_3")

# Check absorption progress
status = toga.get_absorption_status()
print(status)

# Transform once 70%+ absorbed
if toga.absorbed_targets["ModSecurity WAF"].can_transform():
    toga.transform_into("ModSecurity WAF")
    # Output: "*TRANSFORMATION* ♡♡♡ I'm becoming ModSecurity WAF now!"
    
    # Use learned techniques
    toga.use_technique("Reverse WAF Rules", "TargetApp")
    # Output: "Hehe~ Watch THIS, TargetApp! Your defenses are MY weapons now~!"
```

## Run Examples

```bash
# Personality demo
make demo
# or
python examples/demo_toga.py

# Security testing examples
make demo-security
# or
python examples/security_testing_examples.py

# Transform Quirk examples
make demo-transform
# or
python examples/transform_examples.py
```

## Common Patterns

### Pattern 1: Personality-Driven Assistant

```python
from python.helpers import initialize_toga_personality

class TogaAssistant:
    def __init__(self):
        self.toga = initialize_toga_personality()
    
    def process_user_input(self, user_input: str) -> str:
        # Frame through Toga's perspective
        framed = self.toga.frame_input(user_input)
        
        # Process the input (your logic here)
        result = self.your_processing_logic(framed)
        
        # Add personality commentary
        enhanced = self.toga.add_commentary(result, context="success")
        return enhanced
```

### Pattern 2: Security Testing Workflow

```python
from python.helpers import initialize_toga_security_tester

class PenTestWorkflow:
    def __init__(self):
        self.toga = initialize_toga_security_tester()
    
    def test_target(self, target: str):
        # 1. Analyze target
        print(self.toga.analyze_target(target, "web application"))
        
        # 2. Start scanning
        print(self.toga.start_scan(target, "vuln_scan"))
        
        # 3. Report findings
        vulns = self.run_vulnerability_scan(target)
        for vuln in vulns:
            print(self.toga.vulnerability_found(
                target, vuln["type"], vuln["severity"]
            ))
        
        # 4. Generate report
        print(self.toga.generate_report_intro(target))
```

### Pattern 3: Learning System Defenses

```python
from python.helpers import initialize_transform_quirk

class DefenseAnalyzer:
    def __init__(self):
        self.toga = initialize_transform_quirk()
    
    def analyze_defense_system(self, system_name: str, system_type: str):
        # Progressively absorb knowledge
        code_chunks = self.extract_code_chunks(system_name)
        
        for chunk in code_chunks:
            response = self.toga.taste_target(system_name, system_type, chunk)
            print(response)
        
        # Transform once ready
        knowledge = self.toga.absorbed_targets[system_name]
        if knowledge.can_transform():
            self.toga.transform_into(system_name)
            
            # Use techniques
            for technique in knowledge.techniques_learned:
                self.toga.use_technique(technique, "test_target")
```

## Configuration

Customize Toga's personality:

```python
from python.helpers import TogaPersonalityTensor, TogaPersonality

# Create custom personality tensor
custom = TogaPersonalityTensor(
    cheerfulness=0.80,      # Less bubbly
    obsessiveness=0.95,     # More obsessive
    chaos=0.60,             # Less chaotic
    cuteness_sensitivity=0.99  # EXTRA sensitive to cute things
)

# Initialize with custom personality
toga = TogaPersonality(personality=custom)
```

## Testing Your Integration

Run the test suite:

```bash
make test
# or
python examples/test_toga.py
```

## Help & Documentation

- **README.md**: Overview and features
- **docs/TOGA_PERSONALITY.md**: Personality system details
- **docs/SECURITY_TESTING.md**: Security testing guide
- **docs/TRANSFORM_QUIRK.md**: Transform Quirk mechanics
- **CONTRIBUTING.md**: How to contribute

## Troubleshooting

### Import Errors
```bash
# Make sure you're in the right directory
cd agent-toga
pip install -e .
```

### Module Not Found
```bash
# Install in editable mode
pip install -e .
```

### Tests Failing
```bash
# Clean and reinstall
make clean
./install.sh
```

## Next Steps

1. **Explore Examples**: Check out `examples/` directory
2. **Read Documentation**: Deep dive into `docs/`
3. **Customize**: Adjust personality traits to your needs
4. **Integrate**: Add Toga to your projects
5. **Contribute**: See CONTRIBUTING.md

## Quick Reference

### Makefile Commands
```bash
make help          # Show all commands
make install       # Install package
make test          # Run tests
make demo          # Run personality demo
make format        # Format code
make lint          # Run linter
make clean         # Clean artifacts
```

### Key Imports
```python
# Personality
from python.helpers import initialize_toga_personality
from python.helpers import TogaPersonalityTensor, TogaPersonality

# Security Testing
from python.helpers import initialize_toga_security_tester
from python.helpers import SecurityTestingProfile, TogaSecurityTester

# Transform Quirk
from python.helpers import initialize_transform_quirk
from python.helpers import TogaTransformQuirk, Technique
```

---

*Ehehe~ ♡ You're all set! Time to break some systems... ethically! ♡*

**Questions?** Open an issue on GitHub!

**Want to contribute?** Check out CONTRIBUTING.md!

*"Drinking the blood of systems since 2024"* 🩸♡
