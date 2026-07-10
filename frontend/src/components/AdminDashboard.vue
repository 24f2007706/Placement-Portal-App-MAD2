<template>
<div>
    <h2>Admin's Dashboard</h2>
    <input type="text" v-model="search" placeholder="Search Student or Company">

    <button @click="searchUser">Search</button>
    <br><br>
    <button @click="$router.push('/registeredstudents')">Registered Students</button>
    <button @click="$router.push('/registeredcompanies')">Registered Companies</button>
    <button @click="$router.push('/companyregistration')">Company Registration</button>
    <button @click="$router.push('/companyapplications')">Company Applications</button>
    <button @click="$router.push('/ongoingdrives')">All Drives</button>
    <button @click="$router.push('/studentapplications')">Student Applications</button>
    <button @click="logout">Logout</button>
</div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
        search: ""
    }
  },

  async created() {
    try {
      await axios.get("http://127.0.0.1:5000/api/admindashboard",
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        }
      );

    } catch {
      localStorage.removeItem("token");
      this.$router.push("/");
    }
  },

  methods: {
    searchUser() {
      this.$router.push("/search/" + this.search)
    },

    logout() {
      localStorage.removeItem("token")
      this.$router.push("/")
    }
  }
}
</script>