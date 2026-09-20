import os

out_dir = r"c:\Users\faeda\Storage\Faed Docs\Jobs\portfolio\assets\images"
os.makedirs(out_dir, exist_ok=True)

# SVG 1: LiDAR & VLM Pipeline Diagram
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#bgGrad)"/>
  
  <!-- Perspective Road Grid -->
  <path d="M 40 280 L 560 280 M 90 230 L 510 230 M 140 190 L 460 190" stroke="#334155" stroke-width="1.5" opacity="0.6" stroke-dasharray="6,4"/>
  <path d="M 200 190 L 100 280 M 300 190 L 300 280 M 400 190 L 500 280" stroke="#334155" stroke-width="1.5" opacity="0.4"/>
  
  <!-- Roadside LiDAR Mast -->
  <line x1="70" y1="260" x2="70" y2="85" stroke="#64748b" stroke-width="4"/>
  <circle cx="70" cy="80" r="18" fill="#1e293b" stroke="#06b6d4" stroke-width="3" filter="url(#glow)"/>
  <circle cx="70" cy="80" r="7" fill="#38bdf8"/>
  <text x="70" y="50" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Roadside LiDAR</text>

  <!-- LiDAR Scanning Rays -->
  <path d="M 70 80 L 220 180 M 70 80 L 250 220 M 70 80 L 330 250" stroke="#06b6d4" stroke-width="1.5" opacity="0.5" stroke-dasharray="5,4"/>

  <!-- 3D Bounding Box & Vehicle Points -->
  <g transform="translate(200, 145)">
    <!-- Bounding Wireframe -->
    <rect x="15" y="25" width="160" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2" opacity="0.85"/>
    <path d="M 35 25 L 75 0 L 215 0 L 175 25 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
    <path d="M 175 25 L 215 0 L 215 75 L 175 100 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
    
    <!-- Point Cloud Cluster -->
    <circle cx="45" cy="40" r="2.5" fill="#38bdf8"/>
    <circle cx="70" cy="35" r="2" fill="#06b6d4"/>
    <circle cx="105" cy="48" r="2.5" fill="#38bdf8"/>
    <circle cx="140" cy="42" r="2" fill="#a855f7"/>
    <circle cx="160" cy="60" r="2" fill="#38bdf8"/>
    <circle cx="80" cy="70" r="2.5" fill="#06b6d4"/>
    <circle cx="120" cy="75" r="2" fill="#38bdf8"/>
    <circle cx="150" cy="85" r="2" fill="#a855f7"/>

    <!-- Dimension Extractor Bar -->
    <line x1="15" y1="115" x2="175" y2="115" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="15" y1="108" x2="15" y2="122" stroke="#f59e0b" stroke-width="2"/>
    <line x1="175" y1="108" x2="175" y2="122" stroke="#f59e0b" stroke-width="2"/>
    <text x="95" y="133" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">MAE: 0.298 m | MAPE: 5.2%</text>
  </g>

  <!-- Flow Connector -->
  <path d="M 390 190 L 445 190" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="445,186 453,190 445,194" fill="#94a3b8"/>

  <!-- VLM Benchmark Module -->
  <g transform="translate(450, 130)">
    <rect width="130" height="120" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
    <text x="65" y="28" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="bold" fill="#c7d2fe" text-anchor="middle">VLM Ground Truth</text>
    <rect x="15" y="42" width="100" height="26" rx="5" fill="#312e81"/>
    <text x="65" y="59" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#a5b4fc" text-anchor="middle">Visual Verification</text>
    <rect x="15" y="76" width="100" height="26" rx="5" fill="#312e81"/>
    <text x="65" y="93" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#a5b4fc" text-anchor="middle">Catalog Alignment</text>
  </g>

  <!-- Caption Footer -->
  <text x="300" y="322" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748b" text-anchor="middle">Trajectory-Aligned Morphological Roadside LiDAR + Vision-Language Pipeline</text>
</svg>'''

with open(os.path.join(out_dir, "lidar_pipeline.svg"), "w", encoding="utf-8") as f:
    f.write(svg1)

# SVG 2: ARise Multimodal Sensing Diagram
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="arBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#arBg)"/>
  
  <!-- AR App Screen -->
  <g transform="translate(45, 60)">
    <rect width="135" height="195" rx="18" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <rect x="10" y="15" width="115" height="145" rx="10" fill="#090d16"/>
    <!-- 3D Polyhedron -->
    <polygon points="67,42 102,62 102,102 67,122 32,102 32,62" fill="none" stroke="#f43f5e" stroke-width="2.5"/>
    <polygon points="67,42 67,82 102,102" fill="#fda4af" opacity="0.35"/>
    <polygon points="67,82 67,122 32,102" fill="#fb7185" opacity="0.25"/>
    <text x="67" y="178" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="bold" fill="#fda4af" text-anchor="middle">AR Mobile App</text>
  </g>

  <!-- Central Processing Engine -->
  <g transform="translate(210, 70)">
    <rect width="180" height="175" rx="14" fill="#18182e" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="90" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="bold" fill="#c4b5fd" text-anchor="middle">Multimodal Analytics</text>
    <line x1="25" y1="45" x2="155" y2="45" stroke="#4c1d95" stroke-width="1.5"/>
    <text x="90" y="70" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#ddd6fe" text-anchor="middle">Video Frame Analysis</text>
    <text x="90" y="90" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#a78bfa" text-anchor="middle">Attention &amp; Eye Gaze</text>
    <rect x="25" y="108" width="130" height="42" rx="6" fill="#2e1065" stroke="#7c3aed" stroke-width="1"/>
    <text x="90" y="126" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Stimuli Tracking</text>
    <text x="90" y="141" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#c084fc" text-anchor="middle">Response Kinetics</text>
  </g>

  <!-- Wearable Device -->
  <g transform="translate(420, 60)">
    <rect width="135" height="195" rx="18" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="42" y="15" width="50" height="165" rx="10" fill="#334155" stroke="#475569" stroke-width="1"/>
    <rect x="32" y="55" width="70" height="85" rx="12" fill="#022c22" stroke="#10b981" stroke-width="2"/>
    <path d="M 40 98 L 52 98 L 57 82 L 65 118 L 73 90 L 78 98 L 94 98" fill="none" stroke="#34d399" stroke-width="2.5"/>
    <text x="67" y="178" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Wearable Vitals</text>
  </g>

  <!-- Connectors -->
  <path d="M 180 157 L 210 157" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,3"/>
  <path d="M 390 157 L 420 157" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>

  <text x="300" y="318" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748b" text-anchor="middle">ARise: Multimodal Behavioral Tracking &amp; Sensor Analytics for ASD</text>
</svg>'''

with open(os.path.join(out_dir, "arise_diagram.svg"), "w", encoding="utf-8") as f:
    f.write(svg2)

# SVG 3: Traffic Edge YOLO
svg3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="tfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#172554"/>
    </linearGradient>
  </defs>
  <rect width="600" height="340" rx="16" fill="url(#tfBg)"/>
  
  <!-- Perspective Road -->
  <polygon points="110,300 490,300 360,110 240,110" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <!-- Lane lines -->
  <line x1="300" y1="110" x2="300" y2="300" stroke="#facc15" stroke-width="3" stroke-dasharray="14,10"/>
  
  <!-- Detected Vehicle Bounding Box (Violation) -->
  <rect x="215" y="165" width="85" height="70" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="2"/>
  <rect x="215" y="145" width="105" height="20" fill="#ef4444" rx="4"/>
  <text x="220" y="159" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Violation: Lane Drift</text>
  
  <!-- Compliant Vehicle -->
  <rect x="330" y="195" width="95" height="80" rx="6" fill="rgba(34, 197, 94, 0.15)" stroke="#22c55e" stroke-width="2"/>
  <rect x="330" y="175" width="90" height="20" fill="#22c55e" rx="4"/>
  <text x="335" y="189" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Compliant: In-Lane</text>
  
  <!-- Raspberry Pi Edge Badge -->
  <g transform="translate(35, 35)">
    <rect width="180" height="58" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="25" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Raspberry Pi Edge SoC</text>
    <text x="90" y="44" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Real-time YOLO · 78% Acc</text>
  </g>
  
  <text x="300" y="325" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748b" text-anchor="middle">Real-Time Edge Computer Vision for Lane Violation Detection</text>
</svg>'''

with open(os.path.join(out_dir, "traffic_edge.svg"), "w", encoding="utf-8") as f:
    f.write(svg3)

# Favicon SVG
fav = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#0f172a"/>
  <circle cx="32" cy="32" r="26" fill="none" stroke="#06b6d4" stroke-width="3" stroke-dasharray="6 4"/>
  <text x="32" y="41" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="24" font-weight="900" fill="#38bdf8" text-anchor="middle">FA</text>
</svg>'''

with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(fav)

print("Generated all vector illustrations successfully!")
