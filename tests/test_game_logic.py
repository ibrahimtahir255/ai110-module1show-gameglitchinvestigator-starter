from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

# Bug fix 1: hint messages were backwards (Too High said "Go HIGHER", Too Low said "Go LOWER")
def test_too_high_hint_message():
    # When guess is too high, player should be told to go LOWER
    result = check_guess(80, 50)
    assert "LOWER" in result[1]

def test_too_low_hint_message():
    # When guess is too low, player should be told to go HIGHER
    result = check_guess(20, 50)
    assert "HIGHER" in result[1]

# Bug fix 2: Hard difficulty had range 1-50 (easier than Normal), should be 1-200
def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert high > 100  # Hard should be harder than Normal (1-100)

def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

# Bug fix 3: update_score gave +5 points on even attempts for "Too High" instead of always -5
def test_too_high_score_always_deducts():
    # Even attempt — should still deduct, not award points
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 95

def test_too_high_score_odd_attempt_deducts():
    # Odd attempt — should also deduct
    score = update_score(100, "Too High", attempt_number=3)
    assert score == 95

def test_too_low_score_deducts():
    score = update_score(100, "Too Low", attempt_number=1)
    assert score == 95

def test_win_score_awards_points():
    score = update_score(0, "Win", attempt_number=0)
    assert score == 90  # 100 - 10 * (0 + 1) = 90

def test_win_score_minimum_points():
    # Late attempt — should award minimum 10 points
    score = update_score(0, "Win", attempt_number=20)
    assert score == 10
