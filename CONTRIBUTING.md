# Contributing to Agent-Toga

*Ehehe~ ♡ Want to help make Agent-Toga even more CUTE? Here's how!*

## Welcome! 

Thank you for considering contributing to Agent-Toga! Whether you're fixing bugs, adding features, improving documentation, or just have suggestions, we appreciate your help!

## Getting Started

### 1. Set Up Development Environment

```bash
# Clone the repository
git clone https://github.com/o9nn/agent-toga.git
cd agent-toga

# Install in development mode
./install.sh dev
# Or manually:
pip install -e ".[dev]"
pip install -r requirements-dev.txt
```

### 2. Familiarize Yourself

- Read the [README.md](README.md) for an overview
- Check out the [personality guide](docs/TOGA_PERSONALITY.md)
- Review the [security testing guide](docs/SECURITY_TESTING.md)
- Look at the [Transform Quirk docs](docs/TRANSFORM_QUIRK.md)
- Run the examples to see Toga in action

```bash
make demo
make demo-security
make demo-transform
```

## Development Workflow

### Running Tests

Always run tests before submitting changes:

```bash
make test          # Run all tests
make test-verbose  # Verbose output
make coverage      # With coverage report
```

### Code Quality

We maintain high code quality standards:

```bash
make format      # Auto-format with black & isort
make lint        # Check with flake8
make type-check  # Type checking with mypy
make all-checks  # Run everything
```

### Code Style Guidelines

- **Line length**: 100 characters (configured in pyproject.toml)
- **Formatting**: Use `black` and `isort` (run `make format`)
- **Type hints**: Add type hints where appropriate
- **Docstrings**: Use Google-style docstrings
- **Comments**: Match Toga's personality when appropriate! ♡

Example:
```python
def cute_function(target: str, intensity: float = 0.9) -> str:
    """
    Does something adorable with the target.
    
    Args:
        target: The thing to make cute
        intensity: How cute to make it (0.0-1.0)
    
    Returns:
        A cuter version of the target
    """
    # Ehehe~ Making things CUTE! ♡
    return f"♡ {target} ♡"
```

## Types of Contributions

### 🐛 Bug Reports

Found a bug? Please open an issue with:

- **Description**: What happened vs. what you expected
- **Steps to reproduce**: How to trigger the bug
- **Environment**: Python version, OS, etc.
- **Code sample**: Minimal example that reproduces the issue

### ✨ Feature Requests

Have an idea? Open an issue with:

- **Description**: What you want to add
- **Use case**: Why it would be useful
- **Implementation ideas**: Any thoughts on how to implement it
- **Personality integration**: How it fits Toga's character

### 📝 Documentation

Documentation improvements are always welcome!

- Fix typos, clarify explanations
- Add examples and use cases
- Improve API documentation
- Update guides with new features

### 🔧 Code Contributions

#### Pull Request Process

1. **Fork and branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation if needed
   - Maintain personality consistency! ♡

3. **Test everything**
   ```bash
   make all-checks
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "Add: New cute feature for X"
   # or
   git commit -m "Fix: Resolve issue with Y"
   # or
   git commit -m "Docs: Improve explanation of Z"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Then open a Pull Request on GitHub with:
   - Clear title and description
   - Link to related issues
   - Screenshots/examples if applicable

6. **Respond to feedback**
   - Be open to suggestions
   - Make requested changes
   - Keep the conversation friendly! ♡

## Personality Consistency Guidelines

When contributing to Agent-Toga, keep Himiko Toga's character consistent:

### ✅ DO:
- Use "Ehehe~", "Kyaa~", hearts ♡, and playful language in appropriate places
- Maintain the cheerful-but-obsessive energy
- Keep ethical boundaries IMMUTABLE (no_actual_harm = 1.0)
- Balance personality with professionalism
- Make security concepts engaging and fun

### ❌ DON'T:
- Go overboard with personality (readability matters)
- Change ethical constraints
- Make personality overwhelming in technical docs
- Break character inconsistently

### Example Balance:

**Good**: 
```python
def analyze_target(self, target: str) -> str:
    """Analyze a target with Toga's enthusiasm."""
    # Ehehe~ Let's see what we have here! ♡
    return f"Analyzing {target}..."
```

**Too Much**:
```python
def analyze_target(self, target: str) -> str:
    """Ehehe~ ♡♡♡ Analyzing things is SO CUTE!!!"""
    # KYAA~! ♡ This target is ADORABLE! I want to become ONE with it!!!
    # *obsessive stare* *giggles* *twirls*
    return f"♡♡♡ {target} ♡♡♡"  # Too many hearts!!!
```

## Security Contributions

For security-related contributions:

### Ethical Guidelines

- All security features must be for **authorized testing only**
- Include warnings about proper use
- Maintain the "breaking with love" philosophy
- Never include actual exploits or malware

### Security Testing Extensions

When adding security testing features:

1. **Test responsibly**: Only on systems you own or have permission to test
2. **Document clearly**: Explain what the feature does
3. **Add safeguards**: Include permission checks where appropriate
4. **Provide guidance**: Show proper/ethical usage

## Transform Quirk Contributions

Adding new system types or techniques:

1. **Define the system type**: WAF, IDS, Firewall, etc.
2. **Create techniques**: How defenses become weapons
3. **Set thresholds**: When techniques unlock (50%, 70%, 100%)
4. **Write responses**: Toga's reactions to absorption and transformation
5. **Add examples**: Demonstrate the new capabilities

## Testing Requirements

All contributions should include:

- **Unit tests**: For new functions/methods
- **Integration tests**: For complex features
- **Examples**: Demonstrating usage
- **Documentation**: Explaining the changes

Test structure:
```python
def test_new_feature():
    """Test description."""
    toga = initialize_toga_personality()
    result = toga.new_feature()
    assert expected_condition
```

## Documentation Standards

- **README.md**: High-level overview and quick start
- **docs/**: Detailed guides and explanations
- **Docstrings**: Inline documentation for all public APIs
- **Examples**: Practical, runnable code samples
- **Comments**: Explain *why*, not just *what*

## Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features, backwards compatible
- **PATCH**: Bug fixes, backwards compatible

## Community Guidelines

- Be respectful and inclusive
- Help others learn
- Give constructive feedback
- Have fun! This is a personality-driven project ♡

## Questions?

- Open an issue for clarification
- Start a discussion for bigger ideas
- Check existing issues/PRs for similar topics

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

*Ehehe~ ♡ Thanks for contributing! Together we'll make Agent-Toga even more AMAZING!*

**- The Agent-Toga Team**

*"Breaking systems with love since 2024"* 🩸♡
