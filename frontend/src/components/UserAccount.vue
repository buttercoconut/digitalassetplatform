<template>
  <div class="user-account">
    <h2>User Account</h2>
    <form @submit.prevent="updateProfile">
      <label>Name: <input v-model="user.name" /></label>
      <label>Email: <input v-model="user.email" /></label>
      <button type="submit">Save</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const user = ref({ name: '', email: '' });

const fetchUser = async () => {
  const res = await axios.get('/api/user/me');
  user.value = res.data;
};

const updateProfile = async () => {
  await axios.put('/api/user/me', user.value);
  alert('Profile updated');
};

onMounted(fetchUser);
</script>

<style scoped>
.user-account { padding: 1rem; }
</style>
