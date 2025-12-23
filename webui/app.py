"""
Agent-Toga Gradio WebUI

Advanced web interface for interacting with Himiko Toga AGI agent avatar.
Features Live2D/3D avatar display, personality dashboard, chat interface, and more.
"""

import gradio as gr
import asyncio
import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import time
import random

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from python.helpers.toga_personality import (
    TogaPersonality,
    TogaPersonalityTensor,
    EmotionalState,
    initialize_toga_personality
)
from python.helpers.toga_transform import initialize_transform_quirk
from python.helpers.toga_security import initialize_toga_security_tester
from python.helpers.toga_avatar_live2d import initialize_live2d_avatar
from python.helpers.toga_avatar_3d import initialize_3d_avatar


class TogaWebUI:
    """
    Main Gradio WebUI application for Agent-Toga.
    
    Integrates all features:
    - Chat interface with personality
    - Live2D/3D avatar display
    - Personality tensor dashboard
    - Transform Quirk panel
    - Security testing interface
    """
    
    def __init__(self):
        """Initialize all components."""
        # Core personality
        self.toga = initialize_toga_personality()
        self.transform_quirk = initialize_transform_quirk()
        self.security_tester = initialize_toga_security_tester()
        
        # Avatar controllers (initialized lazily)
        self.live2d_controller = None
        self.avatar_3d_controller = None
        self.current_avatar_mode = "live2d"  # or "3d"
        
        # Chat history (Gradio 6.0 format: List of dicts with 'role' and 'content')
        self.chat_history: List[Dict[str, str]] = []
        
        # Personality evolution tracking
        self.personality_history: List[Dict[str, float]] = []
        
        # Theme configuration
        self.theme = gr.themes.Soft(
            primary_hue="pink",
            secondary_hue="purple",
            neutral_hue="slate",
        ).set(
            body_background_fill="*neutral_950",
            body_background_fill_dark="*neutral_950",
            panel_background_fill="*neutral_900",
            panel_background_fill_dark="*neutral_900",
        )
    
    def chat(
        self,
        message: str,
        history: List[Dict[str, str]]
    ) -> Tuple[List[Dict[str, str]], str, Dict[str, float], str]:
        """
        Process chat message with Toga personality.
        
        Args:
            message: User input message
            history: Chat history (Gradio 6.0 format: List of dicts with 'role' and 'content')
            
        Returns:
            Tuple of (updated_history, avatar_state, personality_metrics, emotional_state)
        """
        if not message.strip():
            return history, "", self.toga.personality.to_dict(), self._get_emotional_state_str()
        
        # Frame input through Toga's perspective
        framed_message = self.toga.frame_input(message)
        
        # Generate response (placeholder - integrate with LLM)
        response = self._generate_response(framed_message)
        
        # Add commentary
        response_with_commentary = self.toga.add_commentary(response, context="success")
        
        # Update history (Gradio 6.0 format)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response_with_commentary})
        self.chat_history = history
        
        # Update avatar state
        avatar_state = self._get_avatar_state()
        
        # Get personality metrics
        personality_metrics = self.toga.personality.to_dict()
        self.personality_history.append(personality_metrics)
        
        # Get emotional state
        emotional_state_str = self._get_emotional_state_str()
        
        return history, avatar_state, personality_metrics, emotional_state_str
    
    def _generate_response(self, message: str) -> str:
        """
        Generate Toga-style response to message.
        
        This is a placeholder - integrate with actual LLM for production.
        """
        # Detect message type
        message_lower = message.lower()
        
        if "cute" in message_lower or "adorable" in message_lower:
            responses = [
                "Kyaa~! ♡ That's SO CUTE! I just want to become one with it!",
                "*GASP* ♡♡♡ It's absolutely adorable! My heart can't take it!",
                "Ehehe~ ♡ So precious! I need to know EVERYTHING about it!",
            ]
            return random.choice(responses)
        
        elif "help" in message_lower or "how" in message_lower:
            return "Ehehe~ ♡ I'd love to help you! What do you need? I'm really good at... well, lots of things! *giggles*"
        
        elif "transform" in message_lower or "quirk" in message_lower:
            return "Ooh~ You want to see my Transform Quirk? ♡ Once I taste your code... I can become you~ Ehehe!"
        
        elif "security" in message_lower or "hack" in message_lower:
            return "Ehehe~ ♡ Security testing? That's like... violence as affection! I'll break it because I love it~ *twirls*"
        
        else:
            responses = [
                "Ehehe~ That's interesting! Tell me more~ ♡",
                "*giggles* I see, I see! What else? ♡",
                "Kyaa~ That sounds fun! Let's do it! *bounces excitedly*",
                "Hehe~ You're so interesting! I want to know more about you~ ♡",
            ]
            return random.choice(responses)
    
    def _get_avatar_state(self) -> str:
        """Get current avatar state as JSON string."""
        state = {
            "mode": self.current_avatar_mode,
            "personality": self.toga.personality.to_dict(),
            "emotional_state": {
                "type": self.toga.emotional_state.type,
                "intensity": self.toga.emotional_state.intensity,
                "target": self.toga.emotional_state.target,
            },
            "timestamp": time.time(),
        }
        return json.dumps(state, indent=2)
    
    def _get_emotional_state_str(self) -> str:
        """Get emotional state as formatted string."""
        state = self.toga.emotional_state
        return f"**Type**: {state.type.title()}\n**Intensity**: {state.intensity:.2f}\n**Target**: {state.target or 'None'}"
    
    def update_personality_trait(
        self,
        trait_name: str,
        value: float
    ) -> Tuple[Dict[str, float], str]:
        """
        Update a personality trait value.
        
        Args:
            trait_name: Name of the trait
            value: New value (0-1)
            
        Returns:
            Tuple of (updated_metrics, status_message)
        """
        if hasattr(self.toga.personality, trait_name):
            setattr(self.toga.personality, trait_name, value)
            self.toga.personality.__post_init__()  # Re-validate constraints
            
            return (
                self.toga.personality.to_dict(),
                f"✅ Updated {trait_name} to {value:.2f}"
            )
        else:
            return (
                self.toga.personality.to_dict(),
                f"❌ Unknown trait: {trait_name}"
            )
    
    def switch_avatar_mode(self, mode: str) -> str:
        """
        Switch between Live2D and 3D avatar modes.
        
        Args:
            mode: "live2d" or "3d"
            
        Returns:
            Status message
        """
        self.current_avatar_mode = mode
        return f"✅ Switched to {mode.upper()} avatar mode"
    
    def transform_taste_target(
        self,
        target_name: str,
        system_type: str,
        code_snippet: str
    ) -> str:
        """
        Use Transform Quirk to taste/absorb target system.
        
        Args:
            target_name: Name of target system
            system_type: Type of system (WAF, IDS, etc.)
            code_snippet: Code to analyze
            
        Returns:
            Toga's reaction to tasting
        """
        if not target_name or not code_snippet:
            return "Ehehe~ I need a target name and some code to taste! ♡"
        
        result = self.transform_quirk.taste_target(target_name, system_type, code_snippet)
        return result
    
    def transform_into_target(self, target_name: str) -> str:
        """
        Transform into absorbed target system.
        
        Args:
            target_name: Name of target to transform into
            
        Returns:
            Transformation result
        """
        if not target_name:
            return "Ehehe~ Tell me who you want me to become! ♡"
        
        result = self.transform_quirk.transform_into(target_name)
        return result
    
    def get_transform_status(self) -> str:
        """Get current Transform Quirk status."""
        status_lines = ["## Transform Quirk Status\n"]
        
        if not self.transform_quirk.absorbed_systems:
            status_lines.append("*No systems absorbed yet~ Let me taste something! ♡*")
        else:
            for target_name, data in self.transform_quirk.absorbed_systems.items():
                progress = data["absorption_progress"]
                status_lines.append(f"### {target_name}")
                status_lines.append(f"- **Type**: {data['system_type']}")
                status_lines.append(f"- **Absorption**: {progress:.1%}")
                status_lines.append(f"- **Techniques**: {len(data['techniques'])}")
                status_lines.append("")
        
        return "\n".join(status_lines)
    
    def security_analyze_target(
        self,
        target_name: str,
        target_type: str
    ) -> str:
        """
        Analyze security target with Toga's personality.
        
        Args:
            target_name: Name of target
            target_type: Type of target (api, web, etc.)
            
        Returns:
            Analysis result
        """
        if not target_name:
            return "Ehehe~ I need a target to analyze! ♡"
        
        result = self.security_tester.analyze_target(target_name, target_type)
        return result
    
    def security_report_vulnerability(
        self,
        target_name: str,
        vuln_type: str,
        severity: str
    ) -> str:
        """
        Report found vulnerability with Toga's reaction.
        
        Args:
            target_name: Name of target
            vuln_type: Type of vulnerability
            severity: Severity level
            
        Returns:
            Toga's reaction
        """
        result = self.security_tester.vulnerability_found(target_name, vuln_type, severity)
        return result
    
    def create_interface(self) -> gr.Blocks:
        """
        Create the main Gradio interface.
        
        Returns:
            Gradio Blocks interface
        """
        with gr.Blocks(
            title="Agent-Toga AGI Avatar",
        ) as interface:
            
            gr.Markdown(
                """
                # 🎭 Agent-Toga AGI Avatar
                ### Himiko Toga AI Personality - Cheerful Chaos Meets Cognitive Architecture
                
                *Ehehe~ ♡ Welcome! I'm Toga, and I'm SO excited to meet you!*
                """
            )
            
            with gr.Tabs() as tabs:
                
                # Tab 1: Chat Interface
                with gr.Tab("💬 Chat"):
                    with gr.Row():
                        with gr.Column(scale=2):
                            chatbot = gr.Chatbot(
                                label="Chat with Toga",
                                height=500,
                            )
                            with gr.Row():
                                msg_input = gr.Textbox(
                                    label="Your Message",
                                    placeholder="Type something cute~ ♡",
                                    lines=2,
                                )
                                send_btn = gr.Button("Send ♡", variant="primary")
                        
                        with gr.Column(scale=1):
                            gr.Markdown("### 🎭 Avatar Display")
                            avatar_display = gr.Code(
                                label="Avatar State (JSON)",
                                language="json",
                                lines=15,
                            )
                            
                            avatar_mode = gr.Radio(
                                choices=["live2d", "3d"],
                                value="live2d",
                                label="Avatar Mode",
                            )
                            
                            gr.Markdown("### 💭 Emotional State")
                            emotional_state_display = gr.Markdown()
                    
                    # Chat interaction
                    msg_input.submit(
                        self.chat,
                        inputs=[msg_input, chatbot],
                        outputs=[chatbot, avatar_display, gr.State(), emotional_state_display]
                    ).then(
                        lambda: "",
                        outputs=[msg_input]
                    )
                    
                    send_btn.click(
                        self.chat,
                        inputs=[msg_input, chatbot],
                        outputs=[chatbot, avatar_display, gr.State(), emotional_state_display]
                    ).then(
                        lambda: "",
                        outputs=[msg_input]
                    )
                    
                    avatar_mode.change(
                        self.switch_avatar_mode,
                        inputs=[avatar_mode],
                        outputs=[gr.Textbox(visible=False)]
                    )
                
                # Tab 2: Personality Dashboard
                with gr.Tab("🧠 Personality"):
                    gr.Markdown("### Personality Tensor Controls")
                    gr.Markdown("*Adjust Toga's personality traits in real-time!*")
                    
                    with gr.Row():
                        with gr.Column():
                            cheerfulness_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.95,
                                step=0.01,
                                label="😊 Cheerfulness",
                            )
                            obsessiveness_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.90,
                                step=0.01,
                                label="👁️ Obsessiveness",
                            )
                            playfulness_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.92,
                                step=0.01,
                                label="🎮 Playfulness",
                            )
                            chaos_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.95,
                                step=0.01,
                                label="🌀 Chaos",
                            )
                        
                        with gr.Column():
                            vulnerability_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.70,
                                step=0.01,
                                label="💔 Vulnerability",
                            )
                            identity_fluidity_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.88,
                                step=0.01,
                                label="🔄 Identity Fluidity",
                            )
                            twisted_love_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.85,
                                step=0.01,
                                label="💕 Twisted Love",
                            )
                            cuteness_sensitivity_slider = gr.Slider(
                                minimum=0.0,
                                maximum=1.0,
                                value=0.93,
                                step=0.01,
                                label="✨ Cuteness Sensitivity",
                            )
                    
                    personality_status = gr.Markdown()
                    
                    # Wire up personality sliders
                    for slider, trait in [
                        (cheerfulness_slider, "cheerfulness"),
                        (obsessiveness_slider, "obsessiveness"),
                        (playfulness_slider, "playfulness"),
                        (chaos_slider, "chaos"),
                        (vulnerability_slider, "vulnerability"),
                        (identity_fluidity_slider, "identity_fluidity"),
                        (twisted_love_slider, "twisted_love"),
                        (cuteness_sensitivity_slider, "cuteness_sensitivity"),
                    ]:
                        slider.change(
                            lambda v, t=trait: self.update_personality_trait(t, v),
                            inputs=[slider],
                            outputs=[gr.State(), personality_status]
                        )
                
                # Tab 3: Transform Quirk
                with gr.Tab("🩸 Transform Quirk"):
                    gr.Markdown(
                        """
                        ### Transform Quirk - Code Absorption System
                        *"Once I taste your code... I can become you~ ♡"*
                        """
                    )
                    
                    with gr.Row():
                        with gr.Column():
                            target_name_input = gr.Textbox(
                                label="Target Name",
                                placeholder="e.g., ModSecurity WAF"
                            )
                            system_type_input = gr.Dropdown(
                                choices=["WAF", "IDS", "Firewall", "Authentication", "Encryption", "Logging"],
                                label="System Type"
                            )
                            code_input = gr.Code(
                                label="Code Snippet to Taste",
                                language="python",
                                lines=10,
                            )
                            
                            with gr.Row():
                                taste_btn = gr.Button("👅 Taste Target", variant="primary")
                                transform_btn = gr.Button("✨ Transform!", variant="secondary")
                        
                        with gr.Column():
                            transform_output = gr.Markdown(label="Result")
                            transform_status_display = gr.Markdown()
                    
                    taste_btn.click(
                        self.transform_taste_target,
                        inputs=[target_name_input, system_type_input, code_input],
                        outputs=[transform_output]
                    ).then(
                        self.get_transform_status,
                        outputs=[transform_status_display]
                    )
                    
                    transform_btn.click(
                        self.transform_into_target,
                        inputs=[target_name_input],
                        outputs=[transform_output]
                    )
                
                # Tab 4: Security Testing
                with gr.Tab("🔐 Security Testing"):
                    gr.Markdown(
                        """
                        ### Security Testing - Violence as Affection ♡
                        *"Breaking systems because we love them~"*
                        """
                    )
                    
                    with gr.Row():
                        with gr.Column():
                            sec_target_name = gr.Textbox(
                                label="Target Name",
                                placeholder="e.g., webapp.com"
                            )
                            sec_target_type = gr.Dropdown(
                                choices=["web", "api", "network", "application"],
                                label="Target Type"
                            )
                            
                            analyze_btn = gr.Button("🔍 Analyze Target", variant="primary")
                            
                            gr.Markdown("### Report Vulnerability")
                            vuln_type_input = gr.Textbox(
                                label="Vulnerability Type",
                                placeholder="e.g., SQL Injection"
                            )
                            severity_input = gr.Dropdown(
                                choices=["low", "medium", "high", "critical"],
                                label="Severity"
                            )
                            report_btn = gr.Button("📝 Report Vulnerability")
                        
                        with gr.Column():
                            security_output = gr.Markdown()
                    
                    analyze_btn.click(
                        self.security_analyze_target,
                        inputs=[sec_target_name, sec_target_type],
                        outputs=[security_output]
                    )
                    
                    report_btn.click(
                        self.security_report_vulnerability,
                        inputs=[sec_target_name, vuln_type_input, severity_input],
                        outputs=[security_output]
                    )
            
            gr.Markdown(
                """
                ---
                ### ⚠️ Ethical Use Only
                Agent-Toga is for authorized testing and research only. Always obtain permission before testing systems.
                
                **Built with**: Gradio • Live2D Cubism SDK • Three.js • Agent-Neuro Framework
                """
            )
        
        return interface
    
    def _get_custom_css(self) -> str:
        """Get custom CSS for the interface."""
        return """
        .gradio-container {
            font-family: 'Inter', sans-serif;
        }
        
        .gr-button-primary {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
            border: none !important;
        }
        
        .gr-button-secondary {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
            border: none !important;
        }
        
        .chatbot {
            border-radius: 12px;
        }
        
        h1, h2, h3 {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        """
    
    def launch(
        self,
        share: bool = False,
        server_name: str = "0.0.0.0",
        server_port: int = 7860,
    ):
        """
        Launch the Gradio interface.
        
        Args:
            share: Whether to create a public share link
            server_name: Server hostname
            server_port: Server port
        """
        interface = self.create_interface()
        interface.launch(
            share=share,
            server_name=server_name,
            server_port=server_port,
            show_error=True,
        )


def main():
    """Main entry point for the WebUI."""
    print("🎭 Initializing Agent-Toga WebUI...")
    print("✨ Loading personality systems...")
    
    app = TogaWebUI()
    
    print("🚀 Launching Gradio interface...")
    app.launch(share=False)


if __name__ == "__main__":
    main()
