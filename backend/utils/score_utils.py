def get_score_color(score: int) -> str:
    if score >= 75:
        return "green"
    elif score >= 50:
        return "yellow"
    else:
        return "red"
def is_ready_for_placement(score: int) -> bool:
    return score >= 60
    
