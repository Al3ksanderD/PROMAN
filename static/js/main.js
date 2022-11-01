import {boardsManager} from "./controller/boardsManager.js";


const reloadBtn = document.querySelector("#reload");
function init() {
    boardsManager.loadBoards();
}

init();


function reloadPage(){
    window.location.reload();
}

reloadBtn.addEventListener("click", function(){
    reloadPage();
});
