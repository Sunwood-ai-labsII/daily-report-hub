# 🔄 Latest Code Changes

```diff
diff --git a/example/demo003/index.html b/example/demo003/index.html
new file mode 100644
index 0000000..28df4a9
--- /dev/null
+++ b/example/demo003/index.html
@@ -0,0 +1,20 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>TODO App</title>
+    <link rel="stylesheet" href="style.css">
+</head>
+<body>
+    <div class="container">
+        <h1>TODO App</h1>
+        <form id="todo-form">
+            <input type="text" id="todo-input" placeholder="Add a new task..." autocomplete="off">
+            <button type="submit">Add</button>
+        </form>
+        <ul id="todo-list"></ul>
+    </div>
+    <script src="script.js"></script>
+</body>
+</html>
\ No newline at end of file
diff --git a/example/demo003/script.js b/example/demo003/script.js
new file mode 100644
index 0000000..d0001f2
--- /dev/null
+++ b/example/demo003/script.js
@@ -0,0 +1,54 @@
+document.addEventListener('DOMContentLoaded', () => {
+    const todoForm = document.getElementById('todo-form');
+    const todoInput = document.getElementById('todo-input');
+    const todoList = document.getElementById('todo-list');
+
+    // Load todos from local storage
+    const todos = JSON.parse(localStorage.getItem('todos')) || [];
+
+    const saveTodos = () => {
+        localStorage.setItem('todos', JSON.stringify(todos));
+    };
+
+    const renderTodos = () => {
+        todoList.innerHTML = '';
+        todos.forEach((todo, index) => {
+            const li = document.createElement('li');
+            li.textContent = todo.text;
+            if (todo.completed) {
+                li.classList.add('completed');
+            }
+
+            li.addEventListener('click', () => {
+                todos[index].completed = !todos[index].completed;
+                saveTodos();
+                renderTodos();
+            });
+
+            const deleteButton = document.createElement('button');
+            deleteButton.textContent = 'Delete';
+            deleteButton.addEventListener('click', (e) => {
+                e.stopPropagation();
+                todos.splice(index, 1);
+                saveTodos();
+                renderTodos();
+            });
+
+            li.appendChild(deleteButton);
+            todoList.appendChild(li);
+        });
+    };
+
+    todoForm.addEventListener('submit', (e) => {
+        e.preventDefault();
+        const newTodoText = todoInput.value.trim();
+        if (newTodoText !== '') {
+            todos.push({ text: newTodoText, completed: false });
+            saveTodos();
+            renderTodos();
+            todoInput.value = '';
+        }
+    });
+
+    renderTodos();
+});
\ No newline at end of file
diff --git a/example/demo003/style.css b/example/demo003/style.css
new file mode 100644
index 0000000..57e8f67
--- /dev/null
+++ b/example/demo003/style.css
@@ -0,0 +1,82 @@
+body {
+    font-family: sans-serif;
+    background-color: #f4f4f4;
+    margin: 0;
+    display: flex;
+    justify-content: center;
+    align-items: center;
+    height: 100vh;
+}
+
+.container {
+    background: white;
+    padding: 2rem;
+    border-radius: 8px;
+    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
+    width: 400px;
+}
+
+h1 {
+    text-align: center;
+    color: #333;
+}
+
+#todo-form {
+    display: flex;
+    margin-bottom: 1rem;
+}
+
+#todo-input {
+    flex: 1;
+    padding: 0.5rem;
+    border: 1px solid #ccc;
+    border-radius: 4px;
+}
+
+button {
+    padding: 0.5rem 1rem;
+    border: none;
+    background-color: #28a745;
+    color: white;
+    border-radius: 4px;
+    cursor: pointer;
+    margin-left: 0.5rem;
+}
+
+button:hover {
+    background-color: #218838;
+}
+
+#todo-list {
+    list-style: none;
+    padding: 0;
+    margin: 0;
+}
+
+#todo-list li {
+    background: #eee;
+    padding: 0.75rem;
+    border-radius: 4px;
+    margin-bottom: 0.5rem;
+    display: flex;
+    justify-content: space-between;
+    align-items: center;
+}
+
+#todo-list li.completed {
+    text-decoration: line-through;
+    color: #888;
+}
+
+#todo-list li button {
+    background-color: #dc3545;
+    border: none;
+    color: white;
+    padding: 0.25rem 0.5rem;
+    border-radius: 4px;
+    cursor: pointer;
+}
+
+#todo-list li button:hover {
+    background-color: #c82333;
+}
\ No newline at end of file
```
