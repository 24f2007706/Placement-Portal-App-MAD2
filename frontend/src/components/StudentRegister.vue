<template>
<div>
    <form @submit.prevent="handleRegister">
        <h3>Student Registration</h3><br>
        <label for="username">Username </label>
        <input type="text" name="username" v-model="form.username" required><br><br>

        <label for="email">Email </label>
        <input type="text" name="email" v-model="form.email" required><br><br>

        <label for="Password">Password </label>
        <input type="text" name="password" v-model="form.password" required><br><br>
        <input type="submit" value="Register">
    </form>
    <a href="#" @click.prevent="$emit('login-here')">Login here</a>
</div>
</template>

<script>
import axios from 'axios'
export default {
    emits:['registered'],
    name : 'StudentRegister',
    data(){
        return {
            form :{
                username : '',
                email : '',
                password : '',
            }

        }
    },
    methods: {
        async handleRegister(){
            try{
                await axios.post('http://127.0.0.1:5000/api/register',this.form)
                this.$router.push('/')
            }
             catch (error){
                console.error('Registration Failed', error)

            }
        }
    }
}
</script>