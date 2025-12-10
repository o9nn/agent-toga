# Agent-Zero-HCK Integration

**Integration of Agent-Toga with Agent-Zero Framework**

This directory contains the **Agent-Zero-HCK** (Himiko Toga Cognitive Kernel - Advanced) implementation, which integrates the Agent-Toga personality system with the Agent-Zero multi-agent orchestration framework.

## What is Agent-Zero-HCK?

Agent-Zero-HCK is an advanced multi-agent system that combines:

- **Agent-Toga** (this repository): Himiko Toga personality, Transform Quirk, security testing
- **Agent-Zero**: Multi-agent orchestration, tool ecosystem, memory systems
- **NPU Integration**: GGUF-backed LLM coprocessor (optional)
- **Cognitive Architecture**: AtomSpace, ontogenesis, relevance realization (optional)

## Relationship to Agent-Toga

Agent-Zero-HCK **extends** Agent-Toga by:

1. **Wrapping** the Toga personality modules in an Agent-Zero orchestration layer
2. **Adding** multi-agent coordination with subordinate spawning
3. **Integrating** with Agent-Zero's tool ecosystem
4. **Providing** deployment infrastructure for production use
5. **Enabling** optional cognitive enhancements (NPU, AtomSpace, etc.)

The core Toga personality modules (`python/helpers/toga_*.py`) remain **unchanged** and are reused directly.

## Directory Structure

```
agent-zero-hck/
├── agents/toga_hck/          # Main agent implementation
│   ├── agent.py              # AgentZeroHCK class
│   └── __init__.py
├── python/
│   └── helpers/              # Toga modules (copied from parent)
│       ├── toga_personality.py
│       ├── toga_transform.py
│       └── toga_security.py
├── config/                   # Configuration
├── prompts/                  # System prompts
├── Dockerfile                # Container definition
├── docker-compose.yml        # Multi-service orchestration
├── deploy.sh                 # Deployment automation
├── README.md                 # Main documentation
├── ARCHITECTURE.md           # Architecture details
├── DEPLOYMENT.md             # Deployment guide
└── IMPLEMENTATION_SUMMARY.md # Implementation summary
```

## Quick Start

### From Agent-Toga Repository

```bash
# Navigate to integration directory
cd agent-zero-hck

# Deploy standalone
./deploy.sh standalone

# Or run in development mode
./deploy.sh development
```

### As Standalone Repository

The agent-zero-hck implementation is also available as a standalone repository:

```bash
git clone https://github.com/cogpy/agent-zero-hck.git
cd agent-zero-hck
./deploy.sh standalone
```

## Key Differences from Base Agent-Toga

| Feature | Agent-Toga | Agent-Zero-HCK |
|---------|-----------|----------------|
| Personality System | ✅ Core | ✅ Integrated |
| Transform Quirk | ✅ Core | ✅ Integrated |
| Security Testing | ✅ Core | ✅ Integrated |
| Multi-Agent Orchestration | ❌ | ✅ Added |
| Subordinate Spawning | ❌ | ✅ Added |
| Tool Ecosystem | ❌ | ✅ Agent-Zero tools |
| Memory Systems | ❌ | ✅ Agent-Zero memory |
| Docker Deployment | ❌ | ✅ Full stack |
| Daedalos Integration | ❌ | ✅ Ready |
| NPU Coprocessor | ❌ | ✅ Optional |
| AtomSpace | ❌ | ✅ Optional |
| Ontogenesis | ❌ | ✅ Optional |

## Usage

### Basic Interaction

```python
from agents.toga_hck import initialize_agent_zero_hck

# Initialize agent
agent = initialize_agent_zero_hck()

# Process message with full orchestration
response = agent.process_message("Analyze this web application")
print(response)
```

### With Subordinates

```python
# Spawn subordinate for parallel work
recon_agent = agent.spawn_subordinate(
    role="reconnaissance",
    personality_inheritance=0.7
)

# Coordinate security test
findings = agent.coordinate_security_test(
    target="webapp.com",
    test_types=["recon", "vuln_scan", "exploit"],
    use_subordinates=True
)
```

## Documentation

- **[README.md](README.md)** - Project overview and quick start
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Detailed system architecture
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Comprehensive deployment guide
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Implementation details

## Deployment Options

### Standalone Mode
```bash
./deploy.sh standalone
```

### Daedalos Mode
```bash
export DAEDALOS_AUTH_TOKEN=your_token
ENABLE_DAEDALOS=true ./deploy.sh daedalos
```

### Development Mode
```bash
./deploy.sh development
```

### With Optional Services
```bash
# Enable AtomSpace
ENABLE_ATOMSPACE=true ./deploy.sh standalone

# Enable NPU
ENABLE_NPU=true ./deploy.sh standalone

# Enable all
ENABLE_ATOMSPACE=true ENABLE_NPU=true ./deploy.sh standalone
```

## Integration Notes

### Reusing Toga Modules

The agent-zero-hck implementation **reuses** the Toga personality modules from the parent repository without modification:

```python
# In agents/toga_hck/agent.py
from python.helpers.toga_personality import initialize_toga_personality
from python.helpers.toga_transform import initialize_transform_quirk
from python.helpers.toga_security import initialize_toga_security_tester
```

This ensures:
- No duplication of personality logic
- Updates to base Toga modules automatically propagate
- Consistent behavior across implementations

### Extending vs Replacing

Agent-Zero-HCK **extends** rather than **replaces** Agent-Toga:

- **Base Agent-Toga**: Standalone personality modules for any framework
- **Agent-Zero-HCK**: Specific integration with Agent-Zero for production use

Use **Agent-Toga** when:
- You want to integrate Toga personality into your own framework
- You need standalone personality modules
- You're building custom agent systems

Use **Agent-Zero-HCK** when:
- You want a production-ready multi-agent system
- You need Agent-Zero's orchestration capabilities
- You're deploying to Daedalos environment
- You want optional cognitive enhancements (NPU, AtomSpace)

## Contributing

Contributions to Agent-Zero-HCK should:

1. Maintain compatibility with base Agent-Toga modules
2. Follow Agent-Zero framework conventions
3. Include tests for new features
4. Update documentation

For changes to personality, Transform Quirk, or security testing, contribute to the base Agent-Toga repository.

## License

MIT License - Same as Agent-Toga

## Links

- **Agent-Toga Repository**: https://github.com/o9nn/agent-toga
- **Agent-Zero-HCK Standalone**: https://github.com/cogpy/agent-zero-hck
- **Agent-Zero Framework**: https://github.com/frdel/agent-zero

---

**"Ehehe~ ♡ Agent-Zero-HCK brings Toga's cheerful chaos to the Agent-Zero ecosystem!"**
