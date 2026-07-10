<template>
  <div>
    <h1>Registered Students</h1>
    <table>
      <tr>
        <th>Username</th>
        <th>Email</th>
      </tr>

      <tr v-for="user in users" :key="user.email">
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td><button @click="removeStudent(user.id)">Remove</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "RegisteredStudents",

  data() {
    return {
      users: []
    };
  },

  mounted() {
    this.getStudents();
  },

  methods: {
    async getStudents() {
      try {
        const token = localStorage.getItem("token")
        const response = await axios.get("http://127.0.0.1:5000/api/registeredstudents",{
            headers:{
              Authorization:`Bearer ${token}`
            }
        }
    );
        this.users = response.data;
    }catch (error) {
        console.log(error);
    }
},
    async removeStudent(id) {
        const token = localStorage.getItem("token")
    await axios.delete(`http://127.0.0.1:5000/api/removeuser/${id}`,
        {
            headers:{
              Authorization:`Bearer ${token}`
            }
          }
    )
    console.log("student is removed")
    location.reload()
}
  }
};
</script>