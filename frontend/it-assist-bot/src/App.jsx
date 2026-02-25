import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UploadPage from "./pages/uploadPage";

function App() {
  return (
    <Router>
      <div style={{ padding: "20px" }}>
        <nav>
          <Link to="/upload">Upload</Link>
        </nav>

        <Routes>
          <Route path="/upload" element={<UploadPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;