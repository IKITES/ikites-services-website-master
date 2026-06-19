#!/usr/bin/env python3
"""Generate abstract, brand-styled images for the success-stories cards
via the Gemini image API. No people, no faces, no text in images.

Usage:
  GEMINI_API_KEY=... python tools/gen_story_images.py [slug_or_'test']
"""
import os
import sys
import json
import base64
import urllib.request
import urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
MODELS = [
    "gemini-2.5-flash-image-preview",
    "gemini-2.5-flash-image",
    "gemini-2.0-flash-preview-image-generation",
]
OUT_DIR = os.path.join("assets", "img", "stories")

STYLE = (
    "Abstract, non-representational digital artwork. Deep navy (#092f4d, #002540) "
    "and teal (#00696c, #1C8D90, #3FE0E0) color palette with subtle glowing accents. "
    "Clean, modern, premium deep-tech aesthetic. Soft gradients, geometric forms, "
    "fine line work and luminous particles. Wide 16:9 landscape composition. "
    "Absolutely no people, no faces, no human figures, no text, no words, no letters, no logos."
)

STORIES = {
    "clinical-trials": "Abstract visualization of AI-powered biomarker detection: glowing data nodes and flowing molecular lattice patterns accelerating along a luminous timeline.",
    "healthcare-chatbot": "Abstract generative-AI conversation flow: interlocking speech-bubble silhouettes dissolving into a network of glowing nodes and signal waves.",
    "video-doctor": "Abstract personalised health-education concept: layered translucent video frames and waveform ribbons radiating from a luminous core.",
    "endoscope": "Abstract precision optical calibration: concentric lens rings, light refraction, crosshair grids and a focused beam of teal light.",
    "edtech-notebook": "Abstract edge-AI notebook capture: a grid of glowing ruled lines folding into pixels and neural mesh, running on a compact device silhouette.",
    "automotive": "Abstract software-defined vehicle cockpit: sleek flowing dashboard light trails, circuit pathways and a connected digital grid in motion.",
    "iam": "Abstract identity and access management: interlocking secure key and shield geometry formed from glowing hexagonal access nodes and data streams.",
    "patents": "Abstract patent portfolio for light therapy: radiating beams of structured light, blueprint line work and crystalline protective geometry.",
    "tetr": "Abstract entrepreneurship bootcamp: upward-launching geometric arrows and interconnected growth nodes forming an ascending lattice.",
    "cpo-program": "Abstract product leadership program: interlocking strategy gears, layered roadmap planes and converging directional pathways glowing in teal.",
}


def gen(model, prompt):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={API_KEY}"
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError("no image in response: " + json.dumps(data)[:500])


def working_model():
    """Return the first model name that successfully produces an image."""
    last = None
    for m in MODELS:
        try:
            img = gen(m, STYLE + "\n\nScene: " + next(iter(STORIES.values())))
            os.makedirs(OUT_DIR, exist_ok=True)
            with open(os.path.join(OUT_DIR, "_test.png"), "wb") as f:
                f.write(img)
            print(f"OK model={m} bytes={len(img)}")
            return m
        except urllib.error.HTTPError as e:
            last = f"{m}: HTTP {e.code} {e.read().decode(errors='replace')[:300]}"
            print("FAIL", last)
        except Exception as e:  # noqa
            last = f"{m}: {e}"
            print("FAIL", last)
    raise SystemExit("No working model. Last error:\n" + str(last))


def main():
    if not API_KEY:
        raise SystemExit("Set GEMINI_API_KEY")
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    if arg == "test":
        working_model()
        return
    model = working_model()
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, scene in STORIES.items():
        out = os.path.join(OUT_DIR, slug + ".png")
        if os.path.exists(out) and arg != "force":
            print("skip exists", out)
            continue
        img = gen(model, STYLE + "\n\nScene: " + scene)
        with open(out, "wb") as f:
            f.write(img)
        print("wrote", out, len(img), "bytes")


if __name__ == "__main__":
    main()
