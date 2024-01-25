--[[ 
--
-- Description: Create a simple command-line task manager where users can add tasks, view tasks, mark tasks as completed, and delete tasks.
-- 
-- Add Task: Allow users to add tasks with a title, description, and due date.
-- View Tasks: Display a list of all tasks with their details.
-- Mark Task as Completed: Enable users to mark tasks as completed.
-- Delete Task: Allow users to delete tasks from the list.
-- Save and Load: Implement functionality to save tasks to a file and load them when the program starts.
--
--]]--

-- Get the filename for the tasks file from cmd arg
function GetFilename()
    if #arg == 0 then
        error("Tasks filename required.\nUsage: lua task-manager.lua <filename>")
    elseif #arg == 1 then
        return arg[1]
    else
        error("Only one filename is accepted.\nUsage: lua task-manager.lua <filename>")
    end
end

function CreateTask(id, title, desc, due, status)
  local task = {}

  task.id = id
  task.title = title
  task.desc = desc
  task.due = due
  task.status = status

  function task:displayTask()
    print("ID: " .. self.id .. " Title: " .. self.title .. " Description: "  .. self.desc .. " Due Date: " .. self.due .. " Status: " .. tostring(self.status))
  end

  function task:setComplete()
    self.status = true
  end

  return task
end

function ReadFile(filename)
  local file = io.open(filename, "r")

  if not file then
    error("Could not open file.")
    return
  end

  -- assumed that the file is in the correct format
  local tasks = {}
  for line in file:lines() do
    local fields = {}

    for field in line:gmatch("[^,]+") do
      table.insert(fields, field)
    end

    -- 0 = id, 1 = title, 2 = desc, 3 = due date, 4 = status (true/false)
    table.insert(tasks,CreateTask(fields[1], fields[2], fields[3], fields[4], fields[5] == "true"));

  end

  file:close()

  return tasks

end

function WriteToFile(filename, tasks)

  local file = io.open(filename, "w")

  if file == nil then
    print("Could not save new tasks to file")
    return
  end

  for _, currTask in ipairs(tasks) do
    file:write(currTask.id .."," .. currTask.title .. "," .. currTask.desc .. "," .. currTask.due .. "," .. tostring(currTask.status) .. "\n")
  end

  file:close()
end

function CreateNewTask(totalTasks)
  local id = totalTasks + 1
  local fields = { "Title", "Description", "Due Date [YYY-MM-DD]" }

  local inputs = {}

  for i in pairs(fields) do
    io.write(fields[i] .. ": ")
    local usrIn = io.read()
    table.insert(inputs, usrIn)
  end

  -- 1 = title, 2 = description, 3 = due date
  local newTask = CreateTask(id, inputs[1], inputs[2], inputs[3], false)
  return newTask

end

function MarkTaskComplete(tasks, totalTasks)
  io.write("Enter Id of task to mark complete: ")
  local id = tonumber(io.read())

  if id > 0 and id <= totalTasks then
    local taskToComplete = tasks[id]
    taskToComplete:setComplete()
  else
    print("Id not in list")
  end
end

function DisplayAllTasks(tasks)
  for _, task in ipairs(tasks) do
    task:displayTask()
  end
end

function Main()
    local argStatus , filename = pcall(GetFilename)
    if not argStatus then
        print("Error:", filename)
        return
    end

    local fileStatus , tasks = pcall(ReadFile, filename)

    if not fileStatus then
      print("Error:", tasks)
    end

    local totalTasks = 0
    if tasks == nil then
      return
    else
      for _ in pairs(tasks) do
        totalTasks = totalTasks + 1
      end
    end

    local run = true
    while run do
      print()
      print("Task Manger")
      print("[1] Add a task")
      print("[2] View all tasks")
      print("[3] Complete a task")
      print("[0] Quit")

      io.write("Choice: ")
      local choice = tonumber(io.read())

      if choice == 1 then
        local newTask = CreateNewTask(totalTasks)
        table.insert(tasks, newTask)
      end

      if choice == 2 then
        DisplayAllTasks(tasks)
      end

      if choice == 3 then
        DisplayAllTasks(tasks)
        MarkTaskComplete(tasks, totalTasks)
      end

      if choice == 0 then
        run = false
        WriteToFile(filename, tasks)
      end

    end
end

Main()
