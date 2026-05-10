<template>
  <div class="wallet-dashboard">
    <h2>Wallet Dashboard</h2>
    <ul>
      <li v-for="(balance, asset) in balances" :key="asset">
        {{ asset }}: {{ balance }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const balances = ref({});

const fetchBalances = async () => {
  const res = await axios.get('/api/wallet/balances');
  balances.value = res.data;
};

onMounted(fetchBalances);
</script>

<style scoped>
.wallet-dashboard { padding: 1rem; }
</style>
