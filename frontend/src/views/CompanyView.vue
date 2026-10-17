<template>
<div>
    <div v-if="companyLogin">
        <CompanyLogin/>
    </div>
    <div v-else>
        <CompanyDashboard/>
    </div>
</div>
</template>

<script>
import CompanyLogin from '../components/CompanyLogin.vue';

export default {
    name : 'CompanyView',
    components:{
        CompanyLogin,
    },
    data(){
        return {
            companyLogin:true
        }
    }
}
</script>