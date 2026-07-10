<template>
<div>
    <h2>Student Applications</h2>
    <table border="1">
        <tr>
            <th>Sr No</th>
            <th>Student Name</th>
            <th>Applied Job</th>
            <th>Resume</th>
        </tr>
        <tr v-for="(application,index) in applications" :key="application.id" >
            <td>{{ index + 1 }}</td>
            <td>{{ application.student_name }}</td>
            <td>{{ application.job_title }}</td>
            <td><button @click="$router.push('/resume/' + application.id)">View</button>
            </td>
        </tr>
    </table>
</div>
</template>
<script>

import axios from "axios"
export default {
    data(){
        return {
            applications: []
        }
    },

    async mounted(){
        this.getApplications()
    },

    methods:{
        async getApplications(){
            try{
                const token = localStorage.getItem("token")
                const response = await axios.get("http://127.0.0.1:5000/api/studentapplications",
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            this.applications = response.data
            }catch(error){
            console.log(error)
            }
        },
        viewResume(id){
            this.$router.push('/resume/' + id)
        }
    }
}
</script>