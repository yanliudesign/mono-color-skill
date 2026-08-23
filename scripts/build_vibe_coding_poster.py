#!/usr/bin/env python3
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples" / "vibe-coding-5-minutes-relaxed.png"
WIDTH = 1800
HEIGHT = 2400
PAPER = "#F5F1E8"
COBALT = "#2148B8"


def build_svg():
    cursors = [
        "1320,760 1450,1090 1360,1052 1312,1178 1254,1152 1304,1028 1218,1010",
        "1110,1090 1218,1368 1142,1338 1098,1452 1048,1432 1092,1320 1020,1306",
        "1370,1320 1485,1608 1404,1578 1360,1694 1306,1672 1352,1556 1276,1540",
        "1070,1580 1180,1854 1102,1828 1060,1938 1008,1918 1050,1808 978,1792",
        "1335,1810 1442,2084 1368,2056 1328,2162 1278,2142 1318,2036 1248,2020",
    ]
    cursor_shapes = "\n".join(
        f'<polygon points="{points}" fill="{PAPER}"/>' for points in cursors
    )
    dry_ink_marks = [
      (742, 1110, 92, 18, -8),
      (930, 1205, 66, 13, 5),
      (1210, 1055, 118, 16, -4),
      (1460, 1250, 82, 20, 7),
      (1120, 1488, 104, 15, -6),
      (760, 1640, 76, 14, 4),
      (1370, 1740, 126, 17, -5),
      (980, 1940, 88, 18, 6),
    ]
    dry_ink_shapes = "\n".join(
      f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{height / 2}" '
      f'fill="{PAPER}" opacity="0.78" transform="rotate({angle} {x} {y})"/>'
      for x, y, width, height, angle in dry_ink_marks
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
<defs>
  <filter id="paper-noise" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.72" numOctaves="3" seed="5" result="noise"/>
    <feColorMatrix in="noise" type="saturate" values="0" result="gray"/>
    <feComponentTransfer in="gray" result="soft-noise">
      <feFuncA type="table" tableValues="0 0.085"/>
    </feComponentTransfer>
    <feBlend in="SourceGraphic" in2="soft-noise" mode="multiply"/>
  </filter>
  <pattern id="halftone" width="24" height="24" patternUnits="userSpaceOnUse">
    <circle cx="6" cy="6" r="4" fill="{PAPER}" fill-opacity="0.42"/>
    <circle cx="18" cy="17" r="2.4" fill="{PAPER}" fill-opacity="0.24"/>
    <circle cx="5" cy="20" r="1.2" fill="{PAPER}" fill-opacity="0.18"/>
  </pattern>
  <filter id="ink-wobble" x="-3%" y="-3%" width="106%" height="106%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="5" result="warp"/>
    <feDisplacementMap in="SourceGraphic" in2="warp" scale="5" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <clipPath id="five-clip">
    <text x="650" y="2100" font-family="Helvetica Neue" font-size="1900" font-weight="700">5</text>
  </clipPath>
</defs>

<rect width="1800" height="2400" fill="{PAPER}" filter="url(#paper-noise)"/>

<text x="116" y="120" font-family="Courier New" font-size="22" font-weight="700" letter-spacing="2" fill="{COBALT}">OPEN PRACTICE / 05:00</text>
<text x="1684" y="120" font-family="Courier New" font-size="18" text-anchor="end" letter-spacing="1.5" fill="{COBALT}">START BEFORE YOU FEEL READY</text>
<line x1="116" y1="166" x2="1684" y2="166" stroke="{COBALT}" stroke-width="5"/>

<text x="116" y="390" font-family="PingFang SC" font-size="132" font-weight="600" fill="{COBALT}">每个人都可以</text>
<path d="M 96 270 C 268 218, 548 224, 720 302 C 770 326, 775 368, 736 398" fill="none" stroke="{COBALT}" stroke-width="8" stroke-linecap="round"/>
<path d="M 697 421 C 520 480, 208 466, 102 384" fill="none" stroke="{COBALT}" stroke-width="7" stroke-linecap="round"/>

<text x="108" y="690" font-family="Helvetica Neue" font-size="250" font-weight="700" letter-spacing="0" fill="{COBALT}">vibe</text>
<text x="104" y="908" font-family="Helvetica Neue" font-size="250" font-weight="700" letter-spacing="0" fill="{COBALT}">coding</text>

<text x="657" y="2104" font-family="Helvetica Neue" font-size="1900" font-weight="700" fill="{COBALT}" opacity="0.13">5</text>
<text x="650" y="2100" font-family="Helvetica Neue" font-size="1900" font-weight="700" fill="{COBALT}" filter="url(#ink-wobble)">5</text>
<rect x="650" y="1020" width="980" height="1080" fill="url(#halftone)" clip-path="url(#five-clip)"/>
<g clip-path="url(#five-clip)">{dry_ink_shapes}</g>
{cursor_shapes}

<text x="1220" y="2180" font-family="PingFang SC" font-size="142" font-weight="600" fill="{COBALT}">分钟</text>
<line x1="116" y1="2240" x2="1684" y2="2240" stroke="{COBALT}" stroke-width="3"/>
<text x="116" y="2304" font-family="Courier New" font-size="20" font-weight="700" letter-spacing="1.5" fill="{COBALT}">01 IDEA   02 TYPE   03 RUN   04 LOOK   05 CHANGE</text>
<text x="1684" y="2304" font-family="Courier New" font-size="20" text-anchor="end" fill="{COBALT}">NO PERMISSION REQUIRED</text>
</svg>'''


def main():
    renderer = shutil.which("rsvg-convert")
    if renderer is None:
        raise SystemExit("rsvg-convert is required")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".svg", dir=ROOT) as source:
        source.write(build_svg().encode("utf-8"))
        source.flush()
        subprocess.run(
            [renderer, "--format=png", f"--width={WIDTH}", f"--height={HEIGHT}", "--output", str(OUTPUT), source.name],
            check=True,
        )
    print(f"Exported {OUTPUT} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()