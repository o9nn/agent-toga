"""
Integration tests for Live2D and 3D avatar systems.
"""

import pytest
import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from python.helpers.toga_personality import (
    TogaPersonality,
    TogaPersonalityTensor,
    EmotionalState,
)
from python.helpers.toga_avatar_live2d import (
    Live2DAvatarController,
    Live2DExpressionState,
    PersonalityToExpressionMapper,
)
from python.helpers.toga_avatar_3d import (
    Avatar3DController,
    VRMExpressionState,
    PersonalityTo3DMapper,
)


class TestLive2DAvatarController:
    """Test suite for Live2D avatar controller."""
    
    def test_initialization(self):
        """Test controller initialization."""
        controller = Live2DAvatarController()
        assert controller is not None
        assert controller.current_expression is not None
        assert controller.target_expression is not None
        assert controller.mapper is not None
    
    def test_personality_mapping(self):
        """Test personality to expression mapping."""
        controller = Live2DAvatarController()
        
        personality = {
            "cheerfulness": 0.95,
            "obsessiveness": 0.90,
            "playfulness": 0.92,
            "chaos": 0.95,
            "vulnerability": 0.70,
            "twisted_love": 0.85,
        }
        
        emotional_state = {
            "type": "cheerful",
            "intensity": 0.8,
        }
        
        controller.update_from_personality(personality, emotional_state)
        
        # Verify expression was updated
        assert controller.target_expression is not None
    
    def test_expression_interpolation(self):
        """Test smooth expression interpolation."""
        controller = Live2DAvatarController()
        
        # Set target expression
        controller.target_expression.mouth_form = 1.0
        controller.current_expression.mouth_form = 0.0
        
        # Interpolate
        controller.interpolate_expression(0.016)  # ~60 FPS
        
        # Verify interpolation occurred
        assert 0.0 < controller.current_expression.mouth_form < 1.0
    
    def test_expression_to_dict(self):
        """Test expression serialization to dictionary."""
        expression = Live2DExpressionState()
        expression.mouth_form = 0.8
        expression.eye_open_left = 1.0
        
        expr_dict = expression.to_dict()
        
        assert "ParamMouthForm" in expr_dict
        assert expr_dict["ParamMouthForm"] == 0.8
        assert expr_dict["ParamEyeLOpen"] == 1.0


class TestAvatar3DController:
    """Test suite for 3D avatar controller."""
    
    def test_initialization(self):
        """Test controller initialization."""
        controller = Avatar3DController()
        assert controller is not None
        assert controller.current_expression is not None
        assert controller.target_expression is not None
        assert controller.mapper is not None
    
    def test_personality_mapping_3d(self):
        """Test personality to 3D expression mapping."""
        controller = Avatar3DController()
        
        personality = {
            "cheerfulness": 0.95,
            "obsessiveness": 0.90,
            "playfulness": 0.92,
            "chaos": 0.95,
            "vulnerability": 0.70,
            "twisted_love": 0.85,
        }
        
        emotional_state = {
            "type": "playful",
            "intensity": 0.8,
        }
        
        controller.update_from_personality(personality, emotional_state)
        
        # Verify expression was updated
        assert controller.target_expression is not None
    
    def test_vrm_expression_normalization(self):
        """Test VRM expression value normalization."""
        expression = VRMExpressionState()
        expression.joy = 1.5  # Invalid value
        expression.sorrow = -0.5  # Invalid value
        
        expression.normalize()
        
        assert 0.0 <= expression.joy <= 1.0
        assert 0.0 <= expression.sorrow <= 1.0
    
    def test_pose_creation(self):
        """Test pose creation from personality."""
        mapper = PersonalityTo3DMapper()
        
        personality = {
            "playfulness": 0.8,
            "chaos": 0.9,
            "obsessiveness": 0.7,
        }
        
        pose = mapper.create_pose_from_personality(personality, time=1.0)
        
        assert pose is not None
        assert pose.body_transform is not None
        assert pose.head_transform is not None


class TestPersonalityToExpressionMapping:
    """Test personality to expression mapping algorithms."""
    
    def test_cheerfulness_mapping(self):
        """Test cheerfulness to smile mapping."""
        mapper = PersonalityToExpressionMapper()
        
        result = mapper.map_cheerfulness(0.95)
        
        assert "mouth_form" in result
        assert result["mouth_form"] > 0.5  # Should be smiling
        assert "eye_smile_left" in result
        assert "eye_smile_right" in result
    
    def test_obsessiveness_mapping(self):
        """Test obsessiveness to intense stare mapping."""
        mapper = PersonalityToExpressionMapper()
        
        result = mapper.map_obsessiveness(0.90)
        
        assert "eye_open_left" in result
        assert result["eye_open_left"] > 1.0  # Wide eyes
        assert "eyebrow_left_angle" in result
    
    def test_chaos_mapping(self):
        """Test chaos to random movement mapping."""
        mapper = PersonalityToExpressionMapper()
        
        result1 = mapper.map_chaos(0.95, time=1.0)
        result2 = mapper.map_chaos(0.95, time=2.0)
        
        # Results should be different due to time-based randomness
        assert "eye_ball_x" in result1
        assert "eye_ball_x" in result2
    
    def test_expression_blending(self):
        """Test expression blending algorithm."""
        mapper = PersonalityToExpressionMapper()
        
        base = {"mouth_form": 0.0, "eye_open_left": 1.0}
        overlay = {"mouth_form": 1.0, "eye_open_left": 0.5}
        
        blended = mapper.blend_expressions(base, overlay, blend_factor=0.5)
        
        assert blended["mouth_form"] == 0.5
        assert blended["eye_open_left"] == 0.75


class TestIntegrationScenarios:
    """Integration tests for complete avatar scenarios."""
    
    def test_personality_to_avatar_pipeline(self):
        """Test complete pipeline from personality to avatar expression."""
        # Create personality
        toga = TogaPersonality()
        
        # Create Live2D controller
        live2d = Live2DAvatarController()
        
        # Update personality state
        toga.frame_input("This is so cute!")
        
        # Map to avatar
        personality_dict = toga.personality.to_dict()
        emotional_dict = {
            "type": toga.emotional_state.type,
            "intensity": toga.emotional_state.intensity,
        }
        
        live2d.update_from_personality(personality_dict, emotional_dict)
        
        # Verify pipeline worked
        assert live2d.target_expression is not None
    
    def test_avatar_mode_switching(self):
        """Test switching between Live2D and 3D avatar modes."""
        personality = {
            "cheerfulness": 0.95,
            "playfulness": 0.92,
        }
        
        emotional_state = {
            "type": "cheerful",
            "intensity": 0.8,
        }
        
        # Create both controllers
        live2d = Live2DAvatarController()
        avatar_3d = Avatar3DController()
        
        # Update both with same personality
        live2d.update_from_personality(personality, emotional_state)
        avatar_3d.update_from_personality(personality, emotional_state)
        
        # Both should have valid expressions
        assert live2d.target_expression is not None
        assert avatar_3d.target_expression is not None
    
    @pytest.mark.asyncio
    async def test_websocket_message_format(self):
        """Test WebSocket message format for avatar updates."""
        controller = Live2DAvatarController()
        
        personality = {
            "cheerfulness": 0.95,
            "obsessiveness": 0.90,
        }
        
        controller.update_from_personality(personality)
        
        # Verify expression can be serialized
        expr_dict = controller.current_expression.to_dict()
        
        assert isinstance(expr_dict, dict)
        assert all(isinstance(v, (int, float)) for v in expr_dict.values())


def test_performance_benchmark():
    """Benchmark avatar update performance."""
    import time
    
    controller = Live2DAvatarController()
    
    personality = {
        "cheerfulness": 0.95,
        "obsessiveness": 0.90,
        "playfulness": 0.92,
        "chaos": 0.95,
        "vulnerability": 0.70,
        "twisted_love": 0.85,
    }
    
    # Measure update performance
    iterations = 1000
    start_time = time.time()
    
    for i in range(iterations):
        controller.update_from_personality(personality)
        controller.interpolate_expression(0.016)
    
    elapsed = time.time() - start_time
    fps = iterations / elapsed
    
    print(f"\n🎭 Avatar Update Performance:")
    print(f"   Iterations: {iterations}")
    print(f"   Elapsed: {elapsed:.2f}s")
    print(f"   FPS: {fps:.1f}")
    
    # Should be able to handle at least 60 FPS
    assert fps >= 60, f"Performance too low: {fps:.1f} FPS"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
