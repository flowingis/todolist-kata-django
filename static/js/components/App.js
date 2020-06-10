import TaskApi from '../api/TasksApi.js';

const taskApi = new TaskApi();

export default {
    name: 'App',
    template: `
        <div class="container mx-auto p-4">
            <div>
                <div class="text-2xl mb-2">ToDo List - Django App</div>
            </div>
            
            <hr class="mb-4">
            
            <div class="max-w-sm rounded overflow-hidden shadow-lg">              
                <div class="px-6 py-4">
                    <div class="font-bold text-xl mb-2">New Task</div>
                    <div>
                        <div class="mb-4">
                            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Description</label>
                            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                                   id="username" 
                                   type="text"
                                   v-model="taskDescription">
                        </div>
                    </div>
                </div>
                <div class="px-6 py-4">
                    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4" @click="addTask()">Insert</button>
                </div>
            </div>
                        
            <hr class="mt-4 mb-4">
            
            <div>
                <div class="text-xl mb-2">Task List:</div>
            </div>
            
            <hr class="mb-4">
            
            <ul>
                <li v-for="task in tasks">
                    <div class="mb-2">
                        <div class="float-left">
                            {{task.description}}
                        </div>
                        <div class="float-right">
                            <button class="bg-red-500 hover:bg-red-700 text-white py-1 px-1" @click="deleteTask(task.id)">Delete</button>
                        </div>
                        <div class="clearfix"></div>
                    </div>
                </li>
            </ul>
            
        </div>
    `,
    data: function() {
        return {
            tasks: [],
            taskDescription: ''
        };
    },
    async mounted() {
          await this.getTasks();
    },
    methods: {
        async getTasks() {
            this.tasks = await taskApi.list();
        },
        async addTask() {
            let requestData = {
                description: this.taskDescription
            };
            let newTask = await taskApi.add(requestData);
            this.tasks.unshift(newTask);
            this.clearInputFields();
        },
        async deleteTask(taskId) {
            await taskApi.delete(taskId);
            await this.getTasks();
        },
        clearInputFields() {
            this.taskDescription = '';
        }
    }
};