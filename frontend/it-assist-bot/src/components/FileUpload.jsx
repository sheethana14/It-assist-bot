import { useState } from "react";
import { uploadPDF } from "../services/api";

export default function FileUpload({ onUploadSuccess }) {
  const [loading, setLoading] = useState(false);
  const [uploadedFile, setUploadedFile] = useState(null);

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    try {
      const response = await uploadPDF(file);
      setUploadedFile(response.filename);
      onUploadSuccess(response);
      alert("PDF uploaded successfully!");
    } catch (error) {
      alert(`Upload error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="file-upload">
      <label htmlFor="pdf-input">Upload PDF:</label>
      <input
        id="pdf-input"
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
        disabled={loading}
      />
      {uploadedFile && (
        <p className="success">Uploaded: {uploadedFile}</p>
      )}
      {loading && <p className="loading">Uploading...</p>}
    </div>
  );
}