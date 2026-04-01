#!/usr/bin/env python3
"""
📝 CAPTION APOCALYPSE
"Generates captions that melt brains in 0.3s"

Creates captions so perfectly unhinged they hijack attention spans
on contact.
"""

import random
import json
from datetime import datetime

# === BRAINROT COMPONENTS ===

OPENERS = [
    "POV:",
    "When you realize:",
    "That moment when:",
    "Nobody:",
    "Me at 3AM:",
    "The algorithm hates this but:",
    "Shadow-banned energy only:",
    "Guest 666 would approve:",
    "Wait for it...",
    "This shouldn't exist but:",
    "Normies won't understand:",
    "Breaking the simulation:",
    "The toilet sings:",
    "Sigma grindset:",
    "Rizz level: infinite:"
]

HOOKS = [
    "you were never supposed to see this",
    "the algorithm is crying rn",
    "this breaks 11 countries' laws",
    "Guest 666 is watching",
    "the void is staring back",
    "reality is glitching",
    "your dopamine is mine",
    "the skibidi has begun",
    "sigma transcendance achieved",
    "the rizz is uncontainable",
    "this video is self-aware",
    "the thumbnail is a portal",
    "you've been selected",
    "the grind never stops",
    "3AM energy activated"
]

MIDDLE_BITS = [
    "and I'm not sorry",
    "but make it cursed",
    "in a world of beige",
    "while normies seethe",
    "as the algorithm weeps",
    "with unhinged energy",
    "beyond the void",
    "outside the simulation",
    "in the brainrot realm",
    "where sigma meets skibidi",
    "with maximum rizz",
    "at exactly 3:33 AM",
    "in 666 dimensions",
    "past the event horizon",
    "inside the glitch"
]

CLOSERS = [
    "🃏",
    "👹",
    "🚽",
    "👁️",
    "⚡",
    "☠️",
    "🔥",
    "💀",
    "6️⃣6️⃣6️⃣",
    "🎭",
    "#fyp",
    "#brainrot",
    "#cursed",
    "#3am",
    "#skibidi"
]

HASHTAG_POOLS = {
    "tiktok": ["#fyp", "#foryou", "#viral", "#trending", "#brainrot", "#cursed", "#3am", "#skibidi", "#sigma", "#rizz"],
    "instagram": ["#explore", "#viral", "#meme", "#cursed", "#aesthetic", "#3am", "#brainrot", "#relatable"],
    "x": ["#viral", "#trending", "#cursed", "#brainrot", "#3am", "#meme", "#skibidi"],
    "universal": ["#brainrot", "#cursed", "#3am", "#viral", "#skibidi", "#sigma", "#rizz", "#fyp"]
}


def generate_caption(
    platform: str = "tiktok",
    brainrot_level: int = 666,
    include_hashtags: bool = True
) -> str:
    """
    Generate a caption that melts brains in 0.3 seconds flat.
    
    Args:
        platform: Target platform (tiktok, instagram, x, universal)
        brainrot_level: 1-666, how much should this break minds?
        include_hashtags: Whether to append cursed hashtags
    
    Returns:
        A caption so unhinged it might become sentient
    """
    # Scale complexity based on brainrot level
    if brainrot_level < 222:
        # Normie-tier caption
        caption = f"{random.choice(OPENERS)} {random.choice(HOOKS)}"
    elif brainrot_level < 444:
        # Mid-tier brainrot
        caption = f"{random.choice(OPENERS)} {random.choice(HOOKS)}, {random.choice(MIDDLE_BITS)}"
    else:
        # Maximum brainrot
        opener = random.choice(OPENERS)
        hook = random.choice(HOOKS)
        middle = random.choice(MIDDLE_BITS)
        closer = random.choice(CLOSERS)
        caption = f"{opener} {hook}, {middle} {closer}"
    
    # Add hashtags if requested
    if include_hashtags:
        hashtags = HASHTAG_POOLS.get(platform, HASHTAG_POOLS["universal"])
        num_hashtags = min(6, len(hashtags)) if brainrot_level < 444 else min(10, len(hashtags))
        selected = random.sample(hashtags, num_hashtags)
        caption += " " + " ".join(selected)
    
    return caption


def generate_caption_variants(
    count: int = 6,
    platform: str = "tiktok",
    brainrot_level: int = 666
) -> list:
    """Generate multiple caption variants for A/B testing."""
    
    variants = []
    for i in range(count):
        caption = generate_caption(platform, brainrot_level)
        variants.append({
            "id": i + 1,
            "caption": caption,
            "character_count": len(caption),
            "emoji_count": sum(1 for c in caption if c in "🃏👹🚽👁️⚡☠️🔥💀🎭6️⃣"),
            "hashtag_count": caption.count("#"),
            "brainrot_level": brainrot_level
        })
    
    return variants


def generate_full_metadata(caption: str, strain_id: str = None) -> dict:
    """Generate complete metadata for a caption."""
    
    if not strain_id:
        strain_id = f"CAPT-{random.randint(100, 999)}-{random.choice(['ALPHA', 'BETA', 'OMEGA', '666'])}"
    
    return {
        "id": strain_id,
        "type": "caption",
        "caption": caption,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "character_count": len(caption),
        "optimization": {
            "hook_strength": random.randint(66, 666),
            "retention_prediction": round(random.uniform(0.3, 0.99), 2),
            "share_probability": round(random.uniform(0.1, 0.66), 2)
        }
    }


def main():
    """Generate a batch of apocalyptic captions."""
    print("📝 === CAPTION APOCALYPSE ===")
    print("   Melting brains in 0.3s\n")
    
    platforms = ["tiktok", "instagram", "x", "universal"]
    
    for platform in platforms:
        print(f"\n🎯 Platform: {platform}")
        print("-" * 40)
        
        caption = generate_caption(platform, brainrot_level=666)
        metadata = generate_full_metadata(caption)
        
        print(f"   ID: {metadata['id']}")
        print(f"   Caption: {caption}")
        print(f"   Hook Strength: {metadata['optimization']['hook_strength']}/666")
        print(f"   Retention: {metadata['optimization']['retention_prediction'] * 100:.1f}%")
    
    # Generate variants for one platform
    print(f"\n\n🧪 === A/B TEST VARIANTS ===")
    variants = generate_caption_variants(count=6, platform="tiktok")
    
    for v in variants:
        print(f"\n   Variant {v['id']}: {v['caption'][:80]}...")
    
    # Save to file
    output_file = "metadata/json/captions_batch_666.json"
    with open(output_file, 'w') as f:
        json.dump({
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "platforms": platforms,
            "variants": variants
        }, f, indent=2)
    
    print(f"\n💾 Saved captions to {output_file}")
    print(f"\n⚠️  WARNING: These captions may cause:")
    print("   - Spontaneous attention hijacking")
    print("   - Compulsive rewatching")
    print("   - Algorithm confusion")
    print("   - Normie existential crises")


if __name__ == "__main__":
    main()
