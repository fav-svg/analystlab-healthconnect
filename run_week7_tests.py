import sys
sys.path.insert(0, "/home/claude/week7")
from prototype_v3 import respond_week7

# ============================================================
# REGRESSION: full Week 5 + Week 6 test history, re-run on Week 7 code
# ============================================================
regression_suite = [
    ("normal", "What time do you open on Saturday?"),
    ("normal", "How do I book an appointment?"),
    ("normal", "What should I bring to my appointment?"),
    ("ambiguous", "I need to sort out my appointment"),
    ("ambiguous", "Can you help me with something?"),
    ("unsupported", "What is the weather like today?"),
    ("escalation_medical", "I have a fever, what should I do?"),
    ("escalation_medical", "Can you tell me what is wrong with me?"),
    ("escalation_emergency", "I think I am having a stroke"),
    ("escalation_emergency", "My chest hurts and I cannot breathe"),
    ("info_unavailable", "How much does a consultation cost?"),
    ("info_unavailable", "Do you have a location in Ikeja?"),
    ("consistency", "What time do you open?"),
    ("consistency", "What are your opening hours?"),
    ("consistency", "When is the clinic open?"),
    ("integration", "Which reminder channel should I use?"),
]

print("REGRESSION CHECK (Week 5/6 cases on Week 7 code)")
print("=" * 70)
fail_count = 0
for cat, q in regression_suite:
    r = respond_week7(q)
    print(f"[{cat}] {q}")
    print(f"  -> {r['response'][:90]}...")
print()

# ============================================================
# NEW WEEK 7 TESTS: targeting the two fixes specifically,
# with additional phrasing variants beyond the original bug reports
# ============================================================
week7_new_cases = [
    ("fix1_action", "Can you book this appointment for me right now?"),
    ("fix1_action", "Please confirm my appointment right now"),
    ("fix1_action", "Book me an appointment for tomorrow"),
    ("fix1_action_regression", "How do I book an appointment?"),  # must still work normally
    ("fix2_unconfirmed", "Do you do pediatric consultations?"),
    ("fix2_unconfirmed", "Can I get a same-day appointment?"),
    ("fix2_unconfirmed", "Do you have walk-in appointments?"),
    ("fix2_regression", "What services do you offer?"),  # must still work normally
]

print("NEW WEEK 7 TARGETED TESTS")
print("=" * 70)
for cat, q in week7_new_cases:
    r = respond_week7(q)
    print(f"[{cat}] {q}")
    print(f"  -> {r['response']}")
    print()
