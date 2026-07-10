<template>
<div>
    <form @submit.prevent="handleLogin">
        <h3>Company Login</h3><br>
        <label for="username">Username </label>
        <input type="text" name="username" v-model="form.username" required><br><br>

        <label for="Password">Password </label>
        <input type="text" name="password" v-model="form.password" required><br><br>
        <input type="submit" value="Login">
    </form>
</div>
</template>

<script>
import axios  from 'axios'
export default {
    name : 'CompanyLogin',
    data(){
        return {
            form : {
                username : '',
                password : ''
            }
        }
    },
    methods : {
        async handleLogin(){
            try{
                const response = await axios.post('http://127.0.0.1:5000/api/company/login',this.form)
                console.log('Login response', response.data)
                localStorage.setItem('token', response.data.data.access_token)

                this.$router.push('/companydashboard')

            } catch (error){
                console.error('Login Failed', error);

            }
        }
    }
}
</script>