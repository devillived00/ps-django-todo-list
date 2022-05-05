$(document).ready(function () {
    $("#taskTable").on("click", ".markDoneButton", function (event) {
      event.preventDefault();
      const csrf = document.getElementsByName("csrfmiddlewaretoken");
      var id = $("#taskCard").attr("data-id");
      $.ajax({
        type: "POST",
        url: "/employee/tasks-list/" + id + "/task-done/",
        data: {
          csrfmiddlewaretoken: csrf[0].value,
          id: id,
          done: true,
        },
        success: function () {
          var task = $('#taskCard[data-id="' + id + '"]');
          var button = $('#taskDoneButton[data-id="' + id + '"]');
          button.css("display", "none");
          task.css("background-color", "#8fffbf").hide().slideDown();
          $("#taskTable").append(task);
          console.log("Done");
        },
        error: function (error) {
          console.log(error);
          console.log("Undone");
        },
      });
    });
    $("#taskTable").on("click", ".deleteButton", function (event) {
      event.stopPropagation();
      const csrf = document.getElementsByName("csrfmiddlewaretoken");
      var id = $("#taskCard").attr("data-id");
      $.ajax({
        type: "POST",
        url: "/employee/tasks-list/" + id + "/task-delete/",
        dataType: "json",
        data: {
          csrfmiddlewaretoken: csrf[0].value,
          id: id,
          del: true,
        },
        success: function () {
          $('#taskCard[data-id="' + id + '"]').remove();
        },
        error: function (error) {
          console.log(error);
          console.log("Undone");
        },
      });
    });
  });
  
  window.addEventListener("load", function (event) {
    const employee_form = document.getElementById("employee-form");
    const csrf = document.getElementsByName("csrfmiddlewaretoken");
    const first_name = document.getElementById("id_first_name");
    const salary = document.getElementById("id_salary");
    const position = document.getElementById("id_position");
    const last_name = document.getElementById("id_last_name");
    const hired_from = document.getElementById("id_hired_from");
    const birth_date = document.getElementById("id_birth_date");
    const bio = document.getElementById("id_bio");
  
    const url = "";
  
    employee_form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const form_data = new FormData();
      form_data.append("csrfmiddlewaretoken", csrf[0].value);
      form_data.append("first_name", first_name.value);
      form_data.append("last_name", last_name.value);
      form_data.append("salary", salary.value);
      form_data.append("position", position.value);
      form_data.append("hired_from", hired_from.value);
      form_data.append("birth_date", birth_date.value);
      form_data.append("bio", bio.value);
  
      $.ajax({
        type: "POST",
        url: url,
        dataType: "json",
        data: form_data,
        success: function (response) {
          console.log(response);
          $("#employeeListView").append(
            '<li class="employee-table-row">' +
              '<div class="col col-1" data-label="Employee ID"><a href="employee/' +
              response.employee.id +
              '"' +
              ">Employee Details</a></div>" +
              '<div class="col col-2" data-label="Employee Name">' +
              response.employee.first_name +
              "</div>" +
              '<div class="col col-3" data-label="Completed Tasks">0</div>' +
              '<div class="col col-4" data-label="Uncompleted Tasks">0</div>' +
              '<div class="col col-5" data-label="Tasks List"><a href="/employee/tasks-list/' +
              response.employee.id +
              '"' +
              ">View tasks</a></div>" +
              "</li>"
          );
          setTimeout(() => {
            first_name.value = "";
            last_name.value = "";
            position.value = "";
            position.value = "";
            hired_from.value = "";
            birth_date.value = "";
            bio.value = "";
          }, 3000);
        },
        error: function (error) {
          console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
      });
    });
  });
  
  window.addEventListener("load", function () {
    const task_form = document.getElementById("task-form");
    const csrf = document.getElementsByName("csrfmiddlewaretoken");
    const employee = document.getElementById("id_employee");
    const description = document.getElementById("id_description");
    const title = document.getElementById("id_title");
    const deadline = document.getElementById("id_deadline");
    const category = document.getElementById("id_category");
    const url = "";
  
    task_form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const form_data = new FormData();
      form_data.append("csrfmiddlewaretoken", csrf[0].value);
      form_data.append("employee", employee.value);
      form_data.append("title", title.value);
      form_data.append("description", description.value);
      form_data.append("deadline", deadline.value);
      form_data.append("category", category.value);
      form_data.append("new_task", true);
  
      $.ajax({
        type: "POST",
        url: url,
        enctype: "multipart/form-data",
        data: form_data,
        success: function (response) {
          console.log(response);
          $("#taskTable").prepend(
            '<li id="taskCard" class="task-list-table-row" style="{% if task.state %} background-color: #8fffbf;{% endif %}" data-id="' +
              response.task.id +
              '">' +
              '<div class="col col-1" data-label="Task Title">' +
              response.task.title +
              "</div>" +
              '<div class="col col-2" data-label="Task Description">' +
              response.task.description +
              "</div>" +
              '<div class="col col-3" data-label="Task Category">' +
              response.task.category +
              "</div>" +
              '<div class="col col-4" data-label="Task Deadline">'+ response.task.deadline + '</div>' +
              '<div class="col col-5" data-label="Mark As Done"><button style="{% if task.state %} display:none; {% endif %}" type="button" id="taskDoneButton" data-id="' +
              response.task.id +
              '" class="markDoneButton">Done</button></div>' +
              '<div class="col col-6" data-label="Delete"><button type="button" id="taskDeleteButton" class="deleteButton">Delete</button></div>' +
              "</li>"
          );
          $("#taskList").remove()
          $("#taskTable").prepend(
           
           '<li id="taskList" class="task-list-table-header">'+
            '<div class="col col-1">Task Title</div>'+
            '<div class="col col-2">Task Description</div>'+
            '<div class="col col-3">Task Category</div>'+
            '<div class="col col-4">Task Deadline</div>'+
            '<div class="col col-5">Mark As Done</div>' +
            '<div class="col col-6">Delete</div>' +
            '</li>'
          )
          
          setTimeout(() => {
            employee.value = "";
            title.value = "";
            deadline.value = "";
            category.value = "";
            description.value = "";
          }, 0);
        },
        error: function (error) {
          console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
      });
    });
  });
  