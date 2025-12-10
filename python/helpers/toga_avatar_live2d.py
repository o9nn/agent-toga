"""
Live2D Avatar Controller for Agent-Toga

Implements Live2D Cubism SDK integration with personality-driven expression control.
Maps TogaPersonalityTensor states to Live2D avatar parameters for real-time expression.
"""

import json
import asyncio
import websockets
from typing import Dict, Optional, Any, List, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math
import random


class ExpressionType(Enum):
    """Live2D expression types mapped to Toga personality states."""
    CHEERFUL = "cheerful"
    OBSESSED = "obsessed"
    PLAYFUL = "playful"
    VULNERABLE = "vulnerable"
    CHAOTIC = "chaotic"
    TWISTED_LOVE = "twisted_love"
    NEUTRAL = "neutral"


@dataclass
class Live2DParameter:
    """
    Live2D model parameter configuration.
    
    Parameters control facial expressions, body movements, and physics.
    """
    id: str
    value: float = 0.0
    min_value: float = -1.0
    max_value: float = 1.0
    default_value: float = 0.0
    
    def clamp(self):
        """Ensure value is within valid range."""
        self.value = max(self.min_value, min(self.max_value, self.value))
    
    def normalize(self) -> float:
        """Normalize value to 0-1 range."""
        range_size = self.max_value - self.min_value
        return (self.value - self.min_value) / range_size if range_size > 0 else 0.5
    
    def set_normalized(self, normalized_value: float):
        """Set value from normalized 0-1 range."""
        range_size = self.max_value - self.min_value
        self.value = self.min_value + (normalized_value * range_size)
        self.clamp()


@dataclass
class Live2DExpressionState:
    """
    Complete Live2D expression state with all parameters.
    
    Maps to standard Live2D Cubism parameters for facial expressions.
    """
    # Eye parameters
    eye_open_left: float = 1.0
    eye_open_right: float = 1.0
    eye_smile_left: float = 0.0
    eye_smile_right: float = 0.0
    eye_ball_x: float = 0.0
    eye_ball_y: float = 0.0
    
    # Eyebrow parameters
    eyebrow_left_y: float = 0.0
    eyebrow_right_y: float = 0.0
    eyebrow_left_angle: float = 0.0
    eyebrow_right_angle: float = 0.0
    
    # Mouth parameters
    mouth_open_y: float = 0.0
    mouth_form: float = 0.0  # -1 = sad, 0 = neutral, 1 = smile
    
    # Body parameters
    body_angle_x: float = 0.0
    body_angle_y: float = 0.0
    body_angle_z: float = 0.0
    
    # Hair physics
    hair_front: float = 0.0
    hair_side: float = 0.0
    hair_back: float = 0.0
    
    def to_dict(self) -> Dict[str, float]:
        """Export as dictionary for JSON serialization."""
        return {
            "ParamEyeLOpen": self.eye_open_left,
            "ParamEyeROpen": self.eye_open_right,
            "ParamEyeLSmile": self.eye_smile_left,
            "ParamEyeRSmile": self.eye_smile_right,
            "ParamEyeBallX": self.eye_ball_x,
            "ParamEyeBallY": self.eye_ball_y,
            "ParamBrowLY": self.eyebrow_left_y,
            "ParamBrowRY": self.eyebrow_right_y,
            "ParamBrowLAngle": self.eyebrow_left_angle,
            "ParamBrowRAngle": self.eyebrow_right_angle,
            "ParamMouthOpenY": self.mouth_open_y,
            "ParamMouthForm": self.mouth_form,
            "ParamBodyAngleX": self.body_angle_x,
            "ParamBodyAngleY": self.body_angle_y,
            "ParamBodyAngleZ": self.body_angle_z,
            "ParamHairFront": self.hair_front,
            "ParamHairSide": self.hair_side,
            "ParamHairBack": self.hair_back,
        }


class PersonalityToExpressionMapper:
    """
    Maps TogaPersonalityTensor states to Live2D expressions.
    
    Implements sophisticated mapping algorithms for natural expression synthesis.
    """
    
    @staticmethod
    def map_cheerfulness(cheerfulness: float) -> Dict[str, float]:
        """Map cheerfulness to smile and eye parameters."""
        return {
            "mouth_form": cheerfulness * 0.8,  # Smile intensity
            "eye_smile_left": cheerfulness * 0.6,
            "eye_smile_right": cheerfulness * 0.6,
            "eyebrow_left_y": cheerfulness * 0.3,  # Raised eyebrows
            "eyebrow_right_y": cheerfulness * 0.3,
        }
    
    @staticmethod
    def map_obsessiveness(obsessiveness: float) -> Dict[str, float]:
        """Map obsessiveness to intense stare and focus."""
        return {
            "eye_open_left": 1.0 + (obsessiveness * 0.2),  # Wide eyes
            "eye_open_right": 1.0 + (obsessiveness * 0.2),
            "eyebrow_left_angle": obsessiveness * 0.4,  # Focused brows
            "eyebrow_right_angle": -obsessiveness * 0.4,
            "body_angle_y": obsessiveness * 0.15,  # Lean forward
        }
    
    @staticmethod
    def map_playfulness(playfulness: float) -> Dict[str, float]:
        """Map playfulness to dynamic, energetic expressions."""
        return {
            "eye_smile_left": playfulness * 0.5,
            "eye_smile_right": playfulness * 0.5,
            "mouth_form": playfulness * 0.6,
            "body_angle_z": math.sin(playfulness * math.pi) * 0.1,  # Slight tilt
        }
    
    @staticmethod
    def map_chaos(chaos: float, time: float) -> Dict[str, float]:
        """Map chaos to unpredictable, random movements."""
        # Use time-based randomness for chaotic motion
        seed = int(time * 10) % 1000
        random.seed(seed)
        
        chaos_factor = chaos * 0.3
        return {
            "eye_ball_x": random.uniform(-chaos_factor, chaos_factor),
            "eye_ball_y": random.uniform(-chaos_factor, chaos_factor),
            "body_angle_x": random.uniform(-chaos_factor, chaos_factor),
            "body_angle_z": random.uniform(-chaos_factor, chaos_factor),
            "hair_front": random.uniform(-chaos_factor, chaos_factor),
            "hair_side": random.uniform(-chaos_factor, chaos_factor),
        }
    
    @staticmethod
    def map_vulnerability(vulnerability: float) -> Dict[str, float]:
        """Map vulnerability to soft, downward expressions."""
        return {
            "eye_open_left": 1.0 - (vulnerability * 0.3),  # Slightly closed eyes
            "eye_open_right": 1.0 - (vulnerability * 0.3),
            "eyebrow_left_y": -vulnerability * 0.2,  # Lowered brows
            "eyebrow_right_y": -vulnerability * 0.2,
            "mouth_form": -vulnerability * 0.3,  # Slight frown
            "body_angle_x": -vulnerability * 0.1,  # Look down
        }
    
    @staticmethod
    def map_twisted_love(twisted_love: float) -> Dict[str, float]:
        """Map twisted love to intense, obsessive affection."""
        return {
            "eye_open_left": 1.0 + (twisted_love * 0.3),
            "eye_open_right": 1.0 + (twisted_love * 0.3),
            "eye_smile_left": twisted_love * 0.7,
            "eye_smile_right": twisted_love * 0.7,
            "mouth_form": twisted_love * 0.9,  # Big smile
            "eyebrow_left_angle": twisted_love * 0.3,
            "eyebrow_right_angle": -twisted_love * 0.3,
        }
    
    @staticmethod
    def blend_expressions(
        base: Dict[str, float],
        overlay: Dict[str, float],
        blend_factor: float = 0.5
    ) -> Dict[str, float]:
        """Blend two expression dictionaries with interpolation."""
        result = base.copy()
        for key, value in overlay.items():
            if key in result:
                result[key] = result[key] * (1 - blend_factor) + value * blend_factor
            else:
                result[key] = value * blend_factor
        return result


class Live2DAvatarController:
    """
    Main controller for Live2D avatar with personality-driven expressions.
    
    Features:
    - Real-time personality tensor to expression mapping
    - Smooth expression transitions with interpolation
    - WebSocket communication with Live2D renderer
    - Animation state management
    - Physics simulation integration
    """
    
    def __init__(
        self,
        model_path: str = "assets/live2d/toga_model/toga.model3.json",
        websocket_uri: str = "ws://localhost:8765",
    ):
        self.model_path = model_path
        self.websocket_uri = websocket_uri
        self.current_expression = Live2DExpressionState()
        self.target_expression = Live2DExpressionState()
        self.mapper = PersonalityToExpressionMapper()
        self.websocket = None
        self.is_connected = False
        self.animation_time = 0.0
        self.transition_speed = 0.1  # Interpolation speed for smooth transitions
        
    async def connect(self):
        """Establish WebSocket connection to Live2D renderer."""
        try:
            self.websocket = await websockets.connect(self.websocket_uri)
            self.is_connected = True
            print(f"✅ Connected to Live2D renderer at {self.websocket_uri}")
        except Exception as e:
            print(f"❌ Failed to connect to Live2D renderer: {e}")
            self.is_connected = False
    
    async def disconnect(self):
        """Close WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            self.is_connected = False
            print("🔌 Disconnected from Live2D renderer")
    
    def update_from_personality(
        self,
        personality_tensor: Dict[str, float],
        emotional_state: Optional[Dict[str, Any]] = None,
    ):
        """
        Update avatar expression based on personality tensor and emotional state.
        
        Args:
            personality_tensor: Dictionary with personality trait values
            emotional_state: Optional current emotional state
        """
        # Extract personality traits
        cheerfulness = personality_tensor.get("cheerfulness", 0.5)
        obsessiveness = personality_tensor.get("obsessiveness", 0.5)
        playfulness = personality_tensor.get("playfulness", 0.5)
        chaos = personality_tensor.get("chaos", 0.5)
        vulnerability = personality_tensor.get("vulnerability", 0.5)
        twisted_love = personality_tensor.get("twisted_love", 0.5)
        
        # Map each trait to expression parameters
        expr_cheerful = self.mapper.map_cheerfulness(cheerfulness)
        expr_obsessed = self.mapper.map_obsessiveness(obsessiveness)
        expr_playful = self.mapper.map_playfulness(playfulness)
        expr_chaos = self.mapper.map_chaos(chaos, self.animation_time)
        expr_vulnerable = self.mapper.map_vulnerability(vulnerability)
        expr_twisted = self.mapper.map_twisted_love(twisted_love)
        
        # Blend expressions based on emotional state
        if emotional_state and emotional_state.get("type"):
            emotion_type = emotional_state["type"]
            intensity = emotional_state.get("intensity", 0.5)
            
            # Prioritize current emotion
            if emotion_type == "obsessed":
                base_expr = self.mapper.blend_expressions(expr_cheerful, expr_obsessed, intensity)
                base_expr = self.mapper.blend_expressions(base_expr, expr_twisted, intensity * 0.5)
            elif emotion_type == "playful":
                base_expr = self.mapper.blend_expressions(expr_cheerful, expr_playful, intensity)
            elif emotion_type == "vulnerable":
                base_expr = self.mapper.blend_expressions(expr_cheerful, expr_vulnerable, intensity)
            elif emotion_type == "chaotic":
                base_expr = self.mapper.blend_expressions(expr_cheerful, expr_chaos, intensity)
            else:
                base_expr = expr_cheerful
        else:
            # Default blend of all traits
            base_expr = expr_cheerful
            base_expr = self.mapper.blend_expressions(base_expr, expr_obsessed, 0.3)
            base_expr = self.mapper.blend_expressions(base_expr, expr_playful, 0.3)
            base_expr = self.mapper.blend_expressions(base_expr, expr_chaos, 0.2)
        
        # Update target expression
        self._update_expression_from_dict(self.target_expression, base_expr)
    
    def _update_expression_from_dict(
        self,
        expression: Live2DExpressionState,
        params: Dict[str, float]
    ):
        """Update expression state from parameter dictionary."""
        for key, value in params.items():
            if hasattr(expression, key):
                setattr(expression, key, value)
    
    def interpolate_expression(self, delta_time: float):
        """
        Smoothly interpolate current expression towards target.
        
        Args:
            delta_time: Time elapsed since last update (seconds)
        """
        self.animation_time += delta_time
        
        # Interpolation factor based on transition speed
        factor = min(1.0, self.transition_speed * delta_time * 60)  # Normalize to 60 FPS
        
        # Interpolate each parameter
        for attr in vars(self.current_expression):
            current_val = getattr(self.current_expression, attr)
            target_val = getattr(self.target_expression, attr)
            new_val = current_val + (target_val - current_val) * factor
            setattr(self.current_expression, attr, new_val)
    
    async def send_expression_update(self):
        """Send current expression state to Live2D renderer via WebSocket."""
        if not self.is_connected or not self.websocket:
            return
        
        try:
            message = {
                "type": "expression_update",
                "parameters": self.current_expression.to_dict(),
                "timestamp": self.animation_time,
            }
            await self.websocket.send(json.dumps(message))
        except Exception as e:
            print(f"❌ Failed to send expression update: {e}")
            self.is_connected = False
    
    async def trigger_animation(
        self,
        animation_name: str,
        priority: int = 1,
        loop: bool = False
    ):
        """
        Trigger a predefined animation on the Live2D model.
        
        Args:
            animation_name: Name of the animation (e.g., "idle", "talk", "excited")
            priority: Animation priority (higher = overrides lower)
            loop: Whether to loop the animation
        """
        if not self.is_connected or not self.websocket:
            return
        
        try:
            message = {
                "type": "trigger_animation",
                "animation": animation_name,
                "priority": priority,
                "loop": loop,
                "timestamp": self.animation_time,
            }
            await self.websocket.send(json.dumps(message))
            print(f"🎬 Triggered animation: {animation_name}")
        except Exception as e:
            print(f"❌ Failed to trigger animation: {e}")
    
    async def update_loop(self, fps: int = 30):
        """
        Main update loop for avatar controller.
        
        Args:
            fps: Target frames per second
        """
        frame_time = 1.0 / fps
        
        while self.is_connected:
            # Interpolate expression
            self.interpolate_expression(frame_time)
            
            # Send update to renderer
            await self.send_expression_update()
            
            # Wait for next frame
            await asyncio.sleep(frame_time)
    
    def get_expression_for_message(self, message: str) -> ExpressionType:
        """
        Analyze message content to determine appropriate expression.
        
        Args:
            message: Input message text
            
        Returns:
            Recommended expression type
        """
        message_lower = message.lower()
        
        # Cute trigger detection
        cute_words = ["cute", "adorable", "kawaii", "lovely", "precious"]
        if any(word in message_lower for word in cute_words):
            return ExpressionType.OBSESSED
        
        # Playful trigger detection
        playful_words = ["fun", "play", "game", "hehe", "ehehe"]
        if any(word in message_lower for word in playful_words):
            return ExpressionType.PLAYFUL
        
        # Vulnerable trigger detection
        vulnerable_words = ["sad", "lonely", "understand", "accept"]
        if any(word in message_lower for word in vulnerable_words):
            return ExpressionType.VULNERABLE
        
        # Chaotic trigger detection
        chaotic_words = ["chaos", "random", "unpredictable", "wild"]
        if any(word in message_lower for word in chaotic_words):
            return ExpressionType.CHAOTIC
        
        # Default to cheerful
        return ExpressionType.CHEERFUL


def initialize_live2d_avatar(
    model_path: str = "assets/live2d/toga_model/toga.model3.json",
    websocket_uri: str = "ws://localhost:8765",
) -> Live2DAvatarController:
    """
    Initialize Live2D avatar controller.
    
    Args:
        model_path: Path to Live2D model JSON file
        websocket_uri: WebSocket URI for renderer connection
        
    Returns:
        Configured Live2DAvatarController instance
    """
    controller = Live2DAvatarController(model_path, websocket_uri)
    print("✨ Live2D Avatar Controller initialized")
    print(f"📁 Model path: {model_path}")
    print(f"🔌 WebSocket URI: {websocket_uri}")
    return controller


# Example usage
if __name__ == "__main__":
    async def demo():
        """Demonstration of Live2D avatar controller."""
        controller = initialize_live2d_avatar()
        
        # Connect to renderer
        await controller.connect()
        
        # Simulate personality update
        personality = {
            "cheerfulness": 0.95,
            "obsessiveness": 0.90,
            "playfulness": 0.92,
            "chaos": 0.95,
            "vulnerability": 0.70,
            "twisted_love": 0.85,
        }
        
        emotional_state = {
            "type": "obsessed",
            "intensity": 0.9,
        }
        
        # Update expression
        controller.update_from_personality(personality, emotional_state)
        
        # Run update loop for 10 seconds
        try:
            await asyncio.wait_for(controller.update_loop(fps=30), timeout=10.0)
        except asyncio.TimeoutError:
            print("Demo completed")
        
        # Disconnect
        await controller.disconnect()
    
    asyncio.run(demo())
