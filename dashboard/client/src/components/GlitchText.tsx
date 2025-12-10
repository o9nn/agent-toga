import { cn } from "@/lib/utils";
import { useEffect, useState } from "react";

interface GlitchTextProps {
  text: string;
  className?: string;
  intensity?: "low" | "medium" | "high";
}

export function GlitchText({ text, className, intensity = "medium" }: GlitchTextProps) {
  const [glitchedText, setGlitchedText] = useState(text);
  
  useEffect(() => {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
    let interval: NodeJS.Timeout;
    
    const glitch = () => {
      const glitchChance = intensity === "low" ? 0.05 : intensity === "medium" ? 0.1 : 0.2;
      
      if (Math.random() < glitchChance) {
        const textArray = text.split("");
        const charIndex = Math.floor(Math.random() * text.length);
        textArray[charIndex] = chars[Math.floor(Math.random() * chars.length)];
        setGlitchedText(textArray.join(""));
        
        setTimeout(() => {
          setGlitchedText(text);
        }, 100);
      }
    };

    interval = setInterval(glitch, 2000);
    return () => clearInterval(interval);
  }, [text, intensity]);

  return (
    <span className={cn("relative inline-block", className)}>
      <span className="relative z-10">{glitchedText}</span>
      <span 
        className="absolute top-0 left-0 -z-10 text-primary opacity-70 animate-pulse"
        style={{ transform: "translate(-2px, 2px)" }}
      >
        {text}
      </span>
      <span 
        className="absolute top-0 left-0 -z-10 text-secondary opacity-70 animate-pulse"
        style={{ transform: "translate(2px, -2px)", animationDelay: "0.1s" }}
      >
        {text}
      </span>
    </span>
  );
}
