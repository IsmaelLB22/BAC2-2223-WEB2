const tasks = document.querySelectorAll(".task");
const all_status = document.querySelectorAll(".status");
let draggableTask = null;

tasks.forEach((todo) => {
  todo.addEventListener("dragstart", dragStart);
  todo.addEventListener("dragend", dragEnd);
});

function dragStart() {
  draggableTask = this;
  setTimeout(() => {
    this.style.display = "none";
  }, 0);
  console.log("dragStart");

}

function dragEnd() {
  draggableTask = null;
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
  this.appendChild(draggableTask);
  console.log("dropped");
  // Au drop -> màj
  updateTaskStatus(this.id);
}

function updateTaskStatus(status) {
  // recup l'id du projet
  const pk = document.getElementById("projectID").value
  console.log("id = " + draggableTask.id + " status "+ status);
  //données à envoyer
  const taskId = draggableTask.id;
  const newStatus = status;


  // Methode fetch envoie de données en JSON
  fetch(`/project/${pk}/task-update/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=UTF-8"
    },
    body: JSON.stringify({
      taskId: taskId,
      newStatus: newStatus,
    }),
    credentials: "same-origin"
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // Refresh pour afficher la notif
      document.location.reload()
    });

}


