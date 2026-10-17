<template>
<div>
    <div v-if="!isLoggedIn">
    <StudentLogin v-if="!showRegister" @logged-in="handleLogin" @register-here="showRegister = true"/>
    <StudentRegister v-else @registered="handleRegistration" @login-here="showRegister = false"/>
    </div>
    <div v-else>
        <StudentDashboard/>
    </div>
</div> 
</template>

<script>
import StudentLogin from '../components/StudentLogin.vue';
import StudentDashboard from '../components/StudentDashboard.vue';
import StudentRegister from '../components/StudentRegister.vue';

export default {
    name: 'UserView',
    components:{
        StudentRegister,
        StudentLogin,
        StudentDashboard
    },
    data(){
        return {
            isLoggedIn : false ,
            showRegister: true,

        }
    },
    methods:{
        handleRegistration(){
            this.showRegister = false,
            this.isLoggedIn = true

        },
        handleLogin(){
            this.isLoggedIn = true
        }
    }
}
</script>