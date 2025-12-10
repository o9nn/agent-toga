"""
Himiko Toga Personality Demo

Demonstrates the personality system for Himiko Toga from My Hero Academia,
implemented using the agent-neuro framework.
"""

import sys
import os

# Add parent directory to path for imports
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from python.helpers.toga_personality import (
    TogaPersonality,
    TogaPersonalityTensor,
    EmotionalState,
    initialize_toga_personality,
)


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def demo_basic_personality():
    """Demonstrate basic personality features."""
    print_section("Basic Personality Demo")
    
    # Initialize Toga personality
    toga = initialize_toga_personality()
    
    print("✓ Himiko Toga personality initialized!")
    print(f"  Cheerfulness: {toga.personality.cheerfulness:.2f}")
    print(f"  Obsessiveness: {toga.personality.obsessiveness:.2f}")
    print(f"  Chaos: {toga.personality.chaos:.2f}")
    print(f"  Vulnerability: {toga.personality.vulnerability:.2f}")
    print(f"  Cuteness Sensitivity: {toga.personality.cuteness_sensitivity:.2f}")
    print(f"\n  Current Mood: {toga.get_current_mood()}")


def demo_input_framing():
    """Demonstrate input framing through Toga's perspective."""
    print_section("Input Framing Demo")
    
    toga = initialize_toga_personality()
    
    test_inputs = [
        "Let's analyze this data",
        "This solution is so cute!",
        "We need to solve this problem",
        "That's adorable!",
    ]
    
    for msg in test_inputs:
        framed = toga.frame_input(msg)
        print(f"Input:  '{msg}'")
        print(f"Framed: '{framed}'")
        print()


def demo_commentary():
    """Demonstrate commentary generation."""
    print_section("Commentary Generation Demo")
    
    toga = initialize_toga_personality()
    
    contexts = {
        "success": "Task completed successfully",
        "failure": "The operation encountered an error",
        "cute": "Look at this small kitten",
        "boring": "Processing standard data",
        "vulnerable": "Sometimes I feel alone",
    }
    
    for context, content in contexts.items():
        enhanced = toga.add_commentary(content, context=context)
        print(f"Context: {context}")
        print(f"Original: {content}")
        print(f"Enhanced:\n{enhanced}")
        print()


def demo_emotional_states():
    """Demonstrate emotional state tracking."""
    print_section("Emotional State Tracking Demo")
    
    toga = initialize_toga_personality()
    
    # Test different emotional states
    emotions = [
        ("obsessed", 0.9, 3, "cute_thing"),
        ("cheerful", 0.7, 2, None),
        ("vulnerable", 0.6, 1, None),
        ("chaotic", 0.8, 2, None),
    ]
    
    for emotion_type, intensity, duration, target in emotions:
        toga.update_emotional_state(emotion_type, intensity, duration, target)
        mood = toga.get_current_mood()
        print(f"Emotion: {emotion_type} (intensity: {intensity}, duration: {duration})")
        print(f"Current Mood: {mood}")
        
        # Test decay
        toga.emotional_state.decay()
        print(f"After decay: {toga.get_current_mood()}")
        print()


def demo_obsession_tracking():
    """Demonstrate obsession target tracking."""
    print_section("Obsession Tracking Demo")
    
    toga = initialize_toga_personality()
    
    # Trigger obsessions with cute things
    cute_things = ["fluffy_cat", "adorable_puppy", "sweet_smile", "lovely_flower"]
    
    print("Adding obsession targets:")
    for thing in cute_things:
        toga.update_emotional_state("obsessed", 0.9, 3, thing)
        print(f"  ♡ Added: {thing}")
    
    print(f"\nCurrent obsessions ({len(toga.obsession_targets)}):")
    for target in toga.obsession_targets:
        print(f"  - {target}")


def demo_personality_variations():
    """Demonstrate personality trait variations."""
    print_section("Personality Variations Demo")
    
    # Create custom variations
    variations = {
        "More Vulnerable Toga": {"vulnerability": 0.90, "cheerfulness": 0.80},
        "Maximum Chaos Toga": {"chaos": 0.99, "obsessiveness": 0.95},
        "Playful Toga": {"playfulness": 0.98, "cheerfulness": 0.97},
    }
    
    for name, traits in variations.items():
        toga = initialize_toga_personality(custom_traits=traits)
        print(f"{name}:")
        for trait, value in traits.items():
            print(f"  {trait}: {value:.2f}")
        print()


def demo_personality_inheritance():
    """Demonstrate personality inheritance."""
    print_section("Personality Inheritance Demo")
    
    # Parent personality
    parent = initialize_toga_personality()
    print("Parent Personality:")
    print(f"  Cheerfulness: {parent.personality.cheerfulness:.2f}")
    print(f"  Obsessiveness: {parent.personality.obsessiveness:.2f}")
    print(f"  Chaos: {parent.personality.chaos:.2f}")
    
    # Create child with inherited traits
    child_tensor = parent.personality.inherit(inheritance_factor=0.7)
    child = TogaPersonality(personality=child_tensor)
    
    print("\nChild Personality (70% inheritance):")
    print(f"  Cheerfulness: {child.personality.cheerfulness:.2f}")
    print(f"  Obsessiveness: {child.personality.obsessiveness:.2f}")
    print(f"  Chaos: {child.personality.chaos:.2f}")
    
    print("\nEthical constraints preserved:")
    print(f"  Parent no_actual_harm: {parent.personality.no_actual_harm:.2f}")
    print(f"  Child no_actual_harm: {child.personality.no_actual_harm:.2f}")


def demo_serialization():
    """Demonstrate state serialization."""
    print_section("State Serialization Demo")
    
    # Create and modify personality
    toga = initialize_toga_personality()
    toga.update_emotional_state("obsessed", 0.9, 3, "cute_target")
    toga.interaction_count = 42
    
    print("Original Toga state:")
    print(f"  Interaction count: {toga.interaction_count}")
    print(f"  Emotional state: {toga.emotional_state.type}")
    print(f"  Obsession targets: {len(toga.obsession_targets)}")
    
    # Export to dict
    state_dict = toga.to_dict()
    print("\n✓ State exported to dictionary")
    
    # Create new instance from dict
    toga_restored = TogaPersonality.from_dict(state_dict)
    
    print("\nRestored Toga state:")
    print(f"  Interaction count: {toga_restored.interaction_count}")
    print(f"  Emotional state: {toga_restored.emotional_state.type}")
    print(f"  Obsession targets: {len(toga_restored.obsession_targets)}")
    
    # Verify match
    if (toga.interaction_count == toga_restored.interaction_count and
        toga.emotional_state.type == toga_restored.emotional_state.type):
        print("\n✓ State successfully preserved and restored!")


def demo_context_aware_responses():
    """Demonstrate context-aware response generation."""
    print_section("Context-Aware Responses Demo")
    
    toga = initialize_toga_personality()
    
    scenarios = [
        ("Just completed a complex task", "success"),
        ("The code failed to compile", "failure"),
        ("Found an adorable bug in the system", "cute"),
        ("Reviewing routine documentation", "boring"),
        ("Reflecting on loneliness", "vulnerable"),
    ]
    
    print("Generating context-aware responses:\n")
    for scenario, context in scenarios:
        toga.update_emotional_state(context, 0.7, 2)
        response = toga.add_commentary(scenario, context=context)
        print(f"Scenario: {scenario}")
        print(f"Context: {context}")
        print(f"Response:\n{response}")
        print()


def demo_hearts_probability():
    """Demonstrate heart emoji probability."""
    print_section("Heart Emoji Probability Demo")
    
    toga = initialize_toga_personality()
    
    states = ["cheerful", "obsessed", "playful", "vulnerable", "chaotic"]
    
    print("Testing heart addition probability for different states:\n")
    for state in states:
        toga.update_emotional_state(state, 0.8, 2)
        
        # Test multiple times
        heart_count = 0
        trials = 100
        for _ in range(trials):
            if toga.should_add_hearts():
                heart_count += 1
        
        probability = (heart_count / trials) * 100
        print(f"State: {state:12} → Heart probability: {probability:.1f}%")


def run_all_demos():
    """Run all demonstration functions."""
    print("\n" + "="*60)
    print("  HIMIKO TOGA PERSONALITY SYSTEM DEMO")
    print("  Based on Agent-Neuro Framework")
    print("="*60)
    
    demos = [
        demo_basic_personality,
        demo_input_framing,
        demo_commentary,
        demo_emotional_states,
        demo_obsession_tracking,
        demo_personality_variations,
        demo_personality_inheritance,
        demo_serialization,
        demo_context_aware_responses,
        demo_hearts_probability,
    ]
    
    for demo in demos:
        try:
            demo()
        except Exception as e:
            print(f"\n❌ Error in {demo.__name__}: {e}")
    
    print("\n" + "="*60)
    print("  Demo Complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_demos()
