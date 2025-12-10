import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import { GlitchText } from "./GlitchText";

interface StatusCardProps {
  title: string;
  status: "active" | "warning" | "critical" | "offline";
  value: string;
  icon?: React.ReactNode;
  className?: string;
}

export function StatusCard({ title, status, value, icon, className }: StatusCardProps) {
  const statusColors = {
    active: "text-secondary border-secondary/50 shadow-[0_0_15px_rgba(0,255,255,0.3)]",
    warning: "text-yellow-500 border-yellow-500/50 shadow-[0_0_15px_rgba(255,200,0,0.3)]",
    critical: "text-destructive border-destructive/50 shadow-[0_0_15px_rgba(255,0,0,0.3)]",
    offline: "text-muted-foreground border-muted/50",
  };

  return (
    <Card className={cn(
      "bg-card/80 backdrop-blur-sm border-2 transition-all duration-300 hover:scale-[1.02]",
      statusColors[status],
      className
    )}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium font-mono uppercase tracking-wider">
          {title}
        </CardTitle>
        {icon && <div className="h-4 w-4 opacity-70">{icon}</div>}
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold font-mono">
          <GlitchText text={value} intensity="low" />
        </div>
        <div className="text-xs opacity-70 mt-1 font-mono">
          SYSTEM_STATUS: {status.toUpperCase()}
        </div>
      </CardContent>
    </Card>
  );
}
