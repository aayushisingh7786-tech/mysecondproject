// 1. Load tasks from LocalStorage when the page opens
document.addEventListener('DOMContentLoaded', loadTasks);
// FUNCTION: Add a new task
function addTask() {
    // Get the value from the input box
    let input = document.getElementById("taskInput");
    let taskText = input.value;
    if (taskText === "") {
        alert("Please write a task first!");
        return;
    }
    // Create the list item (li) visually
    createTaskElement(taskText);
    // Save to LocalStorage
    saveTaskToLocal(taskText);
    // Clear the input box
    input.value = "";
}
// FUNCTION: Create the HTML for a task
function createTaskElement(text) {
    let ul = document.getElementById("taskList");
    let li = document.createElement("li");
    li.textContent = text;
    // Add a delete button to the task
    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "X";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.style.backgroundColor = "red";
    deleteBtn.style.padding = "5px 10px";
    // When X is clicked, remove the item
    deleteBtn.onclick = function () {
        ul.removeChild(li);
        removeTaskFromLocal(text);
    };
    li.appendChild(deleteBtn);
    ul.appendChild(li);
}
// FUNCTION: Save to Browser Memory (LocalStorage)
function saveTaskToLocal(task) {
    let tasks;
    if (localStorage.getItem("tasks") === null) {
        tasks = [];
    } else {
        tasks = JSON.parse(localStorage.getItem("tasks"));
    }
    tasks.push(task);
    localStorage.setItem("tasks", JSON.stringify(tasks));
}
// FUNCTION: Load tasks when page refreshes
function loadTasks() {
    let tasks;
    if (localStorage.getItem("tasks") === null) {
        tasks = [];
    } else {
        tasks = JSON.parse(localStorage.getItem("tasks"));
    }
    tasks.forEach(function (task) {
        createTaskElement(task);
    });
}
// FUNCTION: Remove single task from memory
function removeTaskFromLocal(task) {
    let tasks;
    if (localStorage.getItem("tasks") === null) {
        tasks = [];
    } else {
        tasks = JSON.parse(localStorage.getItem("tasks"));
    }
    // Filter out the deleted task
    tasks = tasks.filter(t => t !== task);
    // Save the updated list back
    localStorage.setItem("tasks", JSON.stringify(tasks));
}
// FUNCTION: Clear all tasks
function clearTasks() {
    localStorage.clear();
    document.getElementById("taskList").innerHTML = "";
}