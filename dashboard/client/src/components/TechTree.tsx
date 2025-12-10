import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { CheckCircle2, Circle, Lock } from "lucide-react";

interface TechNode {
  id: string;
  title: string;
  status: "completed" | "in-progress" | "locked";
  description: string;
}

const techTreeData: TechNode[] = [
  { id: "1", title: "Live2D Integration", status: "completed", description: "Real-time personality-driven expressions" },
  { id: "2", title: "3D VRM System", status: "completed", description: "Full body animation & physics" },
  { id: "3", title: "Gradio WebUI", status: "completed", description: "Comprehensive control interface" },
  { id: "4", title: "Docker Containerization", status: "completed", description: "Production-ready deployment" },
  { id: "5", title: "Multimodal Interaction", status: "in-progress", description: "Voice synthesis & recognition" },
  { id: "6", title: "Memory Vector DB", status: "locked", description: "Long-term context retention" },
  { id: "7", title: "Swarm Intelligence", status: "locked", description: "Multi-agent orchestration" },
];

export function TechTree() {
  return (
    <ScrollArea className="h-[300px] w-full pr-4">
      <div className="space-y-4 relative pl-6 border-l-2 border-primary/20 ml-2">
        {techTreeData.map((node, index) => (
          <div key={node.id} className="relative group">
            <div className="absolute -left-[31px] top-1 bg-background rounded-full p-1 border-2 border-primary/20 group-hover:border-primary transition-colors">
              {node.status === "completed" ? (
                <CheckCircle2 className="w-4 h-4 text-secondary" />
              ) : node.status === "in-progress" ? (
                <Circle className="w-4 h-4 text-primary animate-pulse" />
              ) : (
                <Lock className="w-4 h-4 text-muted-foreground" />
              )}
            </div>
            <div className="bg-card/50 border border-border p-3 rounded-sm hover:bg-card/80 transition-colors cursor-pointer group-hover:border-primary/50">
              <div className="flex justify-between items-center mb-1">
                <h4 className="font-mono font-bold text-sm text-foreground group-hover:text-primary transition-colors">
                  {node.title}
                </h4>
                <Badge variant={node.status === "completed" ? "secondary" : node.status === "in-progress" ? "default" : "outline"} className="text-[10px] uppercase">
                  {node.status}
                </Badge>
              </div>
              <p className="text-xs text-muted-foreground font-mono">
                {node.description}
              </p>
            </div>
          </div>
        ))}
      </div>
    </ScrollArea>
  );
}
