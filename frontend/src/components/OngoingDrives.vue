<template>
<div>
    <h2>All Drives</h2>
    <table border="1">
        <tr>
            <th>Sr No</th>
            <th>Drive Name</th>
            <th>Job Title</th>
            <th>CGPA</th>
            <th>Deadline</th>
        </tr>
        <tr v-for="(drive,index) in drives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.drive_name }}</td>
            <td>{{ drive.job_title }}</td>
            <td>{{ drive.eligibility_criteria }}</td>
            <td>{{ new Date(drive.application_deadline).toLocaleDateString('en-GB') }}</td>
        </tr>
    </table>
</div>
</template>

<script>
import axios from "axios"
export default{
    data(){
        return{
            drives:[]
        }
    },

    async mounted(){
        const token = localStorage.getItem("token")
        const response = await axios.get("http://127.0.0.1:5000/api/ongoingdrives",
            {
                headers:{
                    Authorization:`Bearer ${token}`
                }
            }
        )
        this.drives = response.data
    }
}
</script>