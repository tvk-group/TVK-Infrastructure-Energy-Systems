#!/usr/bin/env python3
"""Post-process ur.json and he.json for proper nouns and remaining English."""
import json
import re
from pathlib import Path

MESSAGES = Path(__file__).resolve().parent.parent / "messages"

UR_REPLACEMENTS = [
    ("TVK ماحولیاتی نظام", "TVK Ecosystem"),
    ("وسیع تر TVK ٹیکنالوجی ماحولیاتی نظام", "وسیع TVK ٹیکنالوجی Ecosystem"),
    ("ماحولیاتی نظام ٹیکنالوجی سیدھ", "ایکو سسٹم ٹیکنالوجی ہم آہنگی"),
    ("بڑے ماحولیاتی نظام", "وسیع TVK Ecosystem"),
    ("All rights reserved.", "جملہ حقوق محفوظ ہیں۔"),
    ("Developing future-focused initiatives across energy, infrastructure, industrial systems and strategic technologies within the TVK ecosystem.", 
     "TVK Ecosystem میں توانائی، انفراسٹرکچر، صنعتی نظام اور اسٹریٹجک ٹیکنالوجیز میں مستقبل پر مبنی اقدامات تیار کرنا۔"),
]

HE_REPLACEMENTS = [
    ("המערכת האקולוגית של TVK", "TVK Ecosystem"),
    ("מערכת האקולוגית של TVK", "TVK Ecosystem"),
    ("המערכת האקולוגית הרחבה יותר של TVK", "TVK Ecosystem הרחב"),
    ("בתוך המערכת האקולוגית של TVK", "ב-TVK Ecosystem"),
    ("בתוך מערכת האקולוגית של TVK", "ב-TVK Ecosystem"),
    ("אינטגרציה של מערכת אקולוגית", "שילוב במערכת אקולוגית"),
    ("האקולוגית הרחבה יותר של טכנולוגיית TVK", "TVK Ecosystem הטכנולוגי הרחב"),
    ("יישור טכנולוגיית מערכת אקולוגית", "יישור טכנולוגיית Ecosystem"),
    ("ממערכת אקולוגית גדולה יותר", "מ-TVK Ecosystem הרחב"),
    ("All rights reserved.", "כל הזכויות שמורות."),
]


def apply_replacements(obj, replacements):
    if isinstance(obj, str):
        result = obj
        for old, new in replacements:
            result = result.replace(old, new)
        result = result.replace("TVK Ecosystem", "TVK Ecosystem")
        return result
    if isinstance(obj, list):
        return [apply_replacements(x, replacements) for x in obj]
    if isinstance(obj, dict):
        return {k: apply_replacements(v, replacements) for k, v in obj.items()}
    return obj


def main():
    for locale, replacements in [("ur", UR_REPLACEMENTS), ("he", HE_REPLACEMENTS)]:
        path = MESSAGES / f"{locale}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data = apply_replacements(data, replacements)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Post-processed {locale}.json")


if __name__ == "__main__":
    main()
