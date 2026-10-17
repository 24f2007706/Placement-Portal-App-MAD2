<script>
import AdminView from './AdminView.vue';
import CompanyView from './CompanyView.vue';
import StudentView from './StudentView.vue';

</script>

<template>
    <div class="landing">
        <div class="landing-hero">
            <h1>Placement Portal</h1>
            <p>Connecting students with companies. Choose how you'd like to continue.</p>
        </div>
        <div class="role-grid">
            <div class="role-card" @click="$router.push('/student')">
                <div class="role-icon">🎓</div>
                <h3>Student</h3>
                <p>Browse companies, apply to drives and track your applications.</p>
                <span class="go">Continue →</span>
            </div>
            <div class="role-card" @click="$router.push('/company')">
                <div class="role-icon">🏢</div>
                <h3>Company</h3>
                <p>Create placement drives and review applicants' resumes.</p>
                <span class="go">Continue →</span>
            </div>
            <div class="role-card" @click="$router.push('/admin')">
                <div class="role-icon">🛡️</div>
                <h3>Admin</h3>
                <p>Manage students, companies and approve placement drives.</p>
                <span class="go">Continue →</span>
            </div>
        </div>
    </div>
</template>

<script>
</script>