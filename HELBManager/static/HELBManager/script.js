const todos = document.querySelectorAll(".todo");
const all_status = document.querySelectorAll(".status");
let draggableTodo = null;

todos.forEach((todo) => {
  todo.addEventListener("dragstart", dragStart);
  todo.addEventListener("dragend", dragEnd);
});

function dragStart() {
  draggableTodo = this;
  setTimeout(() => {
    this.style.display = "none";
  }, 0);
  console.log("dragStart");
}

function dragEnd() {
  draggableTodo = null;
  setTimeout(() => {
    this.style.display = "block";
  }, 0);
  console.log("dragEnd");
}

all_status.forEach((status) => {
  status.addEventListener("dragover", dragOver);
  status.addEventListener("dragenter", dragEnter);
  status.addEventListener("dragleave", dragLeave);
  status.addEventListener("drop", dragDrop);
});

function dragOver(e) {
  e.preventDefault();
  //   console.log("dragOver");
}

function dragEnter() {
  this.style.border = "1px dashed #ccc";
  console.log("dragEnter");
}

function dragLeave() {
  this.style.border = "none";
  console.log("dragLeave");
}

function dragDrop() {
  this.style.border = "none";
  this.appendChild(draggableTodo);
  console.log("dropped");
}



/* create task  */


function addElement() {

    var taskName = prompt("Please enter the task's name:", "User managment");

    if(taskName != null || taskName != ""){

        //Create the div & text
        const todo_div = document.createElement("div");
        const txt = document.createTextNode(taskName);

        //Append text child
        //Append to list & set it draggable
        todo_div.appendChild(txt);
        todo_div.classList.add("todo");
        todo_div.setAttribute("draggable", "true");
        todo_div.setAttribute("draggable", "true");

        /* create span */
        const span = document.createElement("span");
        const span_txt = document.createTextNode("\u00D7");
        span.classList.add("close");
        span.appendChild(span_txt);

        todo_div.appendChild(span);

        no_status.appendChild(todo_div);

        span.addEventListener("click", () => {
            span.parentElement.style.display = "none";
        });
        //   console.log(todo_div);

        todo_div.addEventListener("dragstart", dragStart);
        todo_div.addEventListener("dragend", dragEnd);

        document.getElementById("todo_input").value = "";
        todo_form.classList.remove("active");
        overlay.classList.remove("active");
        
    }
}

const close_btns = document.querySelectorAll(".close");

close_btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.parentElement.style.display = "none";
  });
});