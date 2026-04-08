def grade_easy(actions):
    """Grade: did the agent correctly label at least one email as urgent?"""
    if not actions:
        return 0.1
    urgent_count = sum(1 for a in actions if a.get('label') == 'urgent')
    if urgent_count == 0:
        return 0.1
    score = 0.1 + (urgent_count / 10) * 0.8
    return round(min(score, 0.9), 4)


def grade_medium(actions):
    """Grade: fraction of spam/normal labels out of expected 6."""
    if not actions:
        return 0.1
    matched = sum(1 for a in actions if a.get('label') in ['spam', 'normal'])
    score = 0.1 + (min(matched, 6) / 6) * 0.8
    return round(min(max(score, 0.1), 0.9), 4)


def grade_hard(actions):
    """Grade: classification accuracy + reply quality bonus."""
    expected = {
        1: 'urgent',
        2: 'spam',
        3: 'normal',
        4: 'normal',
        5: 'urgent',
        6: 'normal',
        7: 'normal',
        8: 'urgent',
        9: 'normal',
        10: 'spam',
    }
    if not actions:
        return 0.1

    correct = 0
    reply_quality = 0.0

    for a in actions:
        if expected.get(a.get('email_id')) == a.get('label'):
            correct += 1
        if a.get('response') and len(a.get('response', '')) > 20:
            reply_quality += 0.03

    total = len(expected)
    raw = (correct / total) + reply_quality
    score = 0.1 + (min(raw, 1.0) * 0.8)
    return round(min(max(score, 0.1), 0.9), 4)
