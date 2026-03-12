import { useState } from "react";
import FileUpload from "../components/FileUpload";
import ChatBox from "../components/ChatBox";

export default function Dashboard() {
  const [documentUploaded, setDocumentUploaded] = useState(false);
  const [uploadInfo, setUploadInfo] = useState(null);

  const handleUploadSuccess = (uploadResponse) => {
    setDocumentUploaded(true);
    setUploadInfo(uploadResponse);
  };

  return (
    <div className="dashboard">
      <header className="header">
        <h1>IT Assist Bot</h1>
        <p>Upload documents and ask questions</p>
      </header>

      <div className="container">
        <aside className="sidebar">
          <FileUpload onUploadSuccess={handleUploadSuccess} />
          {uploadInfo && (
            <div className="upload-info">
              <h3>Upload Summary</h3>
              <p><strong>File:</strong> {uploadInfo.filename}</p>
              <p><strong>Chunks:</strong> {uploadInfo.total_chunks}</p>
              <p><strong>Embedding Dim:</strong> {uploadInfo.embeddings}</p>
            </div>
          )}
        </aside>

        <main className="main-content">
          <ChatBox documentUploaded={documentUploaded} />
        </main>
      </div>
    </div>
  );
}