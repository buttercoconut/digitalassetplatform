<template>
  <div class="transaction-history">
    <h2>거래 내역</h2>
    <ul>
      <li v-for="tx in transactions" :key="tx.id">
        {{ tx.timestamp }} - {{ tx.asset }} {{ tx.amount }} {{ tx.asset }}
        ({{ tx.type }})
      </li>
    </ul>
    <button @click="loadMore">더 보기</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const transactions = ref([]);
const page = ref(1);

async function fetchTransactions() {
  try {
    const res = await axios.get(`/api/transactions?page=${page.value}`);
    transactions.value = transactions.value.concat(res.data);
  } catch (e) {
    console.error(e);
  }
}

async function loadMore() {
  page.value += 1;
  await fetchTransactions();
}

onMounted(fetchTransactions);
</script>

<style scoped>
.transaction-history {
  max-width: 800px;
  margin: auto;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 6px;
}
</style>
