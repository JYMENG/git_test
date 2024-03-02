<template>
  <div>
    <button @click="downloadExcel">Download Excel</button>
  </div>
</template>

<script>
export default {
  methods: {
    async downloadExcel() {
      try {
        // Make an HTTP GET request to the Django API endpoint
        const response = await fetch('url/to/your/api/vac?filter_parameter1=value1&filter_parameter2=value2');
        
        // Check if the request was successful
        if (!response.ok) {
          throw new Error('Failed to download Excel file');
        }
        
        // Extract the blob (binary data) from the response
        const blob = await response.blob();
        
        // Create a blob URL for the binary data
        const blobUrl = window.URL.createObjectURL(blob);
        
        // Create a link element to trigger the download
        const link = document.createElement('a');
        link.href = blobUrl;
        link.setAttribute('download', 'modified_template.xlsx');
        
        // Append the link to the document body and trigger the download
        document.body.appendChild(link);
        link.click();
        
        // Clean up: remove the link and revoke the blob URL
        document.body.removeChild(link);
        window.URL.revokeObjectURL(blobUrl);
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  }
}
</script>