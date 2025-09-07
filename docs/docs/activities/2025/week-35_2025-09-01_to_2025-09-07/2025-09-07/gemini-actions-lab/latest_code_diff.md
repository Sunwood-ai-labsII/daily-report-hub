# 🔄 Latest Code Changes

```diff
diff --git a/example/todo/index.html b/example/todo/index.html
new file mode 100644
index 0000000..d8355be
--- /dev/null
+++ b/example/todo/index.html
@@ -0,0 +1,22 @@
+<!DOCTYPE html>
+<html lang="ja">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>TODOアプリ</title>
+    <link rel="stylesheet" href="style.css">
+</head>
+<body>
+    <div class="container">
+        <h1>TODOアプリ</h1>
+        <div class="input-area">
+            <input type="text" id="todo-input" placeholder="新しいタスクを入力">
+            <button id="add-button">追加</button>
+        </div>
+        <ul id="todo-list">
+            <!-- タスクがここに追加されます -->
+        </ul>
+    </div>
+    <script src="script.js"></script>
+</body>
+</html>
\ No newline at end of file
diff --git a/example/todo/script.js b/example/todo/script.js
new file mode 100644
index 0000000..ebeb9ba
--- /dev/null
+++ b/example/todo/script.js
@@ -0,0 +1,80 @@
+document.addEventListener('DOMContentLoaded', () => {
+    const todoInput = document.getElementById('todo-input');
+    const addButton = document.getElementById('add-button');
+    const todoList = document.getElementById('todo-list');
+
+    // ローカルストレージからタスクを読み込む
+    const loadTasks = () => {
+        const tasks = JSON.parse(localStorage.getItem('todos')) || [];
+        tasks.forEach(task => createTaskElement(task.text, task.completed));
+    };
+
+    // タスクをローカルストレージに保存する
+    const saveTasks = () => {
+        const tasks = [];
+        todoList.querySelectorAll('.todo-item').forEach(item => {
+            tasks.push({
+                text: item.querySelector('span').textContent,
+                completed: item.classList.contains('completed')
+            });
+        });
+        localStorage.setItem('todos', JSON.stringify(tasks));
+    };
+
+    // タスク要素を作成する
+    const createTaskElement = (taskText, isCompleted = false) => {
+        const li = document.createElement('li');
+        li.classList.add('todo-item');
+        if (isCompleted) {
+            li.classList.add('completed');
+        }
+
+        const checkbox = document.createElement('input');
+        checkbox.type = 'checkbox';
+        checkbox.checked = isCompleted;
+        checkbox.addEventListener('change', () => {
+            li.classList.toggle('completed');
+            saveTasks();
+        });
+
+        const span = document.createElement('span');
+        span.textContent = taskText;
+
+        const deleteButton = document.createElement('button');
+        deleteButton.textContent = '削除';
+        deleteButton.classList.add('delete-button');
+        deleteButton.addEventListener('click', () => {
+            li.remove();
+            saveTasks();
+        });
+
+        li.appendChild(checkbox);
+        li.appendChild(span);
+        li.appendChild(deleteButton);
+        todoList.appendChild(li);
+    };
+
+    // タスクを追加する
+    const addTask = () => {
+        const taskText = todoInput.value.trim();
+        if (taskText === '') {
+            alert('タスクを入力してください。');
+            return;
+        }
+        createTaskElement(taskText);
+        saveTasks();
+        todoInput.value = '';
+        todoInput.focus();
+    };
+
+    // イベントリスナーを設定
+    addButton.addEventListener('click', addTask);
+    todoInput.addEventListener('keypress', (e) => {
+        if (e.key === 'Enter') {
+            addTask();
+        }
+    });
+
+    // 初期タスクを読み込む
+    loadTasks();
+});
diff --git a/example/todo/style.css b/example/todo/style.css
new file mode 100644
index 0000000..b253cf2
--- /dev/null
+++ b/example/todo/style.css
@@ -0,0 +1,97 @@
+body {
+    font-family: sans-serif;
+    background-color: #f4f4f4;
+    margin: 0;
+    padding: 0;
+    display: flex;
+    justify-content: center;
+    align-items: center;
+    min-height: 100vh;
+}
+
+.container {
+    background: #fff;
+    padding: 2rem;
+    border-radius: 8px;
+    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
+    width: 100%;
+    max-width: 500px;
+}
+
+h1 {
+    text-align: center;
+    color: #333;
+}
+
+.input-area {
+    display: flex;
+    margin-bottom: 1rem;
+}
+
+#todo-input {
+    flex-grow: 1;
+    padding: 0.5rem;
+    border: 1px solid #ddd;
+    border-radius: 4px;
+    font-size: 1rem;
+}
+
+#add-button {
+    background-color: #007bff;
+    color: white;
+    border: none;
+    padding: 0.5rem 1rem;
+    border-radius: 4px;
+    cursor: pointer;
+    margin-left: 0.5rem;
+    font-size: 1rem;
+}
+
+#add-button:hover {
+    background-color: #0056b3;
+}
+
+#todo-list {
+    list-style: none;
+    padding: 0;
+    margin: 0;
+}
+
+.todo-item {
+    display: flex;
+    align-items: center;
+    padding: 0.8rem 0.5rem;
+    border-bottom: 1px solid #eee;
+}
+
+.todo-item:last-child {
+    border-bottom: none;
+}
+
+.todo-item.completed span {
+    text-decoration: line-through;
+    color: #aaa;
+}
+
+.todo-item input[type="checkbox"] {
+    margin-right: 1rem;
+    cursor: pointer;
+}
+
+.todo-item span {
+    flex-grow: 1;
+}
+
+.delete-button {
+    background-color: #dc3545;
+    color: white;
+    border: none;
+    padding: 0.3rem 0.6rem;
+    border-radius: 4px;
+    cursor: pointer;
+    font-size: 0.9rem;
+}
+
+.delete-button:hover {
+    background-color: #c82333;
+}
```
