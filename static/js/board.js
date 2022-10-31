let todoId = 0
let draggables = document.querySelectorAll('.draggable')
let containers = document.querySelectorAll('.task-col')
let deleteButtons = document.querySelectorAll("delTodo")
let myEditableElement = document.querySelectorAll(".edit-task-button");

document.getElementById("task-add-button").addEventListener("click", addTask);


function addTask() {
    let title = document.getElementById("task-title").value
    let priority = document.getElementById("priority-title").value

    renderTask(title, priority)
    updateVars()
};

function editTask(event) {
    let string = event.currentTarget.myParam
    let id = string.charAt(string.length-1);

    let editedValue = document.getElementById("afterEdit").value
    let newValue = document.getElementById(event.currentTarget.myParam)
    let delButton = createDeleteButton(id)
    let editButton = createEditButton(id)


    console.log(id + "Thats the last")

    newValue.innerHTML = editedValue + "<br>";

    newValue.appendChild(delButton);
    newValue.appendChild(editButton);

    updateVars()



}

function delTask(element) {

    element.parentNode.removeChild(element);

}

function createDeleteButton(id) {
    const button = document.createElement('button');
    button.innerText = "Delete Todo";
    button.id = `delTodo`;
    button.dataset.Del = `todo${id}`
    button.classList.add("btn");
    button.classList.add("btn-secondary");
    button.classList.add("delete-task-button");
    return button;

}

function createEditButton(id) {
    const edit = document.createElement('button');
    edit.innerText = "Edit";
    edit.id = `editTodo`;
    edit.dataset.Edit = `todo${id}`
    edit.classList.add("btn");
    edit.classList.add("btn-secondary");
    edit.classList.add("edit-task-button");
    return edit;

}

function updateVars() {
    draggables = document.querySelectorAll('.draggable');
    containers = document.querySelectorAll('.task-col');
    deleteButtons = document.querySelectorAll(".delete-task-button");
    myEditableElement = document.querySelectorAll(".edit-task-button");

    checkEvents()
}




function renderTask(title, priority) {
    console.log("render bla bla")
    let edit = createEditButton(todoId)
    let button = createDeleteButton(todoId)

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

    myEditableElement.forEach(button => {
        button.addEventListener("click", () => {
            let editId = event.target.dataset.Edit;
            console.log(editId + " is going to get edited");
            let toChange = document.getElementById(editId);
            let inputArea = '<textarea id="afterEdit"> </textarea>'
            let buttonArea = '<button id="afterEditButton"> Edit! </button>'
            toChange.innerHTML = inputArea + "<br>" + buttonArea;
            let afterEdit = document.getElementById("afterEditButton")
            afterEdit.myParam = editId
            afterEdit.addEventListener("click", editTask);

        })
    })

    deleteButtons.forEach(button => {
        button.addEventListener("click", () => {
            let idToDel = event.target.dataset.Del;
            let element = document.getElementById(idToDel);
            delTask(element);

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







