import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UploadPage from "./pages/uploadPage";
import ChatPage from "./pages/ChatPage";


function App() {
  return (
    <Router>
      <div style={{ padding: "20px" }}>
        <nav style={{ marginBottom: "20px" }}>
          <Link to="/upload" style={{ marginRight: "15px" }}>Upload</Link>
          <Link to="/chat">Chat</Link>
        </nav>

        <Routes>
          <Route path="/upload" element={<UploadPage />} />
          <Route path="/chat" element={<ChatPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;