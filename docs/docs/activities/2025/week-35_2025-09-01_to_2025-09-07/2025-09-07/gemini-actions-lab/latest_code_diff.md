# 🔄 Latest Code Changes

```diff
diff --git a/example/todo/index.html b/example/todo/index.html
index d8355be..2c3f8f6 100644
--- a/example/todo/index.html
+++ b/example/todo/index.html
@@ -10,12 +10,10 @@
     <div class="container">
         <h1>TODOアプリ</h1>
         <div class="input-area">
-            <input type="text" id="todo-input" placeholder="新しいタスクを入力">
+            <input type="text" id="todo-input" placeholder="新しいTODOを入力">
             <button id="add-button">追加</button>
         </div>
-        <ul id="todo-list">
-            <!-- タスクがここに追加されます -->
-        </ul>
+        <ul id="todo-list"></ul>
     </div>
     <script src="script.js"></script>
 </body>
diff --git a/example/todo/script.js b/example/todo/script.js
index ebeb9ba..c23b1bf 100644
--- a/example/todo/script.js
+++ b/example/todo/script.js
@@ -3,78 +3,70 @@ document.addEventListener('DOMContentLoaded', () => {
     const addButton = document.getElementById('add-button');
     const todoList = document.getElementById('todo-list');
 
-    // ローカルストレージからタスクを読み込む
-    const loadTasks = () => {
-        const tasks = JSON.parse(localStorage.getItem('todos')) || [];
-        tasks.forEach(task => createTaskElement(task.text, task.completed));
+    // ローカルストレージからTODOを読み込む
+    const loadTodos = () => {
+        const todos = JSON.parse(localStorage.getItem('todos')) || [];
+        todos.forEach(todo => {
+            addTodoToList(todo.text, todo.completed);
+        });
     };
 
-    // タスクをローカルストレージに保存する
-    const saveTasks = () => {
-        const tasks = [];
-        todoList.querySelectorAll('.todo-item').forEach(item => {
-            tasks.push({
-                text: item.querySelector('span').textContent,
-                completed: item.classList.contains('completed')
+    // ローカルストレージにTODOを保存する
+    const saveTodos = () => {
+        const todos = [];
+        todoList.querySelectorAll('li').forEach(li => {
+            todos.push({
+                text: li.querySelector('span').textContent,
+                completed: li.classList.contains('completed')
             });
         });
-        localStorage.setItem('todos', JSON.stringify(tasks));
+        localStorage.setItem('todos', JSON.stringify(todos));
     };
 
-    // タスク要素を作成する
-    const createTaskElement = (taskText, isCompleted = false) => {
+    // TODOをリストに追加する
+    const addTodoToList = (text, completed = false) => {
         const li = document.createElement('li');
-        li.classList.add('todo-item');
-        if (isCompleted) {
+        if (completed) {
             li.classList.add('completed');
         }
 
-        const checkbox = document.createElement('input');
-        checkbox.type = 'checkbox';
-        checkbox.checked = isCompleted;
-        checkbox.addEventListener('change', () => {
+        const span = document.createElement('span');
+        span.textContent = text;
+        span.addEventListener('click', () => {
             li.classList.toggle('completed');
-            saveTasks();
+            saveTodos();
         });
 
-        const span = document.createElement('span');
-        span.textContent = taskText;
-
         const deleteButton = document.createElement('button');
         deleteButton.textContent = '削除';
         deleteButton.classList.add('delete-button');
         deleteButton.addEventListener('click', () => {
             li.remove();
-            saveTasks();
+            saveTodos();
         });
 
-        li.appendChild(checkbox);
         li.appendChild(span);
         li.appendChild(deleteButton);
         todoList.appendChild(li);
     };
 
-    // タスクを追加する
-    const addTask = () => {
-        const taskText = todoInput.value.trim();
-        if (taskText === '') {
-            alert('タスクを入力してください。');
-            return;
+    // 追加ボタンのクリックイベント
+    addButton.addEventListener('click', () => {
+        const todoText = todoInput.value.trim();
+        if (todoText) {
+            addTodoToList(todoText);
+            saveTodos();
+            todoInput.value = '';
         }
-        createTaskElement(taskText);
-        saveTasks();
-        todoInput.value = '';
-        todoInput.focus();
-    };
+    });
 
-    // イベントリスナーを設定
-    addButton.addEventListener('click', addTask);
+    // Enterキーでの追加
     todoInput.addEventListener('keypress', (e) => {
         if (e.key === 'Enter') {
-            addTask();
+            addButton.click();
         }
     });
 
-    // 初期タスクを読み込む
-    loadTasks();
-});
+    // 初期化
+    loadTodos();
+});
\ No newline at end of file
diff --git a/example/todo/style.css b/example/todo/style.css
index b253cf2..dc6085a 100644
--- a/example/todo/style.css
+++ b/example/todo/style.css
@@ -6,16 +6,15 @@ body {
     display: flex;
     justify-content: center;
     align-items: center;
-    min-height: 100vh;
+    height: 100vh;
 }
 
 .container {
     background: #fff;
-    padding: 2rem;
+    padding: 20px;
     border-radius: 8px;
-    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
-    width: 100%;
-    max-width: 500px;
+    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
+    width: 400px;
 }
 
 h1 {
@@ -25,73 +24,65 @@ h1 {
 
 .input-area {
     display: flex;
-    margin-bottom: 1rem;
+    margin-bottom: 20px;
 }
 
 #todo-input {
     flex-grow: 1;
-    padding: 0.5rem;
+    padding: 10px;
     border: 1px solid #ddd;
     border-radius: 4px;
-    font-size: 1rem;
+    font-size: 16px;
 }
 
 #add-button {
+    padding: 10px 15px;
+    border: none;
     background-color: #007bff;
     color: white;
-    border: none;
-    padding: 0.5rem 1rem;
     border-radius: 4px;
     cursor: pointer;
-    margin-left: 0.5rem;
-    font-size: 1rem;
+    font-size: 16px;
+    margin-left: 10px;
 }
 
 #add-button:hover {
     background-color: #0056b3;
 }
 
-#todo-list {
-    list-style: none;
+ul {
+    list-style-type: none;
     padding: 0;
     margin: 0;
 }
 
-.todo-item {
+li {
+    background: #f9f9f9;
+    padding: 10px;
+    border-bottom: 1px solid #ddd;
     display: flex;
+    justify-content: space-between;
     align-items: center;
-    padding: 0.8rem 0.5rem;
-    border-bottom: 1px solid #eee;
 }
 
-.todo-item:last-child {
-    border-bottom: none;
+li:first-child {
+    border-top: 1px solid #ddd;
 }
 
-.todo-item.completed span {
+li.completed span {
     text-decoration: line-through;
-    color: #aaa;
-}
-
-.todo-item input[type="checkbox"] {
-    margin-right: 1rem;
-    cursor: pointer;
-}
-
-.todo-item span {
-    flex-grow: 1;
+    color: #888;
 }
 
 .delete-button {
-    background-color: #dc3545;
+    background: #dc3545;
     color: white;
     border: none;
-    padding: 0.3rem 0.6rem;
+    padding: 5px 10px;
     border-radius: 4px;
     cursor: pointer;
-    font-size: 0.9rem;
 }
 
 .delete-button:hover {
-    background-color: #c82333;
-}
+    background: #c82333;
+}
\ No newline at end of file
```
