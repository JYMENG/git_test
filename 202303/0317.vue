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
      .then(response => response.blob())
      .then(blob => {
        // Handle the response (e.g., trigger download)
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'generated_excel.xlsx';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
      })
      .catch(error => {
        console.error('Error generating Excel:', error);
      });
    }
  }
}
</script>