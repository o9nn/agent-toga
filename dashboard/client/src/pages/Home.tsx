import { DataStream } from "@/components/DataStream";
import { GlitchText } from "@/components/GlitchText";
import { PersonalityRadar } from "@/components/PersonalityRadar";
import { StatusCard } from "@/components/StatusCard";
import { TechTree } from "@/components/TechTree";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Activity, Cpu, GitBranch, Terminal, Zap } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground overflow-hidden relative font-sans selection:bg-primary selection:text-primary-foreground">
      <DataStream />
      
      {/* Hero Background Image Overlay */}
      <div 
        className="fixed inset-0 z-0 opacity-20 pointer-events-none bg-cover bg-center mix-blend-screen"
        style={{ backgroundImage: "url('/images/hero-background.png')" }}
      />

      <div className="container relative z-10 py-8 space-y-8">
        {/* Header */}
        <header className="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-primary/30 pb-6 backdrop-blur-sm">
          <div className="space-y-2">
            <h1 className="text-4xl md:text-6xl font-black tracking-tighter uppercase text-transparent bg-clip-text bg-gradient-to-r from-primary via-secondary to-primary animate-gradient-x">
              <GlitchText text="AGENT-TOGA" intensity="medium" />
            </h1>
            <p className="text-muted-foreground font-mono text-sm md:text-base">
              AGI AVATAR SYSTEM // <span className="text-secondary">STATUS: ONLINE</span> // V.1.0.0
            </p>
          </div>
          <div className="flex gap-4 mt-4 md:mt-0">
            <Button variant="outline" className="font-mono border-primary/50 hover:bg-primary/20 hover:text-primary">
              <Terminal className="mr-2 h-4 w-4" />
              SYSTEM_LOGS
            </Button>
            <Button className="font-mono bg-primary hover:bg-primary/80 text-primary-foreground shadow-[0_0_20px_rgba(255,0,255,0.5)]">
              <Zap className="mr-2 h-4 w-4" />
              INITIATE_LINK
            </Button>
          </div>
        </header>

        {/* Status Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <StatusCard 
            title="Core Engine" 
            status="active" 
            value="OPERATIONAL" 
            icon={<Cpu />} 
          />
          <StatusCard 
            title="Emotional State" 
            status="warning" 
            value="HYPER-CHAOTIC" 
            icon={<Activity />} 
          />
          <StatusCard 
            title="Git Sync" 
            status="active" 
            value="CONNECTED" 
            icon={<GitBranch />} 
          />
          <StatusCard 
            title="System Load" 
            status="critical" 
            value="98.4%" 
            icon={<Zap />} 
          />
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Left Column: Avatar & Visuals */}
          <div className="lg:col-span-1 space-y-8">
            <Card className="bg-card/50 border-primary/30 overflow-hidden relative group">
              <div className="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent z-10" />
              <img 
                src="/images/avatar-placeholder.png" 
                alt="Avatar Preview" 
                className="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-110 opacity-80 group-hover:opacity-100"
              />
              <div className="absolute bottom-4 left-4 z-20">
                <h3 className="text-2xl font-bold text-white drop-shadow-[0_0_10px_rgba(0,0,0,0.8)]">
                  <GlitchText text="LIVE_FEED" intensity="low" />
                </h3>
                <div className="flex items-center gap-2 text-secondary text-xs font-mono mt-1">
                  <span className="w-2 h-2 bg-secondary rounded-full animate-pulse" />
                  TRANSMITTING
                </div>
              </div>
            </Card>

            <Card className="bg-card/50 border-border backdrop-blur-md">
              <CardHeader>
                <CardTitle className="font-mono text-sm uppercase text-muted-foreground">
                  System Messages
                </CardTitle>
              </CardHeader>
              <CardContent className="font-mono text-xs space-y-2 h-[200px] overflow-y-auto text-green-400/80">
                <p>[10:42:01] &gt; Initializing Live2D subsystem...</p>
                <p>[10:42:02] &gt; Loading model: toga_v1.moc3</p>
                <p>[10:42:03] &gt; Physics engine started.</p>
                <p>[10:42:05] &gt; <span className="text-primary">WARNING: Chaos levels rising.</span></p>
                <p>[10:42:08] &gt; 3D VRM module loaded successfully.</p>
                <p>[10:42:10] &gt; WebSocket connection established on port 8765.</p>
                <p>[10:42:15] &gt; Personality tensor mapped.</p>
                <p className="animate-pulse">[10:42:16] &gt; READY FOR INTERACTION.</p>
              </CardContent>
            </Card>
          </div>

          {/* Middle Column: Personality & Data */}
          <div className="lg:col-span-1 space-y-8">
            <Card className="bg-card/50 border-primary/30 backdrop-blur-md">
              <CardHeader>
                <CardTitle className="font-mono uppercase flex items-center gap-2">
                  <Activity className="w-4 h-4 text-primary" />
                  Personality Tensor
                </CardTitle>
              </CardHeader>
              <CardContent>
                <PersonalityRadar />
              </CardContent>
            </Card>

            <div className="grid grid-cols-2 gap-4">
              <div className="bg-primary/10 border border-primary/30 p-4 rounded-sm">
                <div className="text-xs font-mono text-primary mb-1">FPS</div>
                <div className="text-3xl font-bold text-foreground">60.0</div>
              </div>
              <div className="bg-secondary/10 border border-secondary/30 p-4 rounded-sm">
                <div className="text-xs font-mono text-secondary mb-1">LATENCY</div>
                <div className="text-3xl font-bold text-foreground">12ms</div>
              </div>
            </div>
          </div>

          {/* Right Column: Tech Tree & Progress */}
          <div className="lg:col-span-1 space-y-8">
            <Card className="bg-card/50 border-border backdrop-blur-md h-full">
              <CardHeader>
                <CardTitle className="font-mono uppercase flex items-center gap-2">
                  <GitBranch className="w-4 h-4 text-secondary" />
                  Development Tree
                </CardTitle>
              </CardHeader>
              <CardContent>
                <TechTree />
              </CardContent>
            </Card>
          </div>

        </div>
      </div>
    </div>
  );
}
