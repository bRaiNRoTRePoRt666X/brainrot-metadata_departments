#!/usr/bin/env python3
"""
🎨 THUMBNAIL HELL GENERATOR
"GroK Imagine on bath salts"

Generates thumbnail prompts so unhinged they get banned in 11 countries.
"""

import random
import json
from datetime import datetime

# === CURSED ELEMENT POOLS ===

SUBJECTS = [
    "A toilet with glowing eyes",
    "Sigma male with laser eyes",
    "Skibidi head emerging from phone",
    "Demon child with rizz aura",
    "Cursed emoji fusion",
    "Ancient Aztec meme god",
    "Guest 666 silhouette",
    "Algorithm personified as eldritch horror",
    "Brainrot virus microscopic view",
    "Thumbnail so cursed it glitches"
]

ACTIONS = [
    "singing into a microphone",
    "staring directly into your soul",
    "emerging from the void",
    "laughing at 3AM",
    "summoning the algorithm",
    "breaking the fourth wall",
    "ascending to sigmahood",
    "performing unholy rituals",
    "collecting dopamine",
    "existing outside reality"
]

ENVIRONMENTS = [
    "in a purple void",
    "at exactly 3:33 AM",
    "inside a TikTok thumbnail",
    "on the For You Page",
    "in a shadow-banned dimension",
    "surrounded by cursed emojis",
    "with demonic lighting",
    "against a glitching background",
    "in the brainrot realm",
    "where the algorithm cries"
]

MODIFIERS = [
    "hyper-detailed",
    "glitching",
    "cursed",
    "demonic",
    "sigma-enhanced",
    "rizz-infused",
    "unhinged",
    "forbidden",
    "reality-breaking",
    "666-level brainrot"
]

COLORS = [
    "neon purple",
    "demonic red",
    "cursed green",
    "void black",
    "sigma gold",
    "algorithm blue",
    "brainrot rainbow",
    "3AM gray"
]

EMOJIS = ["🃏", "👹", "🚽", "👁️", "⚡", "☠️", "🔥", "💀", "🎭", "6️⃣"]


def generate_thumbnail_prompt(chaos_level: int = 666) -> str:
    """
    Generate a thumbnail prompt that would make a normal AI therapist concerned.
    
    Args:
        chaos_level: 1-666, how unhinged should this be?
    
    Returns:
        A prompt so cursed it might summon Guest 666
    """
    # Scale complexity based on chaos level
    num_modifiers = max(1, chaos_level // 222)
    
    subject = random.choice(SUBJECTS)
    action = random.choice(ACTIONS)
    environment = random.choice(ENVIRONMENTS)
    modifiers = random.sample(MODIFIERS, min(num_modifiers, len(MODIFIERS)))
    primary_color = random.choice(COLORS)
    emoji = random.choice(EMOJIS)
    
    prompt = f"{emoji} {subject} {action}, {environment}, "
    prompt += f"{', '.join(modifiers)}, {primary_color} color scheme"
    
    if chaos_level >= 333:
        prompt += ", hyper-detailed, 8K resolution"
    
    if chaos_level >= 666:
        prompt += ", so cursed it breaks reality, Guest 666 approved"
    
    return prompt


def generate_thumbnail_metadata(prompt: str, strain_id: str = None) -> dict:
    """Generate full metadata for a cursed thumbnail."""
    
    if not strain_id:
        strain_id = f"THMB-{random.randint(100, 999)}-{random.choice(['ALPHA', 'BETA', 'OMEGA', '666'])}"
    
    return {
        "id": strain_id,
        "type": "thumbnail",
        "prompt": prompt,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "chaos_level": random.randint(333, 666),
        "ban_probability": round(random.uniform(0.3, 0.99), 2),
        "countries_that_will_ban": random.randint(1, 11),
        "guest_666_reaction": random.choice([
            "laughing",
            "approving",
            "summoned",
            "concerned but intrigued",
            "already shared it"
        ])
    }


def main():
    """Generate a batch of cursed thumbnails."""
    print("🎨 === THUMBNAIL HELL GENERATOR ===")
    print("   GroK Imagine on bath salts\n")
    
    count = 6  # Generate 6 thumbnails (not 66, we're not monsters... yet)
    
    thumbnails = []
    for i in range(count):
        prompt = generate_thumbnail_prompt()
        metadata = generate_thumbnail_metadata(prompt)
        thumbnails.append(metadata)
        
        print(f"\n🃏 Thumbnail #{i + 1}:")
        print(f"   ID: {metadata['id']}")
        print(f"   Prompt: {prompt}")
        print(f"   Ban Probability: {metadata['ban_probability'] * 100:.0f}%")
        print(f"   Guest 666: {metadata['guest_666_reaction']}")
    
    # Save to file
    output_file = "metadata/json/thumbnails_batch_666.json"
    with open(output_file, 'w') as f:
        json.dump(thumbnails, f, indent=2)
    
    print(f"\n💾 Saved {count} cursed thumbnails to {output_file}")
    print(f"\n⚠️  WARNING: These thumbnails may cause:")
    print("   - Algorithm confusion")
    print("   - Normie distress")
    print("   - Spontaneous shadow bans")
    print("   - Guest 666 appearances")


if __name__ == "__main__":
    main()
