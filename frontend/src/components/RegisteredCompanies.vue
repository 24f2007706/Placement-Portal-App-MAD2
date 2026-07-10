<template>
  <div>
    <h1>Registered Companies</h1>
    <table border="1">
      <tr>
        <th>Username</th>
        <th>Email</th>
      </tr>

      <tr v-for="user in users" :key="user.email">
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td><button @click="removeCompany(user.id)">Remove</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "RegisteredCompanies",
  data() {
    return {
      users: []
    };
  },

  mounted() {
    this.getCompanies();
  },

  methods: {
    async getCompanies() {
        const token = localStorage.getItem("token")
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/registeredcompanies",
          {
            headers:{
                Authorization:`Bearer ${token}`
            }
          }
        );

        this.users = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    async removeCompany(id) {
        const token = localStorage.getItem("token")
    await axios.delete(`http://127.0.0.1:5000/api/removeuser/${id}`,{
        headers:{
            Authorization:`Bearer ${token}`
        }
        }
    )
    console.log("Company is Removed")
    location.reload()
}
  }
};
</script>