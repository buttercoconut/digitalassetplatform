<template>
  <div class="transaction-history">
    <h2>Transaction History</h2>
    <ul>
      <li v-for="tx in transactions" :key="tx.id">
        {{ tx.id }} - {{ tx.asset }} - {{ tx.amount }} - {{ tx.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const transactions = ref([]);

const fetchTransactions = async () => {
  const res = await axios.get('/api/transaction/history');
  transactions.value = res.data;
};

onMounted(fetchTransactions);
</script>

<style scoped>
.transaction-history { padding: 1rem; }
</style>
