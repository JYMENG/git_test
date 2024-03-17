<template>
  <!-- Your Vue.js component template -->
  <button @click="generateExcel">Generate Excel</button>
</template>

<script>
export default {
  methods: {
    generateExcel() {
      // Assuming you have your JSON object stored in the data property named jsonData
      fetch('http://your-django-backend-url/generate_excel/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.jsonData)
      })
      .then(response => {
        // Use window.location.href to trigger the download
        window.location.href = response.url;
      })
      .catch(error => {
        console.error('Error generating Excel:', error);
      });
    }
  }
}
</script>