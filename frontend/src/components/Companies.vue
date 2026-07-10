<template>
<div>
    <h2>Companies</h2>
    <table border="1">
        <tr v-for="company in companies" :key="company.id">
        <td>{{ company.company_name }}</td>
        <td><button @click="$router.push('/companydata/' + company.id)">View</button></td>
        </tr>
    </table>
</div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            companies: []
        };
    },

    mounted() {
        this.fetchCompanies();
    },

    methods: {
        async fetchCompanies() {
            try {
                const response = await axios.get("http://127.0.0.1:5000/api/companies",{
                        headers: {
                            Authorization:"Bearer " + localStorage.getItem("token")
                        }
                    }
                );
                this.companies = response.data;
            } catch(error) {
                console.log(error);
            }
        }
    }
};
</script>