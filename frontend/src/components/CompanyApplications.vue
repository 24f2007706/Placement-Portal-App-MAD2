<template>
<div>

    <h2>Company Applications</h2>
    <table border="1">
        <thead>
            <tr>
            <th>Company ID</th>
            <th>Drive Name</th>
            <th>Job Title</th>
            <th>Deadline</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="drive in drives" :key="drive.id">
            <td>{{ drive.company_id }}</td>
            <td>{{ drive.drive_name }}</td>
            <td>{{ drive.job_title }}</td>
            <td>{{ new Date(drive.application_deadline).toLocaleDateString('en-GB') }}</td>
            <td>
                <button @click="approveDrive(drive.id)">Approve</button>
                <button @click="rejectDrive(drive.id)">Reject</button>
            </td>
            </tr>
        </tbody>
    </table>
</div>
</template>
<script>
import axios from "axios";
export default {
    data() {
        return {
            drives: []
        };
    },
    mounted() {
        this.fetchApplications();
    },
    methods: {
    async fetchApplications() {
        try {
            const token = localStorage.getItem("token")
            const response = await axios.get("http://127.0.0.1:5000/api/companyapplications",{
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            );
            this.drives = response.data;
        } catch(error) {
            console.log(error);
        }
    },
    async approveDrive(id) {
    try {
        const token = localStorage.getItem("token")
        await axios.put(`http://127.0.0.1:5000/api/approvedrive/${id}`,{},
            {
                headers:{
                    Authorization:`Bearer ${token}`
                }
            }
        )
        console.log("Drive Approved")
        this.fetchApplications()
    } catch(error) {
        console.log(error)
    }
},
    async rejectDrive(id) {
        try {
            const token = localStorage.getItem("token")
            await axios.delete(`http://127.0.0.1:5000/api/rejectdrive/${id}`,
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            );
            console.log("Drive Rejected");
            this.fetchApplications();
        } catch(error) {
            console.log(error);
        }
    }
}
};
</script>