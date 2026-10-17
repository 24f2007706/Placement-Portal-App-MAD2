import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import AdminDashboard from '../components/AdminDashboard.vue'
import AdminView from '../views/AdminView.vue'
import StudentView from '../views/StudentView.vue'
import CompanyView from '../views/CompanyView.vue'
import StudentDashboard from '../components/StudentDashboard.vue'
import Companies from '../components/Companies.vue'
import EditProfile from '../components/EditProfile.vue'
import RegisteredCompanies from '../components/RegisteredCompanies.vue'
import RegisteredStudents from '../components/RegisteredStudents.vue'
import OngoingDrives from '../components/OngoingDrives.vue'
import StudentApplications from '../components/StudentApplications.vue'
import CompanyRegistration from '../components/CompanyRegistration.vue'
import CompanyDashboard from '../components/CompanyDashboard.vue'
import CreateDrives from '../components/CreateDrives.vue'
import UpcommingDrives from '../components/UpcommingDrives.vue'
import CompanyApplications from '../components/CompanyApplications.vue'
import CompanyData from '../components/CompanyData.vue'
import ViewDriveDetails from '../components/ViewDriveDetails.vue'
import AppliedStudents from '../components/AppliedStudents.vue'
import ViewResume from "../components/ViewResume.vue"
import StudentHistory from '../components/StudentHistory.vue'
import Search from "../components/Search.vue"

const routes = [
  
  {path:'/', component:LandingView},
  {path: "/search/:name",component: Search},
  {path:'/studenthistory/:id',component:StudentHistory},
  {path:'/upcommingdrives/:id', component:UpcommingDrives},
  {path:'/appliedstudents/:id',component:AppliedStudents},
  {path:'/resume/:id',component:ViewResume},
  {path:'/viewdrivedetails/:drive_id',component:ViewDriveDetails},
  {path:'/createdrives',component:CreateDrives},
  {path:'/admin', component:AdminView},
  {path:'/companydata/:company_id',component:CompanyData},
  {path:'/admindashboard', component:AdminDashboard},
  {path:'/companydashboard', component:CompanyDashboard},
  {path:'/company', component:CompanyView},
  {path:'/student', component:StudentView},
  {path:'/studentdashboard', component:StudentDashboard},
  {path:'/companies', component:Companies},
  {path:'/editprofile', component:EditProfile},
  {path:'/companyregistration',component:CompanyRegistration},
  {path:'/registeredstudents',component:RegisteredStudents},
  {path:'/registeredcompanies', component:RegisteredCompanies},
  {path:'/ongoingdrives', component:OngoingDrives},
  {path:'/studentapplications', component:StudentApplications},
  {path:'/companyapplications', component:CompanyApplications},
  {path:'/*', redirect:'/'}

]
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
