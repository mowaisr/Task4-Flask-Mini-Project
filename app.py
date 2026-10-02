from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory task storage
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Complete internship task", "completed": True}
]


@app.route("/")
def index():
    """Display all tasks."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task using form data."""
    title = request.form.get("title", "").strip()

    if title:
        new_id = max([task["id"] for task in tasks], default=0) + 1

        tasks.append({
            "id": new_id,
            "title": title,
            "completed": False
        })

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Delete a task."""
    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

