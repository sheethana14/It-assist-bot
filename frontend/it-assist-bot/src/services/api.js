const API_BASE_URL = "http://localhost:8000/api";

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append("files", file);
  
  try {
    const response = await fetch(`${API_BASE_URL}/upload-pdf`, {
      method: "POST",
      body: formData,
    });
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Upload failed");
    }
    return response.json();
  } catch (error) {
    console.error("Upload error:", error);
    throw error;
  }
};

export const sendChat = async (question) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Chat failed");
    }
    return response.json();
  } catch (error) {
    console.error("Chat error:", error);
    throw error;
  }
};
