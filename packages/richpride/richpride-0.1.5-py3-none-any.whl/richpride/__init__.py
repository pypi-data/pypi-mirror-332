from rich.emoji import EMOJI


def flag_setup():
    # B = Blue
    # b = Black

    # P = Pink
    # p = Purple

    # G = Green
    # g = Gray

    EMOJI["trans_flag"] = "🏳️‍⚧️"
    EMOJI["trans_flag_alt"] = "[Trans Flag]"
    EMOJI["trans_flag_ascii"] = "[💙💗🤍💗💙]"
    EMOJI["trans_flag_ascii_alt"] = "[B P W P B]"
    EMOJI["trans_flag_block"] = """
💙💙💙💙💙
💗💗💗💗💗
🤍🤍🤍🤍🤍
💗💗💗💗💗
💙💙💙💙💙
"""
    EMOJI["trans_flag_block_alt"] = """
B B B B B
P P P P P
W W W W W
P P P P P
B B B B B
"""

    EMOJI["pride_flag"] = "🏳️‍🌈"
    EMOJI["pride_flag_alt"] = "[Pride Flag]"
    EMOJI["pride_flag_ascii"] = "[❤️🧡💛💚💙💜]"
    EMOJI["pride_flag_ascii_alt"] = "[R O Y G B p]"
    EMOJI["pride_flag_block"] = """
❤️❤️❤️❤️❤️
🧡🧡🧡🧡🧡
💛💛💛💛💛
💚💚💚💚💚
💙💙💙💙💙
💜💜💜💜💜
"""
    EMOJI["pride_flag_block_alt"] = """
R R R R R
O O O O O
Y Y Y Y Y
G G G G G
B B B B B
p p p p p
"""

    EMOJI["nonbinary_flag_ascii"] = "[💛🤍💜🖤]"
    EMOJI["nonbinary_flag_ascii_alt"] = "[Y W p b]"
    EMOJI["nonbinary_flag_block"] = """
💛💛💛💛💛
🤍🤍🤍🤍🤍
💜💜💜💜💜
🖤🖤🖤🖤🖤
"""
    EMOJI["nonbinary_flag_block_alt"] = """
Y Y Y Y Y
W W W W W
p p p p p
b b b b b
"""

    EMOJI["genderfluid_flag_ascii"] = "[💗🤍💜🖤💙]"
    EMOJI["genderfluid_flag_ascii_alt"] = "[P W p b B]"
    EMOJI["genderfluid_flag_block"] = """
💗💗💗💗💗
🤍🤍🤍🤍🤍
💜💜💜💜💜
🖤🖤🖤🖤🖤
💙💙💙💙💙
"""
    EMOJI["genderfluid_flag_block_alt"] = """
P P P P P
W W W W W
p p p p p
b b b b b
B B B B B
"""

    EMOJI["pansexual_flag_ascii"] = "[💗💛💙]"
    EMOJI["pansexual_flag_ascii_alt"] = "[P Y B]"
    EMOJI["pansexual_flag_block"] = """
💗💗💗💗💗
💗💗💗💗💗
💛💛💛💛💛
💛💛💛💛💛
💙💙💙💙💙
💙💙💙💙💙
"""
    EMOJI["pansexual_flag_block_alt"] = """
P P P P P
P P P P P
Y Y Y Y Y
Y Y Y Y Y
B B B B B
B B B B B
"""

    EMOJI["asexual_flag_ascii"] = "[🖤🩶🤍💜]"
    EMOJI["asexual_flag_ascii_alt"] = "[b g W p]"
    EMOJI["asexual_flag_block"] = """
🖤🖤🖤🖤🖤
🩶🩶🩶🩶🩶
🤍🤍🤍🤍🤍
💜💜💜💜💜
"""
    EMOJI["asexual_flag_block_alt"] = """
b b b b b
g g g g g
W W W W W
p p p p p
"""

    EMOJI["bisexual_flag_ascii"] = "[💗💗💜💙💙]"
    EMOJI["bisexual_flag_ascii_alt"] = "[P P p B B]"
    EMOJI["bisexual_flag_block"] = """
💗💗💗💗💗
💗💗💗💗💗
💜💜💜💜💜
💙💙💙💙💙
💙💙💙💙💙
"""
    EMOJI["bisexual_flag_block_alt"] = """
P P P P P
P P P P P
p p p p p
B B B B B
B B B B B
"""

    EMOJI["lesbian_flag_ascii"] = "[🧡💗🤍💜❤️]"
    EMOJI["lesbian_flag_ascii_alt"] = "[O P W p R]"
    EMOJI["lesbian_flag_block"] = """
🧡🧡🧡🧡🧡
💗💗💗💗💗
🤍🤍🤍🤍🤍
💜💜💜💜💜
❤️❤️❤️❤️❤️
"""
    EMOJI["lesbian_flag_block_alt"] = """
O O O O O
P P P P P
W W W W W
p p p p p
R R R R R
"""

    EMOJI["agender_flag_ascii"] = "[🖤🩶🤍💚🤍🩶🖤]"
    EMOJI["agender_flag_ascii_alt"] = "[B g W G W g B]"
    EMOJI["agender_flag_block"] = """
🖤🖤🖤🖤🖤
🩶🩶🩶🩶🩶
🤍🤍🤍🤍🤍
💚💚💚💚💚
🤍🤍🤍🤍🤍
🩶🩶🩶🩶🩶
🖤🖤🖤🖤🖤
"""
    EMOJI["agender_flag_block_alt"] = """
b b b b b
g g g g g
W W W W W
G G G G G
W W W W W
g g g g g
b b b b b
"""

    EMOJI["genderqueer_flag_ascii"] = "[💜🤍💚]"
    EMOJI["genderqueer_flag_ascii_alt"] = "[p W G]"
    EMOJI["genderqueer_flag_block"] = """
💜💜💜💜💜
💜💜💜💜💜
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
💚💚💚💚💚
💚💚💚💚💚
"""
    EMOJI["genderqueer_flag_block_alt"] = """
p p p p p
p p p p p
W W W W W
W W W W W
G G G G G
G G G G G
"""


flag_setup()


def list_flags():
    at_flags = False

    for emoji in EMOJI:
        if emoji == "trans_flag":
            at_flags = True

        if at_flags:
            print(f":{emoji}:")

        if emoji == "genderqueer_flag_block_alt":
            break


def split_into_n_parts(s: str, n: int) -> list:
    """
    Splits the given string into 'n' parts, middle splits getting extra characters when needed.
    Examples:
        "trans rights" (len=12) → 6×2 → ['tr','an','s ','ri','gh','ts']
        "trans rights!" (len=13) → middle split gets +1 → ['tr','an','s r','ig','ht','s!']
    """
    str_len = len(s)
    base_len, remainder = divmod(str_len, n)

    start = (n - remainder) // 2
    lengths = [base_len] * n

    for i in range(start, start + remainder):
        lengths[i] += 1

    result = []
    idx = 0
    for length in lengths:
        result.append(s[idx : idx + length])
        idx += length

    return result


def transify(text):
    text = str(text)
    if len(text) < 5:
        raise ValueError("Text must be at least 5 characters long.")
    t_blue = "[#5BCEFA]"
    t_pink = "[#F5A9B8]"
    t_white = "[#FFFFFF]"
    split = split_into_n_parts(text, 5)
    transed = []
    for idx, part in enumerate(split):
        if idx in [0, 4]:
            transed.append(t_blue + part)
        if idx in [1, 3]:
            transed.append(t_pink + part)
        if idx == 2:
            transed.append(t_white + part)
    return "".join(transed)


def list_emojis():
    at_flags = False

    for emoji in EMOJI:
        if emoji == "trans_flag":
            at_flags = True

        if at_flags:
            print(EMOJI[emoji])

        if emoji == "genderqueer_flag_block_alt":
            break
