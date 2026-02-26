import { useState } from "react";
import { api } from "../services/api";

function UploadPage() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a PDF file.");
      return;
    }

    // const formData = new FormData();
    // formData.append("file", file);
       for (let i = 0; i < fileList.length; i++) {
  formData.append("files", fileList[i]);
}   

    try {
      setLoading(true);
      const response = await api.post("/upload-pdf", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage("Upload successful!");
      console.log(response.data);
    } catch (error) {
      setMessage("Upload failed.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>Internal IT Document (PDF)</h2>

      <input type="file" accept="application/pdf" onChange={handleFileChange} />

      <br /><br />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      <p>{message}</p>
    </div>
  );
}

export default UploadPage;