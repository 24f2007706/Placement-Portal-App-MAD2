<template>
<div>
    <form @submit.prevent="createDrive">
        <h2>Create Drive</h2><br>
        <label>Drive Name </label>
        <input type="text" v-model="application.drive_name" required><br><br>

        <label>Job Title </label>
        <input type="text" v-model="application.job_title" required><br><br>

        <label>Job Description </label>
        <textarea v-model="application.job_description" required></textarea><br><br>

        <label>Eligibility Criteria (CGPA) </label>
        <input type="number" v-model="application.eligibility_criteria" required><br><br>

        <label>Application Deadline </label>
        <input type="date" v-model="application.application_deadline" required><br><br>

        <button type="submit">Save</button>

    </form>
</div>
</template>

<script>

import axios from "axios";
export default {
  data() {
    return {
      application: {
        company_id: "",
        drive_name: "",
        job_title: "",
        job_description: "",
        eligibility_criteria: "",
        application_deadline: ""
      }
    };
  },


  methods: {
async createDrive() {
  try {
    const token = localStorage.getItem("token")

const response = await axios.post("http://127.0.0.1:5000/api/createdrives",this.application,
  {
    headers:{
      Authorization:`Bearer ${token}`
    }
  }
)
    console.log(response.data)
    console.log("Drive created successfully")
  }
  catch(error){
    console.error(error)
    console.log("Failed to create drive")
  }
}
  }
}
</script>