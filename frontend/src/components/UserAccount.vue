<template>
  <div class="user-account">
    <h2>사용자 계정 관리</h2>
    <form @submit.prevent="updateProfile">
      <label>이메일: <input v-model="user.email" type="email" required /></label>
      <label>비밀번호: <input v-model="user.password" type="password" /></label>
      <label>2FA 설정: <input v-model="user.twoFA" type="checkbox" /></label>
      <button type="submit">저장</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import axios from 'axios';

const user = reactive({
  email: '',
  password: '',
  twoFA: false,
});

async function updateProfile() {
  try {
    await axios.put('/api/user/profile', user);
    alert('프로필이 업데이트되었습니다.');
  } catch (e) {
    console.error(e);
    alert('업데이트에 실패했습니다.');
  }
}
</script>

<style scoped>
.user-account {
  max-width: 400px;
  margin: auto;
}
label {
  display: block;
  margin-bottom: 8px;
}
</style>
