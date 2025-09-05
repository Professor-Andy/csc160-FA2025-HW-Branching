#instructor only code block
def test():
    # Define expected grade boundaries
    def expected_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    failed_cases = []

    for score in range(0, 101):
        try:
            result = grade_to_letter(score)
            expected = expected_grade(score)
            if result != expected:
                failed_cases.append((score, result, expected))
        except Exception as e:
            failed_cases.append((score, str(e), expected_grade(score)))

    if not failed_cases:
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(failed_cases)} test(s) failed:")
        for score, result, expected in failed_cases:
            print(f"  Score: {score} → Returned: {result} | Expected: {expected}")

#work inside this function 
#       |    |   |   |   |
#       V    V   V   V   V
def grade_to_letter(score):
    # Your code goes here
    #example 
    #if score >= 90:
    #   letter_grade = "A"
    #elif ...

    return letter_grade

test()