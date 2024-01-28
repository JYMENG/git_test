// Your Vue component
<template>
  <!-- Your component template -->
</template>

<script>
import clonedeep from 'lodash/clonedeep';

export default {
  data() {
    return {
      date1: '2022-01-01',
      date2: '2022-12-31',
      responseData: [],
    };
  },
  methods: {
    async fetchData() {
      // Convert user input strings to JavaScript Date objects
      const startDate = new Date(this.date1);
      const endDate = new Date(this.date2);

      // Calculate the number of days between start and end dates
      const numDays = Math.floor((endDate - startDate) / (24 * 60 * 60 * 1000));

      // Set the interval for making requests (e.g., every 20 days)
      const requestInterval = 20;

      // Calculate the number of requests needed
      const numRequests = Math.ceil(numDays / requestInterval);

      // Make sequential requests for each interval using Fetch
      const resultSets = [];
      for (let i = 0; i < numRequests; i++) {
        const intervalStart = new Date(startDate.getTime() + i * requestInterval * (24 * 60 * 60 * 1000));
        const intervalEnd = new Date(Math.min(endDate.getTime(), intervalStart.getTime() + requestInterval * (24 * 60 * 60 * 1000)));

        const url = `/api/date-range-data/?date1=${intervalStart.toISOString().split('T')[0]}&date2=${intervalEnd.toISOString().split('T')[0]}`;
        
        const response = await fetch(url);
        const data = await response.json();
        resultSets.push(clonedeep(data));
      }

      // Combine the result sets into a single dataset
      this.responseData = resultSets.flat();
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>
