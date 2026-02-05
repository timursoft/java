<template>
  <div class="feedback-analytics-dashboard">
    <h1>Feedback Analytics</h1>
    <div class="filters">
      <select v-model="selectedCategory" @change="fetchData">
        <option v-for="category in categories" :key="category.value" :value="category.value">
          {{ category.text }}
        </option>
      </select>
      <input type="date" v-model="startDate" @change="fetchData" />
      <input type="date" v-model="endDate" @change="fetchData" />
    </div>
    <div class="charts">
      <line-chart :data="chartData" :options="chartOptions"></line-chart>
    </div>
    <button @click="exportData">Export Data</button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { Line } from 'vue-chartjs';

export default {
  components: {
    LineChart: Line
  },
  data() {
    return {
      selectedCategory: '',
      startDate: '',
      endDate: ''
    };
  },
  computed: {
    ...mapState('feedbackAnalytics', ['feedbackData', 'categories']),
    chartData() {
      // Transform feedbackData to chart.js format
      return {
        labels: this.feedbackData.map(item => item.date),
        datasets: [{
          label: 'Feedback Trends',
          data: this.feedbackData.map(item => item.count),
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      };
    }
  },
  methods: {
    ...mapActions('feedbackAnalytics', ['fetchFeedbackData']),
    fetchData() {
      this.fetchFeedbackData({
        category: this.selectedCategory,
        startDate: this.startDate,
        endDate: this.endDate
      });
    },
    exportData() {
      // Use xlsx package to export data
      import('xlsx').then(xlsx => {
        const worksheet = xlsx.utils.json_to_sheet(this.feedbackData);
        const workbook = xlsx.utils.book_new();
        xlsx.utils.book_append_sheet(workbook, worksheet, 'FeedbackData');
        xlsx.writeFile(workbook, 'FeedbackData.xlsx');
      });
    }
  }
};
</script>

<style scoped>
.feedback-analytics-dashboard {
  /* Design tokens and responsive styles here */
}
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}
.charts {
  margin-top: 2rem;
}
</style>
