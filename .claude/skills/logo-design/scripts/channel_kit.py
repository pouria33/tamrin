#!/usr/bin/env python3
"""Build a video-channel kit (YouTube, Aparat…) from a finished logo (no required dependencies).

SVG outputs (in --out-dir, default next to the symbol):
  <name>-channel-avatar.svg        mark centred on a square tile, sized for the platform's circle crop (800×800 PNG)
  <name>-channel-banner.svg        2560×1440 banner; logo (lockup if given) centred in the 1235×338 safe area
  <name>-channel-banner-guide.svg  the same banner with TV / desktop / safe-area outlines — for checking, not uploading
  <name>-channel-watermark.svg     the mark on a small tile for the video branding watermark (150×150 PNG)

Raster (needs any backend of render_png.py): add --png to write the upload-ready PNGs next to the SVGs.

Usage:
  python3 scripts/channel_kit.py brand-symbol.svg --lockup brand-horizontal.svg --bg "#1C39BB" --fg "#ffffff" --png
  python3 scripts/channel_kit.py brand-symbol.svg --lockup brand-fa-horizontal.svg --bg "#0F3D3E" --pattern khatam

Notes:
- Upload sizes follow YouTube's published guidance (banner ≥2048×1152, logos/text inside 1235×338; avatar 800×800
  shown as a circle down to ~98 px; watermark 150×150). Platforms change these — re-check before delivery.
- --pattern khatam fills the banner with a faint Persian eight-point-star (khatam) lattice; --pattern none (default)
  keeps it flat. The pattern sits outside the logo's safe area at the same low opacity everywhere.
- The mark is recoloured to --fg on tiles; pass --fg keep to leave the original colours.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True  # keep the skill folder clean (no __pycache__)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib  # noqa: E402
import render_png  # noqa: E402
from export_variants import inner_markup, recolor, square_wrap  # noqa: E402

BANNER_W, BANNER_H = 2560, 1440
SAFE_W, SAFE_H = 1235, 338      # text and logos always visible
DESKTOP_H = 423                 # visible strip on desktop at full width


def placed(raw, root, box, fg):
    """Fit the artwork's real bounding box inside box=(x, y, w, h), centred."""
    vb = svglib.view_box(root)
    geo = svglib.document_geometry(root)
    bb = geo["bbox"] or (vb[0], vb[1], vb[0] + vb[2], vb[1] + vb[3])
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    s = min(box[2] / w, box[3] / h)
    tx = box[0] + (box[2] - w * s) / 2 - bb[0] * s
    ty = box[1] + (box[3] - h * s) / 2 - bb[1] * s
    src = recolor(raw, fg) if fg else raw
    carried = ""
    root_tag = re.search(r"<svg\b[^>]*>", src)
    if root_tag:
        for attr in ("fill", "stroke", "fill-rule", "clip-rule", "stroke-width", "stroke-linecap", "stroke-linejoin"):
            m = re.search(r'\s%s\s*=\s*"([^"]*)"' % re.escape(attr), root_tag.group(0))
            if m:
                carried += f' {attr}="{m.group(1)}"'
    return f'<g transform="translate({tx:.2f} {ty:.2f}) scale({s:.4f})"{carried}>{inner_markup(src)}</g>'


def khatam_pattern(color, cell=160, opacity=0.09):
    """Eight-point stars (two squares at 0° and 45°) on a square lattice."""
    c, r = cell / 2, cell * 0.3
    sq = f"M{c - r:g},{c - r:g}h{2 * r:g}v{2 * r:g}h{-2 * r:g}Z"
    d = r * 2 ** 0.5
    dia = f"M{c:g},{c - d:.2f}L{c + d:.2f},{c:g}L{c:g},{c + d:.2f}L{c - d:.2f},{c:g}Z"
    return (f'<defs><pattern id="khatam" width="{cell}" height="{cell}" patternUnits="userSpaceOnUse">'
            f'<g fill="none" stroke="{color}" stroke-width="{cell * 0.02:g}" stroke-linejoin="miter">'
            f'<path d="{sq}"/><path d="{dia}"/></g></pattern></defs>'
            f'<rect width="{BANNER_W}" height="{BANNER_H}" fill="url(#khatam)" opacity="{opacity}"/>')


def banner(raw, root, bg, fg, pattern, guide=False):
    sx, sy = (BANNER_W - SAFE_W) / 2, (BANNER_H - SAFE_H) / 2
    # Logo: up to 90 % of the safe width and 70 % of its height.
    box = (sx + SAFE_W * 0.05, sy + SAFE_H * 0.15, SAFE_W * 0.9, SAFE_H * 0.7)
    parts = [f'<rect width="{BANNER_W}" height="{BANNER_H}" fill="{bg}"/>']
    if pattern == "khatam":
        pat_color = fg if fg and fg != "keep" else "#ffffff"
        parts.append(khatam_pattern(pat_color))
        # Calm field behind the logo so the pattern never touches it.
        parts.append(f'<rect x="{sx:g}" y="{sy:g}" width="{SAFE_W}" height="{SAFE_H}" fill="{bg}"/>')
    parts.append(placed(raw, root, box, None if fg == "keep" else fg))
    if guide:
        dy = (BANNER_H - DESKTOP_H) / 2
        style = 'fill="none" stroke-width="6" stroke-dasharray="24 12"'
        label = 'font-family="sans-serif" font-size="34" fill="#ff3b30"'
        parts += [
            f'<rect x="3" y="3" width="{BANNER_W - 6}" height="{BANNER_H - 6}" stroke="#ff3b30" {style}/>',
            f'<text x="24" y="56" {label}>TV: full 2560×1440</text>',
            f'<rect x="3" y="{dy:g}" width="{BANNER_W - 6}" height="{DESKTOP_H}" stroke="#ff9500" {style}/>',
            f'<text x="24" y="{dy - 16:g}" {label.replace("#ff3b30", "#ff9500")}>desktop: 2560×423</text>',
            f'<rect x="{sx:g}" y="{sy:g}" width="{SAFE_W}" height="{SAFE_H}" stroke="#34c759" {style}/>',
            f'<text x="{sx:g}" y="{sy - 12:g}" {label.replace("#ff3b30", "#34c759")}>'
            f'safe area (all devices): 1235×338</text>',
        ]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BANNER_W} {BANNER_H}" '
            f'width="{BANNER_W}" height="{BANNER_H}">{"".join(parts)}</svg>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("symbol", help="the symbol / mark SVG (used for avatar and watermark)")
    ap.add_argument("--lockup", help="horizontal lockup SVG for the banner (default: the symbol)")
    ap.add_argument("--bg", default="#111111", help="tile and banner colour")
    ap.add_argument("--fg", default="#ffffff", help="mark colour on tiles ('keep' = original colours)")
    ap.add_argument("--pattern", choices=["none", "khatam"], default="none", help="banner background pattern")
    ap.add_argument("--avatar-scale", type=float, default=0.56,
                    help="mark size on the avatar; ≤0.6 keeps it inside the circle crop")
    ap.add_argument("--out-dir")
    ap.add_argument("--name", help="base name for outputs (default: symbol file name)")
    ap.add_argument("--png", action="store_true", help="also write upload-ready PNGs")
    a = ap.parse_args()

    raw, root = svglib.load_svg(a.symbol)
    lraw, lroot = svglib.load_svg(a.lockup) if a.lockup else (raw, root)
    out_dir = a.out_dir or os.path.dirname(os.path.abspath(a.symbol))
    os.makedirs(out_dir, exist_ok=True)
    base = a.name or os.path.splitext(os.path.basename(a.symbol))[0]
    fg = None if a.fg == "keep" else a.fg

    outputs = {
        "channel-avatar": (square_wrap(raw, root, bg=a.bg, fg=fg, symbol_scale=a.avatar_scale), 800, 800),
        "channel-banner": (banner(lraw, lroot, a.bg, a.fg, a.pattern), BANNER_W, BANNER_H),
        "channel-banner-guide": (banner(lraw, lroot, a.bg, a.fg, a.pattern, guide=True), BANNER_W, BANNER_H),
        "channel-watermark": (square_wrap(raw, root, bg=a.bg, radius=0.225, fg=fg, symbol_scale=0.66), 150, 150),
    }
    written = []
    for suffix, (svg, w, h) in outputs.items():
        p = os.path.join(out_dir, f"{base}-{suffix}.svg")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(svg)
        written.append(p)
        if a.png and suffix != "channel-banner-guide":
            png = p[:-4] + ".png"
            if render_png.render(p, png, w, h):
                written.append(png)
            else:
                print("PNG export skipped: no rendering backend (see: python3 scripts/render_png.py --which)")
                a.png = False
    for p in written:
        print("wrote", p)


if __name__ == "__main__":
    main()
