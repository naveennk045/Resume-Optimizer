document.addEventListener('DOMContentLoaded', () => {
    const uploadArea = document.getElementById('uploadArea');
    const resumeUpload = document.getElementById('resumeUpload');
    const jobDescription = document.getElementById('jobDescription');
    const submitBtn = document.getElementById('submitBtn');
    const loading = document.getElementById('loading');
    const downloadBtn = document.getElementById('downloadBtn');

    let uploadedFile = null;
    let downloadURL = null;
    
    const BACKEND_URL = "http://127.0.0.1:5000/optimize_resume"; 

    uploadArea.addEventListener('click', () => resumeUpload.click());

    resumeUpload.addEventListener('change', (e) => {
        const file = e.target.files[0];

        if (!file) return;

        if (file.type !== 'application/pdf') {
            alert('Please upload a valid PDF file.');
            resumeUpload.value = ''; 
            return;
        }

        uploadedFile = file;
        uploadArea.innerHTML = `<span class="upload-icon">✅</span><span>${uploadedFile.name}</span>`;
        uploadArea.classList.add('uploaded'); 
    });

    submitBtn.addEventListener('click', async () => {
        if (!uploadedFile || !jobDescription.value.trim()) {
            alert('Please upload a resume and enter a job description.');
            return;
        }

        if (downloadURL) {
            window.URL.revokeObjectURL(downloadURL);
            downloadBtn.style.display = 'none';
        }

        loading.style.display = 'block';
        submitBtn.disabled = true;
        submitBtn.classList.add('disabled');

        const formData = new FormData();
        formData.append('resume', uploadedFile);
        formData.append('jobDescription', jobDescription.value);

        try {
            const response = await fetch(BACKEND_URL, {  
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error('Failed to optimize resume');

            const blob = await response.blob();
            downloadURL = window.URL.createObjectURL(blob);
            downloadBtn.href = downloadURL;
            downloadBtn.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while optimizing your resume. Please try again.');
        } finally {
            loading.style.display = 'none';
            submitBtn.disabled = false;
            submitBtn.classList.remove('disabled');
        }
    });
});
