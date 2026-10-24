
import gradio as gr

def student_preferences(name, age, course, subjects, learning_mode,
                       study_time, hobbies, notifications):

    if not name.strip():
        return "Please enter your name."

    if not subjects:
        return "Please select at least one preferred subject."

    subject_list = ", ".join(subjects)
    hobby_text = hobbies.strip() if hobbies.strip() else "Not specified"
    notification_text = "Enabled" if notifications else "Disabled"

    return f"""
# Student Preference Summary

**Name:** {name}
**Age:** {age}
**Preferred Course:** {course}

**Favorite Subjects:** {subject_list}
**Learning Mode:** {learning_mode}
**Preferred Study Time:** {study_time}
**Hobbies and Interests:** {hobby_text}
**Notifications:** {notification_text}

Thank you for sharing your preferences!
"""


with gr.Blocks(title="Student Preferences") as demo:
    gr.Markdown("# Student Preferences Portal")
    gr.Markdown(
        "Enter your information and preferences "
        "to personalize your learning experience."
    )

    with gr.Row():
        name = gr.Textbox(label="Student Name", placeholder="Enter your name")
        age = gr.Slider(
            minimum=10, maximum=60, value=18, step=1,
            label="Age"
        )

    course = gr.Dropdown(
        choices=[
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Mechanical Engineering",
            "Business Administration",
            "Arts and Humanities",
            "Science",
            "Other"
        ],
        label="Preferred Course",
        value="Computer Science"
    )

    subjects = gr.CheckboxGroup(
        choices=[
            "Mathematics",
            "Programming",
            "Science",
            "English",
            "Data Science",
            "Artificial Intelligence",
            "Business Studies",
            "Arts"
        ],
        label="Preferred Subjects"
    )

    learning_mode = gr.Radio(
        choices=[
            "Online",
            "Classroom",
            "Hybrid"
        ],
        label="Preferred Learning Mode",
        value="Online"
    )

    study_time = gr.Dropdown(
        choices=[
            "Morning",
            "Afternoon",
            "Evening",
            "Night"
        ],
        label="Preferred Study Time",
        value="Evening"
    )

    hobbies = gr.Textbox(
        label="Hobbies and Interests",
        placeholder="e.g., coding, reading, sports",
        lines=2
    )

    notifications = gr.Checkbox(
        label="Receive learning reminders",
        value=True
    )

    with gr.Row():
        submit = gr.Button("Save Preferences", variant="primary")
        clear = gr.Button("Clear Form")

    output = gr.Markdown(label="Preference Summary")

    submit.click(
        fn=student_preferences,
        inputs=[
            name, age, course, subjects, learning_mode,
            study_time, hobbies, notifications
        ],
        outputs=output
    )

    clear.click(
        fn=lambda: (
            "", 18, "Computer Science", [], "Online",
            "Evening", "", True, ""
        ),
        inputs=[],
        outputs=[
            name, age, course, subjects, learning_mode,
            study_time, hobbies, notifications, output
        ]
    )


if __name__ == "__main__":
    demo.launch()
