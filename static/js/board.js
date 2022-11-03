let todoId = 0
let columnId = 4
let draggables = document.querySelectorAll('.draggable')
let containers = document.querySelectorAll('.task-col')
let deleteButtons = document.querySelectorAll("delTodo")
let myEditableElement = document.querySelectorAll(".edit-task-button")
let deleteColumns = document.querySelectorAll(".delete-col-button")
let editColumns = document.querySelectorAll(".edit-col-button")


document.getElementById("task-add-button").addEventListener("click", addTask);
document.getElementById("column-add-button").addEventListener("click", addColumn);

updateVars();




function addColumn() {

    const newColumn = document.createElement('div');
    newColumn.classList.add("col")
    newColumn.classList.add("task-col")
    newColumn.id = `task-col-${columnId}`

    const title = document.createElement('div');
    title.classList.add("col-title")
    title.id = `col-title-${columnId}`

    const titleText = document.createElement('div');
    titleText.classList.add("title")
    titleText.innerText = "Unnamed"

    const deleteButton = createDeleteColButton();
    const editButton = createEditColButton();

    const todo_container = document.createElement('div');

    document.getElementById("col-container").appendChild(newColumn);

    document.getElementById(`task-col-${columnId}`).appendChild(title);
    document.getElementById(`col-title-${columnId}`).appendChild(titleText);
    document.getElementById(`col-title-${columnId}`).appendChild(deleteButton);
    document.getElementById(`col-title-${columnId}`).appendChild(editButton);

    document.getElementById(`task-col-${columnId}`).appendChild(todo_container);

    columnId += 1;
    updateVars();


}

function addTask() {
    let title = document.getElementById("task-title").value
    let priority = document.getElementById("priority-title").value

    renderTask(title, priority)
    updateVars()
}

function editCol(event) {
    console.log("editcol function")
    let editedValue = document.getElementById("afterColEdit").value
    let newValue = document.getElementById(event.currentTarget.myParam)
    let del = createDeleteColButton();
    let edit = createEditColButton();


    newValue.innerHTML = '<div class="title">' + editedValue + '</div>';

    newValue.appendChild(del);
    newValue.appendChild(edit);

    updateVars()

}

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

function delCol() {
    console.log(event.target);
    let child = event.target.parentNode
    child.parentNode.remove();

    updateVars()
}

function delTask(element) {

    element.parentNode.removeChild(element);

}
function createDeleteColButton() {
    const button = document.createElement('button');
    button.innerText = "Delete";
    button.id = `deleteColButton`;
    button.classList.add("btn");
    button.classList.add("btn-secondary");
    button.classList.add("delete-col-button");
    return button;
}

function createEditColButton() {
    const edit = document.createElement('button');
    edit.innerText = "Edit";
    edit.id = `editColButton`;
    edit.classList.add("btn");
    edit.classList.add("btn-secondary");
    edit.classList.add("edit-col-button");
    return edit;
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
    deleteColumns = document.querySelectorAll(".delete-col-button")
    editColumns = document.querySelectorAll(".edit-col-button")

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


    document.getElementById("task-col-1").appendChild(todo);
    document.getElementById(`todo${todoId}`).appendChild(button);
    document.getElementById(`todo${todoId}`).appendChild(edit);
    todoId += 1;
}

function checkEvents() {

    deleteColumns.forEach(column => {
        column.addEventListener("click", delCol)
    })


    editColumns.forEach(column => {
    column.addEventListener("click", () => {
        let parentId = event.target.parentNode.id;
        let parent = event.target.parentNode
        // let targetChild = document.getElementById(parentId).getElementsByClassName("title")[0];
        let toChange = parent
        let inputArea = '<textarea id="afterColEdit"> Edit Col Name </textarea>'
        let buttonArea = '<button id="afterColEditButton"> Edit! </button>'
        toChange.innerHTML = inputArea + "<br>" + buttonArea;
        let afterEdit = document.getElementById("afterColEditButton")
        afterEdit.myParam = parentId
        afterEdit.addEventListener("click", editCol);





        // let inputArea = '<textarea id="afterEdit"> </textarea>'
        // let buttonArea = '<button id="afterEditButton"> Edit! </button>'
        // toChange.innerHTML = inputArea + "<br>" + buttonArea;
    })
})

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







