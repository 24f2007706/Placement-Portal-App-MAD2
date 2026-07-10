<template>
  <div>
    <h2>{{ User.username }}'s Dashboard</h2>  
    <p>Roll No: {{ User.id }}</p>
    <p>Email: {{ User.email }}</p>

    <button @click="$router.push('/companies')">Companies</button>
    <button @click="$router.push('/editprofile')">Edit Profile</button>
    <button @click="$router.push('/studenthistory/'+User.id)">History</button>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "StudentDashboard",

  data() {
    return {
      User: {}
    };
  },

  mounted() {
    this.getStudent();
  },

  methods: {
    getStudent() {
      const token = localStorage.getItem("token");
      axios.get("http://127.0.0.1:5000/api/studentdashboard", {
  headers: {
    Authorization: "Bearer " + localStorage.getItem("token")
  }
})

.then(response => {
  console.log(response.data);
  this.User = response.data;
})

.catch(error => {
  console.log(error.response.data);
  this.$router.push("/");
});

    },
    async exportApplications() {
    const token = localStorage.getItem("token");
    try {
      const response = await axios.get("http://127.0.0.1:5000/api/exportapplications",
      {
        headers: {
            Authorization: "Bearer " + token
        }
      }
      );
        console.log(response.data.message);
    } catch (error) {
        alert(error.response.data.message);
    }
},

    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    }
  }
};
</script>