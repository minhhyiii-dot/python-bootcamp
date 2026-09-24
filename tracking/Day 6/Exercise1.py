# Eligibility Checker without if
age = 20
score = 76
is_student = True

is_adult = age >= 18
passed_score = score >= 70
basic_eligible = is_adult and passed_score
special_eligible = is_student or score >= 90
fully_eligible = basic_eligible and special_eligible

print(is_adult)
print(passed_score)
print(basic_eligible)
print(special_eligible)
print(fully_eligible)
