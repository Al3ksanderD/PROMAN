let todoId = 0
let draggables = document.querySelectorAll('.draggable')
let containers = document.querySelectorAll('.task-col')

console.log(draggables)
document.getElementById("task-add-button").addEventListener("click", addTask);

function addTask() {
    let title = document.getElementById("task-title").value
    let priority = document.getElementById("priority-title").value

    renderTask(title,priority)
    updateVars()
    console.log(draggables)
}

function updateVars() {
    draggables = document.querySelectorAll('.draggable');
    containers = document.querySelectorAll('.task-col');
    checkEvents()
}

function renderTask(title, priority) {
    console.log("render")
    const todo = document.createElement('div');
    todo.setAttribute("draggable", true);
    todo.innerText = title;
    todo.id = `todo${todoId}`;
    todo.classList.add(`todo${priority}`);
    todo.classList.add("draggable");
    document.getElementById("task-to-do-container").appendChild(todo);
    todoId += 1;
}
function checkEvents() {
    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', () => {
            console.log("dragstart")
            draggable.classList.add('dragging')
        })

        draggable.addEventListener('dragend', () => {
            console.log('dragend')
            draggable.classList.remove('dragging')

        })
    })

    containers.forEach(container => {
        container.addEventListener('dragover', e => {
            e.preventDefault()
            //console.log('dragover')
            //const afterElement = getDragAfterElement(container, e.clientY)
            const draggable = document.querySelector('.dragging')
            //console.log(draggable)
            container.appendChild(draggable)

        })
    })
}
