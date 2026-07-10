<template>
<div>
    <h2>Search Results</h2>
    <table border="1">
        <tr>
            <th>Sr No</th>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
        </tr>
        <tr v-for="(user,index) in users" :key="user.id" >
            <td>{{ index + 1 }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.role }}</td>
        </tr>
    </table>
</div>
</template>
<script>

import axios from "axios"
export default {
    data() {
        return {
            users: []
        }
    },

    async mounted() {
        const name = this.$route.params.name
        const token = localStorage.getItem("token")
        const response = await axios.get(`http://127.0.0.1:5000/api/search/${name}`,
        {
        headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
        }
        }
        )
        this.users = response.data
    }
}
</script>