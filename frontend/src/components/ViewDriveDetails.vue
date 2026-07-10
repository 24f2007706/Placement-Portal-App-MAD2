<template>
<div>

    <h2>{{ drive.drive_name }}</h2>
    <p><b>Job Title:</b> {{ drive.job_title }}</p>
    <p><b>Job Description:</b> {{ drive.job_description }}</p>
    <p><b>Eligibility:</b>{{ drive.eligibility_criteria }}</p>
    <p><b>Deadline:</b>{{new Date(drive.application_deadline).toLocaleDateString('en-GB')}}</p>
    <hr>

    <form @submit.prevent="applyDrive">
        <input type="file" accept=".pdf" @change="handleFileUpload" required>
        <br><br>
        <button type="submit">Apply</button>
    </form>
</div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            drive: {},
            resume: null
        };
    },

    mounted() {
        const drive_id = this.$route.params.drive_id;
        this.fetchDrive(drive_id);
    },

    methods: {
        async fetchDrive(drive_id) {
            try {
                const token = localStorage.getItem("token");
                const response = await axios.get(`http://127.0.0.1:5000/api/viewdrivedetails/${drive_id}`,
                    {
                headers:{
                    Authorization:`Bearer ${token}`
                    }
                }
                );
                this.drive = response.data;
            } catch(error) {
                console.log(error);
            }
        },
        handleFileUpload(event) {
            this.resume = event.target.files[0];
        },

        async applyDrive() {
            try {
                const token = localStorage.getItem("token");
                const formData = new FormData();

                formData.append("drive_id",this.drive.id);
                formData.append("resume",this.resume);

                const response = await axios.post("http://127.0.0.1:5000/api/applydrive",
                    formData,
                    {
                        headers:{
                            Authorization:`Bearer ${token}`,"Content-Type":"multipart/form-data"
                        }
                    }
                );
                console.log("applied")
            } catch(error) {
                console.log(error);

                if(error.response){
                    console.log("already applied ")
                }
            }
        }
    }
}
</script>