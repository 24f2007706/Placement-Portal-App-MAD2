<script>
import AdminView from './AdminView.vue';
import CompanyView from './CompanyView.vue';
import StudentView from './StudentView.vue';

</script>

<template>
    <div>
        <div @click="$router.push('/admin')">
            admin view
        </div>
        <div @click="$router.push('/company')">
            company view
        </div>
        <div @click="$router.push('/student')">
            student view
        </div>

    </div>
</template>

<script>
</script>