def chatbot():
    print("Assistant: Hello! Are you interested in admission to our Nursing College? (Yes/No)")

    while True:
        user = input("You: ").lower()

        if user in ["yes", "haan", "tell me", "okay"]:
            print("Assistant: Did you study Biology in 12th standard? (Yes/No)")
            user = input("You: ").lower()

            if user in ["yes", "haan"]:
                print("Assistant: B.Sc Nursing is a full-time program. Would you like more details? (Yes/No)")
                user = input("You: ").lower()

                if user in ["yes", "haan"]:
                    print("""
Assistant: Course Details:
- Tuition Fee: ₹60,000
- Bus Fee: ₹10,000
- Total per year: ₹70,000

Fees are paid in three parts:
1. ₹30,000 at admission
2. ₹20,000 after first semester
3. ₹20,000 after second semester
""")
                    print("Assistant: Hostel has 24x7 water and electricity, CCTV security, and a warden.")
                    print("Assistant: Hospital training is included, so students work with real patients.")
                    print("Assistant: The college is in Delhi. Do you want to know more about the location? (Yes/No)")
                    user = input("You: ").lower()

                    if user in ["yes", "haan"]:
                        print("Assistant: The college is in a central area, near markets, hospitals, and public transport.")

                    print("""
Assistant: Recognition:
- Approved by the Indian Nursing Council (INC), Delhi

Clinical training happens at:
- District Hospital (Backundpur)
- Community Health Centers
- Regional Hospital (Chartha)
- Ranchi Neurosurgery & Allied Science Hospital (Jharkhand)

Scholarships:
- Govt Post-Matric Scholarship (₹18,000–₹23,000)
- Labour Ministry Scholarship (₹40,000–₹48,000) for students with Labour registration

Total seats: 60
Eligibility:
- Must have studied Biology in 12th grade
- Need to pass the PNT Exam
- Age should be between 17 and 35 years
""")

                    print("Assistant: Do you have any more questions? (Yes/No)")
                    user = input("You: ").lower()
                    if user in ["yes", "haan"]:
                        print("Assistant: Please ask your question now.")
                    else:
                        print("Assistant: Thank you! Best wishes for your admission.")
                        break

                else:
                    print("Assistant: Okay, you can ask for details anytime.")
                    break

            else:
                print("Assistant: Biology in 12th grade is required for B.Sc Nursing admission.")
                break

        elif user in ["no", "nahi"]:
            print("Assistant: Okay, feel free to ask anytime in the future. Thank you!")
            break

        else:
            print("Assistant: Please reply with 'Yes' or 'No'.")

# Start the chatbot
chatbot()
