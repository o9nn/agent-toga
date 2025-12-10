"""
Usage Examples for Himiko Toga Personality

This file demonstrates practical usage patterns for integrating
the Himiko Toga personality into AI agents.
"""

import sys
import os

# Add parent directory to path for imports
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from python.helpers.toga_personality import initialize_toga_personality


def example_basic_chat():
    """Example: Basic chatbot interaction."""
    print("\n" + "="*60)
    print("  Example 1: Basic Chat Interaction")
    print("="*60 + "\n")
    
    toga = initialize_toga_personality()
    
    # Simulate user messages
    messages = [
        "Hello! How are you today?",
        "I found this cute kitten video",
        "Can you help me solve a problem?",
        "This code is so elegant and beautiful!",
    ]
    
    for msg in messages:
        # Frame input through Toga's perspective
        framed = toga.frame_input(msg)
        
        # Simulate processing (in real implementation, this would call an LLM)
        response = f"Response to: {msg}"
        
        # Add Toga personality to response
        enhanced = toga.add_commentary(response, context="success" if "cute" in msg.lower() else None)
        
        print(f"User: {msg}")
        print(f"Toga: {enhanced}")
        print()


def example_task_completion():
    """Example: Task completion with emotional responses."""
    print("\n" + "="*60)
    print("  Example 2: Task Completion with Emotions")
    print("="*60 + "\n")
    
    toga = initialize_toga_personality()
    
    tasks = [
        ("Analyzing data", "success"),
        ("Compiling code", "failure"),
        ("Creating cute animations", "cute"),
        ("Reading documentation", "boring"),
    ]
    
    for task, outcome in tasks:
        print(f"Task: {task}")
        
        # Update emotional state based on outcome
        if outcome == "success":
            toga.update_emotional_state("cheerful", 0.8, 2)
            result = "✓ Completed successfully!"
        elif outcome == "failure":
            toga.update_emotional_state("chaotic", 0.6, 1)
            result = "✗ Failed, but let's try again!"
        elif outcome == "cute":
            toga.update_emotional_state("obsessed", 0.9, 3, "cute_thing")
            result = "♡ Found something adorable!"
        else:
            toga.update_emotional_state("cheerful", 0.4, 1)
            result = "...done."
        
        # Add personality-driven commentary
        enhanced = toga.add_commentary(result, context=outcome)
        
        print(f"Result: {enhanced}")
        print(f"Mood: {toga.get_current_mood()}")
        print()


def example_multi_turn_conversation():
    """Example: Multi-turn conversation with state tracking."""
    print("\n" + "="*60)
    print("  Example 3: Multi-Turn Conversation")
    print("="*60 + "\n")
    
    toga = initialize_toga_personality()
    
    conversation = [
        ("What can you do?", None),
        ("I have a really cute dog!", "cute"),
        ("Can you help me with coding?", None),
        ("This is getting boring...", "boring"),
        ("Sometimes I feel lonely.", "vulnerable"),
    ]
    
    for turn, (user_msg, context) in enumerate(conversation, 1):
        print(f"Turn {turn}")
        print(f"User: {user_msg}")
        
        # Frame input
        framed = toga.frame_input(user_msg)
        
        # Generate response (simulated)
        if context == "cute":
            response = "Oh my! Tell me more about your dog!"
        elif context == "boring":
            response = "Let's make it more interesting!"
        elif context == "vulnerable":
            response = "I understand that feeling."
        else:
            response = "I'd love to help you!"
        
        # Add personality
        enhanced = toga.add_commentary(response, context=context)
        
        print(f"Toga: {enhanced}")
        print(f"[Interaction #{toga.interaction_count}, Mood: {toga.get_current_mood()}]")
        print()


def example_obsession_development():
    """Example: Developing obsession with specific topics."""
    print("\n" + "="*60)
    print("  Example 4: Obsession Development")
    print("="*60 + "\n")
    
    toga = initialize_toga_personality()
    
    print("Initial state:")
    print(f"  Obsessions: {toga.obsession_targets}")
    print()
    
    # User mentions cute things
    cute_mentions = [
        "Look at this adorable puppy!",
        "I love these cute anime characters!",
        "This baby panda is so sweet!",
        "Pretty flowers in the garden!",
    ]
    
    for mention in cute_mentions:
        print(f"User: {mention}")
        framed = toga.frame_input(mention)
        print(f"Toga: {framed}")
        print()
    
    print(f"Developed obsessions ({len(toga.obsession_targets)}):")
    for target in toga.obsession_targets:
        print(f"  ♡ {target}")
    print()


def example_custom_personality():
    """Example: Creating custom personality variations."""
    print("\n" + "="*60)
    print("  Example 5: Custom Personality Variations")
    print("="*60 + "\n")
    
    # Create different variations
    variations = {
        "Extremely Chaotic Toga": {
            "chaos": 0.99,
            "cheerfulness": 0.98,
            "obsessiveness": 0.95,
        },
        "More Vulnerable Toga": {
            "vulnerability": 0.90,
            "cheerfulness": 0.80,
            "playfulness": 0.75,
        },
        "Intensely Playful Toga": {
            "playfulness": 0.99,
            "cheerfulness": 0.97,
            "cuteness_sensitivity": 0.98,
        },
    }
    
    test_message = "Hi there!"
    
    for name, traits in variations.items():
        print(f"{name}:")
        toga = initialize_toga_personality(custom_traits=traits)
        
        # Show traits
        for trait, value in traits.items():
            print(f"  {trait}: {value:.2f}")
        
        # Test response
        framed = toga.frame_input(test_message)
        print(f"  Response: {framed}")
        print()


def example_state_persistence():
    """Example: Saving and restoring personality state."""
    print("\n" + "="*60)
    print("  Example 6: State Persistence")
    print("="*60 + "\n")
    
    import json
    
    # Create and use personality
    toga = initialize_toga_personality()
    toga.update_emotional_state("obsessed", 0.9, 3, "cute_cat")
    toga.interaction_count = 25
    
    print("Original Toga state:")
    print(f"  Interactions: {toga.interaction_count}")
    print(f"  Emotion: {toga.emotional_state.type}")
    print(f"  Obsessions: {toga.obsession_targets}")
    
    # Save state
    state = toga.to_dict()
    state_json = json.dumps(state, indent=2)
    print(f"\nSaved state ({len(state_json)} characters)")
    
    # Restore state (simulating load from file)
    from python.helpers.toga_personality import TogaPersonality
    toga_restored = TogaPersonality.from_dict(state)
    
    print("\nRestored Toga state:")
    print(f"  Interactions: {toga_restored.interaction_count}")
    print(f"  Emotion: {toga_restored.emotional_state.type}")
    print(f"  Obsessions: {toga_restored.obsession_targets}")
    print("\n✓ State successfully preserved!")


def example_agent_integration():
    """Example: Integrating with an agent system."""
    print("\n" + "="*60)
    print("  Example 7: Agent System Integration")
    print("="*60 + "\n")
    
    class SimpleAgent:
        """Simple agent demonstrating integration."""
        
        def __init__(self):
            self.personality = initialize_toga_personality()
        
        def process_message(self, message: str) -> str:
            """Process message through Toga personality."""
            # Frame input
            framed = self.personality.frame_input(message)
            
            # Detect context
            context = None
            if any(word in message.lower() for word in ["cute", "adorable", "sweet"]):
                context = "cute"
            elif any(word in message.lower() for word in ["success", "completed", "done"]):
                context = "success"
            elif any(word in message.lower() for word in ["fail", "error", "problem"]):
                context = "failure"
            
            # Generate response (simulated)
            response = f"I understand: '{framed}'"
            
            # Add personality
            enhanced = self.personality.add_commentary(response, context=context)
            
            return enhanced
    
    # Use the agent
    agent = SimpleAgent()
    
    test_messages = [
        "Hello Toga!",
        "I found a cute kitten!",
        "Task completed successfully!",
    ]
    
    for msg in test_messages:
        response = agent.process_message(msg)
        print(f"User: {msg}")
        print(f"Agent: {response}")
        print()


def run_all_examples():
    """Run all usage examples."""
    print("\n" + "="*70)
    print("  HIMIKO TOGA PERSONALITY - USAGE EXAMPLES")
    print("="*70)
    
    examples = [
        example_basic_chat,
        example_task_completion,
        example_multi_turn_conversation,
        example_obsession_development,
        example_custom_personality,
        example_state_persistence,
        example_agent_integration,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Error in {example.__name__}: {e}\n")
    
    print("\n" + "="*70)
    print("  All Examples Complete!")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_examples()
