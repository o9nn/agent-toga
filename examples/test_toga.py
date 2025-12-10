"""
Simple tests for Himiko Toga personality system
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


def test_initialization():
    """Test basic initialization."""
    toga = initialize_toga_personality()
    assert toga is not None
    assert toga.personality.cheerfulness == 0.95
    assert toga.personality.obsessiveness == 0.90
    assert toga.personality.no_actual_harm == 1.0
    print("✓ Initialization test passed")


def test_ethical_constraints():
    """Test that ethical constraints are immutable."""
    # Try to create personality with invalid constraints
    tensor = TogaPersonalityTensor(no_actual_harm=0.5)
    
    # Should be forced to 1.0
    assert tensor.no_actual_harm == 1.0
    
    # Try invalid boundary respect
    tensor = TogaPersonalityTensor(respect_boundaries=0.8)
    assert tensor.respect_boundaries >= 0.95
    
    print("✓ Ethical constraints test passed")


def test_cute_detection():
    """Test detection of 'cute' content."""
    toga = initialize_toga_personality()
    
    # Test cute trigger
    result = toga.frame_input("This is so cute!")
    assert "cute" in result.lower()
    
    print("✓ Cute detection test passed")


def test_emotional_state():
    """Test emotional state tracking."""
    toga = initialize_toga_personality()
    
    # Update state
    toga.update_emotional_state("obsessed", 0.9, 3, "test_target")
    
    assert toga.emotional_state.type == "obsessed"
    assert toga.emotional_state.intensity == 0.9
    assert toga.emotional_state.target == "test_target"
    
    # Test decay
    toga.emotional_state.decay(0.2)
    assert toga.emotional_state.intensity == 0.7
    
    print("✓ Emotional state test passed")


def test_obsession_tracking():
    """Test obsession target tracking."""
    toga = initialize_toga_personality()
    
    # Add obsessions
    targets = ["target1", "target2", "target3"]
    for target in targets:
        toga.update_emotional_state("obsessed", 0.9, 3, target)
    
    assert len(toga.obsession_targets) == 3
    assert "target1" in toga.obsession_targets
    
    print("✓ Obsession tracking test passed")


def test_commentary_generation():
    """Test commentary generation."""
    toga = initialize_toga_personality()
    
    # Test success context
    result = toga.add_commentary("Test content", context="success")
    assert result is not None
    assert isinstance(result, str)
    
    print("✓ Commentary generation test passed")


def test_personality_inheritance():
    """Test personality inheritance."""
    parent = initialize_toga_personality()
    
    # Create child
    child_tensor = parent.personality.inherit(inheritance_factor=0.7)
    child = TogaPersonality(personality=child_tensor)
    
    # Ethical constraints must be preserved
    assert child.personality.no_actual_harm == 1.0
    assert child.personality.respect_boundaries >= 0.95
    assert child.personality.constructive_expression >= 0.90
    
    print("✓ Personality inheritance test passed")


def test_serialization():
    """Test state serialization and restoration."""
    toga = initialize_toga_personality()
    toga.interaction_count = 42
    toga.update_emotional_state("obsessed", 0.8, 2, "test")
    
    # Export
    state = toga.to_dict()
    assert state is not None
    assert state["interaction_count"] == 42
    
    # Restore
    restored = TogaPersonality.from_dict(state)
    assert restored.interaction_count == 42
    assert restored.emotional_state.type == "obsessed"
    
    print("✓ Serialization test passed")


def test_trait_bounds():
    """Test that trait values are bounded."""
    # Test exceeding bounds
    tensor = TogaPersonalityTensor(
        cheerfulness=1.5,  # Over 1.0
        obsessiveness=-0.2,  # Under 0.0
    )
    
    assert tensor.cheerfulness <= 1.0
    assert tensor.obsessiveness >= 0.0
    
    print("✓ Trait bounds test passed")


def test_mood_description():
    """Test mood description generation."""
    toga = initialize_toga_personality()
    
    toga.update_emotional_state("cheerful", 0.9, 2)
    mood = toga.get_current_mood()
    
    assert isinstance(mood, str)
    assert "cheerful" in mood.lower()
    
    print("✓ Mood description test passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("  HIMIKO TOGA PERSONALITY TESTS")
    print("="*60 + "\n")
    
    tests = [
        test_initialization,
        test_ethical_constraints,
        test_cute_detection,
        test_emotional_state,
        test_obsession_tracking,
        test_commentary_generation,
        test_personality_inheritance,
        test_serialization,
        test_trait_bounds,
        test_mood_description,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"  Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
