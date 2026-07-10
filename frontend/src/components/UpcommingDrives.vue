<template>
<div>

    <h2>Upcoming Drives</h2>

    <table>

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

                <td>
                    {{ new Date(drive.application_deadline).toLocaleDateString('en-GB') }}
                </td>

                <td>

                    <button @click="$router.push('/appliedstudents/' + drive.id)">
                        View
                    </button>

                    <button @click="closeDrive(drive.id)">
                        Close Drive
                    </button>

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

        const company_id = this.$route.params.id;
        this.fetchDrives(company_id);
    },
    methods: {
        async fetchDrives(company_id) {
            const token = localStorage.getItem("token")
            const response = await axios.get(`http://127.0.0.1:5000/api/upcommingdrives/${company_id}`,
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            );
            this.drives = response.data;
        },

        async closeDrive(id) {
            const token = localStorage.getItem("token")
            await axios.delete(`http://127.0.0.1:5000/api/closedrive/${id}`,
                {
                headers:{
                    Authorization:`Bearer ${token}`
                }
            }
            );
            console.log("Drive Closed Successfully");
            this.drives = this.drives.filter(
                drive => drive.id !== id
            );
        }
    }
};

</script>