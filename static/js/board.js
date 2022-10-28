let todoId = 0
let draggables = document.querySelectorAll('.draggable')
let containers = document.querySelectorAll('.task-col')
let deleteButtons = document.querySelectorAll("delTodo")

document.getElementById("task-add-button").addEventListener("click", addTask);


function addTask() {
    let title = document.getElementById("task-title").value
    let priority = document.getElementById("priority-title").value

    renderTask(title,priority)
    updateVars()
}

function delTask(event) {
    console.log(event.target.dataset.Del, " is going to get deleted");

}

function updateVars() {
    draggables = document.querySelectorAll('.draggable');
    containers = document.querySelectorAll('.task-col');
    deleteButtons = document.querySelectorAll(".delete-task-button")
    checkEvents()
}

function renderTask(title, priority) {
    console.log("render bla bla")

    const edit = document.createElement('button');
    edit.innerText = "Edit Todo";
    edit.id = `editTodo`;
    edit.dataset.Edit = `todo${todoId}`
    edit.classList.add("btn");
    edit.classList.add("btn-secondary");
    edit.classList.add("edit-task-button");

    const button = document.createElement('button');
    button.innerText = "Delete Todo";
    button.id = `delTodo`;
    button.dataset.Del = `todo${todoId}`
    button.classList.add("btn");
    button.classList.add("btn-secondary");
    button.classList.add("delete-task-button");

    const todo = document.createElement('div');
    todo.setAttribute("draggable", true);

    todo.innerHTML = title + "<br>";
    todo.id = `todo${todoId}`;
    todo.classList.add(`todo${priority}`);
    todo.classList.add("draggable");



    document.getElementById("task-to-do-container").appendChild(todo);
    document.getElementById(`todo${todoId}`).appendChild(button);
    document.getElementById(`todo${todoId}`).appendChild(edit);
    todoId += 1;
}
function checkEvents() {
    deleteButtons.forEach(button => {
        button.addEventListener("click", () => {
             console.log(event.target.dataset.Del + " is going to get deleted");
             let idToDel = event.target.dataset.Del;
             let element = document.getElementById(idToDel);
             element.parentNode.removeChild(element);

        });
    })
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


 // function refresh(){
 //        window.location.reload("Refresh")
 //      }
