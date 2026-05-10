<template>
  <div id="app">
    <h1>디지털 자산 플랫폼</h1>
    <UserAccount />
    <WalletDashboard />
    <TransactionHistory />
  </div>
</template>

<script setup>
import UserAccount from './components/UserAccount.vue';
import WalletDashboard from './components/WalletDashboard.vue';
import TransactionHistory from './components/TransactionHistory.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
