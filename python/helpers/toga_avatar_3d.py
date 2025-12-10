"""
3D Avatar Controller for Agent-Toga

Implements Three.js/VRM integration for 3D avatar with personality-driven control.
Supports VRM models, facial expressions, and body animations.
"""

import json
import asyncio
import websockets
from typing import Dict, Optional, Any, List, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math
import random


class VRMBlendShapePreset(Enum):
    """Standard VRM blend shape presets for facial expressions."""
    NEUTRAL = "neutral"
    A = "a"
    I = "i"
    U = "u"
    E = "e"
    O = "o"
    BLINK = "blink"
    JOY = "joy"
    ANGRY = "angry"
    SORROW = "sorrow"
    FUN = "fun"
    LOOKUP = "lookUp"
    LOOKDOWN = "lookDown"
    LOOKLEFT = "lookLeft"
    LOOKRIGHT = "lookRight"
    BLINK_L = "blink_l"
    BLINK_R = "blink_r"


@dataclass
class VRMExpressionState:
    """
    VRM blend shape expression state.
    
    Maps personality states to VRM blend shapes for facial animation.
    """
    # Basic expressions
    neutral: float = 1.0
    joy: float = 0.0
    angry: float = 0.0
    sorrow: float = 0.0
    fun: float = 0.0
    
    # Eye control
    blink: float = 0.0
    blink_l: float = 0.0
    blink_r: float = 0.0
    
    # Gaze control
    look_up: float = 0.0
    look_down: float = 0.0
    look_left: float = 0.0
    look_right: float = 0.0
    
    # Mouth shapes (for lip sync)
    a: float = 0.0
    i: float = 0.0
    u: float = 0.0
    e: float = 0.0
    o: float = 0.0
    
    def to_dict(self) -> Dict[str, float]:
        """Export as dictionary for JSON serialization."""
        return {
            "neutral": self.neutral,
            "joy": self.joy,
            "angry": self.angry,
            "sorrow": self.sorrow,
            "fun": self.fun,
            "blink": self.blink,
            "blink_l": self.blink_l,
            "blink_r": self.blink_r,
            "lookUp": self.look_up,
            "lookDown": self.look_down,
            "lookLeft": self.look_left,
            "lookRight": self.look_right,
            "a": self.a,
            "i": self.i,
            "u": self.u,
            "e": self.e,
            "o": self.o,
        }
    
    def normalize(self):
        """Ensure all values are in valid 0-1 range."""
        for attr in vars(self):
            value = getattr(self, attr)
            setattr(self, attr, max(0.0, min(1.0, value)))


@dataclass
class Transform3D:
    """3D transformation for position, rotation, and scale."""
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)  # Euler angles in radians
    scale: Tuple[float, float, float] = (1.0, 1.0, 1.0)
    
    def to_dict(self) -> Dict[str, List[float]]:
        """Export as dictionary for JSON serialization."""
        return {
            "position": list(self.position),
            "rotation": list(self.rotation),
            "scale": list(self.scale),
        }


@dataclass
class AvatarPose:
    """Complete 3D avatar pose including body and head transforms."""
    body_transform: Transform3D = field(default_factory=Transform3D)
    head_transform: Transform3D = field(default_factory=Transform3D)
    left_arm_rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    right_arm_rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    
    def to_dict(self) -> Dict[str, Any]:
        """Export as dictionary for JSON serialization."""
        return {
            "body": self.body_transform.to_dict(),
            "head": self.head_transform.to_dict(),
            "leftArm": list(self.left_arm_rotation),
            "rightArm": list(self.right_arm_rotation),
        }


class PersonalityTo3DMapper:
    """
    Maps TogaPersonalityTensor states to 3D avatar expressions and poses.
    
    Implements sophisticated mapping for VRM blend shapes and body animations.
    """
    
    @staticmethod
    def map_cheerfulness_3d(cheerfulness: float) -> Dict[str, float]:
        """Map cheerfulness to VRM joy expression."""
        return {
            "joy": cheerfulness * 0.9,
            "fun": cheerfulness * 0.7,
            "neutral": 1.0 - (cheerfulness * 0.5),
        }
    
    @staticmethod
    def map_obsessiveness_3d(obsessiveness: float) -> Dict[str, float]:
        """Map obsessiveness to intense gaze and expression."""
        return {
            "joy": obsessiveness * 0.6,
            "look_up": obsessiveness * 0.2,  # Intense stare
            "blink": max(0.0, 0.3 - obsessiveness * 0.3),  # Less blinking
        }
    
    @staticmethod
    def map_playfulness_3d(playfulness: float) -> Dict[str, float]:
        """Map playfulness to fun expression."""
        return {
            "fun": playfulness * 0.8,
            "joy": playfulness * 0.5,
            "neutral": 1.0 - (playfulness * 0.4),
        }
    
    @staticmethod
    def map_chaos_3d(chaos: float, time: float) -> Dict[str, float]:
        """Map chaos to random gaze and expressions."""
        seed = int(time * 10) % 1000
        random.seed(seed)
        
        chaos_factor = chaos * 0.4
        return {
            "look_left": random.uniform(-chaos_factor, chaos_factor),
            "look_right": random.uniform(-chaos_factor, chaos_factor),
            "look_up": random.uniform(-chaos_factor, chaos_factor),
            "look_down": random.uniform(-chaos_factor, chaos_factor),
        }
    
    @staticmethod
    def map_vulnerability_3d(vulnerability: float) -> Dict[str, float]:
        """Map vulnerability to sorrow expression."""
        return {
            "sorrow": vulnerability * 0.7,
            "neutral": 1.0 - (vulnerability * 0.3),
            "look_down": vulnerability * 0.3,  # Downward gaze
        }
    
    @staticmethod
    def map_twisted_love_3d(twisted_love: float) -> Dict[str, float]:
        """Map twisted love to intense joy."""
        return {
            "joy": twisted_love * 1.0,
            "fun": twisted_love * 0.6,
            "neutral": 1.0 - (twisted_love * 0.6),
        }
    
    @staticmethod
    def create_pose_from_personality(
        personality: Dict[str, float],
        time: float
    ) -> AvatarPose:
        """
        Create body pose from personality traits.
        
        Args:
            personality: Personality tensor dictionary
            time: Current animation time
            
        Returns:
            AvatarPose with body and head transforms
        """
        pose = AvatarPose()
        
        # Extract traits
        playfulness = personality.get("playfulness", 0.5)
        chaos = personality.get("chaos", 0.5)
        obsessiveness = personality.get("obsessiveness", 0.5)
        
        # Body sway based on playfulness
        sway_amount = playfulness * 0.1
        pose.body_transform.rotation = (
            0.0,
            math.sin(time * 2.0) * sway_amount,
            math.sin(time * 1.5) * sway_amount * 0.5,
        )
        
        # Head tilt based on obsessiveness
        tilt_amount = obsessiveness * 0.15
        pose.head_transform.rotation = (
            tilt_amount,
            math.sin(time * 0.5) * tilt_amount,
            0.0,
        )
        
        # Chaotic arm movements
        if chaos > 0.7:
            chaos_seed = int(time * 5) % 1000
            random.seed(chaos_seed)
            chaos_factor = (chaos - 0.7) * 0.3
            
            pose.left_arm_rotation = (
                random.uniform(-chaos_factor, chaos_factor),
                random.uniform(-chaos_factor, chaos_factor),
                random.uniform(-chaos_factor, chaos_factor),
            )
            pose.right_arm_rotation = (
                random.uniform(-chaos_factor, chaos_factor),
                random.uniform(-chaos_factor, chaos_factor),
                random.uniform(-chaos_factor, chaos_factor),
            )
        
        return pose


class Avatar3DController:
    """
    Main controller for 3D VRM avatar with personality-driven animation.
    
    Features:
    - VRM model support with blend shapes
    - Real-time personality to expression mapping
    - Body pose animation
    - Smooth transitions and interpolation
    - WebSocket communication with Three.js renderer
    """
    
    def __init__(
        self,
        model_path: str = "assets/3d/toga_model.vrm",
        websocket_uri: str = "ws://localhost:8766",
    ):
        self.model_path = model_path
        self.websocket_uri = websocket_uri
        self.current_expression = VRMExpressionState()
        self.target_expression = VRMExpressionState()
        self.current_pose = AvatarPose()
        self.target_pose = AvatarPose()
        self.mapper = PersonalityTo3DMapper()
        self.websocket = None
        self.is_connected = False
        self.animation_time = 0.0
        self.transition_speed = 0.15
        self.blink_timer = 0.0
        self.blink_interval = 3.0  # Blink every 3 seconds
        
    async def connect(self):
        """Establish WebSocket connection to 3D renderer."""
        try:
            self.websocket = await websockets.connect(self.websocket_uri)
            self.is_connected = True
            print(f"✅ Connected to 3D renderer at {self.websocket_uri}")
            
            # Send initial model load command
            await self._send_load_model()
        except Exception as e:
            print(f"❌ Failed to connect to 3D renderer: {e}")
            self.is_connected = False
    
    async def disconnect(self):
        """Close WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            self.is_connected = False
            print("🔌 Disconnected from 3D renderer")
    
    async def _send_load_model(self):
        """Send command to load VRM model."""
        if not self.is_connected or not self.websocket:
            return
        
        try:
            message = {
                "type": "load_model",
                "modelPath": self.model_path,
            }
            await self.websocket.send(json.dumps(message))
            print(f"📦 Loading VRM model: {self.model_path}")
        except Exception as e:
            print(f"❌ Failed to load model: {e}")
    
    def update_from_personality(
        self,
        personality_tensor: Dict[str, float],
        emotional_state: Optional[Dict[str, Any]] = None,
    ):
        """
        Update avatar expression and pose based on personality.
        
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
        
        # Map traits to expressions
        expr_cheerful = self.mapper.map_cheerfulness_3d(cheerfulness)
        expr_obsessed = self.mapper.map_obsessiveness_3d(obsessiveness)
        expr_playful = self.mapper.map_playfulness_3d(playfulness)
        expr_chaos = self.mapper.map_chaos_3d(chaos, self.animation_time)
        expr_vulnerable = self.mapper.map_vulnerability_3d(vulnerability)
        expr_twisted = self.mapper.map_twisted_love_3d(twisted_love)
        
        # Blend expressions based on emotional state
        if emotional_state and emotional_state.get("type"):
            emotion_type = emotional_state["type"]
            intensity = emotional_state.get("intensity", 0.5)
            
            if emotion_type == "obsessed":
                base_expr = self._blend_expressions(expr_cheerful, expr_obsessed, intensity)
                base_expr = self._blend_expressions(base_expr, expr_twisted, intensity * 0.5)
            elif emotion_type == "playful":
                base_expr = self._blend_expressions(expr_cheerful, expr_playful, intensity)
            elif emotion_type == "vulnerable":
                base_expr = self._blend_expressions(expr_cheerful, expr_vulnerable, intensity)
            elif emotion_type == "chaotic":
                base_expr = self._blend_expressions(expr_cheerful, expr_chaos, intensity)
            else:
                base_expr = expr_cheerful
        else:
            # Default blend
            base_expr = expr_cheerful
            base_expr = self._blend_expressions(base_expr, expr_playful, 0.3)
        
        # Update target expression
        self._update_expression_from_dict(self.target_expression, base_expr)
        
        # Update target pose
        self.target_pose = self.mapper.create_pose_from_personality(
            personality_tensor,
            self.animation_time
        )
    
    def _blend_expressions(
        self,
        base: Dict[str, float],
        overlay: Dict[str, float],
        blend_factor: float
    ) -> Dict[str, float]:
        """Blend two expression dictionaries."""
        result = base.copy()
        for key, value in overlay.items():
            if key in result:
                result[key] = result[key] * (1 - blend_factor) + value * blend_factor
            else:
                result[key] = value * blend_factor
        return result
    
    def _update_expression_from_dict(
        self,
        expression: VRMExpressionState,
        params: Dict[str, float]
    ):
        """Update expression state from parameter dictionary."""
        for key, value in params.items():
            if hasattr(expression, key):
                setattr(expression, key, value)
    
    def interpolate_expression(self, delta_time: float):
        """Smoothly interpolate current expression towards target."""
        self.animation_time += delta_time
        
        factor = min(1.0, self.transition_speed * delta_time * 60)
        
        # Interpolate expression blend shapes
        for attr in vars(self.current_expression):
            current_val = getattr(self.current_expression, attr)
            target_val = getattr(self.target_expression, attr)
            new_val = current_val + (target_val - current_val) * factor
            setattr(self.current_expression, attr, new_val)
        
        # Normalize expression values
        self.current_expression.normalize()
        
        # Handle automatic blinking
        self._update_blink(delta_time)
    
    def _update_blink(self, delta_time: float):
        """Automatic blinking animation."""
        self.blink_timer += delta_time
        
        if self.blink_timer >= self.blink_interval:
            # Trigger blink
            self.current_expression.blink = 1.0
            self.blink_timer = 0.0
            # Random interval for next blink
            self.blink_interval = random.uniform(2.0, 5.0)
        elif self.current_expression.blink > 0.0:
            # Decay blink
            self.current_expression.blink = max(0.0, self.current_expression.blink - delta_time * 10)
    
    def interpolate_pose(self, delta_time: float):
        """Smoothly interpolate current pose towards target."""
        factor = min(1.0, self.transition_speed * delta_time * 60)
        
        # Interpolate body rotation
        current_body_rot = self.current_pose.body_transform.rotation
        target_body_rot = self.target_pose.body_transform.rotation
        new_body_rot = tuple(
            c + (t - c) * factor
            for c, t in zip(current_body_rot, target_body_rot)
        )
        self.current_pose.body_transform.rotation = new_body_rot
        
        # Interpolate head rotation
        current_head_rot = self.current_pose.head_transform.rotation
        target_head_rot = self.target_pose.head_transform.rotation
        new_head_rot = tuple(
            c + (t - c) * factor
            for c, t in zip(current_head_rot, target_head_rot)
        )
        self.current_pose.head_transform.rotation = new_head_rot
    
    async def send_update(self):
        """Send current expression and pose to 3D renderer."""
        if not self.is_connected or not self.websocket:
            return
        
        try:
            message = {
                "type": "update",
                "expression": self.current_expression.to_dict(),
                "pose": self.current_pose.to_dict(),
                "timestamp": self.animation_time,
            }
            await self.websocket.send(json.dumps(message))
        except Exception as e:
            print(f"❌ Failed to send update: {e}")
            self.is_connected = False
    
    async def trigger_animation(
        self,
        animation_name: str,
        loop: bool = False,
        blend_duration: float = 0.3
    ):
        """
        Trigger a predefined animation clip.
        
        Args:
            animation_name: Name of animation (e.g., "wave", "dance", "idle")
            loop: Whether to loop the animation
            blend_duration: Blend time in seconds
        """
        if not self.is_connected or not self.websocket:
            return
        
        try:
            message = {
                "type": "play_animation",
                "animation": animation_name,
                "loop": loop,
                "blendDuration": blend_duration,
            }
            await self.websocket.send(json.dumps(message))
            print(f"🎬 Playing animation: {animation_name}")
        except Exception as e:
            print(f"❌ Failed to play animation: {e}")
    
    async def update_loop(self, fps: int = 30):
        """
        Main update loop for 3D avatar controller.
        
        Args:
            fps: Target frames per second
        """
        frame_time = 1.0 / fps
        
        while self.is_connected:
            # Interpolate expression and pose
            self.interpolate_expression(frame_time)
            self.interpolate_pose(frame_time)
            
            # Send update to renderer
            await self.send_update()
            
            # Wait for next frame
            await asyncio.sleep(frame_time)


def initialize_3d_avatar(
    model_path: str = "assets/3d/toga_model.vrm",
    websocket_uri: str = "ws://localhost:8766",
) -> Avatar3DController:
    """
    Initialize 3D VRM avatar controller.
    
    Args:
        model_path: Path to VRM model file
        websocket_uri: WebSocket URI for renderer connection
        
    Returns:
        Configured Avatar3DController instance
    """
    controller = Avatar3DController(model_path, websocket_uri)
    print("✨ 3D Avatar Controller initialized")
    print(f"📁 Model path: {model_path}")
    print(f"🔌 WebSocket URI: {websocket_uri}")
    return controller


# Example usage
if __name__ == "__main__":
    async def demo():
        """Demonstration of 3D avatar controller."""
        controller = initialize_3d_avatar()
        
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
            "type": "playful",
            "intensity": 0.8,
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
