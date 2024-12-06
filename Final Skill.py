def final_skill(skill1, skill2, skill3, skill4, skill5):
    # Calculate Final Skill Score
    final_score = skill1 + skill2 + skill3 + skill4 + skill5
    
    # Categorize Final Score
    if final_score >= 90:
        category = "Excellent"
    elif final_score >= 70:
        category = "Very Good"
    elif final_score >= 50:
        category = "Good"
    elif final_score >= 30:
        category = "Average"
    else:
        category = "Needs Improvement"
    
    print(f"Your final skill score is: {final_score}")
    print(f"Your skill category is: {category}")
    
    return final_score, category

# Example usage
skill1, skill2, skill3, skill4, skill5 = 20, 15, 10, 8, 12
final_score, category = final_skill(skill1, skill2, skill3, skill4, skill5)
