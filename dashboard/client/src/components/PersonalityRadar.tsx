import { PolarAngleAxis, PolarGrid, PolarRadiusAxis, Radar, RadarChart, ResponsiveContainer } from "recharts";

const data = [
  { subject: "Cheerfulness", A: 95, fullMark: 100 },
  { subject: "Obsessiveness", A: 90, fullMark: 100 },
  { subject: "Playfulness", A: 92, fullMark: 100 },
  { subject: "Chaos", A: 98, fullMark: 100 },
  { subject: "Vulnerability", A: 70, fullMark: 100 },
  { subject: "Twisted Love", A: 85, fullMark: 100 },
];

export function PersonalityRadar() {
  return (
    <div className="h-[300px] w-full relative">
      <div className="absolute inset-0 bg-gradient-to-b from-transparent to-background/20 pointer-events-none z-10" />
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart cx="50%" cy="50%" outerRadius="80%" data={data}>
          <PolarGrid stroke="rgba(255, 0, 255, 0.2)" />
          <PolarAngleAxis 
            dataKey="subject" 
            tick={{ fill: "#00FFFF", fontSize: 12, fontFamily: "monospace" }} 
          />
          <PolarRadiusAxis angle={30} domain={[0, 100]} tick={false} axisLine={false} />
          <Radar
            name="Toga"
            dataKey="A"
            stroke="#FF00FF"
            strokeWidth={3}
            fill="#FF00FF"
            fillOpacity={0.3}
          />
        </RadarChart>
      </ResponsiveContainer>
      <div className="absolute top-2 right-2 text-xs font-mono text-primary animate-pulse">
        LIVE_TENSOR_FEED
      </div>
    </div>
  );
}
