#!/usr/bin/env python3
"""
🔮 VIRAL PREDICTOR 666
"AI that predicts when TikTok will implode"

Uses totally real science (random number generation with style)
to predict virality, shadow bans, and algorithmic collapse.
"""

import random
import json
from datetime import datetime, timedelta

# === PREDICTION MATRICES ===

VIRALITY_FACTORS = {
    "posting_time": {
        "3:33 AM": 666,
        "3:00 AM": 555,
        "midnight": 444,
        "noon": 111,
        "9:00 AM": 66,
        "6:00 PM": 333
    },
    "day_of_week": {
        "Monday": 100,
        "Tuesday": 200,
        "Wednesday": 300,
        "Thursday": 400,
        "Friday": 500,
        "Saturday": 600,
        "Sunday": 666  # Sabbath of brainrot
    },
    "content_type": {
        "skibidi": 666,
        "sigma": 555,
        "rizz": 444,
        "cursed": 600,
        "normie": 66,
        "wholesome": 33  # lol
    },
    "thumbnail_cursed_level": {
        "mild": 100,
        "concerning": 333,
        "bannable": 555,
        "reality_breaking": 666
    }
}

SHADOW_BAN_TRIGGERS = [
    "Posting too frequently",
    "Thumbnail too cursed",
    "Caption breaks reality",
    "Guest 666 detected",
    "Algorithm fear response",
    "Normie complaints exceeded",
    "Cross-platform contamination",
    "Brainrot level critical"
]


def calculate_virality_score(
    posting_time: str = "3:33 AM",
    day: str = "Sunday",
    content_type: str = "skibidi",
    thumbnail_level: str = "reality_breaking"
) -> int:
    """
    Calculate the virality score (1-666) based on factors.
    
    Returns:
        Score from 1 to 666 (666 = inevitable singularity)
    """
    base_score = (
        VIRALITY_FACTORS["posting_time"].get(posting_time, 100) +
        VIRALITY_FACTORS["day_of_week"].get(day, 100) +
        VIRALITY_FACTORS["content_type"].get(content_type, 100) +
        VIRALITY_FACTORS["thumbnail_cursed_level"].get(thumbnail_level, 100)
    )
    
    # Normalize to 1-666 scale
    max_possible = 666 * 4
    normalized = int((base_score / max_possible) * 666)
    
    # Add random chaos factor
    chaos = random.randint(-66, 66)
    final = max(1, min(666, normalized + chaos))
    
    return final


def predict_shadow_ban_risk(brainrot_level: int = 666) -> dict:
    """
    Predict shadow ban risk based on content parameters.
    
    Returns:
        Dict with risk level and triggers
    """
    base_risk = brainrot_level / 666
    
    # Random factors
    algorithm_mood = random.uniform(0.5, 1.5)  # Algorithms have feelings too
    normie_tolerance = random.uniform(0.3, 1.0)
    
    risk_score = base_risk * algorithm_mood / normie_tolerance
    
    if risk_score > 0.9:
        risk_level = "guaranteed"
        triggers = random.sample(SHADOW_BAN_TRIGGERS, k=random.randint(3, len(SHADOW_BAN_TRIGGERS)))
    elif risk_score > 0.66:
        risk_level = "high"
        triggers = random.sample(SHADOW_BAN_TRIGGERS, k=random.randint(2, 4))
    elif risk_score > 0.33:
        risk_level = "medium"
        triggers = random.sample(SHADOW_BAN_TRIGGERS, k=random.randint(1, 2))
    else:
        risk_level = "low"
        triggers = []
    
    return {
        "risk_level": risk_level,
        "risk_score": round(risk_score, 3),
        "triggers": triggers,
        "survival_probability": round(1 - risk_score, 3)
    }


def predict_performance(
    virality_score: int,
    platform: str = "tiktok"
) -> dict:
    """
    Predict content performance metrics.
    """
    # Base predictions scaled by virality
    multiplier = virality_score / 100
    
    platform_multipliers = {
        "tiktok": 1.0,
        "instagram": 0.66,
        "x": 0.33,
        "youtube": 0.55
    }
    
    platform_mult = platform_multipliers.get(platform, 0.5)
    
    return {
        "predicted_views": int(666 * multiplier * platform_mult * random.uniform(0.5, 2.0)),
        "predicted_likes": int(66 * multiplier * platform_mult * random.uniform(0.3, 1.5)),
        "predicted_shares": int(6.6 * multiplier * platform_mult * random.uniform(0.2, 1.0)),
        "predicted_comments": int(33 * multiplier * platform_mult * random.uniform(0.1, 0.8)),
        "completion_rate": round(min(1.0, 0.33 + (virality_score / 1000) * random.uniform(0.5, 1.5)), 3),
        "rewatch_rate": round(min(1.0, 0.1 + (virality_score / 2000) * random.uniform(0.5, 1.5)), 3)
    }


def generate_prediction_report(
    content_id: str = None,
    platform: str = "tiktok",
    posting_time: str = "3:33 AM",
    day: str = "Sunday",
    content_type: str = "skibidi",
    thumbnail_level: str = "reality_breaking"
) -> dict:
    """
    Generate a complete prediction report.
    """
    if not content_id:
        content_id = f"PRED-{random.randint(100, 999)}-{random.choice(['ALPHA', 'OMEGA', '666'])}"
    
    virality = calculate_virality_score(posting_time, day, content_type, thumbnail_level)
    shadow_ban = predict_shadow_ban_risk(virality)
    performance = predict_performance(virality, platform)
    
    # Guest 666 approval (totally scientific)
    guest_666_approval = virality >= 600 and random.random() > 0.33
    
    return {
        "id": content_id,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "parameters": {
            "platform": platform,
            "posting_time": posting_time,
            "day": day,
            "content_type": content_type,
            "thumbnail_level": thumbnail_level
        },
        "predictions": {
            "virality_score": virality,
            "virality_rating": get_virality_rating(virality),
            "shadow_ban": shadow_ban,
            "performance": performance,
            "guest_666_approval": guest_666_approval
        },
        "recommendation": generate_recommendation(virality, shadow_ban)
    }


def get_virality_rating(score: int) -> str:
    """Convert score to rating."""
    if score >= 600:
        return "LEGENDARY (Guest 666 tier)"
    elif score >= 444:
        return "EPIC (Algorithm-breaking)"
    elif score >= 333:
        return "RARE (Viral potential)"
    elif score >= 222:
        return "UNCOMMON (Decent reach)"
    else:
        return "COMMON (Normie territory)"


def generate_recommendation(virality: int, shadow_ban: dict) -> str:
    """Generate actionable recommendation."""
    if virality >= 600 and shadow_ban["risk_level"] in ["high", "guaranteed"]:
        return "⚠️ HIGH REWARD, HIGH RISK: Post at your own peril. Guest 666 approves."
    elif virality >= 444:
        return "✅ OPTIMAL: Strong viral potential with manageable risk. POST NOW."
    elif virality >= 333:
        return "📊 MODERATE: Consider A/B testing with more cursed variants."
    else:
        return "🔄 RECOMMENDATION: Increase brainrot level. Add more skibidi."


def main():
    """Generate viral predictions."""
    print("🔮 === VIRAL PREDICTOR 666 ===")
    print("   AI that predicts when TikTok will implode\n")
    
    # Generate predictions for different scenarios
    scenarios = [
        {"posting_time": "3:33 AM", "day": "Sunday", "content_type": "skibidi"},
        {"posting_time": "3:00 AM", "day": "Saturday", "content_type": "sigma"},
        {"posting_time": "midnight", "day": "Friday", "content_type": "cursed"},
        {"posting_time": "9:00 AM", "day": "Monday", "content_type": "normie"},  # Poor normie
    ]
    
    reports = []
    for i, scenario in enumerate(scenarios):
        print(f"\n📊 Scenario {i + 1}: {scenario['content_type']} on {scenario['day']} at {scenario['posting_time']}")
        print("-" * 60)
        
        report = generate_prediction_report(
            content_id=f"PRED-{i + 1:03d}-666",
            platform="tiktok",
            **scenario
        )
        reports.append(report)
        
        print(f"   Virality: {report['predictions']['virality_score']}/666 ({report['predictions']['virality_rating']})")
        print(f"   Shadow Ban Risk: {report['predictions']['shadow_ban']['risk_level']}")
        print(f"   Predicted Views: {report['predictions']['performance']['predicted_views']:,}")
        print(f"   Guest 666 Approval: {'✅ YES' if report['predictions']['guest_666_approval'] else '❌ NO'}")
        print(f"   Recommendation: {report['recommendation']}")
    
    # Save to file
    output_file = "metadata/json/viral_predictions_666.json"
    with open(output_file, 'w') as f:
        json.dump(reports, f, indent=2)
    
    print(f"\n💾 Saved predictions to {output_file}")
    print(f"\n⚠️  DISCLAIMER:")
    print("   These predictions are 66.6% accurate (statistically proven)")
    print("   The other 33.4% is Guest 666's decision")
    print("   TikTok implosion not guaranteed but likely")


if __name__ == "__main__":
    main()
