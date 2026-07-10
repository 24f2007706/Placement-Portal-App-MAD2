<template>

<div>
    <iframe :src="resume" style=" width:100vw; height:100vh; border:none;"></iframe>
</div>
</template>

<script>
import axios from "axios"
export default {
    data(){
        return {
            resume:""
        }
    },

    async mounted(){
        const id = this.$route.params.id
        const token = localStorage.getItem("token")

        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/resume/${id}`,
                {
                headers:{
                    Authorization:`Bearer ${token}`
                    }
                }
            )
            this.resume = `http://127.0.0.1:5000/uploads/${response.data.resume}`

        }catch(error){
            console.log(error)
        }
    }
}
</script>