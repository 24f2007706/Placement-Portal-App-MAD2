<template>
<div>
    <div v-if="isLoggedIn">
        <AdminDashboard/>
    </div>

    <div v-else>
        <AdminLogin/>
    </div>

</div> 
</template>

<script>
import AdminLogin from '../components/AdminLogin.vue';
import AdminDashboard from '../components/AdminDashboard.vue';

export default {
    name: 'UserView',
    components:{
         AdminLogin,
         AdminDashboard
    },
    data() {
        return {
            isLoggedIn: false
        }
    }
}

</script>