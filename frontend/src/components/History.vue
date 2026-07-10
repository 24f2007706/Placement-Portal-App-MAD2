<template>
<div>
    <table border="1">
        <tr>
        <th>No</th>
        <th>Job Title</th>
        <th>Status</th>
        </tr>
        <tr v-for="(item,index) in history" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.job_title }}</td>
          <td>{{ item.status }}</td>
        </tr>
    </table>
</div>
</template>

<script>
import axios from "axios"
export default {
    data() {
        return {
            history:[]
        }
    },
    async mounted() {
        const user = JSON.parse(
            localStorage.getItem("user"))

        const response = await axios.get(`http://127.0.0.1:5000/api/studenthistory/${user.id}`)
        this.history = response.data
    }
}
</script>