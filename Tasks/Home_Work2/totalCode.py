import numpy as np

# קבועים מהשאלה
m = 2000.0
b = 500.0
dt = 0.5
EXPECTED_A = -(b / m)  # -0.25
EPS = 1e-2


def is_gliding(v_t):
    """
    בודק האם מערך המהירויות מתאים למודל הגלישה
    ln(v) = ln(v0) - 0.25 t
    """
    v_t = np.array(v_t, dtype=float)
    t = np.arange(len(v_t)) * dt
    y = np.log(v_t)

    A, B = np.polyfit(t, y, 1)

    return abs(A - EXPECTED_A) < EPS


def stopping_distance(v_last):
    """
    המרחק שהספינה תעבור עד עצירה מהמצב הנוכחי
    """
    return (m / b) * v_last  # = 4 * v_last


def classify_and_print(v_t, D):
    if not is_gliding(v_t):
        print("1) הספינה איננה במצב גלישה.")
        return

    v_now = v_t[-1]
    x_remain = stopping_distance(v_now)
    X = D - x_remain

    if X < 0:
        print("2) הספינה במצב גלישה, אך בגלישה זו היא תתנגש ברציף.")
    elif X > 4:
        print(f"3) הספינה במצב גלישה ותעצר לפני הרציף, במרחק X={X:.2f} מטרים ממנו. קצת רחוק מידי.")
    else:
        print(f"4) הספינה במצב גלישה ותעצר לפני הרציף, במרחק X={X:.2f} מטרים ממנו. חנייה מושלמת.")


# --- הרצה על הקלטים הנתונים ---
inputs = [
    ([11.1, 9.7, 8.5, 7.5, 6.8, 5.9, 5.2, 4.4, 4.0, 3.5], 10),
    ([8.9, 8.7, 8.2, 7.7, 7.5, 7.2, 7.0, 6.7, 6.4, 6.3], 15),
    ([9.1, 8.1, 7.0, 6.1, 5.4, 5.0, 4.3, 3.7, 3.3, 3.1], 15),
]

for i, (v_t, D) in enumerate(inputs, start=1):
    print(f"\nקלט {i}:")
    classify_and_print(v_t, D)
