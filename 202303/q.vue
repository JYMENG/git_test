// Your Vue.js component

// Function to handle file upload and fetch
async function uploadFilesAndFetch() {
  // Assuming you have references to your JSON files stored in variables file1 and file2
  
  // Create a FormData object to send files
  const formData = new FormData();
  formData.append('file1', file1);
  formData.append('file2', file2);

  try {
    // Make a POST request to your Django backend
    const response = await fetch('your-backend-url/endpoint', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    // Assuming backend returns a blob (Excel file)
    const blob = await response.blob();

    // Create a temporary URL for the blob
    const url = window.URL.createObjectURL(blob);

    // Create a link element to trigger download
    const link = document.createElement('a');
    link.href = url;
    link.download = 'combined_excel_file.xlsx';
    document.body.appendChild(link);
    link.click();

    // Clean up
    window.URL.revokeObjectURL(url);
    document.body.removeChild(link);
  } catch (error) {
    console.error('Error:', error);
    // Handle error
  }
}

// Call the function to upload files and fetch
uploadFilesAndFetch();