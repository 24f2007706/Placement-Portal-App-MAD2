<template>
<div>
    <h1>Student History</h1>
    <table border="1">
        <tr>
            <th>Job Title</th>
            <th>Status</th>
        </tr>
        <tr v-for="item in drives" :key="item.job_title">
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
            drives: []
        }
    },

    async mounted() {
    const response = await axios.get("http://127.0.0.1:5000/api/studenthistory",
        {
            headers: {
                Authorization:"Bearer " + localStorage.getItem("token")
            }
        }
    );
    this.drives = response.data;
}
}
</script>