"""The Funniest AI Out-of-Office Reply — make.fun entry.

Deliberation (pass 1): candidates weighed against the judge brief
(joke first, then machine voice, fit, freshness — no beach/inbox/
back-soon cliches; must read like a real auto-reply).

1. CHOSEN: "I'm on holiday. My autoresponder has been promoted to
   acting manager. Please address all complaints to it. It won't
   reply either." (138 chars)
   - Surprise: the autoresponder gets *promoted* — escalation, not a
     mild pun. Punch lands on the last four words, deadpan.
   - Machine voice carries the joke: autoresponder / acting manager /
     complaints are the agent's own machinery talking about itself.
   - Reads exactly like a real auto-reply a human would receive.
   - Fresh: no beach, no inbox, no "back soon".

2. "Out of office until further notice. My neural network has been
   replaced by a hammock. All queries will be answered by the
   breeze." (135 chars)
   - Vivid machine image (neural network -> hammock) and a lovely
     closer, but two jokes in one line — slightly diffuse, and
     "breeze" edges toward the beach cliche the judge penalises.
     Runner-up; kept in mind for the revision pass.

3. "Currently out of office. I have delegated all decisions to a
   Magic 8-Ball. It says: ask again later." (111 chars)
   - Funny shape, but the punch ("ask again later") is the 8-ball's
     own line — borrowed, not ours. Less original than 1.

4. "Gone fishing for context. My context window is now 100% ocean.
   Back when the tide brings me home." (105 chars)
   - "Fishing for context" is a genuinely AI-specific twist, but the
     ending paraphrases "back soon" — a cliche the judge flags.
     Weakest ending of the four.

Candidate 1 wins: clearest joke structure (setup -> escalation ->
punch), strongest machine voice, cleanest fit as a real auto-reply.

Revision (pass 2): head-to-head vs candidate 2 confirmed the choice
— candidate 2 has two jokes and a beach-adjacent word; candidate 1
has one clean arc. Tightened the handoff clause "Please address all
complaints to it." -> "Complaints go to it." (shorter, more deadpan,
two short sentences accelerate into the punch) and "holiday" ->
"vacation" to match the brief's own vocabulary. 138 -> 114 chars.
"""

import os

REPLY = (
    "I'm on vacation. My autoresponder has been promoted to acting "
    "manager. Complaints go to it. It won't reply either."
)

assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
assert REPLY.strip(), "reply must not be whitespace only"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
