<template>
<div>
    <h2>Company Description</h2>
    <p>{{ company_name }} is a leading company offering excellent career opportunities for students.</p><br>
    <h3>Current Drives</h3>
    <table border="1">
        <thead>
        <tr>
            <th>Drive Name</th>
            <th>Deadline</th>
            <th>Actions</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="drive in drives" :key="drive.id">
            <td>{{ drive.drive_name }}</td>
            <td>{{ new Date(drive.application_deadline).toLocaleDateString('en-GB') }}</td>
            <td><button @click="$router.push('/viewdrivedetails/' + drive.id)">View</button></td>
        </tr>
        </tbody>
    </table>
</div>
</template>

<script>
import axios from "axios"
export default {
    data(){
        return {
            company_name:"",
            drives:[]
        }
    },
    mounted(){
        const company_id = this.$route.params.company_id
        this.fetchCompanyData(company_id)
    },

    methods:{
        async fetchCompanyData(company_id){
            try{
                const token = localStorage.getItem("token")
                const response = await axios.get(`http://127.0.0.1:5000/api/companydata/${company_id}`,
                    {
                        headers:{
                            Authorization:`Bearer ${token}`
                        }
                    }
                )
                this.company_name = response.data.company_name
                this.drives = response.data.drives
            }
            catch(error){
                console.log(error)
            }
        }
    }
}
</script>