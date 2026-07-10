<template>
  <div>
    <h2>Edit Profile</h2>
    <p>Username</p>
    <input v-model="username">

    <p>New Password</p>
    <input type="password" v-model="password">

    <p>Confirm Password</p>
    <input type="password" v-model="confirmPassword">

    <br><br>

    <button @click="updateProfile">
      Update
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {

  data() {
    return {
      username: "",
      password: "",
      confirmPassword: ""
    };
  },

  methods: {
    updateProfile() {
      if (!this.username) {
        console.log("Username is required");
        return;
      }
      if (this.password !== this.confirmPassword) {
        console.log("Passwords do not match");
        return;
      }

      axios.put("http://127.0.0.1:5000/api/editprofile",
        {
          username: this.username,
          password: this.password
        },
        {
          headers: {
            Authorization:"Bearer " + localStorage.getItem("token")
          }
        }
      )
      .then(() => {
        console.log("Profile Updated");
      })
      .catch(() => {
        console.log("Update Failed");
      });
    }
  }
};
</script>