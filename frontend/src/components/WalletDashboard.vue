<template>
  <div class="wallet-dashboard">
    <h2>지갑 대시보드</h2>
    <ul>
      <li v-for="wallet in wallets" :key="wallet.id">
        {{ wallet.asset }}: {{ wallet.balance }} {{ wallet.asset }}
      </li>
    </ul>
    <button @click="refreshBalances">잔액 새로고침</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const wallets = ref([]);

async function fetchWallets() {
  try {
    const res = await axios.get('/api/wallets');
    wallets.value = res.data;
  } catch (e) {
    console.error(e);
  }
}

async function refreshBalances() {
  await fetchWallets();
}

onMounted(fetchWallets);
</script>

<style scoped>
.wallet-dashboard {
  max-width: 600px;
  margin: auto;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 4px;
}
</style>
