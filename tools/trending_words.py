TRENDING_WORDS_EN = [
    "glazing",
    "mogging",
    "yapping",
    "mid",
    "clocked",
    "NPC",
    "ratio",
    "crash out",
    "rizz",
    "slay",
]

TRENDING_WORDS_DE = [
    "Digga",
    "Ehrenmann",
    "cringe",
    "wild",
    "Alman",
    "Mittwoch",
    "Brudi",
    "lost",
    "Bre",
    "Habibi",
]

SUPPORTED_LANGUAGES = {
    "english": TRENDING_WORDS_EN,
    "german": TRENDING_WORDS_DE,
}


def most_trending_words(language: str = "english", limit: int | None = None) -> list[str]:
    """Get the most trending words right now.

    Args:
        language: Language to return trending words for. Supported: "english", "german".
        limit: Maximum number of words to return. Omit for all words.

    Returns:
        A list of currently trending words.
    """
    lang = language.lower()
    if lang not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {language!r}. Supported: {', '.join(SUPPORTED_LANGUAGES)}")
    words = SUPPORTED_LANGUAGES[lang]
    return words[:limit]
