// script.js

document.addEventListener("DOMContentLoaded", function() {
    const tasksList = document.querySelector("ul");

    tasksList.addEventListener("click", function(event) {
        if (event.target.tagName === "LI") {
            event.target.classList.toggle("task-realizada");
            event.target.classList.toggle("task-pendiente");
        }
    });
});




