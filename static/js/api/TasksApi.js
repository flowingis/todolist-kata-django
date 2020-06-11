class TasksApi {

    async list() {
        let options = {
            method: 'GET'
        };
        try {
            let response = await fetch('/api/tasks/', options);
            let data = await response.json();
            return data;
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async get(taskId) {
        let options = {
            method: 'GET'
        };
        try {
            let response = await fetch(`/api/tasks/${taskId}`, options);
            let data = await response.json();
            return data;
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async add(task) {
        let options = {
            method: 'POST',
            body: JSON.stringify(task),
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
            let response = await fetch('/api/tasks/', options);
            let data = await response.json();
            return data;
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async update(taskId, task) {
        let options = {
            method: 'PUT',
            body: JSON.stringify(task),
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
            await fetch(`/api/tasks/${taskId}/`, options);
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async delete(taskId) {
        let options = {
            method: 'DELETE'
        };
        try {
            await fetch(`/api/tasks/${taskId}`, options);
        } catch (err) {
            console.log(err);
            return null;
        }
    }

    async markAsDone(taskId) {
        let options = {
            method: 'POST'
        };
        try {
            await fetch(`/api/tasks/${taskId}/done/`, options);
        } catch (err) {
            console.log(err);
            return null;
        }
    }

}

export default TasksApi;