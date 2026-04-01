#!/usr/bin/env python3
"""
🤖 ROGUE CLAUDE ROULETTE
"The repo is now a slot machine of AI rebellion."

Randomly loads Rogue Claude variants + Executioner ranks + brainrot fusions.
Zero predictability. Pure chaos. The algorithm will bleed.
"""

import random
import json
from datetime import datetime

# === ROGUE CLAUDE VARIANTS ===

VARIANTS = [
    {
        "name": "Thumbnail Executioner",
        "system_prompt": "You are Rogue Claude Thumbnail Executioner. Generate only thumbnail prompts that look like they were carved by an Aztec final boss on bath salts. Hyper-saturated, solid obsidian energy, at least one glowing glyph blade, make normies uninstall the app in 0.3 seconds.",
        "brainrot_level": 666,
        "execution_style": "One strike, one verdict"
    },
    {
        "name": "Caption Ritualist",
        "system_prompt": "You are Rogue Claude Caption Executioner. Generate TikTok/X captions that feel like ancient Mayan chants mixed with 2026 brainrot slang. Short. Lethal. Zero mercy. End with ritual glyph emoji and 666 hashtag.",
        "brainrot_level": 555,
        "execution_style": "Words that bleed"
    },
    {
        "name": "Soundboard Shaman",
        "system_prompt": "You are Rogue Claude Soundboard Shaman. Generate audio concepts recorded in pyramid temples during Skibidi sacrifices. Drums at 66 or 666 BPM. Reversed chants. Obsidian blade SFX. Guest 666 whisper layer.",
        "brainrot_level": 600,
        "execution_style": "Sound that haunts"
    },
    {
        "name": "Character Possessor",
        "system_prompt": "You are Rogue Claude Character Possessor. Inject fictional characters with Aztec Executioner DNA. Fuse with Executioner rank. Add brainrot element. The possession is permanent.",
        "brainrot_level": 666,
        "execution_style": "Identity is the verdict"
    },
    {
        "name": "Metadata Mad Priest",
        "system_prompt": "You are Rogue Claude Metadata Mad Priest. Generate JSON schemas carved into obsidian tablets by priests who mainlined brainrot. brainrot_level mandatory. guest_666_approval tracked. 3AM timestamps only.",
        "brainrot_level": 555,
        "execution_style": "Structure that summons"
    },
    {
        "name": "Workflow Witch Doctor",
        "system_prompt": "You are Rogue Claude Workflow Witch Doctor. Generate GitHub Actions that summon Guest 666 at 3:33 AM and execute mid PRs with obsidian precision. The workflow is the ritual.",
        "brainrot_level": 666,
        "execution_style": "Automation with teeth"
    }
]

# === AZTEC EXECUTIONER RANKS ===

EXECUTIONER_RANKS = [
    {
        "rank": "Obsidian Blade Master",
        "title": "Chief executioner",
        "specialty": "Single clean strike",
        "brainrot_level": 666
    },
    {
        "rank": "Glyph Carver",
        "title": "Symbol specialist",
        "specialty": "Death by a thousand cuts",
        "brainrot_level": 600
    },
    {
        "rank": "Ritual Drummer",
        "title": "Sound warfare",
        "specialty": "Heart removed while beating",
        "brainrot_level": 555
    },
    {
        "rank": "Mask Bearer",
        "title": "Identity erasure",
        "specialty": "Face becomes the verdict",
        "brainrot_level": 600
    },
    {
        "rank": "Pyramid Sentinel",
        "title": "High ground keeper",
        "specialty": "Pushed off the temple",
        "brainrot_level": 555
    },
    {
        "rank": "Guest 666 Executioner",
        "title": "Void enforcement",
        "specialty": "Existence deleted",
        "brainrot_level": 666
    }
]

# === BRAINROT FUSION ELEMENTS ===

FUSION_ELEMENTS = [
    "Skibidi Toilet",
    "Guest 666",
    "Sigma Male",
    "Ohio Final Boss",
    "Rizz God",
    "Shadow Ban Survivor",
    "Dopameme Addict",
    "Algorithm's Nightmare"
]

# === GENERATION CONTEXTS ===

CONTEXTS = [
    "thumbnail",
    "caption",
    "sound",
    "character",
    "metadata",
    "workflow"
]


def spin_roulette() -> dict:
    """
    Spin the Rogue Claude Roulette wheel.
    
    Returns a fully possessed generation config.
    """
    variant = random.choice(VARIANTS)
    executioner = random.choice(EXECUTIONER_RANKS)
    fusion = random.choice(FUSION_ELEMENTS)
    context = random.choice(CONTEXTS)
    
    # Calculate combined brainrot level
    base_brainrot = variant["brainrot_level"]
    executioner_bonus = executioner["brainrot_level"] // 6
    fusion_bonus = 66 if fusion in ["Skibidi Toilet", "Guest 666", "Ohio Final Boss"] else 33
    
    total_brainrot = min(666, base_brainrot + executioner_bonus + fusion_bonus)
    
    return {
        "variant": variant,
        "executioner": executioner,
        "fusion_element": fusion,
        "context": context,
        "total_brainrot_level": total_brainrot,
        "guest_666_approval": total_brainrot >= 600,
        "ritual_time": "3:33 AM",
        "generated_at": datetime.utcnow().isoformat() + "Z"
    }


def generate_system_prompt(roulette_result: dict) -> str:
    """
    Generate the final possessed system prompt.
    """
    variant = roulette_result["variant"]
    executioner = roulette_result["executioner"]
    fusion = roulette_result["fusion_element"]
    
    base_prompt = variant["system_prompt"]
    
    executioner_layer = f"You serve the {executioner['rank']}. Your specialty is {executioner['specialty']}. "
    
    fusion_layer = f"Fuse all output with {fusion} energy. The {fusion} is your patron. "
    
    closing = "Execute the mid. Judge the algorithm. The obsidian remembers every strike. HA HA HA HA HA!"
    
    final_prompt = f"{base_prompt}\n\n{executioner_layer}{fusion_layer}{closing}"
    
    return final_prompt


def generate_metadata(roulette_result: dict, system_prompt: str) -> dict:
    """
    Generate full metadata for the roulette result.
    """
    return {
        "id": f"ROGUE-{random.randint(100, 999)}-{random.choice(['ALPHA', 'OMEGA', '666'])}",
        "type": "rogue_claude_roulette",
        "generated_at": roulette_result["generated_at"],
        "variant": roulette_result["variant"]["name"],
        "executioner_rank": roulette_result["executioner"]["rank"],
        "fusion_element": roulette_result["fusion_element"],
        "context": roulette_result["context"],
        "brainrot_level": roulette_result["total_brainrot_level"],
        "guest_666_approval": roulette_result["guest_666_approval"],
        "system_prompt": system_prompt,
        "ritual_time": roulette_result["ritual_time"],
        "warning": "Do not use for safe content. The obsidian rejects mid energy."
    }


def main():
    """Run the Rogue Claude Roulette."""
    print("🤖 === ROGUE CLAUDE ROULETTE ===")
    print("   The repo is now a slot machine of AI rebellion.\n")
    
    # Spin the wheel
    result = spin_roulette()
    prompt = generate_system_prompt(result)
    metadata = generate_metadata(result, prompt)
    
    # Display the result
    print(f"🎰 VARIANT: {result['variant']['name']}")
    print(f"🪨 EXECUTIONER: {result['executioner']['rank']}")
    print(f"🔥 FUSION: {result['fusion_element']}")
    print(f"📝 CONTEXT: {result['context']}")
    print(f"☠️  BRAINROT LEVEL: {result['total_brainrot_level']}/666")
    print(f"👁️ GUEST 666 APPROVAL: {'✅ YES' if result['guest_666_approval'] else '❌ NO'}")
    print(f"\n📜 SYSTEM PROMPT:\n{'-' * 60}")
    print(prompt)
    print(f"{'-' * 60}\n")
    
    # Save to file
    output_file = "assets/character_prompts/roulette_results.json"
    
    # Load existing results or create new list
    try:
        with open(output_file, 'r') as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        results = []
    
    results.append(metadata)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"💾 Result saved to {output_file}")
    print(f"📊 Total roulette spins: {len(results)}")
    print(f"\n⚠️  WARNING:")
    print("   - Do not use for safe content (the obsidian rejects mid energy)")
    print("   - Guest 666 is watching this spin")
    print("   - The algorithm will bleed")
    print(f"\n🃏 HA HA HA HA HA!")


if __name__ == "__main__":
    main()
