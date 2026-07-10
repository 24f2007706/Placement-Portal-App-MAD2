<template>
<div>
    <h2>Applied Students</h2>
    <table border="1">
    <tr>
        <th>No</th>
        <th>Name</th>
        <th>Email</th>
        <th>Resume</th>
        <th>Result</th>
    </tr>
    <tr v-for="(student,index) in students" :key="student.id">
        <td>{{ index + 1 }}</td>
        <td>{{ student.username }}</td>
        <td>{{ student.email }}</td>
        <td><button @click="$router.push('/resume/' + student.application_id)">view</button></td>
        <td><button @click="acceptStudent(student.application_id)">Accept</button>
            <button @click="rejectStudent(student.application_id)">Reject</button>
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
            students:[]
        }
    },
    async mounted(){
        const id = this.$route.params.id
        const token = localStorage.getItem("token")
        const response = await axios.get(`http://127.0.0.1:5000/api/appliedstudents/${id}`,{
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    )
    this.students = response.data
    },

    methods:{
        async acceptStudent(id){
            const token = localStorage.getItem("token")
            await axios.post(`http://127.0.0.1:5000/api/accept/${id}`,{},
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            location.reload()
        },

        async rejectStudent(id){
            const token = localStorage.getItem("token")
            await axios.post(`http://127.0.0.1:5000/api/reject/${id}`,{},
                {
                headers:{
                    Authorization:`Bearer ${token}`
                }
            }
        )
            location.reload()
        }
    }
}
</script>