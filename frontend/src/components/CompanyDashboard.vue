<template>
  <div>
    <h2>{{ User.username }}'s Dashboard</h2>  
    <p>Email: {{ User.email }}</p>
    <p>Company ID : {{ User.id }}</p>
    <button @click="$router.push('/upcommingdrives/'+ User.id)">Upcomming Drives</button>
    <button @click="$router.push('/createdrives')">Create Drives</button>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
    name:'CompanyDashboard',
  data() {
    return {
      User:{}
    };
  },
  created() {
    const token = localStorage.getItem("token")
    axios.get("http://127.0.0.1:5000/api/companydashboard", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(res => {
      this.User = res.data;
    })
    .catch(err => {
      console.log(err);
      this.$router.push("/");
    });
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    }
  }
};
</script>